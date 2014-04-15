"""
Name: findSqrt
Input: takes single argument (argv[1]) after script from command line
Returns: Formatted output stating the square root
with checking statement and disclaimer
Improvements: this could probably recursively call itself for proper precision
or add more iterations to it
"""
__author__ = "Andrew Delso"

import sys

def findSqrt(x):
	count = 0

	#first find the upper and lower bounding perfect squares
	while count**2 < x-1:
		count += 1
		
	lowerBase = count
	#print lowerBase
	upperBase = count+1
	#print upperBase

	#then divide x by nearer of the perfect squares
	if (x - lowerBase**2) < (upperBase**2 - x):
		firstIteration = x / float(lowerBase)
		#print firstIteration
		average = (firstIteration + lowerBase) / 2
		#print average

	else:
		firstIteration = x / float(upperBase)
		average = (firstIteration + upperBase) / 2

	secondIteration = x / average
	#print secondIteration

	average2 = (secondIteration + average) / 2

	thirdIteration = x / average2
	#print thirdIteration

	result =  (thirdIteration + average2) / 2

	print " "
	print "The square root of ("+ str(x) +") is " + str(result)
	print "The result of " + str(result) + " squared is " + str(result**2) +" *"
	print " "
	print " "
	print "* = Uses three iterations of algorithm for precision;"
	print "    however, square of result is not fully accurate."
	print " "

findSqrt(int(sys.argv[1]))