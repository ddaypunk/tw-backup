import sqlite3

connect = sqlite3.connect("cars.db")

cursor = connect.cursor()

cursor.execute("""CREATE TABLE inventory
	             (Make TEXT, Model TEXT, Quantity INT)""")

connect.close()