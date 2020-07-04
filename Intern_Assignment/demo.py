import PyPDF2
import json
import re


pdf_file = open('data.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
mcq = re.compile


data = json.dumps(page_content)
with open("sample.json", "w") as file: 
    file.write(data)