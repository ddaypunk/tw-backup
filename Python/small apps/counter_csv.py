import csv

row_count = 1
with open('file1.csv','rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print "Row " + row_count + " count: " + str(len(row))
