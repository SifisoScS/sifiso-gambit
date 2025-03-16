import random

class RuleEngine:
    """Manages AI-driven rule shifts during gameplay."""
    
    def __init__(self, game):
        self.game = game
        self.active_rules = []  # Track active rule changes

    def _activate_rule(self, rule_name, message):
        self.active_rules.append(rule_name)
        if message:
            print(message)
        """Selects and applies a random rule change."""
        rule = random.choice([
            self.double_face_card_values,
            self.force_card_discard,
            self.blind_mode,
            self.swap_penalty
        ])
        rule()  # Activate rule

    def double_face_card_values(self):
        """Doubles the value of all face cards (J, Q, K)."""
        for player in self.game.players:
            for card in player.hand:  # ✅ Fix: Ensure indentation
                if card.name[0] in "JQK":  # If it's a face card
                    card.value *= 2  # ✅ Double the card's value
        self.active_rules.append("Double Face Card Values")
        print("⚡ Rule Shift: All face cards now have **double value**!")

    def force_card_discard(self):
        """Forces all players to discard a random card."""
        for player in self.game.players:
            if player.hand:
                discarded = random.choice(player.hand)
                player.hand.remove(discarded)
                print(f"🗑️ {player.name} was **forced to discard** {discarded}!")
        self._activate_rule("Forced Card Discard", None)
        self.active_rules.append("Forced Card Discard")

    def blind_mode(self):
        """Activates blind mode where players cannot see their own hands."""
        self.game.blind_mode = True
        self._activate_rule("Blind Mode Activated", "🕶️ Rule Shift: Players **cannot see their own hands**!")
        self.active_rules.append("Blind Mode Activated")
        print("🕶️ Rule Shift: Players **cannot see their own hands**!")

    def swap_penalty(self):
        """Activates a penalty for swapping cards."""
        self.game.swap_penalty = True
        self._activate_rule("Swaps Now Cost 2 Points", "🔄 Rule Shift: **Swapping cards now costs 2 points!**")
        print("🔄 Rule Shift: **Swapping cards now costs 2 points!**")