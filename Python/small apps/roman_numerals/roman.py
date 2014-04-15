"""
Roman numeral conversion
Info: http://www.novaroma.org/via_romana/numbers.html
"""

def RomanToDec(roman_number):
	decimalNum = 0
	numArray = list(roman_number)
	current = ''
	next = ''
	i = 0

	while roman_number:
		current = [i]
		next = [i+1]

		if current == 'I':
			if next == 'V':
				decimal += 4
			elif next == 'X':
				decimal += 9
			elif next == 'L':
				decimal += 49
			elif next == 'C':
				decimal += 99
			elif next == 'D'
				decmial += 499
			elif next == 'M':
				decimal += 999
			else:
				decimal += 1

	return numArray


print RomanToDec('IXV')