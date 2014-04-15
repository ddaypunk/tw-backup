"""
Class and Method definitions for notepad
"""

class Note:
	def __init__ (self,date,text):
		self.date = date
		self.text = text



class Notepad():
	def __init__(self):
		self.page = []