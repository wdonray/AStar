'''morning assignments'''
import random


# A Dealer deals 5 cards to each player at the beginning of a game.
# Cards can have a value of 5 or 10 if they are "Light" or "Dark".
# Write a function that determines which player has the highest total and
# return that player with the total

class Card(object):
    '''card'''

    def __init__(self, cardnum):
        '''init'''
        randomnum = random.randint(0, 1)
        self._value = 5 if (randomnum == 0) else 10
        self._type = "Light" if (self.value == 5) else "Dark"
        self._cardnum = cardnum

    @property
    def value(self):
        '''value'''
        return self._value

    @property
    def cardtype(self):
        '''card type'''
        return self._type

    @property
    def cardid(self):
        '''card id'''
        return self._cardnum


class Player(object):
    '''player'''

    def __init__(self, name):
        self._name = name
        self._hand = []

    def add_card(self, card):
        '''add a card'''
        self._hand.append(card)

    @property
    def total(self):
        '''total'''
        cardtotal = 0
        for i in self._hand:
            cardtotal += i.value
        return cardtotal

    @property
    def name(self):
        '''name'''
        return self._name


def get_highest(players):
    '''get the highest player'''
    players.sort(key=lambda x: x.total, reverse=True)
    return [players[0], players[0].total]


def main():
    '''main function'''
    cards = []
    # make the cards
    for i in range(25):
        cards.append(Card(i))
    # make the players
    playernames = ["matthew", "dylan", "chris", "jeremy", "max"]

    players = []

    for name in playernames:
        players.append(Player(name))

    counter = 0
    for card in cards:
        players[counter % len(players)].add_card(card)
        counter += 1

    winner = get_highest(players)
    print winner[0].name, winner[1]



if __name__ == "__main__":
    random.seed()
    main()
