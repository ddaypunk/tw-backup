#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


con = mdb.connect('localhost', 'root', '', 'generator');

with con: 

    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    for row in rows:
        print row