def PrintCustManMenu():
	print "\tWelcome to Python Customer Manager"
	print "\t=--------------------------------="
	print " "
	print "\t1. Add a new customer"
	print "\t2. Edit an existing customer"
	print "\t3. Show customer"
	print "\t4. Show all active customers"
	print "\t5. Show all closed/completed customers"
	print "\t6. Show ALL customers"
	print "\t7. Remove a customer"
	print "\t8. Exit"
	print " "
	AcceptMenuChoice()

def AcceptMenuChoice():
	choice = raw_input ("Please make a selection using the menu item number only: ")

	if choice == "1":
		print "Adding customer..."

	elif choice == "2":
		print "Editing customer..."
	
	elif choice == "3":
		print "Showing specified customer..."
	
	elif choice == "4":
		print "Showing all active customers..."

	elif choice == "5":
		print "Showing all closed customers..."

	elif choice == "6":
		print "Showing full customer inventory..."

	elif choice == "7":
		print "Customer removed"

	elif choice == "8":
		print "Exiting app"

	else:
		print "Invalid choice, please choose again"
