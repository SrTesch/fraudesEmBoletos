import pandas as pd

def load_boleto_data(file_path: str):
    #Loads a CSV file containing boleto transactions.
    return pd.read_csv(file_path)

def check_for_duplicates(df):
    #Checks for duplicate boletos, which could indicate fraud.
    duplicates = df[df.duplicated("boleto_number")]
    return duplicates

# Example usage
if __name__ == "__main__":
    df = load_boleto_data("../data/sample_boletos.csv")
    fraud_cases = check_for_duplicates(df)
    print(f"Potential fraud cases found: {len(fraud_cases)}")
