<<<<<<< HEAD
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))
# This is a nice way to iterate using for loops in Python
for i in range(0, n): 
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
=======
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))
# This is a nice way to iterate using for loops in Python
for i in range(0, n): 
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
>>>>>>> 0be82eea013b4a95ecf7d92f4bd55fb50d4253d3
merger.close()