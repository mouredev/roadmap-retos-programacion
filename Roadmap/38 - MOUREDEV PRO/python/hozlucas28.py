# pylint: disable=missing-module-docstring,missing-function-docstring,expression-not-assigned,redefined-outer-name

from typing import TypedDict, Literal
import csv
import os
import random


# ---------------------------------------------------------------------------- #
#                                   FUNCTIONS                                  #
# ---------------------------------------------------------------------------- #


def create_csv(*, content: list[list[str]], path: str) -> None:
    if os.path.exists(path=path):
        os.remove(path=path)

    with open(file=path, mode="x", encoding="utf8") as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")

        for row in content:
            writer.writerow(row)


def get_csv_content(*, path: str) -> list[dict[str, str]]:
    csv_content: list[list[str]] = []

    with open(file=path, mode="r", encoding="utf8") as file:
        reader = csv.reader(file, delimiter=",")

        for row in reader:
            csv_content.append(row)

    csv_content_fmt: list[dict[str, str]] = []

    for row in csv_content[1:]:
        row_fmt: dict[str, str] = {}

        for i, col in enumerate(iterable=row):
            row_fmt[csv_content[0][i]] = col

        csv_content_fmt.append(row_fmt)

    return csv_content_fmt


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


type Status = Literal["active"] | Literal["inactive"]

User = TypedDict(
    "User",
    {
        "id": int,
        "email": str,
        "status": Status,
    },
)

users: list[User] = [
    {
        "email": "test01@gmail.com",
        "id": 1,
        "status": "active",
    },
    {
        "email": "test02@gmail.com",
        "id": 2,
        "status": "inactive",
    },
    {
        "email": "test03@gmail.com",
        "id": 3,
        "status": "inactive",
    },
    {
        "email": "test04@gmail.com",
        "id": 4,
        "status": "active",
    },
    {
        "email": "test05@gmail.com",
        "id": 5,
        "status": "inactive",
    },
    {
        "email": "test06@gmail.com",
        "id": 6,
        "status": "active",
    },
    {
        "email": "test07@gmail.com",
        "id": 7,
        "status": "active",
    },
    {
        "email": "test08@gmail.com",
        "id": 8,
        "status": "active",
    },
]

csvContent: list[list[str]] = [
    list(users[0].keys()),
]

for user in users:
    csvContent.append([str(object=user.get(key)) for key in list(users[0].keys())])

create_csv(content=csvContent, path="./users.csv")

csvUsers: list[dict[str, str]] = get_csv_content(path="./users.csv")

activeUsers: list[dict[str, str]] = list(
    filter(lambda user: user["status"] == "active", csvUsers)
)

winners: list[dict[str, str]] = random.sample(population=activeUsers, k=3)

print("> The first winner is...")
print(
    f"> Congratulations {winners[0]['email']} with id {winners[0]['id']}, you won a subscription!"
)

print("\n> The second winner is...")
print(
    f"> Congratulations {winners[1]['email']} with id {winners[1]['id']}, you won a discount!"
)

print("\n> The third winner is...")
print(
    f"> Congratulations {winners[2]['email']} with id {winners[2]['id']}, you won a book!"
)
