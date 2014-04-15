""" Python Doubler 
This will take a number x, and add a doubled amount each time
This was solved by using powers of 2 in a loop

Returns: compounded powers of 2 up to x

This was a project idea from a website based on the fable
of the inventor of chess and the king of India"""

__author__ = "Andrew Delso"


def doubler(x):
	total = 0
	for each in range(0,x):
		print "2^" +str(each)+": \t\t  " + str(2**each)
		print "Total before: \t+ " + str(total)
		total += 2**each
		print "Total after: \t= " + str(total)
		print " "

	return total

""" howManyCars computes how
many rail cars are needed to transport
an amount of rice.

Conversion: 
32,000,000 grains = 1 short ton
50 tons = 1 rail cars

Returns: Formatted string answer"""

def howManyCars(amount):
	return str((amount / 32000000) / 50) + " cars needed to transport rice"


#Testing
#print doubler(64)
#print str(2**64) + " is 2^64"
#print howManyCars(doubler(64))