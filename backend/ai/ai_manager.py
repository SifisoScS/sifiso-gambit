import random
from game_logic.players import Player

class AIPlayer(Player):
    """Base class for AI players with different personalities."""
    def __init__(self, name, personality):
        super().__init__(name)
        self.personality = personality  # Assign AI type (Trickster, Overlord, Mentor)

    def make_move(self, game):
        """Defines how the AI player acts based on personality."""
        if self.personality == "Trickster":
            from ai.trickster import TricksterAI
            TricksterAI().act(self, game)
        elif self.personality == "Overlord":
            from ai.overlord import OverlordAI
            OverlordAI().act(self, game)
        elif self.personality == "Mentor":
            from ai.mentor import MentorAI
            MentorAI().act(self, game)
