import mysql.connector 

class product:
    def product_edit(id,name):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        sql = "UPDATE products SET name=%s WHERE ID=%s"
        val = (name,id)
        cursor.execute(sql,val) 
        mydb.commit()
    def product_add(name):
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        cursor.execute("CREATE TABLE IF NOT EXISTS products(id INT PRIMARY KEY, name VARCHAR(40));")
        cursor.execute('SELECT * FROM products;')
        r = cursor.fetchall()
        f=1
        for i in r:
            if i[1]==name:
                f=0
                break
        if(f):
            l = len(r)+1
            sql = "INSERT INTO products(id,name) VALUES (%s,%s)"
            val = (l,name)
            cursor.execute(sql,val)
            mydb.commit()
            return 'Product Added Successfully'
        else:
            return 'Product Exists!'

    def get_products():
        mydb = mysql.connector.connect(
        host="localhost",
        user="administrator",
        password="administrator",
        database ="hybrowlabs"
        )
        cursor = mydb.cursor() 
        cursor.execute('CREATE TABLE IF NOT EXISTS products(id INT PRIMARY KEY, name VARCHAR(40) NOT NULL);')
        cursor.execute('SELECT * FROM products;')
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
        sql = """SELECT * FROM products WHERE id=%s or id=%s"""
        val = (id,id)
        cursor.execute(sql,val)
        return cursor.fetchone() 
    def product_id_list():
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM products;')
        cursor.fetchall()
        return str(cursor.rowcount)
    def product_delete(id):
        mydb = mysql.connector.connect(
                host="localhost",
                user="administrator",
                password="administrator",
                database ="hybrowlabs"
                )
        cursor = mydb.cursor()
        cursor.execute('SELECT name FROM products WHERE id=%s OR id=%s;',(id,id))
        pname = cursor.fetchone() 
        cursor.execute('SELECT name FROM locations;')
        locations = cursor.fetchall()
        for i in locations:
            cursor.execute('DELETE FROM '+ i[0]+' WHERE product=%s or product=%s',(pname,pname))
            mydb.commit()
        sql = "DELETE FROM products WHERE id=%s OR id=%s;"
        val=(id,id)
        cursor.execute(sql,val)
        cursor.execute('SELECT * FROM products;')
        data = cursor.fetchall() 
        cursor.execute('TRUNCATE TABLE products')
        d = 1 
        for i in data:
            sql = "INSERT INTO products(id,name) VALUES(%s,%s);"
            val = (d,i[1])
            cursor.execute(sql,val)
            d+=1
        mydb.commit()
        return 'success'
        


            