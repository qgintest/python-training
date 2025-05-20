from click import style
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("TextFiles/*.txt")
print(filepaths)

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    name = Path(filepath).stem
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{name.title()}", ln=1)

    with open(filepath, 'r') as file:
        content = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=5, txt=content)
    #print(content)


pdf.output("PDFFile.pdf")