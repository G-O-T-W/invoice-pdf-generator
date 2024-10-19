# Invoice Generator from Excel

This project generates invoices in PDF format from Excel sheets using Python. It reads product data from the Excel files and automatically generates corresponding invoices with a table format, including totals, and adds company information and a logo.

## Features

- **Excel to PDF Conversion**: Converts Excel sheets into detailed invoice PDFs.
- **Automated Table Generation**: Extracts data from Excel columns to populate a table with product details such as product ID, name, amount purchased, price per unit, and total price.
- **Invoice Summary**: Automatically calculates the total price for all products and includes it at the bottom of the invoice.
- **Customizable Headers and Footers**: Includes invoice number, date, and company branding (logo and name) in the generated PDF.
- **Batch Processing**: Handles multiple Excel files from a directory and generates invoices for each one.

## File Structure

- `invoices/`: A directory that stores all the Excel files for which invoices need to be generated.
- `PDFs/`: The output directory where the generated PDF invoices are stored.
- `main.py`: The Python script that reads the Excel files, processes the data, and generates the invoices in PDF format.
- `logo.png`: The company logo added to each invoice.

## How to Use

1. Install the necessary dependencies:
   ```bash
   pip install fpdf pandas openpyxl
   ```
2. Place your Excel files (with product details) inside the invoices/ directory. Ensure each file is named using the format invoice_number-date.xlsx (e.g., 001-2024-01-01.xlsx).
3. Run the script:
   ```bash
   python invoice_generator.py
   ```
4. The generated invoices will be saved in the PDFs/ directory with the same name as the corresponding Excel file.
