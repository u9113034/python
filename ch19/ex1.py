import openpyxl

wb=openpyxl.Workbook()
ws=wb.active
Rows=[
    ['','國文','英文','數學','物理','化學'],
    ['張三',89,90,92,78,75],
    ['李四',89,67,78,58,94],
    ['洪五',77,88,99,90,69],
    ['陳六',98,56,77,88,91],
]
ws.title='mywork'
ws['A1']='雲林科技大學'
for row in Rows:
    ws.append(row)

wb.save('ex1.xlsx')