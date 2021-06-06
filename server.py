from flask import Flask, render_template, request, redirect, session, jsonify,url_for,abort
from api.signin import user_signin
from api.change_password import change_pass 
from api.products import product as p
from api.locations import location as l
from api.movements import movement as m


app = Flask(__name__)
app.secret_key = 'secretkey'
session=False 
session_user = '1'
product=''
location=''
location_products=''
movement=''

@app.route('/',methods=['GET'])
@app.route('/login',methods=['GET'])
def login_page():
    return render_template("login.html")


@app.route('/auth',methods=['POST'])
def authenticate():
    global session, session_user
    if(request.method=='POST'):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        r=user_signin.authenticate_user(username,password)
        if(r=='success'):
            session=True
            session_user = username      
        return r
@app.route('/loginredirect',methods=['GET'])
def login_redirect():
    global session,session_user
    if(session_user!='1' and session):
        return redirect(f"/user_dashboard/{session_user}")
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/user_dashboard/<username>',methods=['POST','GET'])
def dashboard(username):
    global session,session_user
    if(session and session_user==username):
        return render_template('dashboard.html')
    else:
        session=False
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/password_setting',methods=['POST','GET'])
def password_route():
    global session, session_user
    if(session_user!=1 and session):
        return redirect(f"/change_password/{session_user}")
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/change_password/<username>',methods=['POST','GET'])
def change_password(username):
    global session, session_user
    if(session and session_user==username):
        return render_template('change_password.html')
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/change_pass', methods=['POST'])
def change():
    global session,session_user

    if(request.method=='POST' and session):
        data = request.get_json()
        current = data.get('current')
        new = data.get('new')
        confirm = data.get('confirm')
        return change_pass.change(session_user,confirm,current)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))




@app.route('/products', methods=['POST','GET'])
def products():
    global session,session_user
    if(session):
        products = p.get_products()
        return render_template('products.html',products = products)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/add_product',methods=['POST','GET'])
def add_product():
     global session,session_user
     if(session):
         return render_template('add_product.html')
     else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/add_location',methods=['POST','GET'])
def add_location():
     global session,session_user
     if(session):
         return render_template('add_location.html')
     else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/add_movement',methods=['POST','GET'])
def add_movement():
     global session,session_user
     if(session):
         products = p.get_products()
         locations = l.get_locations()
         return render_template('add_movement.html',products=products,locations=locations)
     else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/product_add',methods=['POST'])
def product_add():
    global session 
    if(session):
        if request.method=='POST':
            data = request.get_json()
            product = data.get('name')
            return p.product_add(product)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/location_add',methods=['POST'])
def location_add():
    global session 
    if(session):
        if request.method=='POST':
            data = request.get_json()
            location = data.get('name')
            return l.location_add(location)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/movement_add',methods=['POST'])
def movement_add():
    global session 
    if(session):
        if request.method=='POST':
            data = request.get_json()
            fr = data.get('from')
            to = data.get('to')
            product = data.get('product')
            quantity = data.get('quantity')
            print(fr,to,product,quantity)
            r= m.movement_add(fr,to,product,quantity)
            return r
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/product_id_list',methods=['POST'])
def product_list():
    global session
    if(session):
        if(request.method=='POST'):
            r=p.product_id_list()
            return r
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/location_id_list',methods=['POST'])
def location_list():
    global session
    if(session):
        if(request.method=='POST'):
            r=l.location_id_list()
            return r
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/movement_id_list',methods=['POST'])
def movement_list():
    global session
    if(session):
        if(request.method=='POST'):
            r=m.movement_id_list()
            return r
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/product_edit_id',methods=['POST'])
def find_product():
    global session,product
    if(session):
        if request.method=='POST':
            data = request.get_json()
            id = data.get('id')
            product = p.get(id)
            return 'success'
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/location_edit_id',methods=['POST'])
def find_location():
    global session,location
    if(session):
        if request.method=='POST':
            data = request.get_json()
            id = data.get('id')
            location = l.get(id)
            return 'success'
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/movement_edit_id',methods=['POST'])
def find_movement():
    global session,movement,location,product
    if(session):
        if request.method=='POST':
            data = request.get_json()
            id = data.get('id')

            movement = m.get(id)


            return 'success'
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/location_view_id',methods=['POST'])
def view_id_location():
    global session,location,location_products,location
    if(session):
        if request.method=='POST':
            data = request.get_json()
            id = data.get('name')
            location=id
            r = l.get_location_products(id)
            location_products=r
            return 'success'
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/location_view_page',methods=['GET','POST'])
def view_location():
    global session, location_products
    if(session):
        return render_template('location_view.html',location=location,items=location_products)
    else:
        session=False   
        session_user='1'
        return redirect(url_for("login_page"))

    

@app.route('/product_edit_page',methods=['POST','GET'])
def product_edit():
    global product
    return render_template('edit_product.html',product=product)

@app.route('/location_edit_page',methods=['POST','GET'])
def location_edit():
    global location
    return render_template('edit_location.html',location=location)

@app.route('/movement_edit_page',methods=['POST','GET'])
def movement_edit():
    global movement
    products = p.get_products()
    locations = l.get_locations()
    return render_template('edit_movement.html',movement=movement,products=products,locations=locations)


@app.route('/product_edit_function',methods=['POST'])
def product_editor():
    global session
    if(session and request.method=='POST'):
        data = request.get_json()
        id = data.get('id')
        name = data.get('name')
        p.product_edit(id,name)
        return 'success'
    else:
        return 'failure'

@app.route('/location_edit_function',methods=['POST'])
def location_editor():
    global session
    if(session and request.method=='POST'):
        data = request.get_json()
        id = data.get('id')
        name = data.get('name')
        l.location_edit(id,name)
        return 'success'
    else:
        return 'failure'

@app.route('/movement_edit_function',methods=['POST'])
def movement_editor():
    global session
    if(session and request.method=='POST'):
        data = request.get_json()
        id = data.get('id')
        fr = data.get('from')
        to = data.get('to')
        pid = data.get('product')
        qty = data.get('quantity')
        m.movement_edit(id,fr,to,pid,qty)
        return 'success'
    else:
        return 'failure'


@app.route('/product_delete',methods=['POST'])
def product_delete():
    global session 
    if(session):
        if(request.method=='POST'):
            data = request.get_json() 
            id = data.get('id')
            return p.product_delete(id)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))

@app.route('/location_delete',methods=['POST'])
def location_delete():
    global session 
    if(session):
        if(request.method=='POST'):
            data = request.get_json() 
            id = data.get('id')
            return l.location_delete(id)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/movement_delete',methods=['POST'])
def movement_delete():
    global session 
    if(session):
        if(request.method=='POST'):
            data = request.get_json() 
            id = data.get('id')
            return m.movement_delete(id)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/locations',methods=['POST','GET'])
def locations():
    global session,session_user
    if(session):
        locations = l.get_locations()
        return render_template('locations.html',locations = locations)
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


@app.route('/movements',methods=['POST','GET'])
def movements():
    global session,session_user
    if(session):
        movements = m.get_movements()
        return render_template('movements.html',movements = movements)  
    else:
        session=False 
        session_user='1'
        return redirect(url_for("login_page"))


    




if __name__ == '__main__':
    app.run(debug=True)