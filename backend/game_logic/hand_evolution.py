import random
from game_logic.cards import Card


class HandEvolution:
    """Manages the dynamic evolution of player hands."""

    def __init__(self, player):
        self.player = player

    def evolve_hand(self):
        """Applies evolution rules to modify a player's hand dynamically."""
        for card in self.player.hand:
            if self.should_mutate():
                self.mutate_card(card)

    def should_mutate(self):
        """Determines if a card should evolve (based on game conditions)."""
        return random.random() < 0.3  # 30% chance of mutation

    def mutate_card(self, card):
        """Modifies a card by upgrading or downgrading its value."""
        change = random.choice([-2, -1, 1, 2])  # Value shift
        new_value = max(2, min(13, card.value + change))  # Keep within 2-13
        card.value = new_value

        print(f"🔀 Card Evolution! {self.player.name}'s {card.name} mutated to {new_value} value.")
