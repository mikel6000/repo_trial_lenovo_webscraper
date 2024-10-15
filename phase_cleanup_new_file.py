# This script creates a new CSV file for the cleaned data

import pandas as pd

# Read the CSV file
input_file = 'TC_TDMS_data - Copy.csv'
output_file = 'processed_TC_TDMS_data.csv'

# Load the data
df = pd.read_csv(input_file)

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

# Save the new DataFrame to a CSV file
expanded_df.to_csv(output_file, index=False)

print(f"New CSV file saved as '{output_file}'")