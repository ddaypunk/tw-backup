"""
script: datediff

Input: two strings
Output: strings

Function: Takes two dates as input and then outputs the number
			of days between the two.
"""

from datetime import date

#Take input of two dates and split them
start_parts = raw_input("Enter Start Date (YYYY/MM/dd): ").split('/')
end_parts = raw_input("Enter End Date(YYYY/MM/dd): ").split('/')

#Create date objects with the split data
start_date_obj = date(int(start_parts[0]),int(start_parts[1]),int(start_parts[2]))
end_date_obj = date(int(end_parts[0]),int(end_parts[1]),int(end_parts[2]))

#Compute number of days between regardless of arrangement and print
print str(abs((end_date_obj - start_date_obj).days)) + " days between provided dates"