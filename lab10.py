# prelab:
from math import fabs, floor
from random import random
from random import randrange

# Print an introduction of the game
def printIntro():
    print("This program simulates the game of Rackquetball between two players")


# Read the number of games to simulate from user:
# How many games to simulate?
# Read probabilities a player wins a server from user:
# What is the prob. player A wins a serve?
def getInputs():
    a = eval(input("What is the probability that player A wins a serve: "))
    b = eval(input("What is the probability that player B wins a serve: "))
    n = eval(input("How many games to simulate: "))
    return a,b,n

# print the summary of the games:
# parameters: winsA, winsB
# winsA: total number of games player A wins, type: integer
# winsB: total number of games player B wins, type: integer
# does not return anything
def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Games simulated: ", n)
    print("Wins for A: ", winsA, "(", round(100*winsA/n,2), "%)")
    print("Wins for B: ", winsB, "(", round(100*winsB/n,2), "%)")


# simulate n games:
# paramters: n, probA, probB
# n = total number of games to be played, type: integer
# probA: player A's probablility to win a serve while he serves, type: floating
# probB: player B's probablility to win a serve while he serves, type: floating
# returns winsA, winsB
def simNGames(n, probA, probB):
    winsA = 0 # number of games that player A wins, type: integer
    winsB = 0 # number of games that player B wins, type: integer
    # simulate each of the n game
    for i in range(n):
        # simulating each game returns the final score of that game.
        # scoreA: Player A's score of game i
        # scoreB: Player B's score of game i
        scoreA, scoreB = simOneGame(probA, probB)
        # update wins count
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

# simulate one game
# parameters: probA, probB
# probA: player A's probablility to win a serve while he serves, type: floating
# probB: player B's probablility to win a serve while he serves, type: floating
# returns scoreA, scoreB
# scoreA: score of player A, type: integer
# scoreB: score of player B, type: integer
def simOneGame(probA, probB):
    gamePoint = 15

    # start the game
    # initially, scores are 0
    scoreA = 0
    scoreB = 0

    #initiallly, serveCounts are 0
    serveCountA = 0
    serveCountB = 0

    # Task 1: At the very beginning of the game players need to decide who will serves first.
    serving = decideServingFirst()

    # Task 2:
    # The game will continue until any player scores the gamePoint first
    while scoreA != gamePoint and scoreB != gamePoint:
        # Check deuce condition and handle it. Update gamePoint if required
        gamePoint = checkAndHandleDeuce(scoreA, scoreB, gamePoint)

        # increment the serveCount of the corresponding player
        if(serving == 'A'):
            serveCountA = serveCountA + 1
        else:
            serveCountB = serveCountB + 1

        # simulate one serve and get the winnser of that serve
        rnd = random()
        if serving == 'A':        
            if rnd < probA:     # A wins the serve
                winner = 'A'
            else:
                winner = 'B' # otherwise, B wins the serve

        else:
            if rnd < probB:     # B wins the serve
                winner = 'B'
            else:
                winner = 'A' # Otherwise, A wins the serve

        # update the score of the winner
        if(winner == 'A'):
            scoreA = scoreA + 1
        else:
            scoreB = scoreB + 1

        # Check if serve change if required.
        # That means, if player A were serving two consecutive times, player B will start serving.
        serving = checkAndDoServeChange(serveCountA, serveCountB, serving)

    return scoreA, scoreB

# Task 1: Complete the function decideServingFirst
# Flip a coin, if it is HEAD, A will serve, otherwise B
# no input parameters
# return a string. The two possible values of the returned string are 'A' or 'B'
def decideServingFirst():
    x = random()
    if x < 0.5:
        return ("A")
    else:
        return ("B")
    
    

# Task 2A: check change of service and if so, do the change
# @parameters: serveCountA, serveCountB, serving
# serveCountA: how many times player A serves, type: integer
# serveCountB: how many times player B serves, type: integer
# serving: who just served, type: string. Possible values could be: 'A' or 'B'
# return servingNext (string datatype), Possible values are 'A' or 'B'
def checkAndDoServeChange(serveCountA, serveCountB, serving):
    if(serving == "A"):
        if(serveCountA % 2 == 0):
            return ("B")
        else:
            return ("A")
    else:
         if(serveCountB % 2 == 0):
             return ("A")
         else:
             return ("B")
    

# Task 2B: check and handle deduce condition
# @paramters: scoreA, scoreB, gamePoint
# scoreA: score of player A, type: integer
# scoreB: score of player B,  type: integer
# gamePoint: current GamePoint,  type: integer
# return updated gamePoint (integer datatype) based on deuce Condition
def checkAndHandleDeuce(scoreA, scoreB, gamePoint):
    # if scores of two players are same and their scores are just 1 point less
    # than the gamePoint, deuce condition occurs.
    # if deuce condition occurs, gamePoint needs to incremented by 1
    # return the gamePoint
    if(scoreA == (gamePoint - 1) and scoreB == (gamePoint - 1)):
        gamePoint = gamePoint + 1
    return (gamePoint)
    
        
    
    
def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

	
#DO NOT DELETE THIS PART
#This part call the main in a way that will make this main only run
#for task1,2A,2B and will not run for task 3 (unit tests)
if __name__ == "__main__":
    main()
