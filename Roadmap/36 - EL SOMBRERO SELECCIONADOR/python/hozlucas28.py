# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,redefined-outer-name

from typing import TypedDict, TypeVar, Literal, Any
from random import choice


# ---------------------------------------------------------------------------- #
#                                     TYPES                                    #
# ---------------------------------------------------------------------------- #

T = TypeVar("T", bound=str)


class Question[T](TypedDict):
    correct_answer: T
    options: list[T]
    points: float
    question: str


QuestionsPerHouse = TypedDict(
    "QuestionsPerHouse",
    {
        "backend": tuple[
            Question[Literal["Java", "JavaScript", "Python", "Ruby"]],
            Question[Literal["MySQL", "MongoDB", "PostgreSQL", "SQLite"]],
        ],
        "data": tuple[
            Question[
                Literal[
                    "Data analysis",
                    "Data visualization",
                    "Data mining",
                    "Data modeling",
                ]
            ],
            Question[Literal["Python", "R", "SQL", "Julia"]],
        ],
        "frontend": tuple[
            Question[Literal["HTML", "CSS", "JavaScript", "Python"]],
            Question[Literal["React", "Angular", "Vue", "Ember"]],
        ],
        "mobile": tuple[
            Question[Literal["iOS", "Android", "React Native", "Flutter"]],
            Question[Literal["Swift", "Kotlin", "Java", "Objective-C"]],
        ],
    },
)


# ---------------------------------------------------------------------------- #
#                                     UTILS                                    #
# ---------------------------------------------------------------------------- #


def list_to_long_disjunction(*, _list: list[T]) -> str:
    rtn: str = str(object=_list[0])

    for element in _list[1 : len(_list) - 1]:
        rtn += f", {element}"

    if len(_list) > 1:
        rtn += f", and {str(object=_list[-1])}"

    return rtn


def make_question(question: Question[T]) -> float:
    user_answer: str = (
        input(
            f"> {question.get('question')} "
            f"({list_to_long_disjunction(_list=question.get('options'))}): "
        )
        .strip()
        .upper()
    )

    uppercased_options: list[str] = [
        str(object=opt).upper() for opt in question.get("options")
    ]

    while user_answer not in uppercased_options:
        print("\n> Invalid option! Try again...")

        user_answer: str = (
            input(
                f"\n> {question.get('question')} "
                f"({list_to_long_disjunction(_list=question.get('options'))}): "
            )
            .strip()
            .upper()
        )

    return (
        question.get("points")
        if user_answer == str(object=question.get("correct_answer")).upper()
        else 0
    )


# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #

questions_per_house: QuestionsPerHouse = {
    "backend": (
        {
            "correct_answer": "JavaScript",
            "options": ["Java", "JavaScript", "Python", "Ruby"],
            "question": "What is the primary language used in backend development?",
            "points": 5,
        },
        {
            "correct_answer": "PostgreSQL",
            "options": ["MySQL", "MongoDB", "PostgreSQL", "SQLite"],
            "points": 5,
            "question": "Which database is commonly used for storing data in backend applications?",
        },
    ),
    "data": (
        {
            "correct_answer": "Data analysis",
            "options": [
                "Data analysis",
                "Data visualization",
                "Data mining",
                "Data modeling",
            ],
            "points": 5,
            "question": "What is the process of analyzing and interpreting data called?",
        },
        {
            "correct_answer": "Julia",
            "options": ["Python", "R", "SQL", "Julia"],
            "points": 5,
            "question": "Which programming language is commonly used for data analysis?",
        },
    ),
    "frontend": (
        {
            "correct_answer": "JavaScript",
            "options": ["HTML", "CSS", "JavaScript", "Python"],
            "points": 5,
            "question": "What is the primary language used in frontend development?",
        },
        {
            "correct_answer": "Angular",
            "options": ["React", "Angular", "Vue", "Ember"],
            "points": 5,
            "question": "Which framework is commonly used for building user interfaces?",
        },
    ),
    "mobile": (
        {
            "correct_answer": "Flutter",
            "options": ["iOS", "Android", "React Native", "Flutter"],
            "points": 5,
            "question": "Which platform is commonly used for developing mobile applications?",
        },
        {
            "correct_answer": "Objective-C",
            "options": ["Swift", "Kotlin", "Java", "Objective-C"],
            "points": 5,
            "question": "What is the primary language used in mobile app development?",
        },
    ),
}

user_name: str = input("> Enter your name: ").strip()

points: list[list[Any]] = [
    ["backend", 0],
    ["data", 0],
    ["frontend", 0],
    ["mobile", 0],
]

print()
points[0][1] += make_question(question=questions_per_house.get("backend")[0])

print()
points[0][1] += make_question(question=questions_per_house.get("backend")[1])

print()
points[1][1] += make_question(question=questions_per_house.get("data")[0])

print()
points[1][1] += make_question(question=questions_per_house.get("data")[1])

print()
points[2][1] += make_question(question=questions_per_house.get("frontend")[0])

print()
points[2][1] += make_question(question=questions_per_house.get("frontend")[1])

print()
points[3][1] += make_question(question=questions_per_house.get("mobile")[0])

print()
points[3][1] += make_question(question=questions_per_house.get("mobile")[1])

max_points: list[list[Any]] = []

for [house, housePoints] in points:
    if len(max_points) == 0:
        max_points.append([house, housePoints])
        continue

    if max_points[0][1] > housePoints:
        continue

    if max_points[0][1] == housePoints:
        max_points.append([house, housePoints])
    else:
        max_points[0] = [house, housePoints]


if len(max_points) == 1:
    print(f"\n> {user_name} will be part of the {max_points[0][0]} house!")
else:
    print(max_points)
    rnd_choice: list[Any] = choice(seq=max_points)

    print(
        f"\n> The decision has been complicated,"
        f" but {user_name} will be part of the {rnd_choice[0]} house!"
    )
