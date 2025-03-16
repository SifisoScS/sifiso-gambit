import random

# Define card suits and values
SUITS = {"Clubs": 1, "Diamonds": 2, "Hearts": 3, "Spades": 4}
VALUES = {str(i): i for i in range(2, 11)}
VALUES.update({"J": 11, "Q": 12, "K": 13, "A": 11})  # Face cards

class Card:
    """Represents a single playing card."""
    def __init__(self, value, suit):
        self.value = VALUES[value]  # Convert value to integer score
        self.suit = SUITS[suit]     # Convert suit to integer score
        self.name = f"{value} of {suit}"  # Display name

    def __repr__(self):
        return self.name

class Deck:
    """Represents a deck of 104 cards (2 x 52)."""
    def __init__(self):
        self.cards = self.create_deck()

    def create_deck(self):
        """Creates a shuffled double deck."""
        deck = [Card(value, suit) for _ in range(2) for suit in SUITS for value in VALUES]
        random.shuffle(deck)
        return deck

    def deal(self, num_cards=5):
        """Deals 'num_cards' cards from the deck."""
        return [self.cards.pop() for _ in range(num_cards)] if len(self.cards) >= num_cards else []

