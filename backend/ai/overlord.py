import random

class OverlordAI:
    """The Overlord AI changes game rules dynamically."""
    def act(self, ai_player, game):
        rule_change = random.choice(["double_score", "hide_cards"])
        
        if rule_change == "double_score":
            ai_player.base_score *= 2
            print(f"👑 {ai_player.name} (Overlord) activated 'Double Score'—new score: {ai_player.base_score}!")

        elif rule_change == "hide_cards":
            game.hidden_cards = True  # Hides all player hands
            print(f"👑 {ai_player.name} (Overlord) activated 'Hide Cards'—players cannot see hands!")
