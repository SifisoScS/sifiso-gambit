import sys
import os
import random

# Add the backend folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game_logic.cards import Deck
from game_logic.players import Player
from ai.ai_manager import AIPlayer
from game_logic.rule_engine import RuleEngine  # Updated import for Rule Engine
from game_logic.hand_evolution import HandEvolution  # Updated import for Hand Evolution

from game_logic.glitch_cards import create_random_glitch_card  # Updated import for Glitch Cards


class Game:
    """Manages the Sifiso Gambit game."""
    
    def __init__(self, player_data):
        self.deck = Deck()
        self.players = [
            AIPlayer(name, personality) if personality else Player(name)
            for name, personality in player_data
        ]
        self.rule_engine = RuleEngine(self)
        self.blind_mode = False
        self.swap_penalty = False
        
        self.deal_cards()  # ✅ Fix: Ensure cards are dealt when game starts

    def deal_cards(self):
        """Deals 5 cards to each player, with a chance to get a Glitch Card."""
        for player in self.players:
            player.receive_hand(self.deck.deal())

            # 10% chance for a glitch card to appear
            if random.random() < 0.1:
                glitch_card = create_random_glitch_card()
                glitch_card.activate(self, player)

    def apply_hand_evolution(self):
        """Triggers hand evolution system for all players."""
        for player in self.players:
            evolution = HandEvolution(player)
            evolution.evolve_hand()

    def apply_ai_moves(self):
        """Triggers AI decision-making.""" 
        for player in self.players:
            if isinstance(player, AIPlayer):
                player.make_move(self)

    def trigger_rule_shift(self):
        """Randomly activates a rule shift in mid-game.""" 
        if random.random() < 0.5:  # 50% chance of rule shift
            self.rule_engine.apply_random_rule()

    def determine_winner(self):
        """Determines the winner based on highest score, using tie-breaker rule.""" 
        self.players.sort(key=lambda p: p.base_score, reverse=True)
        highest_score = self.players[0].base_score
        top_players = [p for p in self.players if p.base_score == highest_score]

        if len(top_players) > 1:
            for player in top_players:
                player.calculate_suit_score()
            top_players.sort(key=lambda p: p.suit_score, reverse=True)

        return top_players[0]

    def play(self):
        """Runs a full round of the game.""" 
        self.deal_cards()
        self.apply_ai_moves()
        self.apply_hand_evolution()
        self.trigger_rule_shift()

        print("\n🎴 Players & Hands:")
        for player in self.players:
            hand_display = "Hidden" if self.blind_mode else player.hand
            print(f"{player.name} received: {hand_display}")

        winner = self.determine_winner()
        print(f"\n🏆 Winner: {winner.name} with Score: {winner.base_score}")
        
    def get_state(self):
        return {
            "players": [{"name": p.name, "hand": [str(card) for card in p.hand]} for p in self.players],

            "rules_active": self.rule_engine.active_rules,
        }
