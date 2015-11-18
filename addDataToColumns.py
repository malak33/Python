#! /usr/bin/python3
# addDataToColumns.py - below will add data to connection_number column and the date_1 column. 3 different examples


# sources
# http://www.thegeekstuff.com/2013/02/wc-nl-examples/
# http://serverfault.com/questions/375096/bash-sed-awk-etc-remove-every-other-newline
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

import sqlite3


# below will add data to connection_number column and the date_1 column. 3 different examples
sqlite_file = 'connections_db.sqlite'
table_name = 'events_1'
id_column = 'connection_number'
column_name = 'date_1'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# A) Inserts an ID with a specific value in a second column
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (12345678, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

# B) Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
        format(tn=table_name, idf=id_column, cn=column_name))

# C) Updates the newly inserted or pre-existing entry
c.execute("UPDATE {tn} SET {cn}=('Hi World!!!') WHERE {idf}=(123456)".\
        format(tn=table_name, cn=column_name, idf=id_column))

conn.commit()
#print(c.execute('SELECT * FROM events_1'))
conn.close()