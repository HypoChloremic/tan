# Easy counter
# (c) Ali Rassolie 2017  

import collections, re
import PyPDF2 as p

def gpe(infile):

	text = ""
	with open(infile, "rb") as file:
		data = file
		print(data)
		decoded_pdf_data = p.PdfFileReader(data)
		a = 0
		for page_pos in range(decoded_pdf_data.numPages):
			obj = decoded_pdf_data.getPage(page_pos)
			text += obj.extractText()
			a += 1
			print(a)

		words = re.findall(r'\w+', text.lower().replace("\n"," ").replace("å","a").replace("ä","a").replace("ö","o"))
		counted_words = collections.Counter(words)
		print(counted_words.most_common(5))
		yield counted_words


def word_counter(infile=None):
	with open(infile, "r", encoding="utf8") as file:
		text = file.read()
		words = re.findall(r'\w+', text.lower().replace("\n"," ").replace("å","a").replace("ä","a").replace("ö","o"))
		counted_words = collections.Counter(words)
		yield counted_words

def easy_write2(*args):
	a = gpe(*args)
	total_count = next(a)
	with open("dfm2count.txt", "w", encoding="utf8") as file:
		output_text = ""
		for each in iter(total_count.most_common(len(total_count))):
			word, number = each
			output_text += "{}: {} \n".format(word, number)	
		file.write(output_text)



def easy_write(*args):
	total_count = next(word_counter(*args))
	with open("dfm2count.txt", "w", encoding="utf8") as file:
		output_text = ""
		for each in iter(total_count.most_common(len(total_count))):
			word, number = each
			output_text += "{}: {} \n".format(word, number)	
		file.write(output_text)

def sort_text(infile):
	with open(infile, "r") as file:
		data = file.read()
		data = data.split("\n")
		data = [ each.split(": ") for each in data ]
		data.sort()
		
	with open("dfm2sortedcount.txt", "w") as file:
		for each in data:
			try:
				file.write("{}: {}\n\n".format(each[0],each[1]))	
			except IndexError as e:
				print(e)
			



if __name__ == '__main__':
	easy_write2("moment1.pdf")
	sort_text("m.txt")
