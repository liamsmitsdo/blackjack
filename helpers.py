from random import shuffle

# Constants used to make cards
SUIT = ('hearts', 'spades', 'diamonds', 'clubs')
RANK = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
VALUE = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
         'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}

# Used to create individual card objects
class Card:
    # Each card has a suit and a rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Creates 52 card objects and stores them on self
class Deck:
    # Inits with empty deck, then creates cards in order with suit and rank
    # And appends to the list which forms the deck
    def __init__(self):
        self.all_cards = []
        for suit in SUIT:
            for rank in RANK:
                self.all_cards.append(Card(suit,rank))

    def __str__(self):
        string_comp = ''
        for card in self.all_cards:
            string_comp += '\n' + card.__str__()
        return string_comp

    # Method to randomly move the cards around within the list
    def shuffle(self):
        shuffle(self.all_cards)

    # Will give the first item in the list to simulate taking the top card
    def deal(self):
        return self.all_cards.pop()


# This represents each player as each player will have a hand
class Hand:
    # Inits with empty list to represent a hand
    # A value property is used to help with math calculations 
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    # Will take a card object and add to the hand list
    # And update the value of the hand for calculations
    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUE[card.rank]

        if card.rank == 'ace':
            self.aces += 1

    # Method to help with ace adjustments, will count aces as 11 until 
    # The value exceeds 21, then will adjust to 1 automatically
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Class to keep track of the players chips
class Chips:
    # Player starts with 100, can be adjusted
    def __init__(self):
        self.total = 100
        self.bet = 0

    # Will update the total chips if player wins
    def win_bet(self):
        self.total += (self.bet * 1.5)

    # Will update the total chips if player loses
    def lose_bet(self):
        self.total -= self.bet
