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
    return render_template('index.html')

@app.route("/register", methods=['POST'])
def register():
    #implement auth
    email = request.form['email']
    uturnmail = request.form['uturnmail']
    notifications = request.form['notifications']
    ##cursor = mysql.connect().cursor()
    ## check to see if uturnmail is taken
    ##cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    ##data = cursor.fetchone()
    if email or uturnmail or notifications is None:
     return "please enter all required info"
    else:
     return "email : " + email + " uturnmail : " + uturnmail + " notifications : " + notifications

@app.route('/contactus', methods=['POST'])
def contactus():
    #implement auth
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']
    if email or name or subject or message is None:
     return "please enter all required info"
    else:
     return "name : " + name + " email : " + email + " subject : " + subject + " message : " + message

if __name__ == '__main__':
    app.run()
