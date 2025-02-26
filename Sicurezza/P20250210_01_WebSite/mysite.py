"""
per scoprire tutte le interfacce di rete della vostra macchina
ip a | grep inet

per impostare un IP nuovo (vedi le slide)
sudo ip a add 192.168.101.10/24 dev enp58s0u1u2
sudo ip a add 192.168.101.2/24 dev enp58s0u1u2
sudo ip a add 192.168.150.2/24 dev enp58s0u1u2

Ricordate che nel progetto abbiamo impostato la
porta 8087

Per impostare mysql
1) creare la cartella dei dati di mysql
    
    docker run --rm -e MYSQL_ROOT_PASSWORD=root -p 33306:3306 -v ./MySqlData/:/var/lib/mysql/ mysql:latest
    sudo apt install mysql-client

    mysql -h 127.0.0.1 -P 33306 -uroot -proot
    
    create database cyber05;
    use cyber05;

    CREATE TABLE users (
        id SERIAL,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL );
    CREATE TABLE items (
        id SERIAL,
        name VARCHAR(255) NOT NULL,
        description VARCHAR(255) NOT NULL );

    insert into items (name, description) values ("pixel9 pro", "latest high cost from google");
    insert into items (name, description) values ("pixel9", "latest low cost from google");

"""

import os
import sqlite3
import pymysql

from flask import Flask, request, g, redirect, url_for, render_template, session, flash


SECRET_KEY = 'AAA'  # Replace with your own secret key.

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

def get_db():
    """
    Open a new database connection if there is none yet for the current application context.
    """
    if 'db' not in g:
# Connect to MySQL
        g.db = pymysql.connect(
            host="10.46.8.107",
            user="root",
            port=33306,
            password="root",
            database="cyber05",
            cursorclass=pymysql.cursors.DictCursor
        )
        # g.db = sqlite3.connect(DATABASE)
        # Return rows as dictionaries
        # g.db.row_factory = sqlite3.Row
        g.cursor = g.db.cursor()
    return g.cursor, g.db


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database connection at the end of the request.
    """
    cursor = g.pop('cursor', None)
    if cursor is not None:
        cursor.close()
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Create user table if it doesn't exist."""
    db, conn = get_db()
    db.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL,
        username VARCHAR(255) UNIQUE NOT NULL,
        password VARCHAR(255) NOT NULL );
    ''')
    conn.commit()

listaQuery=[]

@app.before_request
def initialize():
    """Initialize the database before the first request."""
    init_db()
    #Mi costruisco una lista di query
    #SELECT * FROM users WHERE username = "aaa" and password="aaa"
    # db = get_db()
    # users=db.execute("select username, password from users").fetchall()
    # for item in users:
    #     listaQuery.append('select * from users where username="'+item['username']+'" and password="' + item["password"] + '";')
    


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, conn = get_db()
        
        # Check if user already exists
        db.execute(f"SELECT * FROM users WHERE username = '{username}'")
        existing_user = db.fetchall()

        if existing_user:
            flash("Username already taken, please choose another.", "error")
            return redirect(url_for('register'))

        # Hash and store the new user’s password
        db.execute(
            f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
        conn.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))

    # GET request -> Show registration form
    return render_template('register.html')

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if 'user_id' not in session:
        flash("You must be logged in to add items.", "warning")
        return redirect(url_for('login'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        db, conn = get_db()
        db.execute(f"INSERT INTO items (name, description) VALUES ('{name}', '{description}')")
        conn.commit()
        flash("Item added!", "success")
        return redirect(url_for('show_items'))

    return render_template('base.html', content="""
    <form method="POST">
        <label for="name">Item Name:</label>
        <input type="text" name="name" required><br><br>
        <label for="description">Description:</label>
        <textarea name="description"></textarea><br><br>
        <button type="submit">Add Item</button>
    </form>
    """)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db, conn = get_db()


        sql = f"SELECT * FROM users WHERE username='{username}' and password='{password}'"

        # # è sufficiente che la stringa sql sia in listaQuery
        # if sql.lower() in listaQuery:
        #     #Utente presente!!!
        #     print("Presente!")
        
        # sql = 'SELECT * FROM users WHERE username = "' + '" or 1=1 --' + '" and password="' + password + '"'

        # sql = 'SELECT * FROM users WHERE username = ? and password = ?'

#SELECT * FROM users WHERE username = "" or 1=1 or username = "a" and password="asdasd"
    
        print(request.form)
        print(sql)
        #user = db.execute(sql, (username, password)).fetchone()
        db.execute(sql)
        user=db.fetchall()
        if user:
            user=user[0]

        # Validate user credentials
        if user: # and user['password']==password:
            # Store user info in session
            session['user_id'] = user["username"]
            session['username'] = user["password"]
            
            flash("Login successful!", "success")
            return redirect(url_for('protected_page'))

        flash("Invalid credentials. Please try again.", "error")
        return redirect(url_for('login'))

    # GET request -> Show login form
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


# @app.route('/protected')
# def protected():
#     if 'user_id' not in session:
#         flash("You must be logged in to view this page.", "warning")
#         return redirect(url_for('login'))

#     # If logged in, render a protected page:
#     # This page could be an HTML template or a redirect to a static file
#     return render_template('base.html', content="This is a protected route!")

@app.route('/protected')
def protected_page():
    if 'user_id' not in session:
        flash("You must be logged in to access this page.", "warning")
        return redirect(url_for('login'))

    return render_template('protected_page.html')

@app.route('/protected_static')
def protected_static():
    if 'user_id' not in session:
        flash("You must be logged in to view this page.", "warning")
        return redirect(url_for('login'))
    
    # Return the static content from a file (or a template) only if logged in
    return app.send_static_file('protected_page.html')

@app.route('/public')
def public_page():
    return render_template('free_public_page.html')

@app.route('/')
def index():
    return render_template('index.html')


# La gestione dei dati applicativi
@app.route('/items')
def show_items():
    if 'user_id' not in session:
        flash("You must be logged in to view items.", "warning")
        return redirect(url_for('login'))

    db, conn = get_db()
    db.execute("SELECT * FROM items")
    items = db.fetchall()

    return render_template('dynamic.html', items=items)


myip = "192.168.101.10"
myport = 8087

if __name__ == '__main__':
    with app.app_context():
        init_db()  # Ensure the database is initialized
    app.run(host=myip, port=myport, debug=False)