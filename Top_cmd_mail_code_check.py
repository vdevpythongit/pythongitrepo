import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')
cur = conn.cursor()
chunksize = 6
for chunk in pd.read_csv('username.csv', chunksize = chunksize):
    chunk.columns = chunk.columns.str.replace(',', '_') #replacing spaces with underscores for column names
    chunk.to_sql(name='Table1', con=conn, if_exists='replace')
cur.execute('SELECT Username FROM Table1')
names = list(map(lambda x: x[0], cur.description)) #Returns the column names
print(names)
for row in cur:
    print(row)
cur.close()