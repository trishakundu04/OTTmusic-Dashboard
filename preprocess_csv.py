import pandas as pd

# Load multiple CSV files
files = ['airtel-report.csv', 'jiosaavn-report.csv', 'wynk-report.csv']
dfs = [pd.read_csv(f) for f in files]

# Standardize column names
for i, df in enumerate(dfs):
    df.columns = [c.strip().replace(' ', '_').lower() for c in df.columns]

# Merge all
df = pd.concat(dfs, ignore_index=True)

# Save as JSON for dashboard
df.to_json('dashboard_data.json', orient='records')
