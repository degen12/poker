import random
from collections import deque

##cards = { 'hearts':'ace one two three four five six seven eight nine jack queen king'.split(),
##          'spades':'ace one two three four five six seven eight nine jack queen king'.split(),
##          'clubs':'ace one two three four five six seven eight nine jack queen king'.split(),
##          'diamonds':'ace one two three four five six seven eight nine jack queen king'.split() }
##
##
##
##def getRandomCard(cardDict):
##    cardSuit = random.choice(list(cardDict.keys()))
##    cardNum = random.randint(0, len(cardDict[cardSuit]) - 1)
##          
##    return [cardDict[cardSuit][cardNum], cardSuit]
##
##def formHand():
##    hand = []    
##    while len(hand) < 5:
##        num, suit = getRandomCard(cards)
##        card = num + ' of ' + suit
##        if card in hand:
##            pass
##        else:
##            hand.append(card)
##    return(hand)
##
##player1 = formHand()
##print(player1)

cards = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
         '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
         '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
         '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH' ]

def dealCards(pack):

    random.shuffle(pack)
    hand1 = []
    hand2 = []

    shuffledCards = deque(cards)
    for card in range(0, 5):
        hand1.append(shuffledCards.popleft())
        hand2.append(shuffledCards.popleft())

    return hand1, hand2

print(dealCards(cards))
