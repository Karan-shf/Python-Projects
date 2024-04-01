import msvcrt as gch
import os


def ShowMaze(maze):
    os.system('cls')
    for i in maze:
        for j in i:
            print(j, end=' ')
        print()


def directionIdentify(directionASC):
    if directionASC == 97 or directionASC == 65:
        return 'left'
    elif directionASC == 115 or directionASC == 83:
        return 'down'
    elif directionASC == 100 or directionASC == 68:
        return 'right'
    elif directionASC == 119 or directionASC == 87:
        return 'up'


def insertDirection(direction, cursor):
    l_border = 0
    h_border = len(maze)-1
    if direction == 'left':
        if cursor[1] != l_border:
            cursor[1] -= 1
    elif direction == 'right':
        if cursor[1] != h_border:
            cursor[1] += 1
    elif direction == 'up':
        if cursor[0] != l_border:
            cursor[0] -= 1
    elif direction == 'down':
        if cursor[0] != h_border:
            cursor[0] += 1

def insertCursor(cursor, maze):
    satrr = cursor[0]
    sotoonn = cursor[1]
    if maze[satrr][sotoonn] == '.':
        maze[satrr][sotoonn] = 'O'
        maze[last_loc[0]][last_loc[1]] = '.'

    else:
        cursor = last_loc


def continueCheck():
    if maze[cursor[0]][cursor[1]] == 'E':
        return False
    else:
        return True


maze = [
    ['S', '.', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*'],
    ['*', '.', '*', '*', '*', '.', '*', '*', '*', '*', '*', '*', '.', '*', '*', '*', '*', '.', '.', '*'],
    ['*', '.', '*', '*', '*', '.', '.', '.', '.', '.', '.', '*', '.', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '.', '*', '*', '*', '*', '*', '*', '*', '*', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
    ['*', '.', '.', '.', '*', '*', '*', '*', '.', '*', '.', '*', '*', '*', '*', '*', '*', '*', '.', '*'],
    ['*', '*', '*', '.', '.', '.', '.', '.', '.', '*', '.', '.', '*', '*', '*', '*', '*', '*', '.', '.'],
    ['*', '*', '*', '.', '*', '*', '*', '*', '*', '*', '*', '.', '*', '*', '*', '*', '*', '*', '*', '.'],
    ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '.', '*', '*', '.', '.', '.', '.', '*', '.'],
    ['.', '*', '*', '.', '.', '.', '.', '*', '*', '*', '*', '.', '*', '*', '.', '*', '*', '.', '*', '*'],
    ['.', '*', '*', '.', '*', '*', '.', '.', '*', '*', '*', '.', '*', '.', '.', '*', '*', '.', '*', '*'],
    ['.', '*', '*', '.', '*', '*', '*', '.', '*', '*', '*', '.', '*', '*', '.', '*', '*', '.', '.', '.'],
    ['.', '*', '*', '.', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '.', '*', '.'],
    ['.', '*', '*', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '*', '.'],
    ['.', '*', '*', '.', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '*', '*', '.', '*', '.'],
    ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '.', '*', '*', '.', '*', '.'],
    ['*', '.', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '.', '*', '*', '.', '*', '.'],
    ['*', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.'],
    ['*', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '*', '*', '*', '*', '*', '.', '.', '.'],
    ['*', '*', '*', '*', '*', '*', '.', '*', '*', '*', '*', '.', '*', '*', '*', '*', '*', '.', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '.', '.', '.', '.', '.', '.', '*', '*', '*', '*', '*', '.', '.', 'E']
]

satr = 0
sotoon = 0

cursor = [satr, sotoon]

check = True

while check:
    ShowMaze(maze)

    directionInput = gch.getch()

    direction = directionIdentify(ord(directionInput))

    last_loc = cursor.copy()

    insertDirection(direction, cursor)

    check = continueCheck()

    insertCursor(cursor, maze)


ShowMaze(maze)

print('you won!')
