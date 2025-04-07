from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

def init_db():
    # Create a simple database with users and comments
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS comments (username TEXT, comment TEXT)")
    # Add a test user
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")
    conn.commit()
    conn.close()

init_db()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password)
        print("DEBUG query:", query)
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        if result:
            return "Logged in as " + username
        else:
            return "Login failed", 401
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/post_comment', methods=['GET', 'POST'])
def post_comment():
    if request.method == 'POST':
        username = request.form['username']
        comment = request.form['comment']
        conn = sqlite3.connect('test.db')
        cursor = conn.cursor()
        query = "INSERT INTO comments (username, comment) VALUES ('{}', '{}')".format(username, comment)
        cursor.execute(query)
        conn.commit()
        conn.close()
        return "Comment posted!"
    return '''
        <form method="post">
            Username: <input name="username"><br>
            Comment: <textarea name="comment"></textarea><br>
            <input type="submit" value="Post Comment">
        </form>
    '''

@app.route('/view_comments')
def view_comments():
    # Retrieve comments from the database
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, comment FROM comments")
    rows = cursor.fetchall()
    conn.close()
    
    html = "<h1>Comments</h1>"
    for username, comment in rows:
        html += "<p><strong>{}</strong>: {}</p>".format(username, comment)
    return html

if __name__ == '__main__':
    app.run(debug=True)
