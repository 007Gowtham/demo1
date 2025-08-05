from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'gowtham'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'testDB'

mysql = MySQL(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")



# Change form route to '/form' to avoid conflict with home
@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('view'))


@app.route('/view')
def view():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('view.html', users=data)


def create_users_table():
    cur = mysql.connection.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL
        )
    """)
    mysql.connection.commit()
    cur.close()


# Flask 3.x removed before_first_request, use before_request for table creation
@app.before_request
def initialize():
    if not hasattr(app, '_users_table_created'):
        create_users_table()
        app._users_table_created = True

if __name__ == '__main__':
    app.run(debug=True)
