#########################################
#      Group-35                         #
#        290201099 - Burak ERİNÇ        #
#        290201082 - Arif Ege ÖNDER     #
#                                       #
#########################################

import random

# defining the global variables
PLAYERS = ["A", "B"]

scores = [[], []]
ball_scores = [[], []]
extra_rounds = [0, 0]

# defining the main function that
# the game will run in
def main():
	# using the global variables
	global scores

	# pick a random player to start the game
	turn = random.randint(0, 1)

	# roll with the round number and the turn
	while True:
		roll(turn)

		if len(scores[turn]) == 10 or not len(scores[turn]) == 10 and not len(scores[not turn]) == 10:
			# if a player is finished or
			# if players are both not finished
			# then switch turns
			turn = not turn
		
		if len(scores[turn]) == 10 and len(scores[not turn]) == 10:
			# if both players are finished,
			# finish the game
			break

		# otherwise, don't switch and let the other player finish

	# finish the game and check the scores
	# to determine the winner
	if sum(scores[0]) > sum(scores[1]):
		print("Winner is player A.")
	elif sum(scores[0]) < sum(scores[1]):
		print("Winner is player B.")
	else:
		print("Everyone is a winner! Tie game.")
		

# defining the roll function for every roll
# so we avoid code duplication
def roll(player):
	# using the global variables
	global PLAYERS
	global ball_scores
	global scores

	print("Player", PLAYERS[player], "rolls...")

	# take the pin input from player
	# and check if inputs are valid
	while True:
		pins_1 = int(input("Pins: "))
		pins_2 = int(input("Pins: "))

		if 0 <= pins_1 <= 10 and 0 <= pins_2 <= 10 and pins_1 + pins_2 <= 10:
			break

		print("An invalid input.")

	# if it's a strike, only add the first pin to ball_scores
	# else, add both pin scores
	if is_strike(pins_1): ball_scores[player].append(pins_1)
	else: ball_scores[player].extend([pins_1, pins_2])

	# print out the ball scores in one line
	print("Ball Scores:", *ball_scores[player])

	# set the new scores with custom function
	add_to_scores(player, pins_1, pins_2)

	# print the total scores
	print("Total scores:", end=" ")
	for score in scores[player]:
		print(score, end=" | ")
	print()

def add_to_scores(player, pins_1, pins_2):
	# using the global variables
	global scores
	global ball_scores

	# get the sum of scores so we can add onto it
	sum_of_scores = sum(scores[player])

	if is_strike(pins_1):
		if extra_rounds[player] == 0:
			extra_rounds[player] = 2
			return
		else:
			sum_of_scores = count_total_sum(player, sum_of_scores)

	elif is_spare(pins_1, pins_2):
		if extra_rounds[player] == 0:
			extra_rounds[player] = 1
			return
		else:
			sum_of_scores = count_total_sum(player, sum_of_scores)

	else:
		if extra_rounds[player] == 0:
			sum_of_scores += pins_1 + pins_2
		else:
			sum_of_scores = count_total_sum(player, sum_of_scores)

	scores[player].append(sum_of_scores)

def count_total_sum(player, sum_of_scores):
	for i in range(len(ball_scores[player]) - (extra_rounds[player] + 2), len(ball_scores[player]) + 1):
		if i >= 0:
			sum_of_scores += ball_scores[player][i - 1]

	return sum_of_scores

# checking if given pins are strike
def is_strike(pins_1):
	if pins_1 == 10: return True
	return False

# checking if given pins are spare
def is_spare(pins_1, pins_2):
	if pins_1 + pins_2 == 10: return True
	return False

main()
