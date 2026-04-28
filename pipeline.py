import pandas as pd

def clean_data(df):
    df = df.dropna()
    
    if "price" in df.columns:
        df["price"] = df["price"].astype(float)
    
    return df