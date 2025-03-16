import random

class GlitchCard:
    """Defines a glitch card with a random powerful effect."""
    
    def __init__(self, effect_name, effect_function):
        self.effect_name = effect_name
        self.effect_function = effect_function

    def activate(self, game, player):
        """Triggers the effect when a player gets a glitch card."""
        print(f"⚡ GLITCH CARD ACTIVATED: {self.effect_name}!")
        self.effect_function(game, player)

def quantum_swap(game, player):
    """Forces all players to swap a random card."""
    print("🎭 Quantum Swap! Every player must swap a random card!")

    # Ensure players have at least one card before swapping
    valid_players = [p for p in game.players if len(p.hand) > 0]

    if len(valid_players) < 2:
        print("🚨 Quantum Swap failed: Not enough players with cards!")
        return  # Exit if no valid swap is possible

    for p in valid_players:
        target = random.choice([x for x in valid_players if x != p and len(x.hand) > 0])
        if target and len(p.hand) > 0 and len(target.hand) > 0:
            p_card = random.choice(p.hand)
            t_card = random.choice(target.hand)

            # Swap cards
            p.hand.remove(p_card)
            target.hand.remove(t_card)
            p.hand.append(t_card)
            target.hand.append(p_card)

            print(f"{p.name} swapped {p_card} with {target.name}'s {t_card}!")


def blackout(game, player):
    """Hides all hands for the next round."""
    game.blind_mode = True
    print("🕳️ BLACKOUT! All hands are now hidden!")

def time_rewind(game, player):
    """Allows the player to undo their last move."""
    print(f"⏳ Time Rewind! {player.name} can redo their last move!")

def wild_mutation(game, player):
    """Mutates every player's hand unpredictably."""
    from game_logic.hand_evolution import HandEvolution

    print("🎲 Wild Mutation! Every player's hand is mutating!")
    for p in game.players:
        HandEvolution(p).evolve_hand()

GLITCH_CARD_EFFECTS = [
    ("Quantum Swap", quantum_swap),
    ("Blackout", blackout),
    ("Time Rewind", time_rewind),
    ("Wild Mutation", wild_mutation),
]

def create_random_glitch_card():
    """Creates a new glitch card with a random effect."""
    effect_name, effect_function = random.choice(GLITCH_CARD_EFFECTS)
    return GlitchCard(effect_name, effect_function)
