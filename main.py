from gamehub import user, game, community, RegisterUserFromSmartScan


def main():
    # User operations
    # print(user.register("john_doe", "securepassword123", "john@example.com"))
    # print()

    # print(user.login("john_doe", "securepassword123"))
    # print()

    # print(user.update_profile("john_doe", {"bio": "Gamer and developer"}))
    # print()

    # print(user.get_profile("john_doe"))
    # print()

    # print(user.delete("john_doe"))
    # print()

    # # Game operations
    # print(game.add("Epic Adventure", "RPG", "An epic role-playing game.", "2024-08-15"))
    # print()

    # print(game.update(1, {"description": "An updated description for the epic RPG."}))
    # print()

    # print(game.get_info(1))
    # print()

    # print(game.list_all())
    # print()

    # print(game.delete(1))
    # print()

    # # Community operations
    # print(
    #     community.create_thread(
    #         "Welcome to the Community", "This is the first thread.", "john_doe"
    #     )
    # )
    # print()

    # print(community.post_comment(1, "Great to be here!", "jane_doe"))
    # print()

    # print(
    #     community.schedule_event(
    #         "Game Night",
    #         "Join us for a night of gaming!",
    #         "2024-08-01 20:00",
    #         "john_doe",
    #     )
    # )
    # print()

    # print(community.join_event(1, "jane_doe"))
    # print()

    # print(
    #     community.send_message("john_doe", "jane_doe", "Hey, welcome to the community!")
    # )
    # print()

    # Smart scan registration
    RegisterUserFromSmartScan("Gokul,gokul@test.com")
    RegisterUserFromSmartScan("John,john@test.com")


if __name__ == "__main__":
    main()
