import docx
from docx.shared import Inches
from docx.enum.table import WD_TABLE_ALIGNMENT

wdoc=docx.Document()
table=wdoc.add_table(rows=5, cols=2, style='Table Grid')
row=table.rows[0]
row.cells[0].text='方法'
row.cells[1].text='說明'
row=table.rows[1]
row.cells[0].text='group()'
row.cells[1].text='可傳回搜尋到的字串，本章已有許多實例說明。'
row=table.rows[2]
row.cells[0].text='end()'
row.cells[1].text='可傳回搜尋到字串的結束位置。'
row=table.rows[3]
row.cells[0].text='start()'
row.cells[1].text='可傳回搜尋到字串的開始位置。'
row=table.rows[4]
row.cells[0].text='span()'
row.cells[1].text='可傳回搜尋到字串的（起始，結束）位置。'
#table.style='LightShading-Accent3'
table.alignment=WD_TABLE_ALIGNMENT.RIGHT
table.autofit=False
table.columns[0].width=Inches(3.0)
wdoc.save('ex4_1.docx')