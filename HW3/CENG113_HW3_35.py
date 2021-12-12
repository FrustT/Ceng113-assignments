import random

scoreboard = [[0 for i in range(10)], [0 for i in range(10)]]
ballScores = [[], []]
gameOver = [False, False]
extraRolls = [0, 0]
frameSums= [0,0]
framePointers = [0,0]
playersName = ['A','B']


def print_scoreboard(player):
    global scoreboard

    print("Ball scores: ",*ballScores[player])

    print("Total Scores:", end=" ")
    print(*scoreboard[player],sep = '|')


def calculate_frame(player):
    scoreboard[player] [framePointers[player]] += frameSums[player]

    if framePointers[player] != 9: framePointers[player] += 1
    
    else : gameOver[player] = True

def extra_roll(player): #roll için daha iyi bir isim lazım
    roll= 0

    for a in range(extraRolls[player]):
        roll= random.randrange(0,10-roll)

        rolled(player,roll)

    calculate_frame(player)
    extraRolls[player] = 0


def rolled(player,pins):
    print(f"Pins:{pins}")
    ballScores[player].append(pins)
    frameSums[player] += pins


def Roll(player): #THIS IS NO EXTRA ROLL SEQUENCE
     print(f"Player {playersName[player]} rolls...")

     firstRoll= random.randrange(0,10)
     rolled(player,firstRoll)

     if firstRoll != 10:
          secondRoll= random.randrange(0,10-firstRoll)
          rolled(player,secondRoll)

          if firstRoll + secondRoll == 10 : #SPARE
               print("Spare")
               extraRolls[player] = 1

          else :#OPEN FRAME
               calculate_frame(player)

     else :#STRİKE
          print(f"Strike!!!")
        
          extraRolls[player] = 2

          
     print_scoreboard(player)


def main():

    turn = random.randint(0,1)

    while not all(gameOver):#this loop keeps repeating till both player's game is over

        if extraRolls[turn] != 0:extra_roll(turn)
        else :Roll(turn)

        if not gameOver[turn -1] : turn = (turn+1) % 2
    else:
        print(f"Game Over\n__________")
        
        for playersScores in scoreboard:
            print(f"Player {playersName[scoreboard.index(playersScores)]} got {playersScores[-1]} points")

        winner = 1 if scoreboard[0][-1]> scoreboard[1][-1] else 0
        print(f"{playersName[winner]} Have WON!!!")
    


main()