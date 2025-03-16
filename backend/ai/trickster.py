import random

class TricksterAI:
    """The Trickster loves chaos—swaps cards randomly!"""
    def act(self, ai_player, game):
        if len(game.players) < 2:
            return  # Can't swap if only one player

        # Pick a random opponent
        target = random.choice([p for p in game.players if p != ai_player])
        if not target.hand:
            return

        # Pick a random card from each and swap
        ai_card = random.choice(ai_player.hand)
        target_card = random.choice(target.hand)

        ai_player.hand.remove(ai_card)
        target.hand.remove(target_card)

        ai_player.hand.append(target_card)
        target.hand.append(ai_card)

        print(f"🎭 {ai_player.name} (Trickster) swapped {ai_card} with {target.name}'s {target_card}!")
