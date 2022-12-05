from flask import Flask, render_template, request

from dbHandler import *


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == "POST":
        if request.form['submission'] == 'signup':
            fName = request.form['fName']
            lName = request.form['lName']
            user = request.form['user']
            pass1 = request.form['pass']
            createLogin(user,pass1,fName,lName)
            return render_template('home.html')
        if request.form['submission'] == 'login':
            username = request.form['username']
            password = request.form['password']
            if checkLogin(username,password):
                return "CORRECT"
            else:
                return "FALSE"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


