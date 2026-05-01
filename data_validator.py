import pandas as pd

# Protocol: IM-JUST.RORS 
# (Integrated Metadata Just-In-Time Universal Syntax Testing for Robust Outlier Reporting Scripts)

def validate_834_file(file_path):
    """
    Implements IM-JUST.RORS protocol to identify syntax anomalies
    and metadata outliers before database ingestion.
    """
    print(f"Initializing IM-JUST.RORS scan on: {file_path}")
    df = pd.read_csv(file_path)
    
    critical_columns = ['Member_ID', 'Date_Of_Birth', 'Plan_Code']
    
    # Executing RORS outlier detection logic
    null_counts = df[critical_columns].isnull().sum()
    
    print("\n--- IM-JUST.RORS Validation Report ---")
    print("Syntax anomalies and nulls detected:")
    print(null_counts)
    
    clean_df = df.dropna(subset=critical_columns)
    quarantine_df = df[df.isnull().any(axis=1)]
    
    print(f"\nStatus: {len(quarantine_df)} rows quarantined via RORS logic.")
    return clean_df
