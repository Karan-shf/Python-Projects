import random
import os

def ShowTable():
    for i in table:
        for j in i:
            print(j,end=' ')
        print()

def TableGen():
    li = []
    for i in range(TableSize):
        li.clear()
        for j in range(TableSize):
            li.append('*')
        table.append(li)

def RandBombGen():
    k=0
    while k<TableSize:
        bombIndex=[]
        i = random.randint(0,TableSize-1)
        j = random.randint(0,TableSize-1)
        bombIndex.append(i)
        bombIndex.append(j)
        if bombIndex not in bombs:
            bombs.append(bombIndex)
            k+=1

def Is_Bomb():
    for i in bombs:
        if selected_house==i:
            return True
    return False

def InsertBombs():
    for i in bombs:
        table[i[0]][i[1]]='B'

def BombCount(bombs,selected_house,table):
    
    k=0
    selected_house_copy = selected_house.copy()
    for i in bombs:

        selected_house = selected_house_copy.copy()
        selected_house[0] -= 1
        selected_house[1] -= 1
        if selected_house==i:
            k += 1
        
        selected_house = selected_house_copy.copy()
        selected_house[0] -=1
        if selected_house==i:
            k += 1

        selected_house = selected_house_copy.copy()
        selected_house[0] -= 1
        selected_house[1] += 1
        if selected_house==i:
            k += 1

        selected_house = selected_house_copy.copy()
        selected_house[1] -= 1
        if selected_house==i:
            k += 1
        
        selected_house = selected_house_copy.copy()
        selected_house[1] += 1
        if selected_house==i:
            k += 1
        
        selected_house = selected_house_copy.copy()
        selected_house[0] += 1
        selected_house[1] -= 1
        if selected_house==i:
            k += 1
        
        selected_house = selected_house_copy.copy()
        selected_house[0] += 1
        if selected_house==i:
            k += 1
        
        selected_house = selected_house_copy.copy()
        selected_house[0] += 1
        selected_house[1] += 1
        if selected_house==i:
            k += 1

    satr = selected_house_copy[0]
    sotoon = selected_house_copy[1]

    table[satr][sotoon] = k

    if k==0:

        if satr > 0 and sotoon > 0:
            if table[satr-1][sotoon-1] == '*':
                BombCount(bombs,[satr-1,sotoon-1],table)
        if satr > 0:
            if table[satr-1][sotoon] == '*':
                BombCount(bombs,[satr-1,sotoon],table)
        if satr > 0 and sotoon < TableSize - 1:
            if table[satr-1][sotoon+1] == '*':
                BombCount(bombs,[satr-1,sotoon+1],table)
        if sotoon > 0:
            if table[satr][sotoon-1] == '*':
                BombCount(bombs,[satr,sotoon-1],table)
        if sotoon < TableSize - 1:
            if table[satr][sotoon+1] == '*':
                BombCount(bombs,[satr,sotoon+1],table)
        if satr < TableSize - 1 and sotoon > 0:
            if table[satr+1][sotoon-1] == '*':
                BombCount(bombs,[satr+1,sotoon-1],table)
        if satr < TableSize - 1:
            if table[satr+1][sotoon] == '*':
                BombCount(bombs,[satr+1,sotoon],table)
        if satr < TableSize - 1 and sotoon < TableSize - 1:
            if table[satr+1][sotoon+1] == '*':
                BombCount(bombs,[satr+1,sotoon+1],table)

def WinCheck():
    k=0
    for i in table:
        for j in i:
            if j=='*':
                k+=1
    if k==TableSize:
        return True
    else:
        return False

print('[1]Easy \t [2]Medium \t [3]Hard \n')

check = True

while check:

    DifficultyLevel = int(input('enter deficulty level: '))

    if DifficultyLevel==1:
        TableSize = 10
        check = False
    elif DifficultyLevel==2:
        TableSize = 40
        check = False
    elif DifficultyLevel==3:
        TableSize = 80
        check = False
    else:
        print('invalid input!')


table = []

TableGen()

bombs = []

RandBombGen()

InsertBombs()

while True:

    os.system('clear')          

    ShowTable()

    satr = int(input('enter satr: '))
    sotoon = int(input('enter sotoon: '))

    if satr >0 and satr <=TableSize:
        if sotoon >0 and sotoon <=TableSize:

            satr -=1
            sotoon -=1

            selected_house=[satr,sotoon]

            if Is_Bomb():
                os.system('clear')
                InsertBombs()
                ShowTable()
                print('You Lost! :(')
                break
            
            BombCount(bombs,selected_house,table)

            if WinCheck():
                os.system('clear')
                ShowTable()
                print('You Won! :)')
                break