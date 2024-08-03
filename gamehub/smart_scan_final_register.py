from gamehub.smartscan_registration_module import (
    extract_name_email,
    create_user_record,
    insert_user_record,
    fetch_all_user_records,
)

import cv2
from pyzbar.pyzbar import decode

import qrcode


def generateSmartScanQRCode(name: str, email: str) -> str:
    img = qrcode.make(f"{name},{email}")
    img.save(f"gamehub/smartscan_codes/{name}.png")
    return f"gamehub/smartscan_codes/{name}.png"


def RegisterUserFromSmartScan(image_path: str) -> None:
    image = cv2.imread(image_path)

    decoded_objects = decode(image)
    if not decoded_objects:
        raise ValueError("No QR code found in the image")

    data = decoded_objects[0].data.decode("utf-8")

    name, email = extract_name_email(data)

    user_record = create_user_record(name, email)
    insert_user_record(user_record)

    print(fetch_all_user_records())
