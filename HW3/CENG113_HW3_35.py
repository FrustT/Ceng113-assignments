###########################################
#      Group-35                           #
#        290201099 - Burak ERİNÇ          #
#        290201082 - Arif Ege ÖNDER       #
#                                         #
###########################################

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
scoreboard = [[0 for _ in range(10)], [0 for _ in range(10)]]
ballScores = [[], []]
rolled = False

# in the game, one player can finish before the other,
# so we have to keep track of both players' game states
gameOver = [False, False]

# variables to track each players' frames
frameSums = [[0 for _ in range(10)], [0 for _ in range(10)]]
frameToWrite = [0, 0]
framePointers = [0, 0]

rollCounter = [0, 0]
extraPoints = [[], []]
whenToCalculate = [[], []]

# we can access players' names with indexing the array
playersName = ["A", "B"]

# a way of keeping track of pins left
pinsUp = 10

def main():
    global pinsUp
    global playersName
    global ballScores
    global scoreboard
    global gameOver
    global rolled

    # randomly select a turn at first roll
    turn = randint(0, 1)

    # check if all players are finished, if not continue
    # 'all' function is a built-in function in python
    while not all(gameOver):
        # reset the pins for the new roll
        pinsUp = 10
        rolled = False

        print(f"Player {playersName[turn]} rolls...")

        # take first input and set rolled to true
        # so we don't get false positives
        enter_pins(turn)
        rolled = True
    
        # if first roll was not strike,
        # take the second pin input
        if pinsUp > 0:
            enter_pins(turn)

        # if there was no strike or spare before these
        # inputs, then calculate and write it to scoreboard
        if len(whenToCalculate[turn]) == 0:
            calculate_frame(turn)

        # special case for last frame
        if framePointers[turn] >= 9:

            # if strike or spare was the case
            if len(whenToCalculate[turn]) > 0:
                # we calculate the extra roll time with substracting
                # the whenToCalculate variable from the rollCounter.
                # which if strike is the case, will give us 2 and if
                # space was the case, will give us 1.
                difference = whenToCalculate[turn][0] - rollCounter[turn]

                scoreboard[turn][-1] = scoreboard[turn][-2]

                # take inputs 'difference' times
                for _ in range(difference):
                    pinsUp = 10
                    # take inputs and beware of invalids
                    while True:
                        pin = input("Pins: ").strip()

                        # if invalid throw an error and continue the loop
                        if len(pin) == 0 or int(pin) > pinsUp or int(pin) < 0 :
                            print("An invalid input.")
                            
                        else:
                            # since it's the last scoreboard frame,
                            # if not invalid, add the entered pin directly
                            # to scoreboard's last frame and break out
                            pin = int(pin)
                            scoreboard[turn][-1] += pin
                            break

                # add last hit bowls to the last score
                scoreboard[turn][-1] += frameSums[turn][-1]

            # finish the game for that specific player
            gameOver[turn] = True

        # after the frame was calculated, increment
        # frame pointer by one
        framePointers[turn] += 1

        # print the ball scores and total scores
        print("Ball scores: ", *ballScores[turn])

        print("Total Scores:", end=" ")
        print(*scoreboard[turn], sep = " | ")

        # if game is not over for the other player,
        # switch turns. if not, it won't switch by default
        if not gameOver[not turn]:
            turn = not turn

    else:
        # declare the winner by checking the last index of the scoreboard
        winner = 0 if scoreboard[0][-1] > scoreboard[1][-1] else 1
        print(f"Winner player is player {playersName[winner]}")    

def enter_pins(player):
    global pinsUp
    global whenToCalculate
    global frameSums
    global framePointers
    global rollCounter
    global rolled
    
    # take inputs and beware of invalids
    while True:
        pin = input("Pins: ").strip()

        # if invalid throw an error and continue the loop
        if len(pin) == 0 or int(pin) > pinsUp or int(pin) < 0 :
            print("An invalid input.")
            
        else:
            pin = int(pin)
            
            # increment rollCounter by 1
            rollCounter[player] += 1
            pinsUp -= pin

            # add entered pins to frameSums and ballScores
            frameSums[player][framePointers[player]] += pin
            ballScores[player].append(pin)
            
            # if there was a spare or a strike before this frame,
            # add the entered pin to extraPoints to track the points
            if len(extraPoints[player]) > 0:
                for extra in extraPoints[player]:
                    extra.append(pin)

            # if there was a spare or a strike before and
            # now it's the time to calculate the score,
            # calculate and write it on the scoreboard
            if len(whenToCalculate[player]) > 0 and rollCounter[player] == whenToCalculate[player][0]:
                calculate_frame(player)
            
            # if it's the first time rolling and
            # rolled is 10, STRIKE!
            if pin == 10 and not rolled:
                extraPoints[player].append([])
                # player will get 2 extra rolls
                whenToCalculate[player].append(rollCounter[player] + 2)

            # if left pins on the ground is 0,
            # then it is a SPARE!
            elif pinsUp == 0:
                extraPoints[player].append([])
                # player will get 1 extra roll
                whenToCalculate[player].append(rollCounter[player] + 1)
    
            break
                
def calculate_frame(player):
    global scoreboard
    global extraPoints
    global frameSums
    global frameToWrite

    if frameToWrite[player] > 0:
        # if it's not the first frame,
        # add the last scoreboard frame
        # to current scoreboard frame
        scoreboard[player][frameToWrite[player]] = scoreboard[player][frameToWrite[player] - 1]

    if len(extraPoints[player]) != 0:
        # if there was spare or a strike before,
        # add the tracked extra points to the current frame
        scoreboard[player][frameToWrite[player]] += sum(extraPoints[player].pop(0))
        whenToCalculate[player].pop(0)

    # lastly, add the frameSums to the scoreboard
    scoreboard[player][frameToWrite[player]] += frameSums[player][frameToWrite[player]]

    # after writing to the scoreboard, increment
    # the scoreboard pointer by 1
    frameToWrite[player] += 1

    # if last frame is written, end the game for the player
    if frameToWrite[player] >= 10: gameOver[player] = True

# call the main function to start the game
if __name__ == "__main__":
    main()