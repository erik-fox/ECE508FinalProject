from board import city
class role:
    def __init__(self, city):
        self.city=city
    def movecity(self, newcity):
        self.city=newcity
    def removeblue(self):
        self.city.decbluecube()
    def removered(self):
        self.city.decredcube()
    def removeblack(self):
        self.city.decblackcube()
    def removeyellow(self):
        self.city.decyellowcube()
    def buildstation(self):
        self.city.buildresearchstation()
    def movestation(self, newcity):
        self.city.moveresearchstation()
        newcity.buildresearchstation()

class contingencyplanner(role):
    def __init__(self,city):
        self.eventcard=[]
        super().__init__(city)
    def geteventcard(self,ecard):
        if len(self.eventcard) ==0:
            self.eventcard.append(ecard)
    def removeeventcard(self):
        self.eventcard.clear()

class dispatcher(role):
    def __init__(self,city):
        super().__init__(city)
    def moveplayer(player,newcity):
        player.movecity(newcity)

class medic(role):
    def __init__(self,city):
        super().__init__(city)
    def clearyellow(self):
        self.city.yellowcubes=0
    def clearblack(self):
        self.city.blackcubes=0
    def clearblue(self):
        self.city.bluecubes=0
    def clearred(self):
        self.city.redcubes=0

class operationsexpert(role):
    def __init__(self,city):
        super().__init__(city)

class quarantinespecialist(role):
    def __init__(self,city):
        super().__init__(city)

class researcher(role):
    def __init__(self,city):
        super().__init__(city)

class scientist(role):
    def __init__(self,city):
        super().__init__(city)

class player:
    def __init__(self,playertype,city):
        if playertype =='contingency_planner':
            self.role= contingencyplanner(city)
        elif playertype == 'dispatcher':
            self.role= dispatcher(city)
        elif playertype == 'medic':
            self.role= medic(city)
        elif playertype == 'operations_expert':
            self.role= operationsexpert(city)
        elif playertype == 'quarantine_specialist':
            self.role= quarantinespecialist(city)
        elif playertype == 'researcher':
            self.role= researcher(city)
        elif playertype == 'scientist':
            self.role= scientist(city)
        self.hand=[]
    #Actions:  include role specific actions; might include ellaborating on existing role subclasses; might just be player level specific with card sharing between player

