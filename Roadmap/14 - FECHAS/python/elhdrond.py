from datetime import datetime

"""
    DATES
"""

now = datetime.now()
birth_date = datetime(1991, 2, 20, 10, 30, 0)

print(f"Current date and time : {now}")
print(f"Birth date and time   : {birth_date}")

years = (now - birth_date).days // 365
print(f"Age: {years} years old")

"""
    EXTRA EXERCISE
"""

print(f"\n1.  Day / Month / Year (short)  : {birth_date.strftime('%d/%m/%y')}")
print(f"2.  Day / Month / Year (full)   : {birth_date.strftime('%d/%m/%Y')}")
print(f"3.  Time (HH:MM:SS)             : {birth_date.strftime('%H:%M:%S')}")
print(f"4.  Day of the year             : {birth_date.strftime('%j')} of 365")
print(f"5.  Day of the week             : {birth_date.strftime('%A')}")
print(f"6.  Week number                 : Week {birth_date.strftime('%W')}")
print(f"7.  Month name                  : {birth_date.strftime('%B')}")
print(f"8.  ISO 8601 format             : {birth_date.strftime('%Y-%m-%dT%H:%M:%S')}")
print(f"9.  AM/PM time                  : {birth_date.strftime('%I:%M %p')}")
print(
    f"10. Full readable format        : {birth_date.strftime('%A, %d %B %Y at %H:%M')}"
)
