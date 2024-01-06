import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.card_deck = []
        for suit in suits:
            for rank in ranks:
                self.card_deck.append(Card(suit, rank))

    def __str__(self):
        for i in self.card_deck:
            print(i)

    def __len__(self):
        return int(len(self.card_deck))

    def shuffle(self):
        random.shuffle(self.card_deck)

    def deal(self):
        return self.card_deck.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.cards.extend(new_cards)
        else:
            self.cards.append(new_cards)

    def remove_one(self):
        return self.cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.cards)} cards.'




suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,'Queen':12, 'King':13, 'Ace':14}


player_one = Player("Fahd")
player_two = Player("Maya")

deck = Deck()
deck.shuffle()
for i in range(len(deck)//2):
    player_one.add_cards(deck.deal())
    player_two.add_cards(deck.deal())

playing = True
round_num = 0
while playing:
    if len(player_one.cards) == 0:
        print(f"Player {player_one.name} out of cards! Game Over")
        print(f"Player {player_two.name} Wins!")
        print(f'{len(player_one.cards)} and {len(player_two.cards)}')
        playing = False
        break
    if len(player_two.cards) == 0:
        print(f"Player {player_two.name} out of cards! Game Over")
        print(f"Player {player_one.name} Wins!")
        print(f'{len(player_one.cards)} and {len(player_two.cards)}')
        playing = False
        break
    round_num = round_num+1
    print(f'Round {round_num}')
    round_not_over = True
    card_list = []
    while round_not_over:
        p1_card = player_one.remove_one()
        p2_card = player_two.remove_one()
        card_list.append(p1_card)
        card_list.append(p2_card)
        if p1_card.value == p2_card.value:
            print("War!")
            if len(player_one.cards)>3 and len(player_two.cards)>3:
                for i in range(3):
                    card_list.append(player_one.remove_one())
                    card_list.append(player_two.remove_one())
            elif len(player_one.cards)<=3:
                for card in player_one.cards:
                    player_two.add_cards(card)
                player_two.add_cards(card_list)
                break
            else:
                for card in player_two.cards:
                    player_one.add_cards(card)
                player_one.add_cards(card_list)
                break
        elif p1_card.value > p2_card.value:
            player_one.add_cards(card_list)
            round_not_over = False
        else:
            player_two.add_cards(card_list)
            round_not_over = False
