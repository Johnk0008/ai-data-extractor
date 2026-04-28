def validate_data(df):
    errors = []

    for index, row in df.iterrows():
        if row.get("price", 0) <= 0:
            errors.append(f"Invalid price at row {index}")
        
        if not row.get("product_name"):
            errors.append(f"Missing product name at row {index}")

    return errors