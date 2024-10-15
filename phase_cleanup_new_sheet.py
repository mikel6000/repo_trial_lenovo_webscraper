#Not yet working
# This script adds a new sheet for the cleaned data
#prereq: pip install pandas openpyxl

import pandas as pd

# Read the Excel file
input_file = '.xlsx'
output_sheet_name = 'CleanedData'

# Load the data
df = pd.read_excel(input_file)

# Ensure 'Phase' column is string type
df['Phase'] = df['Phase'].astype(str)

# Create a new DataFrame to store the expanded rows
expanded_rows = []

# Iterate through each row in the original DataFrame
for _, row in df.iterrows():
    phases = row['Phase'].split(',')
    for phase in phases:
        new_row = row.copy()
        new_row['Phase'] = phase.strip()
        expanded_rows.append(new_row)

# Create a new DataFrame from the expanded rows
expanded_df = pd.DataFrame(expanded_rows)

# Save the new DataFrame to a new sheet in the same Excel file
with pd.ExcelWriter(input_file, engine='openpyxl', mode='a') as writer:
    expanded_df.to_excel(writer, sheet_name=output_sheet_name, index=False)

print(f"Processed data saved to a new sheet named '{output_sheet_name}' in '{input_file}'")