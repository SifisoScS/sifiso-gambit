class Player:
    """Represents a player with a hand of cards."""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.base_score = 0
        self.suit_score = 0  # Used for tie-breaker

    def receive_hand(self, cards):
        """Assigns a hand of cards to the player."""
        self.hand = cards
        self.calculate_score()

    def calculate_score(self):
        """Calculates the player's score based on the 3 highest-value cards."""
        sorted_hand = sorted(self.hand, key=lambda card: card.value, reverse=True)
        self.base_score = sum(card.value for card in sorted_hand[:3])

    def calculate_suit_score(self):
        """Calculates suit-based tie-breaker score (sum of all suit values)."""
        self.suit_score = sum(card.suit for card in self.hand)

    def __repr__(self):
        return f"{self.name} (Score: {self.base_score}, Suit Score: {self.suit_score})"
