import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="administrator",
  password="administrator"
)

cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")
print(cursor)
#creating database
if 'hybrowlabs' not in cursor:
    cursor.execute("CREATE DATABASE hybrowlabs")
    print('created successfully')


