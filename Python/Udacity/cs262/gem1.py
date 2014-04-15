def findmax(in_list, func):
	best_element = None
	f_value = None

	for each in in_list:
		f_value = func(each)
		if best_element == None or f_value > func(best_element):
			best_element = each