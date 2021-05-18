import random
class infectioncarddeck:
    def __init__ (self):
        self.infectioncards = ['San Francisco','Chicago', 'Montreal', 'New York', 'Washington', 'Atlanta', 'London', 'Madrid', 'Paris', 'Essen', 'Milan', 'St. Petersburg','Los Angeles', 'Mexico City', 'Miami', 'Bogota', 'Lima', 'Santiago', 'SaoPaolo', 'Buenos Aires', 'Lagos', 'Kinshasa', 'Khartoum', 'Johannesburg','Algiers', 'Istanbul', 'Cairo', 'Moscow','Baghdad','Riyadh','Tehran','Karachi','Mumbai','Delhi','Chennai','Kolkata','Bangkok','Jakarta','Beijing','Shanghai','Hong Kong','Ho Chi Minh City','Seoul', 'Taipei','Manila','Sydney','Tokyo','Osaka']
        self.discardpile=[]
    def playcard (self):
        self.discardpile.append(self.infectioncards.pop(random.randrange(0,len(self.infectioncards))))
    #def Function to shuffel discard pile and place back on top
