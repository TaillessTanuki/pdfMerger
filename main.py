import sys
import PyPDF2
from PyPDF2 import PdfWriter
import os

#choosing folder/dir for the inputs
inputdir = "D:\Documents\Merging_pdf\input"

merger = PdfWriter()

list = [os.path.join(inputdir,a) for a in os.listdir(inputdir)]

for pdf in list:
    if pdf.endswith(".pdf"):
        merger.append(pdf)

#choosing the output location and file name
output_path = "D:\Documents\Merging_pdf\output\merged_pdf.pdf"

merger.write(output_path )
merger.close()

print("all done")
print(sys.version)
