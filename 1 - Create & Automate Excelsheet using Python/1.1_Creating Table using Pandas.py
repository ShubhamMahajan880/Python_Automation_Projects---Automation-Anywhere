import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch

# Define your data
data = {
    "Company Name": ["Package", "Stocks"],
    "Microsoft": [45, 20],
    "Google": [20, 15],
}

# Create DataFrame
df = pd.DataFrame(data)

# Create Excel workbook and sheet
workbook = Workbook()
sheet = workbook.active

# Append DataFrame to the sheet
for row in dataframe_to_rows(df, index=False, header=True):
    sheet.append(row)

# Save the workbook
file_path = "Pandas_Table.xlsx"
workbook.save(file_path)

# Open the Excel application
try:
    x1 = Dispatch("Excel.Application")
    x1.Visible = True

    # Open the saved workbook
    wb = x1.Workbooks.Open(r'E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\1 - Create & Automate Excelsheet using Python\Pandas_Table.xlsx')
    
    # Wait for user input to keep the workbook open
    input("Press Enter to close the workbook...")

    # Close the workbook after user interaction
    wb.Close(SaveChanges=True)  # Save changes before closing
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    x1.Quit()  # Ensure the Excel application is closed
