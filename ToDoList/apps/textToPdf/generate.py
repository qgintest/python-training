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
    pdf.cell(w=50, h=8, txt=f"{name.title()}")


pdf.output("PDFFile.pdf")