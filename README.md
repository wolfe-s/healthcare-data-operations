# Healthcare Data Operations

This repository contains Python tools developed to maintain high-integrity healthcare data pipelines, specifically focusing on the validation and transformation of member eligibility files (EDI 834 formats).

## Projects Included

1. Automated Data Validation Script (`data_validator.py`)
This script uses Pandas to process incoming CSV batches. It targets null values in critical demographic fields (Member ID, DOB) to prevent malformed data from crashing downstream adjudication systems. It automatically quarantines broken rows for manual review, ensuring zero data loss.

2. Healthcare Schema Mapping (`schema_mapper.py`)
This tool acts as a translation layer. It maps disparate, legacy benefit codes from external vendors into a unified internal format. It features a fallback mechanism that flags unrecognized codes for a Jira ticket rather than dropping the data silently.
