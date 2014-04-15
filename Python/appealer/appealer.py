from subprocess import call
from appeal_defs import *

while True:
	printAppealerTitle()
	printAppealerMenu()
	menu_choice = raw_input ("Which task would you like to run?: ")

	#simulated switch-case based on menu_choice
	if menu_choice == "1":
		sslMode()

	#Example of call statement
	#call(["ls", "-l"])

	#loop back check and break
	strChoice = raw_input("Would you like to issue another task? (y/Y/n/N): ")
	if strChoice == "n" or strChoice == "N":
		break