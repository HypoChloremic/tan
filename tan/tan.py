# Text Analysis
# (c) 2017 Ali Rassolie

import os, collections, re, argparse, sys, codecs
import pyautogui as pg
import PyPDF2 as p


class Tan:
	# Run data_handling to get the full experience

	def __init__(self, basepath="C:\\dfm2_tentor", total=16):
	

	# Encoding 

		self.basepath = basepath
		self.total_count = collections.Counter()


	def data_handling(self):
		alt_names = ["REST", "ORD"]
		# Very ugly indeed
		base_name   = [["VT1{}".format(x), "HT1{}".format(x)] for x in range(3,4)]
		name = [[base_name[x][x%2]+" ORD", base_name[x][x%2]+" REST", base_name[x][(x+1)%2]+" ORD", base_name[x][(x+1)%2]+" REST"] for x in range(len(base_name)) ]

		for pos in name:
			for x in range(4):
				filename = pos[x]+".pdf"
				self.full_path ="{}\\{}".format(self.basepath, filename)
				new_counter = next(self.data_generator())
				self.total_count = self.total_count + new_counter
				
		# Using the alt method 
		self.total_count = self.total_count + self.txt_generator()
		with open("dfm2tentoran.txt", "w", encoding="utf8") as file:
			output_text = str()
			for each in iter(self.total_count.most_common(len(self.total_count))):
				word, number = each
				output_text += "\n {}: {} \n".format(word, number)
			output_text = output_text.replace("å","a").replace("ä","a").replace("ö","o")	
			
			file.write(output_text)

		with open("dfm2count.txt", "r", encoding="utf8") as file:
			text = file.read()
			text = text.replace("      ", "\n")
			with open("cleaned_data.txt", "w", encoding="utf8") as file2:
				file2.write(text)

	def data_generator(self):
	# A generator which yields a counter,
	# the counter is then merged with the total_counter, which is then 
	# printed to a txt file for analysis
		text = str()
		while True:
			path = self.full_path
			with open(path, "rb") as file:
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
	
	def word_counter(self, infile=None):
		with open(infile, "r") as file:
			text = file.read()
			words = re.findall(r'\w+', text.lower().replace("\n"," ").replace("å","a").replace("ä","a").replace("ö","o"))
			counted_words = collections.Counter(words)
			yield counted_words

	def easy_write(self):
		with open("dfm2count.txt", "w", encoding="utf8") as file:
			output_text = str()
			for each in iter(self.total_count.most_common(len(self.total_count))):
				word, number = each
				output_text += "\n {}: {} \n".format(word, number)
			output_text = output_text.replace("å","a").replace("ä","a").replace("ö","o")	
			
			file.write(output_text)


	def txt_generator(self):
		with open("data_from_tent.txt", "r") as file:
			text = file.read()
			words = re.findall(r'\w+', text.lower().replace("\n"," ").replace("å","a").replace("ä","a").replace("ö","o"))
			counted_words = collections.Counter(words)
			return counted_words

	def sorter(self, filename=None):
		with open("dfm2tentoran", "r", encoding="utf8") as file:
			text = file.read()
			l_data = text.split("\n")



if __name__ == '__main__':

	run_instance = Tan()
	# run_instance.data_handling()
	
	with open("dfm2tentoran.txt", "r", encoding="utf8") as file:
		# This seems to solve the problem regarding reading and
		# iterating over a large file, by row!
		for line in file:
			if line in "\n":
				pass
			elif line in  "\n\n":
				print("double new")
				pass
			else: 
				print(line)