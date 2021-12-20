# importing randint method from the module random
# since we are going to use the module once
# while selecting a turn at first roll
from random import randint

# defining the global variables of players
# each variable is an array consists of
# 2 different indexes, first one is for
# player A, while the second one is
# for player B

# this way, we keep track
# of player with arrays acting as databases

# fill the scoreboard of both players with 10 zeros
scoreboard = [[0 for i in range(10)], [0 for i in range(10)]]
ballScores = [[], []]

# in the game, one player can finish before the other,
# so we have to keep track of both players' game states
gameOver = [False, False]

extraRolls = [0, 0]
frameSums= [0, 0]
framePointers = [0, 0]

# we can access players' names with indexing the array
playersName = ["A", "B"]

# a way of keeping track of pins left
pinsUp = 10

def main():
    global pinsUp
    global playersName
    global extraRolls
    global ballScores
    global scoreboard
    global gameOver

    # randomly select a turn at first roll
    turn = randint(0, 1)

    # check if all players are finished, if not continue
    # 'all' function is a built-in function in python
    while not all(gameOver):
        # reset the pins for the new roll
        pinsUp = 10

        print(f"Player {playersName[turn]} rolls...")

        if extraRolls[turn] != 0:
            # calculate_frame is used for calculating
            # the extra rolls if exists before
            calculate_frame(turn)

        roll(turn)
        
        if extraRolls[turn] == 0:
            # calculate_frame is used for calculating
            # the extra rolls if exists before
            calculate_frame(turn)

        extraRolls[turn] = 0

        # print the ball scores and total scores
        print("Ball scores: ", *ballScores[turn])

        print("Total Scores:", end=" ")
        print(*scoreboard[turn], sep = " | ")

        # if game is not over for the other player,
        # switch turns. if not, it won't switch by default
        if not gameOver[not turn]: turn = not turn

    else:
        # declare the winner by checking the last index of the scoreboard
        winner = 0 if scoreboard[0][-1] > scoreboard[1][-1] else 1
        print(f"Winner player is player {playersName[winner]}")

def roll(player):
    global framePointers
    global extraRolls

    # take the first roll
    firstRoll = enter_pins(player)
    
    # check if it is a strike
    if firstRoll != 10:
        # take the second roll
        secondRoll = enter_pins(player)        

        # if spare, add extra rolls to the player
        if firstRoll + secondRoll == 10:
            extraRolls[player] = 1

            # if the roll is the last roll, ask another input to user
            if framePointers[player] == 9:
                enter_pins(player)

    else:
        extraRolls[player] = 2

        # if the roll is the last roll, ask another input to user
        if framePointers[player] == 9:
            enter_pins(player)

def enter_pins(player):
    global pinsUp
    global ballScores
    global frameSums

    # take inputs in a loop and return to break
    while True:
        # take the pins input and strip
        # spaces for avoiding false positives
        pins = input("Pins: ").strip()

        # check if given input is valid
        if not pins.isnumeric() or int(pins) > pinsUp or len(pins) == 0:
            print("An invalid input.")

        # if valid, return entered pins
        else:
            pins = int(pins)
            pinsUp -= pins

            # add pins to the sums
            ballScores[player].append(pins)
            frameSums[player] += pins

            return pins

def calculate_frame(player):
    global scoreboard
    global framePointers
    global frameSums

    scoreboard[player][framePointers[player]] += frameSums[player]

    framePointers[player] += 1

    # if last frame is written, end the game for the player
    if framePointers[player] >= 10: gameOver[player] = True

# call the main function to start the game
if __name__ == "__main__":
    main()