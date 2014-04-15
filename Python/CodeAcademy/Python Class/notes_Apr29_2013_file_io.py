#opening a file
var = open("file_name", "access_type")
#w = write
#r+ = read and write
#r = read only

#write to a file (one line at a time)
var.write("string_expression")

#read the file
#this will read the entire file
var.read()

#this will read and print the entire file to the output console
print var.read()


#read one line at a time
#this will include a newline between reads
var.readline()


#close the file
var.close()

"""simple example use"""

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

"""getting python to take care of file closes"""
#while this file is open as a name, do something.  After, close.
with open("text.txt", "w") as textfile:
	textfile.write("Success!")
#check that it is truly closed
if my_file.closed == False:
    my_file.close()
#output that status    
print my_file.closed