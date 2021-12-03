import random

Jack = 11
Queen = 12
King = 13
Ace = 11
card = [Ace,2,3,4,5,6,7,8,9,10,Jack,Queen,King] * 4
playerCards = []
dealerCards = []
sumDealer = 0
sumPlayer = 0
hitCountPlayer = 1
hitCountDealer = 1

def blackJack():
    global hitCountPlayer
    global hitCountDealer

    firstTurn()
    playerCalculation()
    dealerCalculation()
    print('Player : ' + str(sumPlayer))
    print('Dealer : ' + str(dealerCards[0]))

    while True:
        if sumPlayer > 21:
            print('Player Busted | Player Cards : ' + str(playerCards) + ' | ' + str(sumPlayer))
            return
        wantHit = input('Do you want to hit ? y/n\n')
        if wantHit.lower() == 'y':
            hitCountPlayer += 1
            playerHit()
            playerCalculateHit(hitCountPlayer)
            print('Player Cards : ' + str(playerCards))
            print('Player = ' + str(sumPlayer))
        else:
            break
    
    while True:
        if sumDealer < 17:
            dealerHit()
            hitCountDealer += 1
            dealerCalculateHit(hitCountDealer)
        elif sumDealer > 21:
            print('Dealer = ' + str(sumDealer) + ' ' + str(dealerCards) + '\n' + 'Player = ' + str(sumPlayer) + ' ' + str(playerCards))
            print('Dealer Busted, Player Wins')
            return
        else:
            break

    if sumDealer > sumPlayer:
        print('Dealer Wins')
        print('Dealer = ' + str(sumDealer) + ' ' + str(dealerCards) + '\n' + 'Player = ' + str(sumPlayer) + ' ' + str(playerCards))
    elif sumDealer == sumPlayer:
        print('Its a tie')
        print('Dealer = ' + str(sumDealer) + ' ' + str(dealerCards) + '\n' + 'Player = ' + str(sumPlayer) + ' ' + str(playerCards))
    else:
        print('Player Wins')
        print('Dealer = ' + str(sumDealer) + ' ' + str(dealerCards) + '\n' + 'Player = ' + str(sumPlayer) + ' ' + str(playerCards))



def dealer():
    dealerCards.append(random.choice(card))
    dealerCards.append(random.choice(card))
    print('Dealer Cards : ' + str(dealerCards[0]))

def player():
    playerCards.append(random.choice(card))
    playerCards.append(random.choice(card))
    print('Player Cards : ' + str(playerCards))
    
def firstTurn():
    dealer()
    player()

def playerHit():
    playerCards.append(random.choice(card))
    
def dealerHit():
    dealerCards.append(random.choice(card))

def playerCalculation():
    global sumPlayer
    for x in playerCards:
        if x == Ace:
            if sumPlayer > 11:
                Ace == 1
                sumPlayer += x
            else:
                sumPlayer += x
        else:
            sumPlayer += x

def playerCalculateHit(counters):
    global sumPlayer
    for x in playerCards[counters::]:
        if x == Ace:
            if sumPlayer > 11:
                Ace == 1
                sumPlayer += x
            else:
                sumPlayer += x
        else:
            sumPlayer += x

def dealerCalculation():
    global sumDealer
    for x in dealerCards:
        if x == Ace:
            if sumDealer > 11:
                Ace == 1
                sumDealer += x
            else:
                sumDealer += x
        else:
            sumDealer += x

def dealerCalculateHit(counters):
    global sumDealer
    for x in dealerCards[counters::]:
        if x == Ace:
            if sumDealer > 11:
                Ace == 1
                sumDealer += x
            else:
                sumDealer += x
        else:
            sumDealer += x

blackJack()