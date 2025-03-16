from flask import Blueprint, request, jsonify
from game_logic.game import Game

game_routes = Blueprint('game_routes', __name__)

# Global game instance
game = Game([
    ("Player 1", "Trickster"),
    ("Player 2", "Overlord"),
    ("Player 3", "Mentor"),
    ("Player 4", None),
    ("Human", None)
])

@game_routes.route('/state', methods=['GET'])
def get_game_state():
    """Returns the current state of the game."""
    return jsonify(game.get_state())  # Ensure this method returns the full state of the game

@game_routes.route('/start', methods=['POST'])
def start_game():
    """Starts the game and deals cards."""
    game.deal_cards()
    return jsonify({"message": "Game started, cards dealt!"})

@game_routes.route('/play', methods=['POST'])
def play_round():
    """Triggers the next round of the game."""
    game.play()
    return jsonify({"message": "Game round played", "winner": game.determine_winner().name})

@game_routes.route('/join', methods=['POST'])
def join_game():
    """Allows a new human player to join the game."""
    data = request.json
    new_player_name = data.get("name", "Guest")
    game.players.append(("New Player", None))
    return jsonify({"message": f"{new_player_name} joined the game!"})
