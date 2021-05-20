import random
class infectioncarddeck:
    def __init__ (self):
        self.infectioncards = ['San Francisco','Chicago', 'Montreal', 'New York', 'Washington', 'Atlanta', 'London', 'Madrid', 'Paris', 'Essen', 'Milan', 'St. Petersburg','Los Angeles', 'Mexico City', 'Miami', 'Bogota', 'Lima', 'Santiago', 'SaoPaolo', 'Buenos Aires', 'Lagos', 'Kinshasa', 'Khartoum', 'Johannesburg','Algiers', 'Istanbul', 'Cairo', 'Moscow','Baghdad','Riyadh','Tehran','Karachi','Mumbai','Delhi','Chennai','Kolkata','Bangkok','Jakarta','Beijing','Shanghai','Hong Kong','Ho Chi Minh City','Seoul', 'Taipei','Manila','Sydney','Tokyo','Osaka']
        self.discardpile=[]
    def playcard (self):
        self.discardpile.append(self.infectioncards.pop(random.randrange(0,len(self.infectioncards))))
    def return2deck(self):
        for i in range(len(self.discardpile)):
            self.infectioncards.append(self.discardpile.pop(random.randrange(0,len(self.discardpile))))

class playercarddeck:
    def __init__(self):
        self.playercards =['San Francisco','Chicago', 'Montreal', 'New York', 'Washington', 'Atlanta', 'London', 'Madrid', 'Paris', 'Essen', 'Milan', 'St. Petersburg','Los Angeles', 'Mexico City', 'Miami', 'Bogota', 'Lima', 'Santiago', 'SaoPaolo', 'Buenos Aires', 'Lagos', 'Kinshasa', 'Khartoum', 'Johannesburg','Algiers', 'Istanbul', 'Cairo', 'Moscow','Baghdad','Riyadh','Tehran','Karachi','Mumbai','Delhi','Chennai','Kolkata','Bangkok','Jakarta','Beijing','Shanghai','Hong Kong','Ho Chi Minh City','Seoul', 'Taipei','Manila','Sydney','Tokyo','Osaka','Epidemic','Epidemic','Epidemic', 'Epidemic', 'Epidemic','Epidemic','Resilient Population', 'Airlift', 'Forecast','One Quiet Night', 'Government Grant']
        self.discardpile=[]
    def playcard(self):
        self.discardpile.append(self.playercards.pop(random.randrange(0,len(self.playercards))))

class city:
    def __init__(self,name,connectedcities):
        self.city=name
        self.connections=connectedcities
        self.redcubes=0
        self.bluecubes=0
        self.blackcubes=0
        self.yellowcubes=0
        self.researchstation=0
    def incredcube(self):
        if self.redcubes < 3:
            self.redcubes = self.redcubes + 1
    def decredcube(self):
        if self.redcubes>0:
            self.redcubes=self.redcubes -1
    def incbluecube(self):
        if self.bluecubes < 3:
            self.bluecubes = self.bluecubes + 1
    def decbluecube(self):
        if self.bluecubes>0:
            self.bluecubes=self.bluecubes -1
    def incblackcubes(self):
        if self.blackcubes < 3:
            self.blackcubes = self.blackcubes + 1
    def decblackcube(self):
        if self.blackcubes>0:
            self.blackcubes=self.blackcubes -1
    def incyellowcubes(self):
        if self.yellowcubes < 3:
            self.yellowcubes = self.yellowcubes + 1
    def decyellowcube(self):
        if self.yellowcubes>0:
            self.yellowcubes=self.yellowcubes -1
    def buildresearchstation(self):
        if self.researchstation < 1:
            self.researchstation= self.researchstation +1
    def moveresearchstation(self):
        self.researchstation =0

class map:
    def __init__(self,text):
        self.list=dict()
        fp=open(text,'r')
        lines=fp.readlines()
        for line in lines:
            line=line.rstrip("\n")
            line=line.split(" ")
            point=city(line[0],line[1:len(line)])
            self.list[line[0]]=point


class board:
    def __init__(self,mapfile):
        self.infectiondeck=infectioncarddeck()
        self.playerdeck=playercarddeck()
        self.map= map(mapfile)
        self.cureddiseases={'yellow':0,'red':0,'blue':0,'black':0}
        self.infectionrate=[2,2,2,3,3,4,4]
        self.outbreaks=0
