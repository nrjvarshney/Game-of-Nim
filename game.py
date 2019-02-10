
# coding: utf-8

# In[6]:


import numpy as np
import random
def distribute_coins(total_coins):
    b = random.randint(2, total_coins-2)
    a = random.randint(1, b - 1)
    c = random.randint(b + 1, total_coins-1)

    return np.array([a, b - a, c - b, total_coins - c]) 

def computeNim(piles):
    XOR = 0
    for pile in piles:
        XOR = XOR^pile
    return XOR

def move(number_of_piles, piles):
    nim = computeNim(piles)
    if(nim != 0):
        # you can win so try to make nimsum 0
        for i in range(number_of_piles):
            if(piles[i]^nim < piles[i]):
                piles[i] = piles[i]^ nim
                break
    else:
        # print("Nice Move! You have a chance to win. Let's see if you can")
        for i in range(number_of_piles):
            if(piles[i] > 0):
                piles[i] -= 1
                break
                
def gameEnded(number_of_piles, piles):
    for index in range(number_of_piles):
        if(piles[index]!=0):
            return False
    return True

def checkInputValidity(pileInput, coinInput, number_of_piles, piles):
    if(pileInput<0 or pileInput>=number_of_piles):
        return False
    if(coinInput < 1 or piles[pileInput] < coinInput):
        return False
    return True
        
def playBotFirst(number_of_piles, piles):
    while(gameEnded(number_of_piles, piles) == False):
        move(number_of_piles, piles)
        print("After Bot's move")
        print(piles)
        if(gameEnded(number_of_piles, piles) == True):
            print("Game Ended. Bon won!")
            break
        humanPileInput = input("Pile number 0 or 1 or 2 or 3: ")
        humanCoinInput = input("Coin input ")
        while(checkInputValidity(humanPileInput, humanCoinInput, number_of_piles, piles) !=True):
            print("Invalid input. Please enter again!")
            humanPileInput = input("Pile number 0 or 1 or 2 or 3: ")
            humanCoinInput = input("Coin input ")
        
        piles[humanPileInput] -= humanCoinInput
        print("After Human's move")
        print(piles)
        if(gameEnded(number_of_piles, piles) == True):
            print("Game Ended. Human won!")
            break
            
def playHumanFirst(number_of_piles, piles):
    while(gameEnded(number_of_piles, piles) == False):
        humanPileInput = input("Pile number 0 or 1 or 2 or 3: ")
        humanCoinInput = input("Coin input ")
        while(checkInputValidity(humanPileInput, humanCoinInput, number_of_piles, piles) !=True):
            print("Invalid input. Please enter again!")
            humanPileInput = input("Pile number 0 or 1 or 2 or 3: ")
            humanCoinInput = input("Coin input ")
        
        piles[humanPileInput] -= humanCoinInput
        print("After Human's move")
        print(piles)
        if(gameEnded(number_of_piles, piles) == True):
            print("Game Ended You Won!")
            break
        
        move(number_of_piles, piles)
        print("After Bot's move")
        print(piles)
        if(gameEnded(number_of_piles, piles) == True):
            print("Game Ended. Bot won!")
            break
        
def play(turn, number_of_coins):
    number_of_piles = 4 
    piles = distribute_coins(number_of_coins)
    nim = computeNim(piles)
    retry_count = 0
    if(turn == 2):
        # bot's turn first nim!= 0
        while(nim==0 and retry_count < 100):
            piles = distribute_coins(number_of_coins)
            nim = computeNim(piles)
            retry_count+= 1
        print("Initial piles")
        print(piles)
        playBotFirst(number_of_piles, piles)    
    else:
        # human's turn is first. nim==0
        while(nim!=0 and retry_count < 100):
            piles = distribute_coins(number_of_coins)
            nim = computeNim(piles)
            retry_count+= 1
        print("Initial piles")
        print(piles)
        playHumanFirst(number_of_piles, piles)
        
turn = 0
while(turn!=2 or turn!=1):
    number_of_coins = int(input("Enter total number of coins: "))
    turn = int(input("Select Player 1 or 2 : "))
    if(turn == 2 or turn == 1):
        play(turn, number_of_coins)
        break
    else:
        print("Wrong Input. Please try again")
        

