##########################################################################################
#      Group-35                                                                          #
#        290201099 - Burak ERİNÇ                                                         #    
#        290201082 - Arif Ege ÖNDER                                                      #
#                                                                                        #
##########################################################################################

import random

# defining global variables to
# use them throughout the game
round_number = 1
total_points = 0
earned_points = 0

bunco_points = 21
mini_bunco_points = 5
matching_points = 1
bunco_count = 0
mini_bunco_count = 0

rolls_left = 3
dices_matches_round_number = 0

print(f"*****************\n|....ROUND{round_number}!....|\n*****************")

# start by rolling the dice
input("Enter to roll the dices")

# roll 3 dices randomly at once
# with using 'random' module
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print("Rolled dices are:", dice_1, dice_2, dice_3)

# checking if any dices are matching
# with the round number
dices_matches_round_number = 0

if dice_1 == round_number: dices_matches_round_number += 1
if dice_2 == round_number: dices_matches_round_number += 1
if dice_3 == round_number: dices_matches_round_number += 1

# checks for bunco 
if dices_matches_round_number == 3:
    print("BUNCO!! You earned", bunco_points, "points!")

    bunco_count += 1
    earned_points += bunco_points
    rolls_left -= 1

elif dices_matches_round_number == 0:
    # there are 2 cases when no dice matches round number
    # checks for mini-bunco
    if dice_1 == dice_2 and dice_2 == dice_3:
        print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
        mini_bunco_count += 1
        earned_points += mini_bunco_points
        rolls_left -= 1

    # no points earned
    else:
        print("You did not earn any points!")
        rolls_left = 0
else:
    # if there is no bunco and mini-bunco
    # we check for matching dices
    earned_points += dices_matches_round_number
    print('You earned', earned_points, 'point(s)!')
    rolls_left -= 1

# ROLL 2 (if needed)
if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)

    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    # checks for bunco 
    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        # there are 2 cases when no dice matches round number
        # checks for mini-bunco
        if dice_1 == dice_2 and dice_2 == dice_3:
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        # no points earned
        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        # if there is no bunco and mini-bunco
        # we check for matching dices
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

# ROLL 3 (if needed)
if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)
    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    # checks for bunco 
    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        # there are 2 cases when no dice matches round number
        # checks for mini-bunco
        if dice_1 == dice_2 and dice_2 == dice_3 :
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        # no points earned
        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        # if there is no bunco and mini-bunco
        # we check for matching dices
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

# round ending message
print("Round", round_number, "ended with total of", earned_points, "point(s).")

# setting the global variables for
# the next round
round_number += 1
total_points += earned_points
earned_points = 0
rolls_left = 3

# now we will copy this code for 6 times
# since we are not allowed to use loops

# 2nd round

print(f"*****************\n|....ROUND{round_number}!....|\n*****************")

input("Enter to roll the dices")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print("Rolled dices are:", dice_1, dice_2, dice_3)

dices_matches_round_number = 0

if dice_1 == round_number: dices_matches_round_number += 1
if dice_2 == round_number: dices_matches_round_number += 1
if dice_3 == round_number: dices_matches_round_number += 1

if dices_matches_round_number == 3:
    print("BUNCO!! You earned", bunco_points, "points!")

    bunco_count += 1
    earned_points += bunco_points
    rolls_left -= 1

elif dices_matches_round_number == 0:
    
    if dice_1 == dice_2 and dice_2 == dice_3:
        print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
        mini_bunco_count += 1
        earned_points += mini_bunco_points
        rolls_left -= 1

    else:
        print("You did not earn any points!")
        rolls_left = 0
else:
    earned_points += dices_matches_round_number
    print('You earned', earned_points, 'point(s)!')
    rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)

    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:

        if dice_1 == dice_2 and dice_2 == dice_3:
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)
    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        
        if dice_1 == dice_2 and dice_2 == dice_3 :
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else :
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

print("Round", round_number, "ended with total of", earned_points, "point(s).")

round_number += 1
total_points += earned_points
earned_points = 0
rolls_left = 3

# 3

print(f"*****************\n|....ROUND{round_number}!....|\n*****************")

input("Enter to roll the dices")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print("Rolled dices are:", dice_1, dice_2, dice_3)

dices_matches_round_number = 0

if dice_1 == round_number: dices_matches_round_number += 1
if dice_2 == round_number: dices_matches_round_number += 1
if dice_3 == round_number: dices_matches_round_number += 1

if dices_matches_round_number == 3:
    print("BUNCO!! You earned", bunco_points, "points!")

    bunco_count += 1
    earned_points += bunco_points
    rolls_left -= 1

elif dices_matches_round_number == 0:
    
    if dice_1 == dice_2 and dice_2 == dice_3:
        print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
        mini_bunco_count += 1
        earned_points += mini_bunco_points
        rolls_left -= 1

    else:
        print("You did not earn any points!")
        rolls_left = 0
else:
    earned_points += dices_matches_round_number
    print('You earned', earned_points, 'point(s)!')
    rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)

    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:

        if dice_1 == dice_2 and dice_2 == dice_3:
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)
    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        
        if dice_1 == dice_2 and dice_2 == dice_3 :
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else :
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

print("Round", round_number, "ended with total of", earned_points, "point(s).")

round_number += 1
total_points += earned_points
earned_points = 0
rolls_left = 3

# 4

print(f"*****************\n|....ROUND{round_number}!....|\n*****************")

input("Enter to roll the dices")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print("Rolled dices are:", dice_1, dice_2, dice_3)

dices_matches_round_number = 0

if dice_1 == round_number: dices_matches_round_number += 1
if dice_2 == round_number: dices_matches_round_number += 1
if dice_3 == round_number: dices_matches_round_number += 1

if dices_matches_round_number == 3:
    print("BUNCO!! You earned", bunco_points, "points!")

    bunco_count += 1
    earned_points += bunco_points
    rolls_left -= 1

elif dices_matches_round_number == 0:
    
    if dice_1 == dice_2 and dice_2 == dice_3:
        print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
        mini_bunco_count += 1
        earned_points += mini_bunco_points
        rolls_left -= 1

    else:
        print("You did not earn any points!")
        rolls_left = 0
else:
    earned_points += dices_matches_round_number
    print('You earned', earned_points, 'point(s)!')
    rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)

    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:

        if dice_1 == dice_2 and dice_2 == dice_3:
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)
    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        
        if dice_1 == dice_2 and dice_2 == dice_3 :
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else :
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

print("Round", round_number, "ended with total of", earned_points, "point(s).")

round_number += 1
total_points += earned_points
earned_points = 0
rolls_left = 3

# 5

print(f"*****************\n|....ROUND{round_number}!....|\n*****************")

input("Enter to roll the dices")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print("Rolled dices are:", dice_1, dice_2, dice_3)

dices_matches_round_number = 0

if dice_1 == round_number: dices_matches_round_number += 1
if dice_2 == round_number: dices_matches_round_number += 1
if dice_3 == round_number: dices_matches_round_number += 1

if dices_matches_round_number == 3:
    print("BUNCO!! You earned", bunco_points, "points!")

    bunco_count += 1
    earned_points += bunco_points
    rolls_left -= 1

elif dices_matches_round_number == 0:
    
    if dice_1 == dice_2 and dice_2 == dice_3:
        print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
        mini_bunco_count += 1
        earned_points += mini_bunco_points
        rolls_left -= 1

    else:
        print("You did not earn any points!")
        rolls_left = 0
else:
    earned_points += dices_matches_round_number
    print('You earned', earned_points, 'point(s)!')
    rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)

    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:

        if dice_1 == dice_2 and dice_2 == dice_3:
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)
    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        
        if dice_1 == dice_2 and dice_2 == dice_3 :
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else :
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

print("Round", round_number, "ended with total of", earned_points, "point(s).")

round_number += 1
total_points += earned_points
earned_points = 0
rolls_left = 3

# 6

print(f"*****************\n|....ROUND{round_number}!....|\n*****************")

input("Enter to roll the dices")

dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)
dice_3 = random.randint(1, 6)

print("Rolled dices are:", dice_1, dice_2, dice_3)

dices_matches_round_number = 0

if dice_1 == round_number: dices_matches_round_number += 1
if dice_2 == round_number: dices_matches_round_number += 1
if dice_3 == round_number: dices_matches_round_number += 1

if dices_matches_round_number == 3:
    print("BUNCO!! You earned", bunco_points, "points!")

    bunco_count += 1
    earned_points += bunco_points
    rolls_left -= 1

elif dices_matches_round_number == 0:
    
    if dice_1 == dice_2 and dice_2 == dice_3:
        print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
        mini_bunco_count += 1
        earned_points += mini_bunco_points
        rolls_left -= 1

    else:
        print("You did not earn any points!")
        rolls_left = 0
else:
    earned_points += dices_matches_round_number
    print('You earned', earned_points, 'point(s)!')
    rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)

    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:

        if dice_1 == dice_2 and dice_2 == dice_3:
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else:
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

if rolls_left > 0:
    input("Enter To Roll the dices")

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    dice_3 = random.randint(1, 6)

    print("Rolled dices are:", dice_1, dice_2, dice_3)
    dices_matches_round_number = 0

    if dice_1 == round_number: dices_matches_round_number += 1
    if dice_2 == round_number: dices_matches_round_number += 1
    if dice_3 == round_number: dices_matches_round_number += 1

    if dices_matches_round_number == 3:
        print("BUNCO!! You earned", bunco_points, "points!")

        bunco_count += 1
        earned_points += bunco_points
        rolls_left -= 1

    elif dices_matches_round_number == 0:
        
        if dice_1 == dice_2 and dice_2 == dice_3 :
            print("Mini-BUNCO! You earned", mini_bunco_points, "points!")
            mini_bunco_count += 1
            earned_points += mini_bunco_points
            rolls_left -= 1

        else :
            print("You did not earn any points!")
            rolls_left = 0
    else:
        earned_points += dices_matches_round_number
        print('You earned', earned_points, 'point(s)!')
        rolls_left -= 1

print("Round", round_number, "ended with total of", earned_points, "point(s).")

# this time we are not setting the global
# variables because there is no round to be played

# game ending message
print("*****************\n|..GAME ENDED!..|\n*****************")
print("Total points:", total_points)
print("Played rounds:", round_number)
print("You've had", bunco_count, "bunco(s)")
print("You've had", mini_bunco_count ,"mini bunco(s)")
