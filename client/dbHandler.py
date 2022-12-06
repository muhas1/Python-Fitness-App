import sqlite3

connection = sqlite3.connect('fitness.db',check_same_thread=False)
c = connection.cursor()

def createLogin(username,password,firstName,lastName):
    c.execute("INSERT INTO trainee(email,password,Fname,Lname,height,weight,trainerID) VALUES (?,?,?,?,?,?,?)",
        [username,password,firstName,lastName,165,200,1]
    )
    print('Added value into Trainee')
    closeConnect()


def checkLogin(username,password):
    c.execute("SELECT traineeID FROM trainee WHERE ( email == (?) AND password == (?) )",[username,password])
    if (len(c.fetchall()) == 1):
        closeConnect()
        return True
    else:
        closeConnect()
        return False

def addMeal(mealID,calories,protein,carbs,fat,TRUserID):
    c.execute("INSERT INTO meal(protein,calories,carbs,fat,TR_userID,mealName) VALUES (?,?,?,?,?,?)",
        [protein,calories,carbs,fat,TRUserID,mealID]
    )
    closeConnect()

def addExercise(exName,muscleGroup,EXWeight,number,reps,restTime,EXintensity):
    c.execute("INSERT INTO exercise(exName,muscleGroup,EXWeight,number,reps,restTime,EXintensity) VALUES (?,?,?,?,?,?,?)", 
        [exName,muscleGroup,EXWeight,number,reps,restTime,EXintensity]
    )
    closeConnect()

def getNameFromUser(username):
    c.execute("SELECT * FROM trainee WHERE email == (?)",[username])
    returnValue = c.fetchall()
    closeConnect()
    return returnValue

def updateTrainee(original, email,password,first,last,height,weight,trainer):
    c.execute("""UPDATE trainee SET email = (?), password = (?), Fname = (?), Lname = (?),
    height = (?), weight = (?), trainerID = (?) WHERE email = (?)""", 
    [email,password,first,last,height,weight,trainer,original])
    closeConnect()

def updateMeal(protein, calories, carbs, fat, Trainer, mealName,mealID):
    c.execute("""UPDATE meal SET protein = (?), calories = (?), carbs = (?), fat = (?), TR_userID = (?), mealName = (?) WHERE meaLID == (?)""", 
    [protein,calories,carbs,fat,Trainer,mealName,mealID])
    closeConnect()

def deleteMeal(mealID):
    c.execute("DELETE FROM meal WHERE mealID == (?)",[mealID])
    closeConnect()

def deleteExercise(exerciseName):
    c.execute("DELETE FROM exercise WHERE exName == (?)",[exerciseName])
    closeConnect()

def updateExercise(name,group,weight,setS,reps,rest,intensity):
    c.execute("""UPDATE exercise SET muscleGroup = (?), EXWeight = (?), number = (?), reps = (?), restTime = (?),
    EXIntensity = (?) WHERE exName == (?)""", [group,weight,setS,reps,rest,intensity,name])
    closeConnect()

def closeConnect():
    connection.commit()

if __name__ == "__main__":
    updateExercise("Muscle Up",'Arms',0,5,6,5,9)
