from gamehub.smartscan_registration_module import (
    extract_name_email,
    create_user_record,
    insert_user_record,
    fetch_all_user_records,
)


def RegisterUserFromSmartScan(data: str) -> None:
    name, email = extract_name_email(data)
    user_record = create_user_record(name, email)
    insert_user_record(user_record)
    print(fetch_all_user_records())
