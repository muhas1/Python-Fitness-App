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


def closeConnect():
    connection.commit()
