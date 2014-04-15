"""
CODE ACADEMY NOTES - MAR 3	
"""

""" Lists """

#the following will add a value to the end of a list
list_name.append(value)

#the follwing will add a list to the end of a list
list_name.extend(value)
#alternately using append
for each in list_name2:
	list_name1.append(each)

#the following will search for a value in list, returns position
list_name.index(value)

#the following will insert a value into the list at a position
list_name.insert(pos,value)
#moves all items from pos and back, forward one space or pos+1

#remove the value from the list
list_name.remove(value)

#the following will sort a list in increasing alpha/num order
list_name.sort()
#does not return a list, replaces list_name

#get the total items in a list
len(list_name)

""" Dictionaries """

dict_name = {'key1': value1, 'key2': value2, ...}

#adds new key/value pair to dictionary
dict_name[new_key] = new_value

#deletes key and value at supplied key
del dict_name[key]

#dictionaries do not seem to have += opperators

""" Arbitrary number of args example """
m = 5
n = 13
def myFun(*args):
	return sum(args)