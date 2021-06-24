import random
from collections import Counter

username = ''
lifes = 0
ranks = ['K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'A']
suits = ['c', 'h', 's', 'd']
checkHand = []
deck = []
playerHand = []
aiHand = []
flop = []

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

def generateDeck():

    k = 0

    for i in suits:
        for j in ranks:
            card = Card(j, i)
            deck.append(card)
            k += 1
    
    for k in deck:
        print(k.suit + k.rank)

def clearDeck():
    deck.clear()
    playerHand.clear()
    aiHand.clear()
    flop.clear()

def drawCard():
    deckLen = len(deck)
    draw = deck[random.randint(0, deckLen-1)]
    deck.remove(draw)
    return draw

def dealCards():
    playerHand.append(drawCard())
    playerHand.append(drawCard())
    aiHand.append(drawCard())
    aiHand.append(drawCard())
    flop.append(drawCard())
    flop.append(drawCard())
    flop.append(drawCard())

def checkCards(checkArray):

    checkSuits = []
    checkRanks = []
    matchingSuits = 0
    pairs = 0
    threes = 0
    fourOfKind = False


    for i in checkArray:
        checkSuits.append(i.suit)
        checkRanks.append(i.rank)

    countSuits = Counter(checkSuits)
    countRanks = Counter(checkRanks)

    for c in list(countSuits.values()):
        if c > matchingSuits:
            matchingSuits = c
    
    for c in list(countRanks.values()):
        if c == 4:
             fourOfKind = True
        if c == 3:
            threes += 1
        if c == 2:
            pairs +=1

    if fourOfKind == True:
        return 6
    elif threes == 1 and pairs == 1:
        return 5
    elif matchingSuits == 5:
        return 4
    elif threes == 1 and pairs == 0:
        return 3
    elif pairs == 2:
        return 2
    elif pairs == 1 and threes == 0:
        return 1
    else:
        return 0


def checkScores():
    global lifes
    score = 0
    winningComb = ''
    pCheckArray = playerHand + flop
    aiCheckArray = aiHand + flop

    playerScore = checkCards(pCheckArray)
    aiScore = checkCards(aiCheckArray)

    if playerScore > aiScore:
        score = playerScore
    else:
        score = aiScore

    if score == 6:
        winningComb = 'four of a kind'
    elif score == 5:
        winningComb = 'full house'
    elif  score == 4:
        winningComb = 'flush'
    elif  score == 3:
        winningComb = 'three of kind'
    elif  score == 2:
        winningComb = 'two pair'
    elif  score == 1:
        winningComb = 'one pair'
    else:
        winningComb = 'high card'
        

    if playerScore > aiScore:
        print(username + ' won this time with a ' + winningComb)
    elif playerScore < aiScore:
        print('AI is clearly better with a ' + winningComb)
    elif playerScore == aiScore:
        print('A tie! Noice... You both had ' + winningComb)

def writeToFile():
    
    try:
        dataFile = open('pokerhandhistory.txt', 'x+')
    except FileExistsError:
        dataFile = open('pokerhandhistory.txt', 'a+')

    dataFile.write(username + ': ')
    for i in playerHand:
        cardName = i.rank + i.suit
        dataFile.write(cardName + ' ')
    
    dataFile.write('AI: ')
    for i in aiHand:
        cardName = i.rank + i.suit
        dataFile.write(cardName + ' ')
    
    dataFile.write('Flop: ')
    for i in flop:
        cardName = i.rank + i.suit
        dataFile.write(cardName + ' ')
    
    dataFile.write('\n')

if __name__ == "__main__":

    answer = 'a'
    lifes = 5

    username = input('What is your name, playa?\n')
    print('Welcome to the game of texas holdem!')
    
    while answer != 'q' or lifes == 0:
        while answer != 'start':
            answer = input('Type "start" to enter the game...\n')
        
        answer = ''

        clearDeck()
        generateDeck()
        dealCards()

        print('Player hand:')
        for i in playerHand:
            print(i.suit + i.rank)

        print('AI Hand:')
        for j in aiHand:
            print(j.suit + j.rank)

        print('Flop: ')
        for k in flop:
            print(k.suit + k.rank)

        writeToFile() 

        yesOrNo = input('Wanna fold? (You will lose a life)\n')
        if yesOrNo == 'yes' or yesOrNo == "Yes":
            if lifes > 0:
                lifes -= 1
                continue     
            else:
                print('Not enough lifes to do this again')

        checkScores()

        print('Number of lifes left: ', lifes)

    
    print('Thx for playing :DDDD')

