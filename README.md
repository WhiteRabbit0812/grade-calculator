# 成績計算小工具（軟體工程自主學習）

![自動化測試](https://github.com/<你的帳號>/grade-calculator/actions/workflows/test.yml/badge.svg)

讀取 `姓名,分數` 格式的 CSV，輸出每位學生的等第與全班平均。
這個專案是軟體工程課「自主學習」的實作：為既有程式補單元測試、分析覆蓋率，並用 GitHub Actions 自動化測試。

## 執行

```bash
python src/grade.py sample.csv
```

## 測試

```bash
pip install -r requirements.txt
pytest --cov=src --cov-report=term-missing
```

## 檔案說明

| 路徑 | 說明 |
|---|---|
| `src/grade.py` | 主程式 |
| `tests/test_grade.py` | 單元測試（22 個案例） |
| `.github/workflows/test.yml` | GitHub Actions 設定 |
| `docs/test_before.txt` | 修正前測試結果（10 失敗） |
| `docs/test_after.txt` | 修正後測試結果（全部通過、覆蓋率 95%） |
