import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="administrator",
  password="administrator"
)

print(mydb)