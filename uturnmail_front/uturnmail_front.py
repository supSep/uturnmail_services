from flask import Flask, request, render_template
from flaskext.mysql import MySQL


mysql = MySQL()
app = Flask(__name__)
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
# app.config['MYSQL_DATABASE_DB'] = 'EmpData'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

@app.route('/')
def hello_world():
    render_template('index2.html')
@app.route("/register", methods=['POST'])
def Authenticate():
    email = request.args.get('email')
    uturnmail = request.args.get('uturnmail')
    notifications = request.args.get('notifications')
    cursor = mysql.connect().cursor()
    ## check to see if uturnmail is taken
    ##cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

if __name__ == '__main__':
    app.run()
