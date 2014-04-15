import ply.lex as lex

#specify list of which are important
tokens = (
	'LANGLE', #<
	'LANGLESLASH', #</
	'RANGLE', #>
	'EQUAL', #=
	'STRING', #"asdf asdf"
	'WORD',#asdf
	'EQUAL',#=
	'NEWLINE',#\n
	'ERROR', #Error
	'IDENTIFIER',#var_name
	'NUMBER', #-12.123
	'EOLCOMMENT' # //comment
	)

#create a state for when an html comment is encountered
states = (('htmlcomment', 'exclusive'),)

t_ignore = ' '

#then list the definition of each from above

#if I find a comment, go exclusive
def t_htmlcomment(token):
	r'<!--'
	token.lexer.begin('htmlcomment')

#when you find the end of the comment, switch back to INITIAL state
def t_htmlcomment_end(token):
	r'-->'
	#make sure to count the new lines as we won't have that in this state
	token.lexer.lineno += token.value.count('\n')
	token.lexer.begin('INITIAL')

#all other characters curing comment mode are errors and should be skipped
def t_htmlcomment_error(token):
	token.lexer.skip(1) #pass


def t_LANGLESLASH(token):
	r'</'
	return token

def t_LANGLE(token):
	r'<'
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

#def t_WHITESPACE(token):
	#r' '
	#pass #passes a space by

def t_WORD(token):
	#pass up < and >, don't change value
	r'[^<> \n]+'
	return token

def t_EQUAL(token):
	r'='
	return token

def t_NEWLINE(token):
	r'\n'
	token.lexer.lineno += 1
	pass

def t_ERROR(token):
	r'\s'
	return token

def t_IDENTIFIER(token):
	#ex a_zone
	r'[a-zA-Z][a-zA-Z_]*]'
	return token

def t_NUMBER(token):
	r'-?[0-9]+(?:\.[0-9]*)?'
	token.value = float(token.value)
	return token

def t_EOLCOMMENT(token):
	r'//[^\n]*'
	pass

""" ====================================== """

#example of using this
webpage = "hello <!-- comment --> all!"
#create lexer object
htmllexer = lex.lex()
#set lexer input to our webpage
htmllexer.input(webpage)

#while there are lines in the page
while True:
	#token is the first token the lexer finds
	tok = htmllexer.token()
	#when out of tokens, break out
	if not tok: break
	#print the current token line
	print tok

#DEFAULT FORMAT==> LexToken(TOKEN_NAME,FOUND_ITEM,LINE,CHARACTER)
#EXAMPLE OUTPUT==> LexToken(WORD,'This',1,0)
