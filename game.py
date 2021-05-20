from board import board
from player import player
def game():
#SETUP
##set out the board and place research station at pieces
    b = board('map.txt')
    b.map.list['atlanta'].buildresearchstation()
    b.researchstations=5

##select role
    numplayers=int(input('How many players?'))
    players=[]
    for i in range (numplayers):
        for j in range(len(b.roles)):
            print("role "+str(j)+":" +b.roles[j])
        roleselect=int(input('Enter number of role'))
        players.append(player(b.roles.pop(roleselect),b.map.list['atlanta']))
##distribute non epidemic player cards based on num of players
##infect 9 cities
##play game
####Start with player 1
####display each players role, hand, map, cured, outbreak num and infection rate
####Do 4 actions:ensure all legal actions are enabled; Give user all there legal options( limited by role, location, hand)
####draw 2 player cards
####infect cities
#### check if game is over before going to next player
game()
