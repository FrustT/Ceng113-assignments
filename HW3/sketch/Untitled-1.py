scoreboard = [[0 for i in range(10)], [0 for i in range(10)]]
ballScores = [[], []]
gameOver = [False, False]
extraRolls = [0, 0]
#frame sum ayrı arrya pointer ayrı
frameSumA,frameSumB,framePointerA,framePointerB = 0,0,0,0
frames =[[frameSumA,framePointerA],[frameSumB,framePointerB]]

def main():
    while not (*gameOver):
        print("rewrawr")
	#roll()
""""""

def print_scoreboard(player):
	global scoreboard

	print("Total Scores:", end=" ")
	for i in range(len(scoreboard[player])):
		if i == len(scoreboard[player]) - 1:
			print(scoreboard[player][i])
		else:
			print(scoreboard[player][i], end=" | ")

def write_ballScores(player):
    print("Ball scores:", end=" ")
    print(*ballScores[0])

print_scoreboard(0)

#Total Scores:  5  |  14  |  22  |  27  |  36  |  45  |  54  |  59  |  59  |  67