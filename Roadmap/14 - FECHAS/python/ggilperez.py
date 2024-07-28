# 14 Datetime
from datetime import datetime

utc_now = datetime.utcnow()
birth_datetime = datetime.strptime("14/06/1993 12:13:14", "%d/%m/%Y %H:%M:%S")

print(f"{utc_now = }")
print(f"{birth_datetime = }")
print(f"Time elapse between dates: {(utc_now - birth_datetime).days / 365 :.0f} years")
print()

# Extra
print("Extra")

# List of format types in: https://docs.python.org/3/library/datetime.html
print(f"1.  {birth_datetime.strftime('%d-%m-%y')}")  # ESP
print(f"2.  {birth_datetime.strftime('%m-%d-%y')}")  # US
print(f"3.  {birth_datetime.strftime('%d-%m-%y %H:%M:%S')}")  # With time
print(f"4.  {birth_datetime.strftime('%d-%B-%y')}")  # ESP
print(f"5.  {birth_datetime.strftime('%B-%d-%y')}")  # US
print(f"6.  {birth_datetime.strftime('%d-%m-%Y')}")  # With full year
print(f"7.  {birth_datetime.strftime('%Y-%m-%dT%H:%M:%S %Z')}")  # UTC ISO manual
print(f"8.  {birth_datetime.isoformat()}")  # ISO auto
print(f"9.  {birth_datetime.strftime('%d-%m-%Y %I:%M:%S %p')}")  # With 12 am/pm hour
print(f"10. {birth_datetime.strftime('%a-%b-%y')}")  # With day/month names
