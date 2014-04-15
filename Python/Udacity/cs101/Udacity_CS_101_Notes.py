#Python Notes

#Commands/operators/operations

print #is what it sounds like
str(<expression>) #converts an expression resolving to a number into a str

def proc_name(input,input2,inputx): #the ":" denotes anytime a block of code will follow
	code
	code2
	code3 = code + code2
	return code3, code2

if <expression>:
	<block>
else:
	<block>

<expression> or <expression> #will not evaluate the second expression if the first evaluates to true
<expression> and <expression>

#****LISTS****#

<list> = [<expression>,...,<expression>] #lists are mutable (able to be mutated) and nested lists are possible

#integers are not mutable, meaning procedures can not change paramater values of integers.  Lists can be changed by procs

<list>.append(<element>) #appends an element to the end of the list

<list> + <list> #does not mutate, creates a new list
len(<list>) #returns length (total elements in) of a list, but only counts the outer layer of elements, not elements of nested lists
            #can be used on strings as well

<list>.index(<value>) #returns the index of the first location of the value

<value> in <list> #"is 3 in the list" returns bool

<list>.pop() -> element #removes and returns the last element in a list

<string>.split() -> [<word>, <word>, ...]

"""
asdf
asdf
asdf
"""
#triple quotes are used to divide strings over multiple lines

try: #try this, but if it fails, move to except
	pass
except Exception, e:
	raise
else:
	pass
finally:
	pass
#****LOOPS****#

#while loop

while <expression>: #loops while expression is true
	<block>
	break #break from the loop (use when needed), generally in if statement

#for loop

for <name> in <list>:
    <block>

    #each element in the list is assigned to i for each loop through

#exponents

x ** y
2**10 = 1024 = 1KB
2**20 = 1MB
2**30 = 1GB
2**40 = 1TB

#------------#

#looks like it has no types like in Ruby so:
#ex
hour = 1
minutes = hour * 60
seconds = minutes * 60

hundreths = seconds * 1.0/100 #the 1.0 will cause printing of this value to show .00 as python truncates automatically

#------------#

#Extracting Links

page = #input stream of a website

start_quote = page.find('"',page.find('<a href=')) #find the first quote of an href using the location of the href
end_quote = page.find('"',start_quote + 1) #find the end quote of the href
url = page[start_quote+1:end_quote] #store the url between the "s
print url, end_quote

#these look as though they can be all combined as such

print page[((page.find('"',page.find('<a href='))+1)):page.find('"',(page.find('"',page.find('<a href=')) + 1))]

#this works at http://try-python.appspot.com/, but is hard to read, stick with variables


#Rounding numbers

x = #a decimal number

x = x + 0.5 #this will cause any number with a tenths digit of .5 or higher to round up

y = str(x) #convert item to string value

pt = y.find('.') #find the location of the decimal

print y[:pt]

#in one line this would be

print str(x+0.5)[:str(x+0.5).find('.')]


