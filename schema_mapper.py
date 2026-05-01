import pandas as pd

def map_benefit_codes(df):
    code_mapping = {
        'MED-01': 'MEDICAL_STANDARD',
        'MED-PREM': 'MEDICAL_PREMIUM',
        'RX-TIER1': 'PHARMACY_BASE',
        'RX-TIER2': 'PHARMACY_SPECIALTY'
    }
    
    df['Internal_Code'] = df['Vendor_Code'].map(code_mapping)
    df['Requires_Manual_Audit'] = df['Internal_Code'].isnull()
    
    unmapped_count = df['Requires_Manual_Audit'].sum()
    print(f"Schema Check: Found {unmapped_count} unmapped legacy codes.")
    
    return df
