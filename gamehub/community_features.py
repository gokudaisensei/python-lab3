# community_features.py

threads = {}  # A dictionary to store forum threads
events = {}  # A dictionary to store community events
messages = []  # A list to store private messages


def create_forum_thread(title, content, username):
    """Create a new forum thread."""
    thread_id = len(threads) + 1
    threads[thread_id] = {
        "title": title,
        "content": content,
        "username": username,
        "comments": [],
    }
    return f"Forum thread '{title}' created successfully with ID {thread_id}."


def post_comment(thread_id, comment, username):
    """Post a comment on a forum thread."""
    if thread_id in threads:
        threads[thread_id]["comments"].append(
            {"username": username, "comment": comment}
        )
        return "Comment posted successfully."
    return "Thread not found."


def schedule_event(title, description, date_time, organizer):
    """Schedule a new community event."""
    event_id = len(events) + 1
    events[event_id] = {
        "title": title,
        "description": description,
        "date_time": date_time,
        "organizer": organizer,
        "participants": [],
    }
    return f"Event '{title}' scheduled successfully with ID {event_id}."


def join_event(event_id, username):
    """Join an existing community event."""
    if event_id in events:
        events[event_id]["participants"].append(username)
        return "Event joined successfully."
    return "Event not found."


def send_private_message(sender, receiver, message):
    """Send a private message from one user to another."""
    messages.append({"sender": sender, "receiver": receiver, "message": message})
    return "Message sent successfully."
