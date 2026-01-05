import pandas as pd

def parse_excel(file):
    xls = pd.ExcelFile(file)
    content = []

    for sheet in xls.sheet_names:
        df = xls.parse(sheet)
        content.append(f"--- Feuille : {sheet} ---")
        content.append(df.astype(str).to_string(index=False))

    return "\n\n".join(content)
