# import modules
import PyPDF2

# input path of pdf file, watermark file and merged file

# open pdf and watermark file
pdf = PyPDF2.PdfFileReader(open(r"C:\Users\User\PycharmProjects\Scripting With Python\pdf playground\Super.pdf", 'rb'))
wtr = PyPDF2.PdfFileReader(open(r"C:\Users\User\PycharmProjects\Scripting With Python\pdf playground\wtr.pdf", 'rb'))

output = PyPDF2.PdfFileWriter()

# create loop to merge pdfs
for i in range(pdf.getNumPages()):
    pdf_page = pdf.getPage(i)
    pdf_page.mergePage(wtr.getPage(0))
    output.addPage(pdf_page)

with open('merged.pdf', 'wb') as merged_file:
    output.write(merged_file)
