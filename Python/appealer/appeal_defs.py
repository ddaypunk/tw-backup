def printAppealerTitle():
	print "\t********************************************"
	print "\t\tWelcome to the Appealer Tool"
	print "\t********************************************"


def printAppealerMenu():
	print("1: SSL against IP")
	print("2: SSH against IP by port")

def sslMode():
	print " "
	print "***Open SSL Mode***"
	print " "
	strAddress = raw_input("Please enter the IP address you would like to run OpenSSL against: ")
	print strAddress + " is the IP Address you entered."
