#! /usr/bin/python3
# createSqliteFromText.py - created an sql lite database from a text file
# use use ch02_database, ch03_oo/starter/create_documents_db.py
# sources
# http://www.thegeekstuff.com/2013/02/wc-nl-examples/
# http://serverfault.com/questions/375096/bash-sed-awk-etc-remove-every-other-newline
# http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html

from subprocess import call

import csv
import time
import sqlite3

path = '/Users/mnobile/PycharmProjects/ClamPy/PreClass/betaTest5.txt'

sqlite_file = 'connections_db.sqlite'    # name of the sqlite database file
table_name1 = 'connection_events'

INSERT_RECORD = '''INSERT INTO connection_events(connection_number, date_1, time_1, date_2, time_2, action_1, Reason_1,
              Reason_2, ip_1, misc_1, misc_2, misc_3, misc_4, misc_5, misc_6, ip_2, sz_1, sz_2,
              port_1, data_1, misc_7, proto_1, port_2, misc_8, proto_2, misc_9, misc_10, misc_11, misc_12,
              proto_3, proto_4, misc_13, misc_14, misc_15, misc_16, proto_5, proto_6, client_1, risk_1, risk_2, vlan,
               file_1, ac_policy, ac_rule, nap_1, nap_2, nap_3, nap_4, device, int_1, int_2) VALUES (?,?,?,?,?,?,?,?,?,
               ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
DROP_CONNECTIONS_SQL = 'DROP TABLE IF EXISTS connection_events'

"""
 , date1 VARCHAR(30), time1 VARCHAR(15), date2 VARCHAR(30)), time2 VARCHAR(15), action VARCHAR(15),
  reason VARCHAR(15), ip1 VARCHAR(15), userView VARCHAR(15), auth VARCHAR(30), ip2 VARCHAR(15), sz1 VARCHAR(15),
   sz2 VARCHAR(15), port1 VARCHAR(15), protoData1 VARCHAR(15), proto1 VARCHAR(15), port2 VARCHAR(15),
    proto2 VARCHAR(15), appView1 VARCHAR(30), protoData2 VARCHAR(15), appView2 VARCHAR(30), protoData3 VARCHAR(15),
     client VARCHAR(15), risk1 VARCHAR(15), risk2 VARCHAR(15), vlan VARCHAR(15), file VARCHAR(15)
INSERT_RECORD = INSERT INTO connections(connections_id, fullname, date1, time1, date2, time2, action, reason, ip1,
 userView, auth, ip2, sz1, sz2, port1, protoData1, proto1, port2, proto2, appView1, protoData2, appView2, protoData3,
  client, risk1, risk2, vlan, file, 29, 30, 31, 32, 33) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
"""
# this puts all the data from the text file, and puts it into a list. THIS works
connection_data = []
try:
    with open(path, encoding='utf8') as f:
        try:
            for row in csv.reader(f):
                connection_data.append(row)
        except csv.Error as e:
            print('Error: {err}'.format(err=e))
except IOError as e:
    print(e)
print(connection_data)


connection_data = connection_data[1:]
# need to add a blank line to the first line of the text document
connection = None
try:
# changing line below to try to get it to work
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()
    cursor.execute(DROP_CONNECTIONS_SQL)

    cursor.execute('''CREATE TABLE connection_events
             (connection_number TEXT, date_1 TEXT, time_1 TEXT, date_2 TEXT, time_2 TEXT, action_1 TEXT, Reason_1 TEXT,
              Reason_2 TEXT, ip_1 TEXT, misc_1 TEXT,
             misc_2 TEXT, misc_3 TEXT, misc_4 TEXT, misc_5 TEXT, misc_6 TEXT, ip_2 TEXT, sz_1 TEXT, sz_2 TEXT,
              port_1 TEXT, data_1 TEXT, misc_7 TEXT, proto_1 TEXT,
             port_2 TEXT, misc_8 TEXT, proto_2 TEXT, misc_9 TEXT, misc_10 TEXT, misc_11 TEXT, misc_12 TEXT,
              proto_3 TEXT, proto_4 TEXT, misc_13 TEXT, misc_14 TEXT, misc_15 TEXT,
             misc_16 TEXT, proto_5 TEXT, proto_6 TEXT, client_1 TEXT, risk_1 TEXT, risk_2 TEXT, vlan TEXT, file_1 TEXT,
              ac_policy TEXT, ac_rule TEXT, nap_1 TEXT, nap_2 TEXT, nap_3 TEXT,
             nap_4 TEXT, device TEXT, int_1 TEXT, int_2 TEXT)''')




    cursor.executemany(INSERT_RECORD, connection_data)

    connection.commit()
#    cursor.execute('Select * from connections.db')
    print('Data loaded into schools table')
except sqlite3.Error as e:
    if connection:
        connection.rollback()
    print('Data not loaded into schools table')
    print('Error: {0}'.format(e))
finally:
    if connection:
        connection.close()
