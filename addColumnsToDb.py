#! /usr/bin/python3
# addColumnsToDb.py - adds a two new columns to the events_1 table, and sets the default value for the new column rows for  for the 2nd column


# sources
# http://www.thegeekstuff.com/2013/02/wc-nl-examples/
# http://serverfault.com/questions/375096/bash-sed-awk-etc-remove-every-other-newline
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

import sqlite3


#DROP_CONNECTIONS_SQL = 'DROP TABLE IF EXISTS events_1'
sqlite_file = 'connections_db.sqlite'    # name of the sqlite database file
table_name = 'events_1'   # name of the table to be created
id_column = 'connection_number' # name of the PRIMARY KEY column
new_column1 = 'date_1'  # name of the new column
new_column2 = 'time_1'  # name of the new column
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = 'Hello World' # a default value for the new column rows






# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
#c.execute(DROP_CONNECTIONS_SQL)

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name, cn=new_column1, ct=column_type))

# B) Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
        .format(tn=table_name, cn=new_column2, ct=column_type, df=default_val))

# Committing changes and closing the connection to the database file
conn.commit()
c.execute('SELECT * FROM events_1')
conn.close()