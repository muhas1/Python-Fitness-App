import sqlite3

connection = sqlite3.connect('fitness.db',check_same_thread=False)
c = connection.cursor()

def createLogin(username,password,firstName,lastName):
    c.execute("INSERT INTO trainee(email,password,Fname,Lname,height,weight,trainerID) VALUES (?,?,?,?,?,?,?)",
        [username,password,firstName,lastName,165,200,1]
    )
    print('Added value into Trainee')
    closeConnect()


def closeConnect():
    connection.commit()
    connection.close()

if __name__ == "__main__":
    createLogin("muhment@gmail.com","muhment123","Muha","Shah")