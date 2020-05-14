import PyPDF2

# My Attempt

# with open('super.pdf','rb') as file:
# 	input_file = PyPDF2.PdfFileReader(file)
# 	page_count = input_file.getNumPages()

# 	for page_number in range(page_count):
# 		current_page = input_file.getPage(page_number)
# 		with open('wtr.pdf','rb') as wtr_file:
# 			watermark= PyPDF2.PdfFileReader(wtr_file)
# 			current_page.mergePage(watermark.getPage(0))
# 			writer = PyPDF2.PdfFileWriter()
		
# 	with open('merged.pdf', 'wb') as new_file:
# 		writer.write(new_file)

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
  page = template.getPage(i)
  page.mergePage(watermark.getPage(0))
  output.addPage(page)

  with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)



