import mysql.connector
from crypto import cryptography as e

mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
cursor = mydb.cursor()
cursor.execute('SELECT * FROM users;')
d=cursor.fetchone()
print(e.decrypt(d[0]))
print(e.check('administrator',d[1]))
print(cursor.rowcount, "record inserted.")

cursor.close() 
mydb.close()
