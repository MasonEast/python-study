"""
Pillow是由从著名的Python图像处理库PIL发展出来的一个分支，通过Pillow可以实现图像压缩和图像处理等各种操作
    pip install pillow  Pillow中最为重要的是Image类，读取和处理图像都要通过这个类来完成。
"""

from PIL import Image
image = Image.open('./res/guido.jpg')
image.format, image.size, image.mode
('JPEG', (500, 750), 'RGB')
image.show()

"""
处理excel
Python的openpyxl模块让我们可以在Python程序中读取和修改Excel电子表格，
由于微软从Office 2007开始使用了新的文件格式，这使得Office Excel和LibreOffice Calc、OpenOffice Calc是完全兼容的，
这就意味着openpyxl模块也能处理来自这些软件生成的电子表格。
"""
import datetime

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = 42
ws.append([1, 2, 3])
ws['A2'] = datetime.datetime.now()

wb.save("sample.xlsx")

"""
处理word文档
利用python-docx模块，Python可以创建和修改Word文档，
当然这里的Word文档不仅仅是指通过微软的Office软件创建的扩展名为docx的文档，
LibreOffice Writer和OpenOffice Writer都是免费的字处理软件。
"""

from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')
p.add_run('italic.').italic = True

document.add_heading('Heading, level 1', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_paragraph(
    'first item in unordered list', style='List Bullet'
)
document.add_paragraph(
    'first item in ordered list', style='List Number'
)

document.add_picture('monty-truth.png', width=Inches(1.25))

records = (
    (3, '101', 'Spam'),
    (7, '422', 'Eggs'),
    (4, '631', 'Spam, spam, eggs, and spam')
)

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for qty, id, desc in records:
    row_cells = table.add_row().cells
    row_cells[0].text = str(qty)
    row_cells[1].text = id
    row_cells[2].text = desc

document.add_page_break()

document.save('demo.docx')