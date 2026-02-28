def validate(df):
    if df.isnull().sum().sum() > 0:
        raise ValueError("Data contains null values")

    if len(df) == 0:
        raise ValueError("Dataset empty")

    return True

def remove_duplicates(df):
    return df.drop_duplicates()