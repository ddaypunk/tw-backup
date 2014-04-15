#used to import regular expressions
import re


#this is how regular expressions are rep in python
r"a" #just look for 'a'
r"[0-9]"
r"[a-c][1-2]"
r"a+" #as many a's as you can find in a row
r"[0-1]+" #as many 1 or 0's as you can find in sequence
r"[a-z]+|[0-9]+" #using a disjunction (OR)
r"-?[0-9]+" #find positive or negative numbers
r"\+\+" #you can use escape sequences in regexps too
r"[0-9].[0-9]" # "1a1 222 cc3" ==> 1a1 222
r"[0-9][^ab]" # "1a1 222 cc3" ==> 1 22 2
r"(?:xyz)+" #find 
r'"(?:[^\\]|(?:\\.))*"' #will find double quoted strings with double quotes in them


#maximal munch, regular expressions should find biggest first

#find something using a regular expressions

re.findall(r"[0-9]","1+2==3")
#==> ['1','2','3']

#options
r"+" #one or more copies
r"?" #means optional; previous thing one or zero times
r"*" # zero or more copies
r"." #any character except a newline
r"^" #anything except what follows

--------------
#sum all numbers in a string
import re
def sumnums(sentence):
    regexp = r'[0-9]+'
    total = 0
    
    if nums == 0:
        return 0
    else:
        for each in re.findall(regexp,sentence):
            total += int(each)
        return total

-------------
#Python token definition examples for HTML tokens
#A group of tokens is a Lexical Analyzer or a Lexer
#Ordering of the tokens is very important

def t_LANGLE(token):
	r'<'
	return token

def t_LANGLESLASH(token):
	r'</'
	return token

def t_RANGLE(token):
	r'>'
	return token

def t_STRING(token):
	#multiword strings with no symbols
    r'\"(?:(?:[a-z]|[A-Z]) ?)+\"' #my answer
    r'\"[^"]*\"' #prof's answer
    token.value = token.value[1:-1] #snip off the quotes
    return token

def t_WHITESPACE(token):
	r' '
	pass #passes a space by

def t_WORD(token):
	#pass up < and >, don't change value
	r'[^<> ]+'
	return token

------------

#add this to change the value of the token from a string
token.value = int(token.value)

#example where token = "1389"
def t_NUMBERED(token):
	r'[0-9]+'
	token.value = int(token.value)
	return token
#returns the integer value of the string fitting the re

#you can also import the python lexical analyzer and specify the tokens
#you want

import ply.lex as lex

#specify list of which are important
tokens = (
	'LANGLE', #<
	'LANGLESLASH', #</
	'RANGLE', #>
	'EQUAL', #=
	'STRING', #"asdf asdf"
	'WORD',#asdf
	)
t_ignore = ' '

#then list the definition of each from above

#example of using this
webpage = "This is <b>my</b> webpage!"
htmllexer = lex.lex()
htmllexer.input(webpage)

while True:
	tok = htmllexer.token()
	#when out of tokens, break out
	if not tok: break
	print tok
