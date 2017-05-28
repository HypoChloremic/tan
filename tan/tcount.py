import tkinter as tk



class tcount:
	def __init__(self):
		self.recount()
		root = tk.Tk()
		f1 = tk.Frame(root)
		f1.grid()
		b1 = tk.Button(f1, text="corr", command=self.corr_)
		b2 = tk.Button(f1, text="incorr", command= self.incorr_)
		b3 = tk.Button(f1, text="save", command= self.save)
		b4 = tk.Button(f1, text="reset", command= self.reset_count)
		b5 = tk.Button(f1, text="copy", command= self.copy)
		self.l1 = tk.Label(f1, text=self.text_to_save)
		b1.grid(column=0,row=0)
		b2.grid(column=1, row=0)
		b3.grid(column=1, row=1)
		b4.grid(column=0,row=1)
		b5.grid(column=0,row=2)
		self.l1.grid(column=3, row=0)
		root.mainloop()

	def recount(self):
		try: 
			with open("tcount.txt", "r") as file:
				for line in file:
					t_list = line.split("\t")
				
				self.total = int(t_list[0])
				self.corr = int(t_list[1])
				self.incorr = int(t_list[2])
				self.text_to_save = "{}\t{}\t{}".format(self.total, self.corr, self.incorr)


		except Exception as e:
			raise e

	def corr_(self):

		self.total += 1
		self.corr += 1
		self.refresh()
		self.save()

	def incorr_(self):
		self.total += 1
		self.incorr += 1
		self.refresh()
		self.save()

	def refresh(self):
		self.text_to_save = "{}\t{}\t{}".format(self.total, self.corr, self.incorr)
		self.ref_lab()

	def ref_lab(self):
		self.l1.configure(text=self.text_to_save)
		self.l1.grid(column=3, row=0)

	def save(self):
		# self.text_to_save = "{}\t{}\t{}".format(self.total, self.corr, self.incorr)
		with open("tcount.txt", "w") as file:
			file.write(self.text_to_save)
	
	def reset_count(self):
		
		self.text_to_save = "0\t0\t0"
		self.ref_lab()
		self.save()
		self.recount()

	def copy(self):
		with open("tcount_copied.txt", "a") as file:
			file.write("{}\n".format(self.text_to_save))






if __name__ == '__main__':
	a = tcount()