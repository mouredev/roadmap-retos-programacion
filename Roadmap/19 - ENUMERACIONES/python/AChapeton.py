from enum import Enum

class WeekDays(Enum):
  Monday = 1
  Tuesday = 2
  Wednesday = 3
  Thursday = 4
  Friday = 5
  Saturday = 6
  Sunday = 7

def getDayOfWeek(number):
  for day in WeekDays:
    if day.value == number:
      return day.name
  return "Invalid number"

print(getDayOfWeek(3))