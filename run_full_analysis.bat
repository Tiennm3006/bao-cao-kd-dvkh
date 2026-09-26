@echo off
chcp 65001 > nul
title CHAY PHAN TICH GEMINI AI - DASHBOARD KD-DVKH

echo ======================================================================
echo ⚡ CHUONG TRINH PHAN TICH BAO CAO KD-DVKH BANG GEMINI AI ⚡
echo ======================================================================
echo.

IF "%GEMINI_API_KEY%"=="" (
    echo [BUOC 1] Nhap Gemini API Key cua ban (Dang AIzaSy...):
    set /p GEMINI_API_KEY="> Dan API Key tai day: "
)

IF "%GEMINI_API_KEY%"=="" (
    echo.
    echo ❌ LOI: Ban chua nhap Gemini API Key! Vui long chay lai.
    pause
    exit /b
)

IF "%GEMINI_MODEL%"=="" (
    set GEMINI_MODEL=gemini-2.0-flash
)

echo.
echo 🤖 Model dang su dung: %GEMINI_MODEL%
echo.
echo [BUOC 2] Dang trich xuat du lieu 13 sheet va tao Prompt phan tich...
python tools/prepare_gemini_analysis.py "KD-SO LIEU KD-DVKH TUAN 38.xlsx" --previous "KD-SO LIEU KD-DVKH TUAN 37.xlsx" --output gemini_analysis_requests.json

echo.
echo [BUOC 3] Dang gui Prompt den Gemini AI (Model %GEMINI_MODEL%)...
python tools/run_gemini_analysis.py gemini_analysis_requests.json --model %GEMINI_MODEL% --output gemini_analysis_results.json

echo.
echo ======================================================================
echo ✅ HOAN THANH PHAN TICH! Ket qua da ghi vao gemini_analysis_results.json
echo ======================================================================
pause
