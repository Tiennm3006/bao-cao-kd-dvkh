#!/usr/bin/env python3
"""Run prepared sheet prompts through Gemini and save validated results."""

from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "gemini-3.6-flash"


def call_gemini(api_key: str, model: str, prompt: str, timeout: int = 120) -> dict:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    instruction = (
        "Bạn phải trả về đúng một JSON object, không markdown và không giải thích ngoài JSON. "
        "Giữ nhận định bám sát số liệu trong bảng, không bịa số. Schema bắt buộc: "
        '{"assessment":"string","recommendation":["string"],"risk_level":"low|medium|high",'
        '"key_metrics":[{"label":"string","value":"string"}],'
        '"comparison":"string","data_quality_notes":["string"]}'
    )
    body = {
        "contents": [{"role": "user", "parts": [{"text": instruction + "\n\n" + prompt}]}],
        "generationConfig": {"temperature": 0.15, "responseMimeType": "application/json"},
    }
    request = urllib.request.Request(
        url, data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.loads(response.read().decode("utf-8"))
    text = payload["candidates"][0]["content"]["parts"][0]["text"].strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.IGNORECASE)
    return json.loads(text)


def normalize_result(value: object) -> dict:
    result = value if isinstance(value, dict) else {}
    risk = result.get("risk_level")
    if risk not in {"low", "medium", "high"}:
        risk = "medium"
    metrics = result.get("key_metrics")
    if not isinstance(metrics, list):
        metrics = []
    metrics = [m for m in metrics if isinstance(m, dict) and "label" in m and "value" in m]
    recs = result.get("recommendation")
    if isinstance(recs, str):
        recs = [recs]
    if not isinstance(recs, list):
        recs = []
    notes = result.get("data_quality_notes") or []
    if isinstance(notes, str):
        notes = [notes]
    return {
        "assessment": str(result.get("assessment") or ""),
        "recommendation": [str(item) for item in recs if str(item).strip()],
        "risk_level": risk,
        "key_metrics": metrics,
        "comparison": str(result.get("comparison") or ""),
        "data_quality_notes": [str(item) for item in notes],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("gemini_analysis_results.json"))
    parser.add_argument("--model", default=os.getenv("GEMINI_MODEL", DEFAULT_MODEL))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--delay", type=float, default=0.5)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    requests = payload.get("requests") or []
    api_key = os.getenv("GEMINI_API_KEY")
    if not args.dry_run and not api_key:
        raise SystemExit("Thiếu GEMINI_API_KEY. Dùng --dry-run để kiểm tra không gọi API.")

    results = []
    for index, item in enumerate(requests, start=1):
        if args.dry_run:
            analysis = normalize_result({
                "assessment": "DRY RUN: chưa gọi Gemini.",
                "risk_level": "medium",
                "data_quality_notes": ["Kết quả mô phỏng để kiểm tra pipeline."],
            })
        else:
            analysis = None
            last_error = None
            for attempt in range(3):
                try:
                    analysis = normalize_result(call_gemini(api_key, args.model, item["prompt"]))
                    break
                except urllib.error.HTTPError as exc:
                    body = exc.read().decode("utf-8", errors="replace")[:500]
                    last_error = f"HTTP {exc.code}: {body}"
                    time.sleep(2 ** attempt)
                except (urllib.error.URLError, KeyError, ValueError, json.JSONDecodeError, TypeError, IndexError) as exc:
                    last_error = str(exc)
                    time.sleep(2 ** attempt)
                except Exception as exc:
                    last_error = f"{type(exc).__name__}: {exc}"
                    time.sleep(2 ** attempt)
            if analysis is None:
                analysis = normalize_result({
                    "assessment": "Không tạo được phân tích Gemini cho sheet này.",
                    "risk_level": "high",
                    "data_quality_notes": [last_error or "Lỗi không xác định"],
                })
        results.append({"sheet_name": item.get("sheet_name"), "prompt_id": item.get("prompt_id"), "analysis": analysis})
        print(f"[{index}/{len(requests)}] {str(item.get('sheet_name')).encode('ascii', 'backslashreplace').decode('ascii')}")
        if args.delay and index < len(requests):
            time.sleep(args.delay)

    output = {
        "source_file": payload.get("source_file"), "previous_file": payload.get("previous_file"),
        "model": args.model, "dry_run": args.dry_run, "results": results,
    }
    args.output.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(results)} results to {args.output}")


if __name__ == "__main__":
    main()
