from board import board
from player import player
def displaygamestate(b,players):
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
    print('\n')
    print("CURED DISEASES")
    print(b.cureddiseases)
    print('\n')
    print("AVAILABLE DISEASE CUBES")
    print(b.diseasecubes)
    print('\n')
    for i in range(len(players)):
        print("Player City: " +players[i].role.city.city)
        print("Player "+str(i)+" Hand:")
        print(players[i].hand)
        print('\n') 
            

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
                b.diseasecubes['red']=b.diseasecubes['red']-3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].redcubes=2
                b.diseasecubes['red']=b.diseasecubes['red']-2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].redcubes=1
                b.diseasecubes['red']=b.diseasecubes['red']-1
        if b.infectiondeck.discardpile[i] in b.map.bluecities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].bluecubes=3
                b.diseasecubes['blue']=b.diseasecubes['blue']-3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].bluecubes=2
                b.diseasecubes['blue']=b.diseasecubes['blue']-2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].bluecubes=1
                b.diseasecubes['blue']=b.diseasecubes['blue']-1
        if b.infectiondeck.discardpile[i] in b.map.blackcities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].blackcubes=3
                b.diseasecubes['black']=b.diseasecubes['black']-3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].blackcubes=2
                b.diseasecubes['black']=b.diseasecubes['black']-2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].blackcubes=1
                b.diseasecubes['black']=b.diseasecubes['black']-1
        if b.infectiondeck.discardpile[i] in b.map.yellowcities:
            if i<=2:
                b.map.list[b.infectiondeck.discardpile[i]].yellowcubes=3
                b.diseasecubes['yellow']=b.diseasecubes['yellow']-3
            elif i<=5:
                b.map.list[b.infectiondeck.discardpile[i]].yellowcubes=2
                b.diseasecubes['yellow']=b.diseasecubes['yellow']-2
            else:
                b.map.list[b.infectiondeck.discardpile[i]].yellowcubes=1
                b.diseasecubes['yellow']=b.diseasecubes['yellow']-1
##play game
####Start with player 1
####display each players role, hand, map, cured, outbreak num and infection rate
    while True:
        for i in range(numplayers):
            displaygamestate(b,players)
####Do 4 actions:ensure all legal actions are enabled; Give user all there legal options( limited by role, location, hand); add list of research cities for shuttle flights
            for j in range(4):
                print("Available actions")
                print("1: Movement action")
                if players[i].role.city.city in players[i].hand:
                    if players[i].role.city.researchstation ==0:
                        if b.researchstations>0:
                            print("2: Build research station")
                if players[i].role.city.redcubes or players[i].role.city.bluecubes or players[i].role.city.blackcubes or players[i].role.city.yellowcubes:
                    print("3: Treat disease")
                if players[i].role.city.city in players[i].hand:
                    print("4: Share Knowledge")
                else:
                        for k in range(numplayers):
                            if i !=k:
                                if players[i].role.city.city in players[k].hand:
                                    print("4: Share Knowledge")
                                    break
                if players[i].role.city.researchstation ==1:
                    print("5: Discover a cure")

                action=int(input("Enter selection"))
                


                if action == 1:
                    print("legal moves:")
                    if players[i].role.city.city in players[i].hand:
                        destination=input('Enter any city')
                        players[i].hand.remove(players[i].role.city.city)
                    else:
                        print(players[i].role.city.connections)
                        print(players[i].hand)
                        destination=input('Enter name of above cities')
                        if destination in players[i].hand:
                            if destination not in players[i].role.city.connections:
                                players[i].hand.remove(destination)
                    players[i].role.movecity(b.map.list[destination])

                elif action ==2:
                    players[i].hand.remove(players[i].role.city.city)
                    players[i].role.city.buildresearchstation()
                    b.researchstations=b.researchstations-1
                elif action ==3:
                    if players[i].role.city.yellowcubes:
                        if input('yellow? y/n') == 'y':
                            players[i].role.city.decyellowcube()
                            b.diseasecubes['yellow']=b.diseasecubes['yellow']+1
                    elif players[i].role.city.bluecubes:
                        if input('blue? y/n') == 'y':
                            players[i].role.city.decbluecube()
                            b.diseasecubes['blue']=b.diseasecubes['blue']+1
                    elif players[i].role.city.blackcubes:
                        if input('black? y/n') == 'y':
                            players[i].role.city.decblackcube()
                            b.diseasecubes['black']=b.diseasecubes['black']+1
                    else:
                        if input('red? y/n') == 'y':
                            players[i].role.city.decredcube()
                            b.diseasecubes['red']=b.diseasecubes['red']+1
                elif action ==4:
                    if players[i].role.city.city in players[i].hand:
                        numplayer=int(input('Which player would you like to share with?'))
                        numcard=int(input('Which card are you sharing?'))
                        players[numplayer].hand.append(players[i].hand[numcard])
                        players[i].hand.remove(players[i].role.city.city)
                    else:
                        for k in range(numplayers):
                            if i !=k:
                                if players[i].role.city.city in players[k].hand:
                                    answer=input('Do you want to share with player '+str(k)+'? y/n')
                                    if answer =='y':
                                        numcard=int(input('Which card would you like from this player)'))
                                        players[i].hand.append(players[k].hand[numcard])
                                        players[k].hand.pop(numcard)
                                        break
                elif action ==5:
                    numyellow=0
                    numblack=0
                    numblue=0
                    numred=0
                    for k in range(len(players[i].hand)):
                        if players[i].hand[k] in b.map.yellowcities:
                            numyellow=numyellow+1
                        if players[i].hand[k] in b.map.blackcities:
                            numblack=numblack+1
                        if players[i].hand[k] in b.map.bluecities:
                            numblue=numblue+1
                        if players[i].hand[k] in b.map.redcities:
                            numred=numred+1
                    if numyellow>=5 and b.cureddiseases['yellow']==0:
                        players[i].hand.pop(int(input("which yellow card would you like to play")))
                        players[i].hand.pop(int(input("which yellow card would you like to play")))
                        players[i].hand.pop(int(input("which yellow card would you like to play"))) 
                        players[i].hand.pop(int(input("which yellow card would you like to play")))
                        players[i].hand.pop(int(input("which yellow card would you like to play")))
                        b.cureddiseases['yellow']=1 
                    if numblue>=5 and b.cureddiseases['blue']==0:
                        players[i].hand.pop(int(input("which blue card would you like to play"))) 
                        players[i].hand.pop(int(input("which blue card would you like to play"))) 
                        players[i].hand.pop(int(input("which blue card would you like to play"))) 
                        players[i].hand.pop(int(input("which blue card would you like to play"))) 
                        players[i].hand.pop(int(input("which blue card would you like to play"))) 
                        b.cureddiseases['blue']=1 
                    if numred>=5 and b.cureddiseases['red']==0:
                        players[i].hand.pop(int(input("which red card would you like to play"))) 
                        players[i].hand.pop(int(input("which red card would you like to play"))) 
                        players[i].hand.pop(int(input("which red card would you like to play"))) 
                        players[i].hand.pop(int(input("which red card would you like to play"))) 
                        players[i].hand.pop(int(input("which red card would you like to play"))) 
                        b.cureddiseases['red']=1 
                    if numblack>=5 and b.cureddiseases['black']==0:
                        players[i].hand.pop(int(input("which black card would you like to play"))) 
                        players[i].hand.pop(int(input("which black card would you like to play"))) 
                        players[i].hand.pop(int(input("which black card would you like to play"))) 
                        players[i].hand.pop(int(input("which black card would you like to play"))) 
                        players[i].hand.pop(int(input("which black card would you like to play"))) 
                        b.cureddiseases['black']=1 
####draw 2 player cards
            for j in range(2):
                if len(players[i].hand)<7:
                    b.playerdeck.playcard()
                    players[i].hand.append(b.playerdeck.discardpile.pop())
                    if players[i].hand[len(players[i].hand)-1]=='Epidemic':
                        players[i].hand.remove('Epidemic')
                        b.outbreaks+=1
                        b.infectionrate.pop(0)
                        for k in range(3):
                            b.infectiondeck.playcard()
                            if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.yellowcities:
                                if b.cureddiseases['yellow'] ==0:
                                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].yellowcubes==3:
                                        for m in range(len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].yellowcube+=1
                                            b.diseasecubes['yellow']-=1
                                        b.outbreaks+=1
                                    else:
                                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incyellowcubes()
                                        b.diseasecubes['yellow']-=1
                            if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.bluecities:
                                if b.cureddiseases['blue'] ==0:
                                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].bluecubes==3:
                                        for m in range(len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].bluecube+=1
                                            b.diseasecubes['blue']-=1
                                        b.outbreaks+=1
                                    else:
                                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incbluecube()
                                        b.diseasecubes['blue']-=1
                            if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.redcities:
                                if b.cureddiseases['red'] ==0:
                                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].redcubes==3:
                                        for m in range(len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].redcube+=1
                                            b.diseasecubes['red']-=1
                                        b.outbreaks+=1
                                    else:
                                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incredcube()
                                        b.diseasecubes['red']-=1
                            if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.blackcities:
                                if b.cureddiseases['black'] ==0:
                                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].blackcubes==3:
                                        for m in range(len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].blackcube+=1
                                            b.diseasecubes['black']-=1
                                        b.outbreaks+=1
                                    else:
                                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incblackcubes()
                                        b.diseasecubes['black']-=1
                        b.infectiondeck.return2deck()    
####infect cities
            for j in range(b.infectionrate[0]):
                b.infectiondeck.playcard()
                if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.yellowcities:
                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].yellowcubes==3:
                        for m in range( len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].yellowcubes+=1
                            b.diseasecubes['yellow']-=1
                        b.outbreaks+=1
                    else:
                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incyellowcubes()
                        b.diseasecubes['yellow']-=1
                if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.bluecities:
                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].bluecubes==3:
                        for m in range( len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].bluecubes+=1
                            b.diseasecubes['blue']-=1
                        b.outbreaks+=1
                    else:
                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incbluecube()
                        b.diseasecubes['blue']-=1
                if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.redcities:
                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].redcubes==3:
                        for m in range( len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].redcubes+=1
                            b.diseasecubes['red']-=1
                        b.outbreaks+=1
                    else:
                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incredcube()
                        b.diseasecubes['red']-=1
                if b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1] in b.map.blackcities:
                    if b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].blackcubes==3:
                        for m in range( len(b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections)):
                            b.map.list[b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].connections[m]].blackcubes+=1
                            b.diseasecubes['black']-=1
                        b.outbreaks+=1
                    else:
                        b.map.list[b.infectiondeck.discardpile[len(b.infectiondeck.discardpile)-1]].incblackcubes()
                        b.diseasecubes['black']-=1

#### check if game is over before going to next player
            if b.outbreaks ==8:
                print("you lose")
                break
            if len(b.playerdeck.playercards)==0:
                print("you lose")
                break
            if b.diseasecubes['yellow']==0 and b.diseasecubes['blue']==0 and b.diseasecubes['red']==0 and b.diseasecubes['black']==0:
                print("you lose")
                break
            if b.cureddiseases['yellow']==1 and b.cureddiseases['red']==1 and b.cureddiseases['blue']==1 and b.cureddiseases['black']==1:
                print("congrats you win")
                break
game()

