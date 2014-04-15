"""
The below script will:
-open an existing db
-insert entries from predefined CSV file

Be sure to edit this script each time this is used.
"""

import csv
import sqlite3

# Create the connection
# Create the cursor
# Open or create the DB if it doesn't exist

with sqlite3.connect("steamgen.db") as connection:
    cursor = connection.cursor()

# Open the csv
# INSERT values from CSV into DB

    csv_file = csv.reader(open("races_initial.csv", "rU"))

    cursor.executemany("INSERT INTO races(race_id, race_name, race_allowed_archetypes, race_start_languages, race_add_char1, race_add_char2, race_add_char3, race_add_char4, race_add_char5, race_start_stat_id, race_hero_stat_id, race_vet_stat_id, race_epic_stat_id)\
                         values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", csv_file)


# When done, close the connection
connection.close()