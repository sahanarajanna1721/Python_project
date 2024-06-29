'''pip install xlrd==1.2.0'''

'''
1. open the workbook
2. open the worksheet object
3. reading the data in the worksheet
'''

import xlrd

file_path = r'C:\Users\QSP\PycharmProjects\excel_\sample_excel.xlsx'

##opening workbook
work_book = xlrd.open_workbook(file_path)

## opening worksheet object
work_sheet = work_book.sheet_by_name('Sheet1')

# rows = work_sheet.get_rows()
# print(rows)

## skipping the header
# header = next(rows)
#
#
# for ele in rows:
#     # print(ele)      #list
#     # print(ele[0], ele[1])
#     print(ele[0].value, ele[1].value)

#-------------------
## using dict comprehension
rows = work_sheet.get_rows()
header = next(rows)
result = {row[0].value:row[1].value for row in rows}
print(result)