from board import board
from player import player
def game():
#SETUP
##set out the board and place research station at pieces
    b = board('map.txt')
    b.map.list['atlanta'].buildresearchstation()
    b.researchstations=5

##give each player cards and a pawn
    numplayers=int(input('How many players?'))
    players=[]
    for i in range (numplayers):
        for j in range(len(b.roles)):
            print("role "+str(j)+":" +b.roles[j])
        roleselect=int(input('Enter number of role'))
        players.append(player(b.roles.pop(roleselect),b.map.list['atlanta']))
        print(players[i].role)
game()
