import mysql.connector 

class location:
    def get_location_products(name):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM '+ name)
        r = cursor.fetchall()
        return r
    def location_edit(id,name):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        sql = "UPDATE locations SET name=%s WHERE ID=%s"
        val = (name,id)
        cursor.execute(sql,val) 
        mydb.commit()
    def location_add(name):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        cursor.execute("CREATE TABLE IF NOT EXISTS locations(id INT PRIMARY KEY, name VARCHAR(40));")
        cursor.execute("CREATE TABLE IF NOT EXISTS "+name+ "(id INT PRIMARY KEY, product VARCHAR(40) NOT NULL, quantity INT);")
        cursor.execute('SELECT * FROM locations;')
        r = cursor.fetchall()
        f=1
        for i in r:
            if i[1]==name:
                f=0
                break
        if(f):
            l = len(r)+1
            sql = "INSERT INTO locations(id,name) VALUES (%s,%s)"
            val = (l,name)
            cursor.execute(sql,val)
            mydb.commit()
            return 'Location Added Successfully'
        else:
            return 'Location Exists!'

    def get_locations():
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        cursor.execute("CREATE TABLE IF NOT EXISTS locations(id INT PRIMARY KEY, name VARCHAR(40));")
        cursor.execute('SELECT * FROM locations;')
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
        sql = """SELECT * FROM locations WHERE id=%s or id=%s"""
        val = (id,id)
        cursor.execute(sql,val)
        return cursor.fetchone() 
    def location_id_list():
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM locations;')
        cursor.fetchall()
        return str(cursor.rowcount)
    def location_delete(id):
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        cursor.execute("SELECT name FROM locations WHERE id=%s OR id=%s;",(id,id))
        name=cursor.fetchone()
        cursor.execute('DROP TABLE '+name[0])
        sql = "DELETE FROM locations WHERE id=%s OR id=%s;"
        val=(id,id)
        cursor.execute(sql,val)
        cursor.execute('SELECT * FROM locations;')
        data = cursor.fetchall() 
        cursor.execute('TRUNCATE TABLE locations')
        d = 1 
        for i in data:
            sql = "INSERT INTO locations(id,name) VALUES(%s,%s);"
            val = (d,i[1])
            cursor.execute(sql,val)
            d+=1
        mydb.commit()
        return 'success'
        


            