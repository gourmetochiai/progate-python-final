import argparse
from pathlib import Path
import pandas as pd

def parse_args():
    p = argparse.ArgumentParser(description="CSV を Excel に変換するツール")
    p.add_argument("--input", required=True, help="CSVファイルの場所")
    p.add_argument("--output", required=True, help="Excelファイルの保存先")
    p.add_argument("--columns", default="", help="列の順番（例: id,name,amount）")
    p.add_argument("--sheet-name", default="Sheet1", help="シートの名前")
    p.add_argument("--encoding", default="utf-8-sig", help="文字コード（例: utf-8-sig）")
    return p.parse_args()

def read_csv_safely(path: Path, encoding: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path, encoding=encoding)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="cp932")  # 日本語CSV対策

def main():
    args = parse_args()
    in_path = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    df = read_csv_safely(in_path, args.encoding)

    if args.columns.strip():
        cols = [c.strip() for c in args.columns.split(",") if c.strip()]
        missing = [c for c in cols if c not in df.columns]
        if missing:
            raise ValueError(f"CSVに無い列があるよ: {missing}")
        df = df[cols]

    df.to_excel(out_path, index=False, sheet_name=args.sheet_name)
    print(f"変換完了: {in_path} -> {out_path} (sheet='{args.sheet_name}')")


if __name__ == "__main__":
    main()
