import mysql.connector
from crypto import cryptography as e
mydb = mysql.connector.connect(
  host="localhost",
  user="administrator",
  password="administrator",
  database ="hybrowlabs"
)

cursor = mydb.cursor() 
cursor.execute('CREATE TABLE IF NOT EXISTS users(username BLOB NOT NULL, password BLOB NOT NULL);')


username = 'administrator'
password = 'administrator'

username = e.encrypt(username)
password = e.hash(password)

sql = "INSERT INTO users(username, password) VALUES (%s,%s);"
val = (username, password)
cursor.execute(sql,val)

mydb.commit()

print(cursor.rowcount, "record inserted.")