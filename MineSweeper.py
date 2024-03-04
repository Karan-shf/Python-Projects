import random
import os

def ShowTable(table):
    for i in table:
        for j in i:
            print(j,end=' ')
        print()

def RandBombGen(bombs):
    k=0
    while k<10:
        bombIndex=[]
        i = random.randint(0,9)
        j = random.randint(0,9)
        bombIndex.append(i)
        bombIndex.append(j)
        if bombIndex not in bombs:
            bombs.append(bombIndex)
            k+=1

def Is_Bomb(bombs,selected_house):
    for i in bombs:
        if selected_house==i:
            return True
    return False

def InsertBombs(table,bombs):
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
        if satr > 0 and sotoon < 9:
            if table[satr-1][sotoon+1] == '*':
                BombCount(bombs,[satr-1,sotoon+1],table)
        if sotoon > 0:
            if table[satr][sotoon-1] == '*':
                BombCount(bombs,[satr,sotoon-1],table)
        if sotoon < 9:
            if table[satr][sotoon+1] == '*':
                BombCount(bombs,[satr,sotoon+1],table)
        if satr < 9 and sotoon > 0:
            if table[satr+1][sotoon-1] == '*':
                BombCount(bombs,[satr+1,sotoon-1],table)
        if satr < 9:
            if table[satr+1][sotoon] == '*':
                BombCount(bombs,[satr+1,sotoon],table)
        if satr < 9 and sotoon < 9:
            if table[satr+1][sotoon+1] == '*':
                BombCount(bombs,[satr+1,sotoon+1],table)

def WinCheck(table):
    k=0
    for i in table:
        for j in i:
            if j=='*':
                k+=1
    if k==10:
        return True
    else:
        return False

table = [
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
    ['*','*','*','*','*','*','*','*','*','*'] ,
]

bombs = []

RandBombGen(bombs)

while True:

    os.system('clear')          

    ShowTable(table)

    satr = int(input('enter satr: '))
    sotoon = int(input('enter sotoon: '))

    if satr >0 and satr <=10:
        if sotoon >0 and sotoon <=10:

            satr -=1
            sotoon -=1

            selected_house=[satr,sotoon]

            if Is_Bomb(bombs,selected_house):
                os.system('clear')
                InsertBombs(table,bombs)
                ShowTable(table)
                print('You Lost! :(')
                break
            
            BombCount(bombs,selected_house,table)

            if WinCheck(table):
                os.system('clear')
                ShowTable(table)
                print('You Won! :)')
                break