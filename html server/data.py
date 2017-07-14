import psycopg2
# from config import config
 

conn = psycopg2.connect(database="test", user="nirali",host="localhost", password="nirali", port="5432") 
print "Opened database successfully"

cur = conn.cursor()
cur.execute("create table data(username varchar,password varchar);")

conn.commit()

conn.close()
