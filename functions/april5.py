def countto5():
    print(1, 2, 3, 4, 5)

def findX():
    x = 5
    print(x*5)

def findY():
    x = 5
    z = 2
    y = x + z
    return y

def showLeaderboard():
    print('__________________________\n')
    print('       LEADERBOARD        \n')
    print('__________________________\n')
    print('|     NAME     |   SCORE  \n')
    print('|   Ahmad Sani |    50    \n')
    print('__________________________\n')

play = False

while play:
    answer = input("Enter your answer here: ")
    if answer == "1":
        print("Oops! Wrong answer\n")
        showLeaderboard()
    elif answer == "2":
        print("Nice! you are right\n")
        showLeaderboard()
    else:
        print("Game Over!!!\n")
        showLeaderboard()
        play = False

# q1 write a function that prints out the result of multiplying 6 and 9 when called
# q2 write a function that prints out your name when called