import random 


def gameboard():
    x=[[0,0,0],
       [0,0,0],
       [0,0,0]]
    return x 

def randomboard(arg):
    '''
    arg = 0 ; with zero i.e. the board is not lost
    arg = 1 ; without zero i.e. a lost board
    '''
    vals = [2,4,8,16,32,64,128,256,512,1024,2048]
    rboard = list()
    for i in range(3):
        temp = list()
        for k in range(3):
            x = random.sample(vals,1)[0]
            temp.append(x)
        rboard.append(temp)
    if arg == 0:
        x = random.randint(0,2) 
        row = [0,random.sample(vals,1)[0],random.sample(vals,1)[0]]
        rboard.remove(rboard[x])
        rboard.insert(x,row)
        return rboard
    else:
        return rboard

def showboard(board):
    for i in board:
        rows = ''
        for j in i:
            k = ' '*(5 - len(str(j)))
            rows += f'{j}{k}'
        print(rows)  

def status(board):
    # 0=continue 1=won 2=lost
    statuslist = list()
    for i in board:
        for j in i:
            if j == 2048:
                statuslist.append(1)
            elif j == 0:
                statuslist.append(0)
            else:
                statuslist.append(2)
    if 1 in statuslist:
        return 'Game Won!'
    elif 0 in statuslist:
        return 'Continue'
    else:
        return 'Game Lost!'


def update(game_board,key):
    pressed_key = key.lower() 
    if pressed_key == 'w':
        ... 
    elif pressed_key == 'a':
        ...
    elif pressed_key == 's':
        ...
    elif pressed_key == 'd':
        ...
    else:
        print("Enter a valid choice!")


board = randomboard(0)
showboard(board)
print(status(board))