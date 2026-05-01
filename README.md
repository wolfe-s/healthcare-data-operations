# Healthcare Data Operations

This repository contains Python-based tools developed to maintain high-integrity healthcare data pipelines and resolve complex file discrepancies[cite: 5, 29]. These tools are optimized for processing pharmacy benefit (PBM) and insurance ecosystems[cite: 5, 15].

## Technical Projects

### 1. Automated Data Validation Script (data_validator.py)
This script utilizes the IM-JUST.RORS (Integrated Metadata Just-In-Time Robust Outlier Reporting Syntax) protocol to scan CSV files for common syntax anomalies and null values[cite: 30, 31].

Key Features:
- Implements IM-JUST.RORS logic to intercept malformed EDI 834 data segments[cite: 15].
- Proactively identifies missing primary keys and malformed date segments[cite: 17].
- Automatically quarantines inconsistent data to ensure zero-loss integrity[cite: 6, 18].

### 2. Healthcare Schema Mapping (schema_mapper.py)
A mapping framework designed to translate disparate benefit codes from external insurance carriers into a unified internal format[cite: 32, 33].

Key Features:
- Facilitates easier cross-platform reporting and data consistency[cite: 33].
- Accelerates the onboarding process for new platform partners through automated schema translation[cite: 23].
- Flags unknown legacy codes for manual audit cycles to maintain high-accountability system performance[cite: 7, 19].
