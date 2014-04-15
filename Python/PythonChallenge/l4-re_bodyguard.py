import re
import urllib2

url = 'http://www.pythonchallenge.com/pc/def/equality.html' # write the url here

usock = urllib2.urlopen(url)
data = usock.read()
usock.close()

#looking for something like ABCdEFG
regexp1 = re.compile(r'[A-Z]{3}[a-z][A-Z]{3}')

regexp1.match(data)