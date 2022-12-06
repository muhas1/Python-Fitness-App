from flask import Flask, flash, render_template, request

from dbHandler import *

from currentUser import *

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
            return render_template('login.html')
        if request.form['submission'] == 'login':
            username = request.form['username']
            password = request.form['password']
            if checkLogin(username,password):
                a = getNameFromUser(username)
                global trainee
                trainee = CurrentTrainee(a[0][3],a[0][4],username,password,a[0][7])
                return render_template('home.html')
            else:
                return render_template('login.html')
    return render_template('login.html')

@app.route("/home",methods=["GET","POST"])
def home():
    if request.method == "POST":
        if request.form['menu'] == 'meals':
            return render_template('MealForm.html')
        if request.form['menu'] == 'exercise':
            return render_template('ExerciseForm.html')
        if request.form['menu'] == 'trainer':
            if int(trainee.getTrainer()) == 1:
                return render_template('TrainerInfo.html', first="Muhammad", last="Shah")
            if int(trainee.getTrainer()) == 2:
                return render_template('TrainerInfo.html', first="Jinsu", last="Kwak")  
        if request.form['menu'] == 'personal':
            return render_template('update_trainer.html')
    return render_template('home.html')

@app.route("/meals",methods=["GET","POST"])
def meal():
    if request.method == "POST":
        if request.form['Chooser'] == 'add':
            mealID = request.form['mealID']
            calories = request.form['calories']
            protein = request.form['protein']
            carbs = request.form['carbs']
            fat = request.form['fat']
            TRUserID = request.form['TR_userID']
            addMeal(mealID,calories,protein,carbs,fat,TRUserID)
            return mealID + calories + protein + carbs + fat + TRUserID
        else:
            return render_template('delete.html')
    return render_template('MealForm.html')

@app.route("/exercise",methods=["GET", "POST"])
def exercise():
    if request.method == "POST":
        if request.form['Chooser2'] == "add":
            exName = request.form["exName"]
            muscleGroup = request.form["muscleGroup"]
            EXWeight = request.form["EXWeight"]
            number = request.form['number']
            reps = request.form["reps"]
            restTime = request.form["restTime"]
            EXintensity = request.form["EXintensity"]
            addExercise(exName,muscleGroup,EXWeight,number,reps,restTime,EXintensity)
            return render_template('ExerciseForm.html')
        else:
            return render_template('delete.html')
    return render_template('ExerciseForm.html')


@app.route("/personal",methods=["GET","POST"])
def personal():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form['password']
        Fname = request.form['Fname']
        Lname = request.form['Lname']
        height = request.form['height']
        weight = request.form['weight']
        trainerID = request.form['trainerID']
        updateTrainee(trainee.getUser(),email,password,Fname,Lname,height,weight,trainerID)
    return render_template('update_trainer.html')


@app.route("/trainer",methods=["GET","POST"])
def trainer():
    return render_template('TrainerInfo.html')

@app.route("/delete",methods=["GET","POST"])
def update():
    if request.form['update'] == 'updateMeal':
        meal = request.form['mealID']
        cal = request.form['calories']
        protein = request.form["protein"]
        carbs = request.form["carbs"]
        fat = request.form["fat"]
        mealName = request.form['mealName']
        updateMeal(protein,cal,carbs,fat,trainee.getTrainer(),mealName,meal)
        return render_template('delete.html')
    if request.form['update'] == 'deleteMeal':
        mealID = request.form['mealID']
        deleteMeal(mealID)
        return render_template('delete.html')
    if request.form['update'] == "updateExercise":
        exName = request.form['exName']
        muscleGroup = request.form['muscleGroup']
        EXWeight = request.form['EXWeight']
        sets = request.form['number']
        reps = request.form['Sets']
        restTime = request.form['restTime']
        EXintensity = request.form['EXintensity']
        updateExercise(exName,muscleGroup,EXWeight,sets,reps,restTime,EXintensity)
        return render_template('delete.html')
    if request.form['update'] == 'deleteExercise':
        exName = request.form['exName']
        deleteExercise(exName)
        return render_template('delete.html')
    return render_template('delete.html')

if __name__ == '__main__':
    app.run(debug=True)


