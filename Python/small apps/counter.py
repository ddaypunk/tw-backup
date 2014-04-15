"""
Character Counter
By: Andrew Delso

Function: For use with the QA - Data Mart Reporting - 
Canned Reports - "DSC Data Sync - Number Filter"

Input: Copy and pasted string from Excel Reports

Output:
1. Count of total characters in the string
2. Count of total account numbers in the string
"""


string_entry = raw_input("Enter string: ")

#print out input string length of total characters
print "\nCharacters: " + str(len(string_entry))

# Print the len of the list of the split input string
print "\nAccounts: " + str(len(string_entry.split(',')))