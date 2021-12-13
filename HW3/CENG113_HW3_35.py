import random

scoreboard = [[0 for i in range(10)], [0 for i in range(10)]]
ballScores = [[], []]
gameOver = [False, False]
extraRolls = [0, 0]
frameSums= [0, 0]
framePointers = [0, 0]
playersName = ['A', 'B']

pinsUp = 10

def enter_pins(player):
    pins = 0
 ###INVALID INPUT'A BAK
    while pins <= pinsUp:
        pins = int(input(f'Please enter pins(0-{pinsUp}):'))
        pinsUp -= pins
        
    return pins

def print_scoreboard(player):
    print("Ball scores: ",*ballScores[player])

    print("Total Scores:", end=" ")
    print(*scoreboard[player], sep = " | ")

def calculate_frame(player):
    scoreboard[player][framePointers[player]] += frameSums[player]

    if framePointers[player] != 9: framePointers[player] += 1
    else: gameOver[player] = True

def extra_roll(player):
    pins = 0

    for i in range(extraRolls[player]):
        pins = int(input())#ENTER PINSI ÇAĞIR

        rolled(player, roll)

    calculate_frame(player)
    extraRolls[player] = 0

def rolled(player,pins):
    ballScores[player].append(pins)
    frameSums[player] += pins

def roll(player):
    print(f"Player {playersName[player]} rolls...")

    firstRoll = enter_pins(player)
    rolled(player, firstRoll)

    if firstRoll != 10:
        secondRoll = int(input("Pins: "))

        rolled(player,secondRoll)

        if firstRoll + secondRoll == 10 :
            extraRolls[player] = 1
            
            if framePointers[player] == 9: extra_roll(player)  

        else:
            calculate_frame(player)

    else:
        extraRolls[player] = 2
        
        if framePointers[player] == 9: 
            extraRolls[player] = 1
            extra_roll(player)

    print_scoreboard(player)

def main():
    turn = random.randint(0, 1)

    while not all(gameOver):
        if extraRolls[turn] != 0: extra_roll(turn)
        else: roll(turn)

        if not gameOver[not turn]: turn = not turn
    else:
        print(f"Game Over\n__________")
        
        for playersScores in scoreboard:
            print(f"Player {playersName[scoreboard.index(playersScores)]} got {playersScores[-1]} points")

        winner = 1 if scoreboard[0][-1] > scoreboard[1][-1] else 0
        print(f"{playersName[winner]} Have WON!!!")

main()