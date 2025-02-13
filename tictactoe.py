import random
from Tictactoerules import haswon, displayboard


def playagainst(func, yournumber, stepfunc = False):
    board = [0]*9
    for i in range(9):
        print(displayboard(board),'\n')
        player = ((i+1)%2)*2-1

        if stepfunc:
            stepfunc(board, player)

        if player == -yournumber:
            move = func(board, player)
            tick = 0
            while 0 > move or move >= 9 or board[move] != 0:
                move = func(board, player)
                tick += 1
                if tick > 50:
                    return 'AI has given up. '+str(yournumber)+'  has won!'


        else:
            move = int(input())
            tick = 0
            while 0 > move or move >= 9 or board[move] != 0:
                move = int(input('Try again.\n'))
                tick += 1
                if tick > 50:
                    return 'You\'ve given up. '+str(-yournumber)+'  has won!'


        if haswon(board) == 0 and move is not None:
            board[move] = player
            if haswon(board):
                print(displayboard(board),'\n')
                return str(haswon(board)) + ' has won!'
        else:
            print(displayboard(board),'\n')
            return str(haswon(board)) + ' has won!'
    print(displayboard(board),'\n')
    return 'Tie!'

rand = lambda x,y: random.randint(0,8)

#print(playagainst(midai, -1))




def networkplayagainst(network):
    return lambda board, player : getmovefromairesults(network.fire(board))

def networkplayagainst2(network):
    return lambda board, player: getmovefromairesults2(network.fire(board))

def getmovefromairesults(results):
    return results[0].argmax()

def getmovefromairesults2(results):
    num1 = round(results[0][0]) + 1
    num2 = round(results[0][1]) + 1
    return num1 * 3 + num2

    