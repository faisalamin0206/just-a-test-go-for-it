from openpyxl import workbook, load_workbook
from openpyxl.worksheet.properties import worksheetproperties, pagesetupproperties

wb = load_workbook('People not on lists.xlsx')
ws = wb.active

ws.append(['Hello'])

wsprops = ws.sheet_properties
ws.props.tabColor = 008000


