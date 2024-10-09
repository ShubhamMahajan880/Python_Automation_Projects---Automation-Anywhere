"""
Prerequiremmets -
1 - pip install pywin32
2 - pip install openpyxl
3 - >pip install pandas
"""

from openpyxl import Workbook
from win32com.client import Dispatch 

workbook = Workbook()
sheet = workbook.active

sheet["A1"] = "Student Name" # This format includes column where we have to create the desired column
sheet["B1"] = "Desired Location"


workbook.save(filename="my_excelsheet.xlsx")# Command for Excelsheet Creation


#Another way to add value in cell

cell = sheet["F1"]
cell.value = "Package"
print(cell.value)

workbook.save(filename="my_excelsheet.xlsx")# Way to save the workbook

#Command for Automatically open the file -
x1 = Dispatch("Excel.Application")
x1.Visible = True
wb = x1.Workbooks.Open(r'E:\DarkBox\12 LPA - Shubham Mahajan_Automtion Anywhere\Finally Bro...!!\Python_Automation_Projects\1 - Create & Automate Excelsheet using Python\my_excelsheet.xlsx')



