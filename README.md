# 成績計算小工具

![自動化測試](https://github.com/WhiteRabbit0812/grade-calculator/actions/workflows/test.yml/badge.svg)

大一寫的小程式：讀進「姓名,分數」格式的 CSV，印出每個人的等第和全班平均。

這學期軟體工程課的自主學習，我拿它來練習補單元測試、看測試覆蓋率，並設定 GitHub Actions 自動跑測試。計畫書和成果報告都放在 `docs/` 裡。

## 執行

```bash
python src/grade.py sample.csv
```

## 跑測試

```bash
pip install -r requirements.txt
pytest --cov=src --cov-report=term-missing
```

## 資料夾內容

- `src/grade.py`：主程式
- `tests/test_grade.py`：單元測試，共 22 個
- `.github/workflows/test.yml`：GitHub Actions 設定
- `docs/test_before.txt`：修改前的測試結果（10 個沒過）
- `docs/test_after.txt`：修改後的測試結果（全部通過，覆蓋率 95%）
