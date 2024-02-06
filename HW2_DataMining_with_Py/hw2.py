import pandas as pd
import numpy as np
# Create a dictionary of data

# Create a DataFrame
df = pd.DataFrame({
    'Attended': [25, 6, 31],
    'Skipped': [8, 15, 23],
}, index=['Passed', 'Failed', 'Total'])

# Calculate row and column totals
row_totals = df.loc[:, 'Attended':'Skipped'].sum(axis=1)
col_totals = df.loc['Total', :]

# Calculate grand total
grand_total = df.loc['Total', 'Attended':'Skipped'].sum()

# Calculate expected values for each cell
expected_values = pd.DataFrame()
for row in ['Passed', 'Failed']:
    for col in ['Attended', 'Skipped']:
        expected_values.loc[row, col] = (row_totals[row] * col_totals[col]) / grand_total
expected_values = round(expected_values,2)

# print the DataFrames
print("The DataFrame is:")
print(df, '\n')
print("The Expected Values are:")
print(expected_values)