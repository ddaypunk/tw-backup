#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

#create connection to generator DB
con = mdb.connect('localhost', 'root', '', 'generator');

with con:
    
    #set cursor and create table if it does not exist
    #this will not be needed for reference tables, but will be
    #for creating a character
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS \
        Writers(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(25))")

    #insert rows into created DB
    cur.execute("INSERT INTO Writers(Name) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(Name) VALUES('Truman Capote')")