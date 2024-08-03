from dataclasses import dataclass, asdict
import re
from typing import Any
import cv2
from pyzbar import pyzbar


@dataclass
class User:
    name: str
    email: str


database: list[dict] = list()

create_user_record = lambda name, email: asdict(User(name, email))
insert_user_record = lambda record: database.append(record)
fetch_all_user_records = lambda: database if database else "No records found."


def extract_name_email(data: str) -> tuple[str, str] | tuple[str | Any, ...]:
    match = re.match(r"(\w+),(\w+@\w+\.\w+)", data)
    return match.groups() if match else ("", "")
