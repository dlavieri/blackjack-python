import random

################### GLOBAL VARIABLES ######################  

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
cards = [('One', 1), ('Two',2), ('Three',3), ('Four',4), ('Five',5), ('Six',6), ('Seven',7), 
            ('Eight',8), ('Nine',9), ('Ten',10), ('Jack',10), ('Queen', 10), ('King',10), ('Ace',11)]
playing = True
    
    
################### CLASSES ######################  

class Card:
    
    def __init__(self, name, suit, val):
        self.name = name
        self.suit = suit
        self.val = val
        
    def __str__(self):
        return f'{self.name} of {self.suit}'

class Deck:
    
    def __init__(self):
        self.cards = []
        # Iterate through all the suits, and all the possible cards in each rank 
        for suit in suits:
            for card,val in cards:
                curr = Card(card, suit, val)
                self.cards.append(curr)
                
    def __str__(self):
        s = 'This deck contains:\n'
        for card in self.cards:
            s += card.__str__() + "\n"
        return s
    
    def shuffle(self):
        ''' shuffle cards in place, return void '''
        random.shuffle(self.cards)
        
    def deal_card(self):
        ''' take top card off the deck stack, return card obj '''
        return self.cards.pop()
                     

class Hand:
    def __init__(self):
        self.cards = []
        self.total = 0
    
    def add_card(self, card):
        ''' append the new card, update hand total, return void '''
        self.cards.append(card)
        self.total += card.val
    
    def adjust_for_ace(self):
        ''' check if hand contains an Ace, and if total has busted, adjust ace 11 -> 1, return void '''
        for card in self.cards:
            if card.name == "Ace" && self.total > 21:
                card.val = 1

class Chips:
    def __init__(self):
        self.bank = 100
        self.bet = 0
        
    def win_bet(self):
        ''' add bet amount to bank account, print new bank amount, return void '''
        self.bank += self.bet*2
        
    def lose_bet(self):
        ''' subtract bet amount from bank account, print new bank amount, return void '''
        self.bank -= self.bet
    
    def push(self):
        ''' return bet back to bank '''
        self.bank += self.bet

def make_bet(chips):
    while True:
        try:
            bet = int(input('How much would you like to bet?'))
            if bet > chips.bank:
                print(f'That amount exceeds your bank! Please choose a number below {chips.bank}')
            else:
                break
        except TypeError:
            print('Please enter a number')
    chips.bet = bet
    print('You bet {bet}')
    

################### FUNCTIONS ######################    

def hit(deck,hand):
    ''' take a card from top of the deck and add to player hand, return void '''
    # deal a new card, remove from top of deck
    new_card = deck.deal_card()
    # add it to hand 
    hand.add_card()
    
def prompt(deck,hand):
    ''' ask a player if they will hit or stand '''
    global playing #to switch control if player stands
    
    move = input("hit or stand? ")
    if (move != 'hit' and move != 'stand'):
        # if player enters invalid command
        move = input('please choose "hit" or "stand" ')
    elif move == 'hit':
        # call hit function
        hit(deck,hand)
    else:
        # change control if stand
        playing = False

################### END HAND FUNCTIONS ######################  
        
def player_busts(player_chips, dealer_chips):
    player_chips.lose_bet()
    dealer_chips.win_bet()

def player_wins(player_chips, dealer_chips):
    player_chips.win_bet()
    dealer_chips.lose_bet()

def push(player_chips, dealer_chips):
    player_chips.push()
    dealer_chips.push()

    
    
################### PLAY GAME ######################     

while True:
    
    ### PLAYERS ROUND
    
    ### DEALERS ROUND
    
    break
    