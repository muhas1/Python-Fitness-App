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
                return render_template('home.html')
            else:
                return render_template('login.html')
    return render_template('login.html')

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "POST":
        if request.form['menu'] == 'meals':
            return render_template('MealForm.html')
    return render_template('home.html')

@app.route("/meals",methods=["GET","POST"])
def meal():
    if request.method == "POST":
        mealID = request.form['mealID']
        calories = request.form['calories']
        protein = request.form['protein']
        carbs = request.form['carbs']
        fat = request.form['fat']
        TRUserID = request.form['TR_userID']
        addMeal(mealID,calories,protein,carbs,fat,TRUserID)
        return mealID + calories + protein + carbs + fat + TRUserID
    return render_template('MealForm.html')

if __name__ == '__main__':
    app.run(debug=True)


