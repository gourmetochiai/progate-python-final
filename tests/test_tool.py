import subprocess
from pathlib import Path
import pandas as pd

def test_csv_to_excel(tmp_path):
    # 入力CSV（サンプル）
    input_csv = Path("data/input_sample.csv")
    output_xlsx = tmp_path / "out.xlsx"

    # tool.py を実行（Pythonコマンドを呼ぶ）
    result = subprocess.run([
        "python", "tool.py",
        "--input", str(input_csv),
        "--output", str(output_xlsx),
        "--columns", "id,name,date,amount,notes",
        "--sheet-name", "Demo",
        "--encoding", "utf-8-sig"
    ], capture_output=True, text=True)

    # 実行が成功したか（エラーコード0か？）
    assert result.returncode == 0

    # 出力されたExcelが存在するか？
    assert output_xlsx.exists()

    # Excelの内容を読み込んで、行数がCSVと一致しているか？
    df_csv = pd.read_csv(input_csv)
    df_xlsx = pd.read_excel(output_xlsx)
    assert len(df_csv) == len(df_xlsx)

def test_columns_order(tmp_path):
    from pathlib import Path
    import pandas as pd, subprocess
    input_csv = Path("data/input_sample.csv")
    out_xlsx = tmp_path / "ordered.xlsx"

    cols = "name,id,amount,date,notes"
    r = subprocess.run(
        ["python", "tool.py",
         "--input", str(input_csv),
         "--output", str(out_xlsx),
         "--columns", cols,
         "--sheet-name", "Demo",
         "--encoding", "utf-8-sig"],
        capture_output=True, text=True
    )
    assert r.returncode == 0
    df = pd.read_excel(out_xlsx)
    assert list(df.columns) == [c.strip() for c in cols.split(",")]
