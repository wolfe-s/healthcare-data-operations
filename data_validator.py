import pandas as pd

def validate_834_file(file_path):
    print(f"Loading incoming file: {file_path}")
    df = pd.read_csv(file_path)
    
    critical_columns = ['Member_ID', 'Date_Of_Birth', 'Plan_Code']
    null_counts = df[critical_columns].isnull().sum()
    
    print("\n--- Data Validation Report ---")
    print("Missing critical values found:")
    print(null_counts)
    
    clean_df = df.dropna(subset=critical_columns)
    quarantine_df = df[df.isnull().any(axis=1)]
    
    print(f"\nAction: {len(quarantine_df)} rows quarantined for manual review.")
    return clean_df
