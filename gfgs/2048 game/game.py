import random 


def gameboard():
    x=[[2,0,2],
       [4,4,0],
       [0,0,2]]
    game = list()
    for i in range(3):
        temp = list()
        for j in range(3):
            temp.append(random.sample([0,0,0,2,2,4],1)[0])
        game.append(temp)
    
    return game


    

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
        row1 = game_board[0] 
        row2 = game_board[1]
        row3 = game_board[2]
        for j in range(3):
            if row1[j] == row2[j]:
                row1[j] *= 2
                if row3[j] == 0:
                    row2[j] = random.sample([0,2,4],1)[0]
                    row3[j] = 0
                else:
                    row2[j] = row3[j]
                    row3[j] = random.sample([0,2,4],1)[0]
            elif row2[j] == row3[j] and row3[j] != 0:
                row2[j] *= 2
                row3[j] = random.sample([0,0,2,4],1)[0]
            if row1[j] == 0:
                row1[j] = row2[j]
                row2[j] = random.sample([0,0,2,4],1)[0]
                row3[j] = 0
    elif pressed_key == 's':
        row3 = game_board[0] 
        row2 = game_board[1]
        row1 = game_board[2]
        for j in range(3):
            if row1[j] == row2[j]:
                row1[j] *= 2
                if row3[j] == 0:
                    row2[j] = random.sample([0,2,4],1)[0]
                    row3[j] = 0
                else:
                    row2[j] = row3[j]
                    row3[j] = random.sample([0,2,4],1)[0]
            elif row2[j] == row3[j] and row3[j] != 0:
                row2[j] *= 2
                row3[j] = random.sample([0,0,2,4],1)[0]
            if row1[j] == 0:
                row1[j] = row2[j]
                row2[j] = random.sample([0,0,2,4],1)[0]
                row3[j] = 0
    elif pressed_key == 'a':
        for i in game_board:
            row = i
            if row[1] == 0:
                row[1] = row[2]
                row[2] = 0
            while row[0] == 0:
                row[0] = row[1]
                if row[2] == 0:
                    row[1] = random.sample([0,2,4],1)[0]
                else:
                    row[1] = row[2]
                    row[2] = 0
            if row[0] == row[1]:
                row[0] *= 2
                if row[2] == 0:
                    row[1] = random.sample([0,2,4],1)[0]
                    row[2] = 0
                else:
                    row[1] = row[2]
                    row[2] = random.sample([0,2,4],1)[0]      
    elif pressed_key == 'd':
        for i in game_board:
            row = i
            if row[1] == 0:
                row[1] = row[0]
                row[0] = 0
            while row[2] == 0:
                row[2] = row[1]
                if row[0] == 0:
                    row[1] = random.sample([0,2,4],1)[0]
                else:
                    row[1] = row[0]
                    row[0] = 0
            if row[2] == row[1]:
                row[2] *= 2
                if row[0] == 0:
                    row[1] = random.sample([0,2,4],1)[0]
                    row[0] = 0
                else:
                    row[1] = row[0]
                    row[0] = random.sample([0,2,4],1)[0]            
    else:
        print("Enter a valid choice!")


board = gameboard()

while status(board):
    ...

