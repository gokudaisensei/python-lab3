# user_management.py

users = {}  # A dictionary to store user information


def register_user(username, password, email):
    """Register a new user with a username, password, and email."""
    if username in users:
        return "Username already exists."
    users[username] = {"password": password, "email": email, "profile": {}}
    return "User registered successfully."


def login_user(username, password):
    """Login a user with a username and password."""
    if username in users and users[username]["password"] == password:
        return "Login successful."
    return "Invalid username or password."


def update_profile(username, profile_data):
    """Update the profile information for a user."""
    if username in users:
        users[username]["profile"].update(profile_data)
        return "Profile updated successfully."
    return "User not found."


def delete_user(username):
    """Delete a user account by username."""
    if username in users:
        del users[username]
        return "User deleted successfully."
    return "User not found."


def get_user_profile(username):
    """Retrieve the profile information of a user."""
    if username in users:
        return users[username]["profile"]
    return "User not found."
