import mysql.connector 
import datetime
class movement:
    def movement_edit(id,fr,to,pid,qty):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 

        cursor.execute('SELECT * FROM movements WHERE id=%s OR id=%s',(id,id))
        current = cursor.fetchone() 
        if fr!='':
            cursor.execute('SELECT quantity from '+fr +' WHERE product=%s OR product=%s',(pid,pid))
            r=cursor.fetchone()
            pq = r[0]
            quantity = int(pq)+int(current[5])-int(qty)
            cursor.execute('UPDATE '+fr+ ' SET QUANTITY=%s WHERE product=%s;',(quantity,pid))
            mydb.commit()
        if to!='':
            cursor.execute('SELECT quantity from '+to +' WHERE product=%s OR product=%s',(pid,pid))
            r=cursor.fetchone()
            pq = r[0]
            quantity = int(pq)-int(current[5])+int(qty)
            cursor.execute('UPDATE '+to+ ' SET QUANTITY=%s WHERE product=%s;',(quantity,pid))
            mydb.commit()

        sql = "UPDATE movements SET from_loc=%s, to_loc=%s, product_id=%s, quantity=%s  WHERE ID=%s"
        val = (fr,to,pid,qty,id)
        cursor.execute(sql,val) 
        mydb.commit()
    def movement_add(fr,to,product_id,quantity):
        timestamp=datetime.datetime.now()
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        cursor.execute("CREATE TABLE IF NOT EXISTS movements(id INT PRIMARY KEY, timestamp VARCHAR(40) NOT NULL, from_loc VARCHAR(40) NOT NULL, to_loc VARCHAR(40) NOT NULL,product_id VARCHAR(40), quantity INT);")
        cursor.execute('SELECT * FROM movements;')
        r = cursor.fetchall()
        l = len(r)+1
        sql = "INSERT INTO movements(id,timestamp,from_loc,to_loc,product_id,quantity) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (l,timestamp,fr,to,product_id,quantity)
        cursor.execute(sql,val)
        if(fr!=''):
            sql = "CREATE TABLE IF NOT EXISTS " + fr +"(id INT PRIMARY KEY, product VARCHAR(40) NOT NULL, quantity INT);"
            cursor.execute(sql)
            cursor.execute("SELECT * FROM "+fr)
            r = cursor.fetchall() 
            f=0
            for i in r:
                if i[1]==product_id:
                    if int(i[2])<int(quantity):
                        return 'Insufficient stock in From Location!'
                    f=1

            if(f==0):
                return 'Product Not found in From Location!'
            else:
                cursor.execute('SELECT quantity from '+fr +' WHERE product=%s OR product=%s',(product_id,product_id))
                r=cursor.fetchone() 
                if not r:
                     cursor.execute('SELECT * FROM '+to)
                     cursor.fetchall()
                     id = cursor.rowcount +1
                     cursor.execute('INSERT INTO '+fr+'(id,product,quantity) VALUES(%s,%s,%s)',(id,product_id,quantity))
                     mydb.commit()
                else:
                     pq = r[0]
                     quantity1 = int(pq)-int(quantity)
                     cursor.execute('UPDATE '+fr+ ' SET QUANTITY=%s WHERE product=%s;',(quantity1,product_id))
                     mydb.commit()
        if(to!=''):
            sql = "CREATE TABLE IF NOT EXISTS " + to +"(id INT PRIMARY KEY, product VARCHAR(40) NOT NULL, quantity INT);"
            cursor.execute(sql)   
            cursor.execute('SELECT quantity from '+ to +' WHERE product=%s OR product=%s;',(product_id,product_id))
            r=cursor.fetchone() 
            if not r:
                cursor.execute('SELECT * FROM '+to)
                cursor.fetchall()
                id = cursor.rowcount +1
                cursor.execute('INSERT INTO '+ to +'(id,product,quantity) VALUES(%s,%s,%s)',(id,product_id,quantity))
                mydb.commit()
            else:
                pq = r[0]
                quantity = int(pq)+int(quantity)
                cursor.execute('UPDATE '+to+ ' SET QUANTITY=%s WHERE product=%s;',(quantity,product_id))
                mydb.commit()
        return 'Movement Added Successfully'

    def get_movements():
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        cursor.execute("CREATE TABLE IF NOT EXISTS movements(id INT PRIMARY KEY, timestamp VARCHAR(40) NOT NULL, from_loc VARCHAR(40) NOT NULL, to_loc VARCHAR(40) NOT NULL,product_id VARCHAR(40), quantity INT);")
        cursor.execute('SELECT * FROM movements;')
        r=cursor.fetchall()
        return r 

    def get(id):
        id=int(id)
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        sql = """SELECT * FROM movements WHERE id=%s or id=%s"""
        val = (id,id)
        cursor.execute(sql,val)
        return cursor.fetchone() 
    def movement_id_list():
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM movements;')
        cursor.fetchall()
        return str(cursor.rowcount)
    def movement_delete(id):
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        cursor.execute("SELECT from_loc,to_loc,product_id,quantity FROM movements WHERE id=%s OR id=%s",(id,id))
        res = cursor.fetchone() 
        if res[0]!='':
            cursor.execute('SELECT quantity from '+res[0] +' WHERE product=%s OR product=%s',(res[2],res[2]))
            r=cursor.fetchone()
            pq = r[0]
            quantity = int(pq)+int(res[3])
            cursor.execute('UPDATE '+res[0]+ ' SET QUANTITY=%s WHERE product=%s;',(quantity,res[2]))
            mydb.commit()
        if res[1]!='':
            cursor.execute('SELECT quantity from '+res[1] +' WHERE product=%s OR product=%s',(res[2],res[2]))
            r=cursor.fetchone()
            pq = r[0]
            quantity = int(pq)-int(res[3])
            cursor.execute('UPDATE '+res[1]+ ' SET QUANTITY=%s WHERE product=%s;',(quantity,res[2]))
            mydb.commit()


        sql = "DELETE FROM movements WHERE id=%s OR id=%s;"
        val=(id,id)
        cursor.execute(sql,val)
        cursor.execute('SELECT * FROM movements;')
        data = cursor.fetchall() 
        cursor.execute('TRUNCATE TABLE movements')
        d = 1 
        for i in data:
            sql = "INSERT INTO movements(id,timestamp,from_loc,to_loc,product_id,quantity) VALUES (%s,%s,%s,%s,%s,%s);"
            val = (d,i[1],i[2],i[3],i[4],i[5])
            cursor.execute(sql,val)
            d+=1
        mydb.commit()
        return 'success'
        


            