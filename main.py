import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

# Define the path to the directory containing the CSV files
filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Create a new PDF document
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]

    # Set invoice header
    pdf.set_font("Times", size=18, style="B")
    pdf.cell(w=0, h=9, txt=f"Invoice nr. {invoice_nr}", align="l", ln=1)
    pdf.cell(w=0, h=9, txt=f"Date {date}", align="l", ln=1)

    pdf.output(f"PDFs/{filename}.pdf")








