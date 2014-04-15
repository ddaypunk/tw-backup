"""
Class: Udacity CS 101
Project: Webcrawler
Status: In progress
"""

#------------#

#Extracting Links proceedure

def extract_link(x):
	start_link = x.find(x.find('<a href=')) #find the first quote of an href using the location of the href
	
	if start_link == -1: #send back special values if no further URL's found
		return None, 0 #None has a Bool value of False
	start_quote = x.find('"', start_link)
	end_quote = x.find('"',start_quote + 1) #find the end quote of the href
	url = x[start_quote+1:end_quote]
	return url, end_quote #return the url between the "s and the end quote location

#------------#

def print_all_links(page):
	while True:
		url, endpos = extract_link(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

#------------#

def get_all_links(page):
	#create empty list to return
	links = []
	#loops is structured to exit using else with break
	#find urls and save to list, while updating the page position
	while True:
		url, endpos = extract_link(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	#return the list of links
	return links

#-------------#

def find_element(lister, query):
    if query not in lister:
        return -1
    return lister.index(query)

def union(a,b):
    for i in b:
        if i not in a:
            a.append(e)    

#-------------#

def web_crawl(seed, max_pages):
	to_crawl = [seed]                                         # = pages found that need to be crawled
	crawled = []                                              # = pages that have been crawled
	next_depth = []
	index = []
	depth = 0                                            
	while to_crawl:                                           # while to crawl is not empty
		page = to_crawl.pop()                                 # pick a page to_crawl next
		if page_link not in crawled and len(crawled) < max_pages: # check that we have not crawled the page yet
		    content = get_page(page)                          #get the page content
		    add_page_to_index(index,page,content)             #add all content words to the index with the URL
			union(to_crawl,get_all_links(content)             # add all links from the page content
			crawled.append(page)                              # add that page to crawled list
		if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
	#return crawled                                            # send back the list
    return index
#-=-=-=-=-=-=-=-=-#

def lookup(index, keyword): #used to look up a particular keyword in an index
	for each in index:
		if each[0] == keyword:
			return each[1]

def add_to_index(index,keyword,url): #adds a keyword and associated URL to the index
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content): #prepares the content from a URL to be added to the index
	temp_list = content.split()
	for each in temp_list:
		add_to_index(index,each,url)