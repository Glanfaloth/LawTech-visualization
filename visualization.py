# Python program to create
# a pdf file

from decimal import MAX_EMAX
import json
import re
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

max_score = 0
for i in range(len(pages_list)):
	page = pages_list[i]["rows"]
	for j in range(len(page)):
		row_list = page[j]["words"]
		for k in range(len(row_list)):
			word_dict = row_list[k]
			score = word_dict["s"][0]
			max_score = max(max_score, score)

for i in range(len(pages_list)):
	page = pages_list[i]["rows"]
	# Add a page
	pdf.add_page()
	for j in range(len(page)):
		row_list = page[j]["words"]
		word_count = 0
		row = []
		for k in range(len(row_list)):
			word_dict = row_list[k]
			word = word_dict["w"][0]
			if word != "" and word != ":" and not re.match("^[0-9]+\.$", word):
				row.append(word)
			score = word_dict["s"][0]
			# create a cell
			pdf.set_fill_color(255, 255 - score / max_score * 255, 255)
			word_count += 1
			if word_count == 15:
				row_str = " ".join(row)
				pdf.cell(len(row_str) * 3, 5, txt = row_str, fill = True, align = 'L')
				pdf.ln()
				word_count = 0
				row = []
		row_str = " ".join(row)
		pdf.cell(len(row_str) * 3, 5, txt = row_str, fill = True, align = 'L')
		pdf.ln()

# save the pdf with name .pdf
pdf.output("test.pdf")
