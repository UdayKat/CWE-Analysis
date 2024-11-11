import json

# Load JSON file
with open(r'C:\Users\udayk\OneDrive\Desktop\CWEAnalysis\MSR_data_cleaned.json', 'r') as f:
    data = json.load(f)
filtered_data=[]
for number in data:
    if data[number]["CWE ID"] == "CWE-416" and data[number]["vul"] =='1':
        filtered_data.append(data[number]['func_before'])
    if len(filtered_data) == 10:
        break 
print(filtered_data)

from openpyxl import Workbook
from openpyxl import load_workbook


# Your list


wb = load_workbook("CWE-416_vul.xlsx")
ws = wb.active

# Iterate through each row and print the values
for row in ws.iter_rows(values_only=True):
    print(row) = load_workbook("my_list.xlsx")
ws = wb.active

# Iterate through each row and print the values
for row in ws.iter_rows(values_only=True):
    print(row)
