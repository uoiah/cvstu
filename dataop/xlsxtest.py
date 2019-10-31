import xlsxwriter as xw

workbook = xw.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()
# worksheet.write('A1', 'hello')
for row in range(10):
    worksheet.write(row, 0, row)
workbook.close()