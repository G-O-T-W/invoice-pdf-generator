import pandas as pd
import glob

# Define the path to the directory containing the CSV files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")




