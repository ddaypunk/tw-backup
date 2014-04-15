"""
barista-menu procs
by: Andy Delso
To be used with the Barista-matic main program flow
"""

#Proceedure Definitions
def printHeader(): #procedure to print the title of the app
	print "****** Barista-Matic ******"
	print "Your daily dose of caffeine"

def printInventory(n1, n2, n3, n4, n5, n6, n7, n8, n9): #procedure to print the current inventory status
	print "Inventory:"
	print "Cocoa," + str(n1)
	print "Coffee," + str(n2)
	print "Cream," + str(n3)
	print "Decaf Goffee," + str(n4)
	print "Espresso," + str(n5)
	print "Foamed Milk," + str(n6)
	print "Steamed Milk," + str(n7)
	print "Sugar," + str(n8)
	print "Whipped Cream," + str(n9)

def printMenu(): #procedure to print out the menu with prices
    print "Menu:"
    print "1,Caffe Americano,$"