def displayboard(state):
    assert len(state) == 9
    diction = {1:'X', 0:' ', -1:'O'}
    string = ''
    for i in range(3):
        for j in range(3):
            current = state[3*i+j]
            if current in diction:
                string += diction[current]
            else:
                string += str(current)
            string += '|'
        string = string[0:-1] + '\n'
    return string



def tostr(board):
    return '|'.join(list(map(str, board)))

def fromstr(board):
    return list(map(int, board.split('|')))


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

