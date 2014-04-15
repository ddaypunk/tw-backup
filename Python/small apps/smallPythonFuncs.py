"""
Small python functions
"""

def squareSum(numArray):
	#make storage for squared numbers, square them and append
	resultArray = []
	for each in numArray:
    	resultArray.append(each**2)
    
    #print out using reduced list with lambda function to sum
	print reduce(lambda x,y: x+y, resultArray)

