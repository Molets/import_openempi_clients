#! /usr/bin/python

import os
import pandas as pd

path = os.getcwd()

# Read the Excel file
df = pd.read_excel(path + '/HTS_EXPORT_NEW.xlsx')
	
# Replace '\N' with NaN (missing value)
df.replace({'\\N': pd.NA}, inplace=True)

# Write back to Excel
df.to_csv('HTS_EXPORT_OUTPUT.csv', index=False)

