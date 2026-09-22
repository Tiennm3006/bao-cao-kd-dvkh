# Gemini analysis pipeline

The first integration layer is `tools/prepare_gemini_analysis.py`. It reads the
uploaded workbook, detects the 13 report sheets by normalized subject/name, and
creates one Gemini-ready prompt per sheet. It also injects the matching sheet
from the previous workbook when provided.

## Local verification

```powershell
python -m pip install -r requirements.txt
python tools/prepare_gemini_analysis.py `
  "KD-SO LIEU KD-DVKH TUAN 38.xlsx" `
  --previous "KD-SO LIEU KD-DVKH TUAN 37.xlsx" `
  --output gemini_analysis_requests.json
```

The output is intentionally an auditable intermediate artifact. It does not
call Gemini and does not contain an API key. The next integration step should
send each `requests[].prompt` from a protected backend or GitHub Actions job,
validate the returned JSON, and then update the weekly store.

## Gemini runner

`tools/run_gemini_analysis.py` reads `GEMINI_API_KEY` from the environment,
calls Gemini once per sheet, and writes a normalized JSON result. Validate the
pipeline without consuming API quota:

```powershell
python tools/run_gemini_analysis.py gemini_analysis_requests.json `
  --dry-run `
  --output gemini_analysis_results.json
```

For a real run, keep the key outside the repository:

```powershell
$env:GEMINI_API_KEY = "..."
$env:GEMINI_MODEL = "gemini-2.0-flash"
python tools/run_gemini_analysis.py gemini_analysis_requests.json
```

## Current mapping result

The Tuần 38 workbook maps all 13 sheets successfully, including the new
`11LAPDATTBDD` sheet. Numeric prefixes are aliases; the subject and normalized
sheet name are the source of truth.
