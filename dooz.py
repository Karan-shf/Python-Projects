import os

def ShowTable(table):
    for i in range(3):
        for j in range(3):
            print(table[i][j],end=' ')
        print()

def WinCheck(table,turn):
    if table[0][0]==turn and table[0][1]==turn and table[0][2]==turn:
        return True
    if table[1][0]==turn and table[1][1]==turn and table[1][2]==turn:
        return True
    if table[2][0]==turn and table[2][1]==turn and table[2][2]==turn:
        return True
    if table[0][0]==turn and table[1][0]==turn and table[2][0]==turn:
        return True
    if table[0][1]==turn and table[1][1]==turn and table[2][1]==turn:
        return True
    if table[0][2]==turn and table[1][2]==turn and table[2][2]==turn:
        return True
    if table[0][0]==turn and table[1][1]==turn and table[2][2]==turn:
        return True
    if table[2][0]==turn and table[1][1]==turn and table[0][2]==turn:
        return True
    return False

def DrawCheck(table):
    for i in range(3):
        for j in range(3):
            if table[i][j]=='*':
                return False
    return True

table = [
    ['*','*','*'],
    ['*','*','*'],
    ['*','*','*']
]

k=1
turn='randstr'

while True:

    os.system('clear')

    ShowTable(table)

    print()

    if WinCheck(table,turn):
        print(turn,'Wins!')
        break
    if DrawCheck(table):
        print('Draw!')
        break

    if k%2==0:
        turn = 'O'
    else:
        turn = 'X'

    print(turn,'turn')

    satr = int(input('enter satr: '))
    sotoon = int(input('enter sotoon: '))

    if satr>0 and satr<=3:
        
        if sotoon>0 and sotoon<=3:

            satr -= 1
            sotoon -= 1

            if table[satr][sotoon]=='*': 

                table[satr][sotoon] = turn

                k +=1