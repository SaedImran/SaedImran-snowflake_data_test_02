
#!/usr/bin/env python
import snowflake.connector
import pandas as pd

# import snowflake as sf
# from snowflake import connector

#Gets the version
ctx = snowflake.connector.connect(
    user='simran',
    password='Tnk-17cv###',
    account='ov18267.eu-central-1',
    warehouse= 'COMPUTE_WH',
    database='TEST_SAED',
    schema= 'PUBLIC'
    )
conn = ctx.cursor()
# try:
#     conn.execute("SELECT current_version()")
#     one_row = conn.fetchone()
#     print(one_row[0])

# finally:
#     conn.close()
#      ctx.close()



# conn.execute("SELECT * FROM RAW_GIT_DATA_TABLE")
# one_row = conn.fetchone()
# print(one_row)


# create test table and insert data
# conn.execute( "CREATE OR REPLACE TABLE test_GIT_table(col1 integer, col2 string)" )
# conn.execute( "INSERT INTO test_GIT_table(col1, col2) VALUES " 
# + " (123, 'test string1'), " 
# + " (456, 'test string2')")

# conn.execute("SELECT * FROM test_GIT_table")


# df = pd.read_sql('select * from IT_SERVICEBERICHTE.AFA.TARGET_AFA limit 20;', con = conn)

conn.execute("SELECT * FROM test_GIT_table")
results = conn.fetchall()
for n in results:
    print(n, 'fetch all data')

# create test 2nd table and insert data
conn.execute( "CREATE OR REPLACE TABLE test_GIT_table_Contact(CodeNo integer, Name string, City string, Email string)" )

conn.execute( "INSERT INTO test_GIT_table_Contact(CodeNo , Name , City , Email ) VALUES " 
+ " (20178, 'Fabian S.',    'Fabian.Schleizer@funkemedien.de',   'Erfurt'), " 
+ " (20178, 'Axel S.',      'Axel.schramm@funkemedien.de',       'Essen'), " 
+ " (20182, 'Sebastian W.', 'Sebastian.Wirries@funkemedien.de',  'Braunschweig'),"
+ " (20196, 'Ali T.',       'Ali.Thaifa@funkemedien.de',         'Braunschweig')"
)