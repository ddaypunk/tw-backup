def split_string(source,splitchars):
	i=0 #source string position iterator
	pos=0 #position in the string for the beginning of the next load to the return string
	ret_str = [] #the string to return at the end

	while i < len(source):
		j=0 #split condition loop iterator
		while j < len(splitchars):
			if source[i] == splitchars[j]:
				ret_str[i] = source[pos:j]
				pos = j
				break
        i = i + 1
    print ret_str



This is only, a test - give up now!
- + = , . ! ?

source = "This is only, a test - don't give up now!"
splitchars = ["-", "+", "=", ",", ".", "'", "!", "?", " "]
i=0
pos=0
ret_str=[]