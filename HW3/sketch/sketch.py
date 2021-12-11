import random
notAvailableToRoll = []
notAvailableToRoll[:] = noRollLeftA,noRollLeftB = False, False
Players = ["A","B"]
frameSumA,frameSumB,framePointerA,framePointerB,extraRollA,extraRollB= 0,0,0,0,0,0
scoreboard = []
frames =[frameSumA,framePointerA],[frameSumB,framePointerB]
ballScores = ["Ball Scores =","Ball Scores ="]
scoreboard[:] =A,B= [[0 for i in range(10)],ballScores[0],extraRollA,noRollLeftA],[[0 for i in range(10)],ballScores[1],extraRollB,noRollLeftB]
#One table would be more efficent but this is just a sketch for now


def write_scoreboard(player):
  commonIndex = scoreboard.index(player)
  table = scoreboard[commonIndex]
  
  flag = False
  print(ballScores[commonIndex])
  

  print(f"Total Scores:  ",end='')

  for frame in table[0]:

    if flag:
      print("  |  ",end ='')
    else:flag=True

    print(frame,end='')
  print("")



def calculate_frame(player):
  commonIndex = scoreboard.index(player)
  table ,frame= scoreboard[commonIndex],frames[commonIndex]

  if frame[1] >= 1:
    table[0][frame[1]] += table[0][frame[1]-1]
  table[0][frame[1]] += frame[0]
    
  frame[0]=0
  frame[1]+= 1
  if frame[1] == 10:
      notAvailableToRoll[commonIndex] = True


def roll(player):
    commonIndex =scoreboard.index(player)

    if not notAvailableToRoll[commonIndex]:
        print(f"Player {Players[commonIndex]} rolls…")

    # this code checks for extrarolls from spare or strike
        if player[2]:
            extra_roll(player[2],player)
        else:
            

            firstRoll= random.randrange(0,10)
            print(f"Pins:{firstRoll}")
            
            ballScores[commonIndex]+= f"  {firstRoll}"
            frames[commonIndex][0] += firstRoll

            if firstRoll != 10:
                secondRoll= random.randrange(0,10-firstRoll)
                print(f"Pins:{secondRoll}")
                ballScores[commonIndex] += f"  {secondRoll}"
                frames[commonIndex][0] += secondRoll
            
                if firstRoll + secondRoll ==10:#spare
                    print("Spare")
                    write_scoreboard(player)
                    player[2] += 1
                
                else:#open frame
                    print(f"open frame")

                    calculate_frame(player)

                    write_scoreboard(player)
                
            else:#Strike
                print(f"Strike")
                write_scoreboard(player)
                player[2] += 2


def extra_roll(extraRoll,player):
    commonIndex =scoreboard.index(player)
    roll= 0

    for a in range(extraRoll):
        roll= random.randrange(0,10-roll)
        ballScores[commonIndex] += f" {roll}"
        frames[commonIndex][0] += roll
    calculate_frame(player)
    extraRoll = 0



def main():
    firstPlayerToRoll = scoreboard[random.randint(0,1)] 
    player = firstPlayerToRoll
    while not (noRollLeftA and noRollLeftB):
        roll(player)
        if notAvailableToRoll[scoreboard.index(player)-1] == False:
            player = scoreboard[scoreboard.index(player)-1]
        else:
            if notAvailableToRoll[scoreboard.index(player)]== True:
                break
    print(f"Game Over\n__________\nPlayer A got {A[0][9]} points\nPlayer B got {B[0][9]} points")
    if A[0][9]> B[0][9]: 
        print(f"{Players[scoreboard.index(A)]} Have WON!!!")
    else:print(f"{Players[scoreboard.index(B)]} Have WON!!!")
            
        
            



main()