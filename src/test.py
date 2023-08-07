import openpyxl

inputExcelFile =r"C:\D_Drive\Kantor\test\src\data.xlsx"
datas = openpyxl.load_workbook(inputExcelFile)

sheetNames=datas.sheetnames

# Traversing in the sheetNames list
for name in sheetNames:
   print(name)