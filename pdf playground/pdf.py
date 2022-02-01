import PyPDF2

# if we use 'r' we'll get and PdfReadWarning error. To read binary files we've to use 'rb'(read binary) instead of 'r'
file = open(r"{file_location}", 'rb')
reader = PyPDF2.PdfFileReader(file)
writer = PyPDF2.PdfFileWriter()
count = reader.numPages

for i in range(count):
    page = reader.getPage(i)   # getting the first page
    page.rotateClockwise(90)  # rotating
    writer.addPage(page)

new_file = open(r"{new_file_location}", 'wb')
writer.write(new_file)
new_file.close()
file.close()
