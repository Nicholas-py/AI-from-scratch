import random


testboards = [[1, 0,-1, 0, 0, 0, 1,-1,-1],
              [1, 1, 1, 0, 0, 0, 0, 0, 0],
              [-1,1, 1, 1,-1, 1, 1, 1,-1],
              [1, 0,-1, 0,-1, 0, 0, 0, 1]]


def displayboard(state):
    assert len(state) == 9
    diction = {1:'X', 0:' ', -1:'O'}
    string = ''
    for i in range(3):
        for j in range(3):
            string += diction[state[3*i+j]]
            string += '|'
        string = string[0:-1] + '\n'
    return string


def haswon(state):
    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]
    
    for line in wins:
        player = state[line[0]]
        for i in line:
            if state[i] != player:
                player = 0
        if player != 0:
            return player
    return 0





def bestmove(board, player):
    corners = [0,2,6,8]
    edges = [1,3,5,7]


    if haswon(board):
        return None
    allowedmoves = []
    for i in range(9):
        if board[i] == 0:
            allowedmoves.append(i)
    if allowedmoves == []:
        return None

    board = board.copy()
    for i in allowedmoves:
        board[i] = player
        if haswon(board) == player:
            return i
        board[i] = 0
    
    for i in allowedmoves:
        board[i] = -player
        if haswon(board) == -player:
            return i
        board[i] = 0
    
    if board[4] == 0:
        return 4
    
    if board[0] == -player and board[8] == -player:
        return 1
    
    if board[2] == -player and board[6] == -player:
        return 1
    
    if board == [player,-player,0,0,player,0,0,0,-player]:
        return 6

    for i in corners:
        if board[i] == 0:
            return i
    
    return allowedmoves[0]

    
def midai(board, player):
    if haswon(board):
        return None
    allowedmoves = []
    for i in range(9):
        if board[i] == 0:
            allowedmoves.append(i)
    if allowedmoves == []:
        return None

    board = board.copy()
    for i in allowedmoves:
        board[i] = player
        if haswon(board) == player:
            return i
        board[i] = 0
    
    for i in allowedmoves:
        board[i] = -player
        if haswon(board) == -player:
            return i
        board[i] = 0
    return random.randint(0,8)

#for board in testboards:
#    print(displayboard(board))
#    print('winner:',haswon(board))
#    print('X best move:', bestmove(board,1))
#    print('O best move:', bestmove(board,-1))

def playagainst(func, yournumber):
    board = [0]*9
    for i in range(9):
        print(displayboard(board),'\n')

        player = ((i+1)%2)*2-1
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


def recurse(board, active):
    lst = [board]
    for i in range(9):
        if board[i] == 0:
            board = board.copy()
            board[i] = -active
            lst += recurse(board, -active)
            board[i] = 0
    return lst

def generatedata(player):
    inputs = recurse([0]*9, 1)
    random.shuffle(inputs)
    ops  = []
    for i in inputs:
        best = bestmove(i, player)
        new = [0]*9
        if best:
            new[best] = 1
        ops.append(new)
    return inputs, ops

def networkplayagainst(network):
    return lambda board, player : getmovefromairesults(network.fire(board))

def getmovefromairesults(results):
    return results[0].argmax()
    maxi = max(results[0])
    print(maxi)
    return results[0].index(maxi)


inputs, targets = generatedata(1)
