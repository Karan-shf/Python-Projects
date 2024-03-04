import os
import time
# import sys

# sys.setrecursionlimit(9999)

def ShowMaze(maze):
    time.sleep(0.1)
    os.system('clear')
    for i in maze:
        for j in i:
            print(j,end=' ')
        print()

def MazeSolver(maze,cursor,last_loc=None):
    
    satr = cursor[0]
    sotoon = cursor[1]

    if sotoon > 0:
        if [satr,sotoon-1] != last_loc:
            if maze[satr][sotoon-1] == '.' or maze[satr][sotoon-1] == 'E':
                # sotoon -= 1
                maze[satr][sotoon] = '0'
                if last_loc != None: 
                    maze[last_loc[0]][last_loc[1]] = '.'
                ShowMaze(maze)
                MazeSolver(maze,[satr,sotoon-1],[satr,sotoon])
    if satr > 0:
        if [satr-1,sotoon] != last_loc:
            if maze[satr-1][sotoon] == '.' or maze[satr-1][sotoon] == 'E':
                # satr -= 1
                maze[satr][sotoon] = '0'
                if last_loc != None: 
                    maze[last_loc[0]][last_loc[1]] = '.'
        
                ShowMaze(maze)
                MazeSolver(maze,[satr-1,sotoon],[satr,sotoon])
    if sotoon < maze_size-1:
        if [satr,sotoon+1] != last_loc:
            if maze[satr][sotoon+1] == '.' or maze[satr][sotoon+1] == 'E':
                # sotoon += 1
                maze[satr][sotoon] = '0'
                if last_loc != None:
                    maze[last_loc[0]][last_loc[1]] = '.'
         
                ShowMaze(maze)
                MazeSolver(maze,[satr,sotoon+1],[satr,sotoon])
    if satr < maze_size-1:
        if [satr+1,sotoon] != last_loc:
            if maze[satr+1][sotoon] == '.' or maze[satr+1][sotoon] == 'E':
                # satr += 1
                maze[satr][sotoon] = '0'
                if last_loc != None:
                    maze[last_loc[0]][last_loc[1]] = '.'
       
                ShowMaze(maze)
                MazeSolver(maze,[satr+1,sotoon],[satr,sotoon])

    flag = True

    if maze[satr][sotoon] == 'E':
        flag = False
        maze[satr][sotoon]='O'
        ShowMaze(maze)
    if sotoon > 0:
        flag = False
        if maze[satr][sotoon-1] == 'O':
            maze[satr][sotoon]='O'
            ShowMaze(maze)
    if satr > 0:
        flag = False
        if maze[satr-1][sotoon] == 'O':
            maze[satr][sotoon]='O'
            ShowMaze(maze)
    if sotoon < maze_size-1:
        flag = False
        if maze[satr][sotoon+1] == 'O':
            maze[satr][sotoon]='O'
            ShowMaze(maze)
    if satr < maze_size-1:
        flag = False
        if maze[satr+1][sotoon] == 'O':
            maze[satr][sotoon]='O'
            ShowMaze(maze)

    #vol 2
    if flag:
        maze[satr][sotoon] = '.'
        if last_loc != None:
            maze[last_loc[0]][last_loc[1]] = '0'
        ShowMaze(maze)
    

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

maze_size = len(maze) # = 20

cursor = [0,0]

# ShowMaze(maze)
# print('-----------------------------------------------------------')
MazeSolver(maze,cursor)
ShowMaze(maze)