"""
The below script will:
-open/create a database in sqlite3
-create table within the db with specific fields

Be sure to edit this script each time this is used.
"""

import sqlite3


# Create the connection
# Create the cursor
# Open or create the DB if it doesn't exist

with sqlite3.connect("steamgen.db") as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE races
	                (race_id INTEGER PRIMARY KEY, 
	                 race_name TEXT,
	                 race_allowed_archetypes TEXT,
	                 race_start_languages TEXT,
	                 race_add_char1 TEXT,
	                 race_add_char2 TEXT,
	                 race_add_char3 TEXT,
	                 race_add_char4 TEXT,
	                 race_add_char5 TEXT,
	                 race_start_stat_id INTEGER,
	                 race_hero_stat_id INTEGER,
	                 race_vet_stat_id INTEGER,
	                 race_epic_stat_id INTEGER,
	                 FOREIGN KEY(race_start_stat_id) REFERENCES race_stats(race_stat_id),
	                 FOREIGN KEY(race_hero_stat_id) REFERENCES race_stats(race_stat_id),
	                 FOREIGN KEY(race_vet_stat_id) REFERENCES race_stats(race_stat_id),
	                 FOREIGN KEY(race_epic_stat_id) REFERENCES race_stats(race_stat_id)
	                 )""")

# When done, close the connection
connection.close()