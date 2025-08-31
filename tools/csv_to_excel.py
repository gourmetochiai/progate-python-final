import argparse
from pathlib import Path
import pandas as pd

def convert_csv_to_excel(input_path: Path, output_path: Path, columns=None, sheet_name="Sheet1", encoding="utf-8"):
    # CSV読み込み（BOM対策）
    try:
        df = pd.read_csv(input_path, encoding=encoding)
    except UnicodeDecodeError:
        df = pd.read_csv(input_path, encoding="utf-8-sig")

    # ヘッダーの余分なスペースを削除（内包表記）
    df.columns = [c.strip() for c in df.columns]

    # 列順の指定があれば並べ替え
    if columns:
        wanted = [c.strip() for c in columns]
        missing = [c for c in wanted if c not in df.columns]
        if missing:
            raise ValueError(f"CSVに無い列があります: {missing}. ある列: {list(df.columns)}")
        df = df[wanted]

    # 出力フォルダが無ければ作成
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Excel保存
    df.to_excel(output_path, index=False, sheet_name=sheet_name, engine="openpyxl")

def self_test():
    # 最小テスト（列順と行数をチェック）
    tmp_csv = Path("tmp_selftest.csv")
    tmp_xlsx = Path("tmp_selftest.xlsx")
    try:
        df = pd.DataFrame({"name": ["a", "b"], "age": [1, 2]})
        df.to_csv(tmp_csv, index=False, encoding="utf-8")

        convert_csv_to_excel(tmp_csv, tmp_xlsx, columns=["age", "name"])
        back = pd.read_excel(tmp_xlsx, engine="openpyxl")
        assert list(back.columns) == ["age", "name"], "列順が想定と違います"
        assert len(back) == 2, "行数が想定と違います"
        print("SELF TEST PASSED")
    finally:
        for p in [tmp_csv, tmp_xlsx]:
            if p.exists():
                p.unlink()

def parse_args():
    p = argparse.ArgumentParser(description="CSV を Excel に変換する簡易ツール")
    p.add_argument("-i", "--input", required=True, help="入力CSVパス")
    p.add_argument("-o", "--output", help="出力Excelパス（省略時はCSV名を.xlsxに）")
    p.add_argument("-c", "--columns", help="列順（カンマ区切り: 例 'age,name' ）")
    p.add_argument("--sheet-name", default="Sheet1", help="Excelのシート名")
    p.add_argument("--encoding", default="utf-8", help="CSVの文字コード（既定: utf-8）")
    p.add_argument("--self-test", action="store_true", help="最小テストを実行")
    return p.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.self_test:
        self_test()
    else:
        in_path = Path(args.input)
        out_path = Path(args.output) if args.output else in_path.with_suffix(".xlsx")
        columns = args.columns.split(",") if args.columns else None
        convert_csv_to_excel(in_path, out_path, columns=columns, sheet_name=args.sheet_name, encoding=args.encoding)
        print(f"Done: {out_path}")
