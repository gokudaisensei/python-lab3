# game_management.py

games = {}  # A dictionary to store game information


def add_game(title, genre, description, release_date):
    """Add a new game to the platform."""
    game_id = len(games) + 1
    games[game_id] = {
        "title": title,
        "genre": genre,
        "description": description,
        "release_date": release_date,
    }
    return f"Game '{title}' added successfully with ID {game_id}."


def update_game(game_id, updated_info):
    """Update the information of an existing game."""
    if game_id in games:
        games[game_id].update(updated_info)
        return f"Game ID {game_id} updated successfully."
    return "Game not found."


def delete_game(game_id):
    """Delete a game from the platform."""
    if game_id in games:
        del games[game_id]
        return f"Game ID {game_id} deleted successfully."
    return "Game not found."


def get_game_info(game_id):
    """Retrieve information about a specific game."""
    if game_id in games:
        return games[game_id]
    return "Game not found."


def list_all_games():
    """List all games available on the platform."""
    return list(games.values())
