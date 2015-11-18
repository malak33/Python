#! /usr/bin/python3
# createDb.py - this creates a database file, a table called events_1, if the table exists already it deletes it , and
# create a table called events_2, and sets the first column as the primary key


# sources
# http://www.thegeekstuff.com/2013/02/wc-nl-examples/
# http://serverfault.com/questions/375096/bash-sed-awk-etc-remove-every-other-newline
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

import sqlite3

# this creates a database file, a table called events_1, if the table exists already it deletes it.
# create a table called events_2, and sets the first column as the primary key
DROP_CONNECTIONS_SQL = 'DROP TABLE IF EXISTS events_1'
sqlite_file = 'connections_db.sqlite'    # name of the sqlite database file
table_name1 = 'events_1'  # name of the table to be created
table_name2 = 'events_2'  # name of the table to be created
new_field = 'connection_number' # name of the column
field_type = 'INTEGER'  # column data type

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute(DROP_CONNECTIONS_SQL)

# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=new_field, ft=field_type))

# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
        .format(tn=table_name2, nf=new_field, ft=field_type))

# Committing changes and closing the connection to the database file
conn.commit()
c.execute('SELECT * FROM events_1')
conn.close()