import random

class MentorAI:
    """The Mentor AI gives strategic advice... sometimes misleading!"""
    def act(self, ai_player, game):
        advice_options = [
            "Keep high-value cards to maximize your score!",
            "Swapping suits can help in a tie-breaker situation.",
            "Your current hand is strong—consider keeping it.",
            "Swapping now might give you a better advantage.",
        ]
        advice = random.choice(advice_options)
        print(f"🧙‍♂️ {ai_player.name} (Mentor) says: '{advice}'")
