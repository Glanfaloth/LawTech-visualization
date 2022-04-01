# Python program to create
# a pdf file

import json
from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

with open('test.json', 'r') as f:
	data = json.load(f)
	data_str = data[0]
	data_dict = json.loads(data_str)

attention_scores_dict = data_dict["attention_scores"]

pages_list = attention_scores_dict["pages"]

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size = 10)

for i in range(len(pages_list)):
	page = pages_list[i]["rows"]
	# Add a page
	pdf.add_page()
	for j in range(len(page)):
		row_list = page[j]["words"]
		row = []
		for k in range(len(row_list)):
			word_dict = row_list[k]
			word = word_dict["w"][0]
			score = word_dict["s"][0]
			row.append(word)
		row_str = " ".join(row)
		# create a cell
		pdf.cell(len(row_str) * 2, 5, txt = row_str, fill = True,
				ln = j, align = 'C')

# save the pdf with name .pdf
pdf.output("test.pdf")
