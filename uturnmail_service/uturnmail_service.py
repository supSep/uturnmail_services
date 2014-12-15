from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

def authenticate():
    #implement auth
    return "Authenticated"

@app.route('/create_uturn')
def create_uturn():
    return 'create_uturn !'

@app.route('/create_adguru')
def create_adguru():
    return 'create_adguru!'

@app.route('/sendmail_adguru')
def sendmail_adguru():
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
