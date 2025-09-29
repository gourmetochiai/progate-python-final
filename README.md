# CSV → Excel 変換ツール (v1)

中学生でもわかる説明：
**CSV（表データのテキスト）を、Excel（.xlsx）に変換するコマンド**です。
列の並び順を指定でき、間違った列名があれば分かりやすく止まります。

---

## できること

- CSVをExcelに変換（.xlsx）
- 列の順番を `--columns "id,name,date,amount"` のように指定
- 列名チェック（足りない列があればエラー表示）
- シート名（`--sheet-name`）と文字コード（`--encoding`）の指定
  - 既定：`sheet-name="Sheet1"`, `encoding="utf-8-sig"`

---

## 動作環境

- Python 3.10+ 推奨
- ライブラリ：`pandas`, `openpyxl`
bash pip install -r requirements.txt # もしくは pip install pandas openpyxl
`

---

## 使い方（最短）
bash python tool.py \ --input data/input_sample.csv \ --output out/result.xlsx \ --columns "id,name,date,amount" \ --sheet-name Demo \ --encoding utf-8-sig
### よくある文字コード

* 日本語CSVで文字化けする → `--encoding cp932`（Shift\_JIS系）を試す
* UTF-8(BOM付き) → `--encoding utf-8-sig`（既定値）

---

## 例：サンプル入出力
project-root/ ├─ tool.py ├─ data/ │ └─ input_sample.csv ├─ out/ │ └─ (ここに Excel を出力) └─ docs/ └─ demo.gif ← READMEから表示
実行例：
bash python tool.py --input data/input_sample.csv --output out/final.xlsx \ --columns "id,name,date,amount" --sheet-name Demo --encoding utf-8-sig
---

## エラー例（不足列の表示）

* 指定した列がCSVにないとき、次のようなメッセージで止まります：
Error: missing columns: amount,date
※ 列名はCSVの1行目（ヘッダー）と**完全一致**が必要です（大小文字や空白に注意）。

---

## ヘルプ
bash python tool.py -h
---

## テスト（品質チェック）

最小テストを1本だけ用意しています（列順を確認）。
bash pytest -q
* 緑（`1 passed`）になればOK。
* 失敗する場合は、列名の綴り・区切り・エンコーディングを確認してください。

---

## よくあるつまずき

* **列名ちがい**：`"Name"` と `"name"` は別物。CSVのヘッダーを確認。
* **カンマ以外区切り**：現在はカンマ（`,`）前提。タブ区切りは未対応（将来 `--delimiter` 追加予定）。
* **エンコーディング**：日本語で文字化け → `--encoding cp932` を試す。

---

## デモGIF

ツールの実行と `pytest` が動いている様子を短いGIFにして、`docs/demo.gif` に保存してください。
README では次の1行で表示します：
markdown ![demo](docs/demo.gif)