import urllib2
from collections import OrderedDict

#the following opens the URL source and counts characters in the code block
#the block is designed around what is seen on the page.
#more elaborate code needed to detect the code (probably with regexp)

url = 'http://www.pythonchallenge.com/pc/def/ocr.html' # write the url here

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

catalog = OrderedDict() #changed this to use OrderedDict so that it would
                        #spell the word correctly

search_block = data[data.index('%'):-3]
#print ''.join([x for x in search_block if x.isalpha()])
#print search_block[:10]

for char in search_block:
	if char in catalog:
		catalog[char] += 1
	else:
		catalog.update({char:1})

rare_chars = ""


for each in catalog:
	if catalog[each] == 1:
		rare_chars += each

print rare_chars

#alternate method with a counter object

#cnt = Counter()
#for character in search_block:
#	cnt[character] += 1
#
#print cnt
