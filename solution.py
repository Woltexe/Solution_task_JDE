import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Validate new column name
    if not re.fullmatch(r"[A-Za-z_]+", new_column):
        return pd.DataFrame([])

    # Allowed characters in role: letters, underscores, + - * and spaces
    if not re.fullmatch(r"[A-Za-z_+\-* ]+", role):
        return pd.DataFrame([])

    # Extract all column names from the role expression
    column_names = re.findall(r"[A-Za-z_]+", role)

    # Check all column names are in df and valid
    for name in column_names:
        if name not in df.columns or not re.fullmatch(r"[A-Za-z_]+", name):
            return pd.DataFrame([])

    # Evaluate the expression
    try:
        df = df.copy()
        df[new_column] = pd.eval(role, engine='python', local_dict=df)
        return df
    except:
        return pd.DataFrame([])
