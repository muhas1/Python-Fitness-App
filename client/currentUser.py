class CurrentTrainee:

    def __init__(self,fName,lName,user,password, trainerID) -> None:
        self.fName = fName
        self.lName = lName
        self.user = user
        self.password = password
        self.trainerID = trainerID

    def getFname(self):
        return self.fName

    def getLname(self):
        return self.lName
    
    def getUser(self):
        return self.user
    
    def getPassword(self):
        return self.password

    def getTrainer(self):
        return self.trainerID