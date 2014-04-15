"""
PYGLATIN
"""

print "Welcome to the English to Pig Latin translator!"

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
	word = original.lower()
	first = word[0]
	
	#if it begins with a vowel, add translator
	if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u'):
		new_word = word + pyg
	#if it is not a vowel, move first letter to end, then add translator	
	else:
		new_word = word[1:len(word)]
		new_word = new_word + word[0] + pyg
	print new_word
else:
	print 'empty'