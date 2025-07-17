from flask import Flask
from flask import render_template
from flask import request
import models as dbHandler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        dbHandler.insertUser(username,email,password)
        users = dbHandler.retrieveUsers()
        return render_template('login.html', users=users)
    else:
        return render_template('register.html')









if __name__ == '__main__':
    app.run(debug=True)