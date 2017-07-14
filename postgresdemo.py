
print "kkkkkkkkkkkkkkkkkkkkkkkkkk"
import psycopg2

con = psycopg2.connect(database='project_task',user='nirali',password='nirali',host='localhost',port='5432' )
print "Connection Successfully"

cur = con.cursor()
cur.execute('select * from sale_order')
res = cur.fetchall()
print res


cur.execute('select name,state from sale_order')
result1 = cur.fetchall()
print result1



cur.execute("update sale_order set state='draft' where id=27")
con.commit()
print " \n \n \n \n \n \n Record Updatedddddddddddddddddddddddddddddddddddddddddddddddddddddd"


cur.execute('select * from account_invoice')
con.commit()
resssss = cur.fetchall()
print resssss



#cur.execute("INSERT INTO account_invoice VALUES (25,2)")
#con.commit()

#print "Record Inserted"

print "Close Connection"
cur.close()
con.close()




