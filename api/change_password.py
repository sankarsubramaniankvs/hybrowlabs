import mysql.connector
from .crypto import cryptography as e

class change_pass:
    def change(username,new,old):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        mydb.autocommit = True

        cursor = mydb.cursor() 

        cursor.execute('SELECT * FROM users;')
        user = cursor.fetchone()
        cursor.close()
        cursor = mydb.cursor()
        res=''        
        if e.decrypt(user[0]) == username:
            if( e.check(old,user[1])):
                username = user[0]
                new = e.hash(new)
                sql="""UPDATE users SET password = %s WHERE username = %s""";
                val=(new,username)
                cursor.execute(sql,val)
                res= 'Password change successful'
            else:
                res= 'Current password incorrect!'
        else:
            res='User not found!'
        mydb.commit()
        cursor.close()
        mydb.close()
        return res



