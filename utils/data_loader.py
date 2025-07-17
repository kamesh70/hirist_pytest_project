
import pandas as pd


def load_excel_data(file_path, sheet_name, columns=None):
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
        if columns:
            df = df[columns]
        return list(df.itertuples(index=False, name=None))
    except Exception as e:
        raise RuntimeError(f"Error loading Excel data: {e}")
