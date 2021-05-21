from board import board
from player import player
def game():
#SETUP
##set out the board and place research station at pieces
    b = board('map.txt')
    b.map.list['atlanta'].buildresearchstation()
    b.researchstations=5

##select role
    numplayers=int(input('How many players? 2-4'))
    players=[]
    for i in range (numplayers):
        for j in range(len(b.roles)):
            print("role "+str(j)+":" +b.roles[j])
        roleselect=int(input('Enter number of role'))
        players.append(player(b.roles.pop(roleselect),b.map.list['atlanta']))
##distribute non epidemic player cards based on num of players
    if numplayers == 2:
        numcards=4
    elif numplayers ==3:
        numcards=3
    else:
        numcards=2
    for j in range(numplayers):
        for i in range(numcards):
            while True:
                b.playerdeck.playcard()
                if b.playerdeck.discardpile[len(b.playerdeck.discardpile)-1]=='Epidemic':
                    b.playerdeck.playercards.append(b.playerdeck.discardpile.pop())
                else:
                    players[j].hand.append(b.playerdeck.discardpile.pop())
                    break
##infect 9 cities
    for i in range (9):
        b.infectiondeck.playcard()
        if b.infectiondeck.discardpile[i] in b.map.redcities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].redcubes=3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].redcubes=2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].redcubes=1
        if b.infectiondeck.discardpile[i] in b.map.bluecities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].bluecubes=3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].bluecubes=2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].bluecubes=1
        if b.infectiondeck.discardpile[i] in b.map.blackcities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].blackcubes=3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].blackcubes=2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].blackcubes=1
        if b.infectiondeck.discardpile[i] in b.map.yellowcities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].yellowcubes=3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].yellowcubes=2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].yellowcubes=1
##play game
####Start with player 1
####display each players role, hand, map, cured, outbreak num and infection rate
    while True:
        for i in range(numplayers):
            print("MAP:")
            print("Yellow cities:")
            for i in range(len(b.map.yellowcities)):
                print(str(b.map.list[b.map.yellowcities[i]].city)+':  blue:'+str(b.map.list[b.map.yellowcities[i]].bluecubes)+'  yellow:'+str(b.map.list[b.map.yellowcities[i]].yellowcubes)+'  black:'+str(b.map.list[b.map.yellowcities[i]].blackcubes)+'  red:'+str(b.map.list[b.map.yellowcities[i]].redcubes))
                print("researchstation:")
                print(b.map.list[b.map.yellowcities[i]].researchstation)
                print("connections:")
                print(b.map.list[b.map.yellowcities[i]].connections)
                print('\n')
            print("Black cities:")
            for i in range(len(b.map.blackcities)):
                print(str(b.map.list[b.map.blackcities[i]].city)+':  blue:'+str(b.map.list[b.map.blackcities[i]].bluecubes)+'  yellow:'+str(b.map.list[b.map.blackcities[i]].yellowcubes)+'  black:'+str(b.map.list[b.map.blackcities[i]].blackcubes)+'  red:'+str(b.map.list[b.map.blackcities[i]].redcubes))
                print("researchstation:")
                print(b.map.list[b.map.blackcities[i]].researchstation)
                print("connections:")
                print(b.map.list[b.map.blackcities[i]].connections)
                print('\n')
            print("Blue cities:")
            for i in range(len(b.map.bluecities)):
                print(str(b.map.list[b.map.bluecities[i]].city)+':  blue:'+str(b.map.list[b.map.bluecities[i]].bluecubes)+'  yellow:'+str(b.map.list[b.map.bluecities[i]].yellowcubes)+'  black:'+str(b.map.list[b.map.bluecities[i]].blackcubes)+'  red:'+str(b.map.list[b.map.bluecities[i]].redcubes))
                print("researchstation:")
                print(b.map.list[b.map.bluecities[i]].researchstation)
                print("connections:")
                print(b.map.list[b.map.bluecities[i]].connections)
                print('\n')
            print("Red cities:")
            for i in range(len(b.map.redcities)):
                print(str(b.map.list[b.map.redcities[i]].city)+':  blue:'+str(b.map.list[b.map.redcities[i]].bluecubes)+'  yellow:'+str(b.map.list[b.map.redcities[i]].yellowcubes)+'  black:'+str(b.map.list[b.map.redcities[i]].blackcubes)+'  red:'+str(b.map.list[b.map.redcities[i]].redcubes))
                print("researchstation:")
                print(b.map.list[b.map.redcities[i]].researchstation)
                print("connections:")
                print(b.map.list[b.map.redcities[i]].connections)
                print('\n')
            print("NUMBER OF OUTBREAKS:")
            print(" "+str(b.outbreaks))
            print("INFECTION RATE:")
            print(" "+str(b.infectionrate[0]))
            for i in range(len(players)):
                print("Player "+str(i)+" Hand:")
                print(players[i].hand)
                print('\n') 
            

####Do 4 actions:ensure all legal actions are enabled; Give user all there legal options( limited by role, location, hand); add list of research cities for shuttle flights
####draw 2 player cards
####infect cities
#### check if game is over before going to next player
        break
game()
