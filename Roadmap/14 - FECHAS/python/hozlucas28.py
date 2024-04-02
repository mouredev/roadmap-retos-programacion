import datetime

from typing import TypedDict

"""
    Dates...
"""

print("Dates...")

today: datetime.date = datetime.datetime.today()
born_date: datetime.date = datetime.datetime(year=2002, month=2, day=20)

print(f"\nToday is: {today}")
print(f"\nLucas Hoz born date: {born_date}")

years_between_dates: int = today.year - born_date.year
print(f"\nYears between today and born date: {years_between_dates} years")

print(
    "\n# ---------------------------------------------------------------------------------- #\n"
)

"""
    Additional challenge...
"""

print("Additional challenge...")

print(
    f"\nDay, month, and year: {born_date.day}, {born_date.month}, and {born_date.year}"
)

print(
    f"\nHours, minutes, and seconds: {born_date.hour} hours, "
    + f"{born_date.minute} minutes, and {born_date.second} seconds"
)

print(f"\nDay of the year: {born_date.timetuple().tm_yday}")

print(f"\nDay of the week: {born_date.weekday() + 1}")

print(f"\nMonth name: {born_date.strftime(format="%B")}")
