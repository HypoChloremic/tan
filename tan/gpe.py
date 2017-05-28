# Extracting from pdf in a more generic way

def gpe(self):

	text = ""
	with open(infile, "rb") as file:
		data = file
		print(data)
		decoded_pdf_data = p.PdfFileReader(data)
		for page_pos in range(decoded_pdf_data.numPages):
			obj = decoded_pdf_data.getPage(page_pos)
			text += obj.extractText()

		words = re.findall(r'\w+', text.lower().replace("\n"," ").replace("å","a").replace("ä","a").replace("ö","o"))
		counted_words = collections.Counter(words)
		print(counted_words.most_common(5))
		yield counted_words

if __name__ == '__main__':
	text = next(gpe("moment2.pdf"))
	with open("moment2.txt", "w") as file:
		file.write(text)