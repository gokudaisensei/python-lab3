from .user_management import (
    register_user as user_register_user,
    login_user as user_login_user,
    update_profile as user_update_profile,
    delete_user as user_delete_user,
    get_user_profile as user_get_user_profile,
)

from .game_management import (
    add_game as game_add_game,
    update_game as game_update_game,
    delete_game as game_delete_game,
    get_game_info as game_get_game_info,
    list_all_games as game_list_all_games,
)

from .community_features import (
    create_forum_thread as community_create_forum_thread,
    post_comment as community_post_comment,
    schedule_event as community_schedule_event,
    join_event as community_join_event,
    send_private_message as community_send_private_message,
)

from .smart_scan_final_register import RegisterUserFromSmartScan


class user:
    register = user_register_user
    login = user_login_user
    update_profile = user_update_profile
    delete = user_delete_user
    get_profile = user_get_user_profile


class game:
    add = game_add_game
    update = game_update_game
    delete = game_delete_game
    get_info = game_get_game_info
    list_all = game_list_all_games


class community:
    create_thread = community_create_forum_thread
    post_comment = community_post_comment
    schedule_event = community_schedule_event
    join_event = community_join_event
    send_message = community_send_private_message


__all__ = ["user", "game", "community", "RegisterUserFromSmartScan"]
