import random
import os

def showOptions():

    check = True

    while check:

        os.system('clear')

        if GameCount != 0:
            print(f'last round\'s result: User: {User} - Computer: {Computer} - Winner: {game_result[GameCount-1]}\n')

        print('enter [1] for sang')
        print('enter [2] for kaghaz')
        print('enter [3] for gheychee')

        n = int(input('enter command: '))

        if n>0 and n<=3:
            check = False

    return n

def computerInput():

    n = random.randint(1,3)

    return n

def WinCheck(user,computer):

    # 0 = draw
    # 1 = user
    # 2 = computer

    if user==computer:
        return 0
    if user == 'sang' and computer=='kaghaz':
        return 2
    if user == 'sang' and computer=='gheychee':
        return 1
    if user == 'kaghaz' and computer=='sang':
        return 1
    if user == 'kaghaz' and computer=='gheychee':
        return 2
    if user == 'gheychee' and computer=='sang':
        return 2
    if user == 'gheychee' and computer=='kaghaz':
        return 1

def ShowResult():

    print()

    if UserWinCount==5:
        print('Winner is User\n')
    else:
        print('Winner is Computer\n')

    print('Total Game Count :',GameCount)
    print('User Win Count:',UserWinCount)
    print('Computer Win Count:',ComputerWinCount)
    print('Draw Count:',DrawCount,'\n')

    print('Game Results:')

    for i in range(len(game_result)):
        print(f'Round Num {i+1}. {game_result[i]}')

game = {
    1 : 'sang' ,
    2 : 'kaghaz' ,
    3 : 'gheychee'
}

game_result = []

GameCount = 0
UserWinCount = 0
ComputerWinCount = 0
DrawCount = 0

while UserWinCount<5 and ComputerWinCount<5:

    # if GameCount != 0:
    #     print(f'last round\'s result: \t User: {User} - Computer: {Computer} - Winner: {game_result[GameCount-1]}\n')

    userInput = showOptions()
    ComputerInput = computerInput()

    User = game[userInput]
    Computer = game[ComputerInput]

    result = WinCheck(User,Computer)

    if result==0:
        DrawCount += 1
        game_result.append('Draw')
    elif result==1:
        UserWinCount += 1
        game_result.append('User')
    else:
        ComputerWinCount +=1
        game_result.append('Computer')

    GameCount +=1

ShowResult()