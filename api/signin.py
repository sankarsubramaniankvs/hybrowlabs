import mysql.connector
from .crypto import cryptography as e

class user_signin:
    def authenticate_user(username,password):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )

        cursor = mydb.cursor() 
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        res=''
        for i in users:
            if username == e.decrypt(i[0]):
                r=e.check(password,i[1])
                if(r):
                   res='success'
                   break
                else:
                    res='Password Incorrect!'
            else:
                res= 'username not found!'
        cursor.close()
        mydb.close()
        return res



