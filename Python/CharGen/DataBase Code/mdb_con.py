#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

#initialize connetion to None
con = None

try:
#first try to connect to the generator database
	con = mdb.connect('localhost','root','','generator');

	#set the cursor and issue the SQL command for version
	cur = con.cursor()
	cur.execute("SELECT VERSION()")

	#fetch and print the line returned
	data = cur.fetchone()
	print "database version : %s" % database

except mdb.Error, e: 
#exception for when DB errors, and exit python
	print "Error %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)

finally:
#final step to close data connection to DB
	if con:
		con.close()