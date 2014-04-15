class Customer:
	"""A class to hold all data related to a customer"""
	#define the initialization of a customer
	def __init__ (self, customer_number, bridename, groomname, surname, address, weddate):

		self.customer_number = customer_number
		self.bridename = bridename
		self.groomname = groomname
		self.surname = surname
		self.address = address
		self.weddate = weddate

	def printCustomer(self):
		print "\t" + self.surname + " Wedding Information | Customer Number: " #+ self.customer_number
		print "\t" + "========================"
		print "\t" + "Bride's Name: " + self.bridename + " " + self.surname
		print "\t" + "Groom's Name: " + self.groomname + " " + self.surname
		print "\t" + "Address: " + self.address
		print "\t" + "Wedding Date: " + self.weddate

