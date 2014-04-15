"""
CODE ACADEMY NOTES - MAR 4
"""

""" Range function """

#runs from 0 -> x
range(x)

#runs from X -> y
range(x,y)

#runs from x -> y, at z increments
range(x,y,z)

---
#takes tuple of args and appends(extends) them all into one list

m = [1,2,3]
n = [4,5,6]
o = [7,8,9]

def myFun(*args):
	longList = []
	for each in args:
		longList.extend(each)
	return longList

print myFun(m,n,o)