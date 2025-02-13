from Tictactoerules import haswon, tostr, fromstr, displayboard
import random




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
    
    if board[0] == -player and board[8] == -player and 1 in allowedmoves:
        return 1
    
    if board[2] == -player and board[6] == -player and 1 in allowedmoves:
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


def recurse(board, active):
    st = set()
    if bestmove(board, -active) is not None:
        st.add(tostr(board))

    for i in range(9):
        if board[i] == 0:
            board[i] = -active
            st = set.union(st, recurse(board, -active))
            board[i] = 0
    return st


def recurse2(board, active):
    st = set()
    if bestmove(board, -active) is not None:
        st.add(tostr(board)+"|"+str(-active))
        

    for i in range(9):
        if board[i] == 0:
            board[i] = -active
            st = set.union(st, recurse2(board, -active))
            board[i] = 0
    return st


def generatetictac(player):
    inputs = list(map(fromstr, recurse([0]*9, 1)))
    random.shuffle(inputs)
    ops  = []
    for i in inputs:
        best = bestmove(i, player)
        if best is not None:
            new = [best // 3 -1, best %3 -1]
        else:
            new = [0,0]
        ops.append(new)
    return inputs, ops


def generateclassifierdata():
    inputs = list(map(fromstr, recurse2([0]*9, 1)))+list(map(fromstr, recurse2([0]*9, -1)))
    ops = []
    for i in inputs:
        ops.append([whowillwin(i[0:9],i[9])])
    return inputs, ops

def whowillwin(board, player):
    while bestmove(board, player) is not None:
        board[bestmove(board,player)] = player
        player = -player
    return haswon(board)



def tictacdata():
    inputs, targets = recurse([0,0,0,0,0,0,0,0,0],1)
    lst = [0]*9
    for i in targets:
        lst[3*(i[0]+1)+i[1]+1] += 1
    bymoves = [[],[],[],[],[],[],[],[],[],[]]
    for i in inputs:
        bymoves[9-i.count(0)].append(i)
    
    bestmoves = [[0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9, [0]*9]
    for i in range(len(bymoves)):
        for j in bymoves[i]:
            bestmoves[i][bestmove(j, (i%2 - 1)*2+1)] += 1


    print("Counts by best move:")
    print(displayboard(lst))
    string = "".join([str(i)+": "+str(len(bymoves[i]))+", " for i in range(len(bymoves))])
    print("By move count: ", string)

    for i in range(9):
        print(i, 'moves: ')
        print(displayboard(bestmoves[i]))

