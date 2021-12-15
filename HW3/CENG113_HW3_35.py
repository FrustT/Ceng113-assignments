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
    global pinsUp
    pins = 0

    while True:
        pins = input(f'Please enter pins(0-{pinsUp}):').strip()
        if not pins.isnumeric() or int(pins) > pinsUp or len(pins) == 0:
            print(f"Invalid Input")
        else:
            pins = int(pins)
            pinsUp -= pins
            rolled(player,pins)
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
    for i in range(extraRolls[player]):
        enter_pins(player)    
    extraRolls[player] = 0

def rolled(player,pins):
    print(f"Pins:{pins}")
    ballScores[player].append(pins)
    frameSums[player] += pins

def roll(player):
    firstRoll = enter_pins(player)
    
    if firstRoll != 10:
        secondRoll = enter_pins(player)        

        if firstRoll + secondRoll == 10 :
            
            if framePointers[player] == 9:LastFrame_ExtraRoll(player) 
            else : extraRolls[player] = 1

    else:
        
        if framePointers[player] == 9:LastFrame_ExtraRoll(player)
        else : extraRolls[player] = 2


def LastFrame_ExtraRoll(player):
    global pinsUp
    while True:
        pinsUp = 10
        pins = enter_pins(player)
        if pins < 10 :
            break

def main():
    global pinsUp#bu global pinsup'ı doğru yere koyarsak bu line'ı sadece bir kere yazabiliriz gibi geliyo bana, kavrayamadım bu saatte
    turn = random.randint(0, 1)

    while not all(gameOver):

        print(f"Player {playersName[turn]} rolls...")
        pinsUp = 10
        if extraRolls[turn]: extra_roll(turn)
        else: roll(turn)

        if not extraRolls[turn]: calculate_frame(turn)
        print_scoreboard(turn)

        if not gameOver[not turn]: turn = not turn
    else:
        print(f"Game Over\n__________")
        
        for playersScores in scoreboard:
            print(f"Player {playersName[scoreboard.index(playersScores)]} got {playersScores[-1]} points")

        winner = 0 if scoreboard[0][-1] > scoreboard[1][-1] else 1
        print(f"{playersName[winner]} Have WON!!!")

main()