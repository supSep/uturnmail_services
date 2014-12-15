from flask import Flask

app = Flask(__name__)

def authenticate():
    #implement auth
    return "Authenticated"

@app.route('/email_validator')
def email_validator():
    return 'email_validator!'


@app.route('/create_uturn')
def create_uturn():
        #receives from RMQ
    return 'create_uturn !'

@app.route('/create_adguru')
def create_adguru():
        #receives from RMQ
    return 'create_adguru!'

@app.route('/sendmail_adguru')
def sendmail_adguru():
        #receives from RMQ
    return 'Hello World!'

@app.route('/visit_url')
def visit_url():
    #receives from RMQ
    return 'visit_url!'


if __name__ == '__main__':
    app.run()
