import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'Spam Bacon Eggs Sheet'
wb.create_sheet(index=0, title='First Sheet')
wb.remove_sheet(wb.get_sheet_by_name('First Sheet'))
sheet['A1']='Hello world!'
wb.save('example_copy.xlsx')

