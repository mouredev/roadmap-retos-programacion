# 16 Regex
import re

pattern = r"\d+"
rand_string = "qwe7865qwe978123087qwe"
print(f"{rand_string = }")

# Match with regex
matches = re.findall(pattern, rand_string)
for match in matches:
    print(match)

# Extra
email_pattern = r"^\S+@\S+\.\S+$"
phone_pattern = r"^(\+\d{1,3})? ?\d{1,4}[ -]?\d{1,4}[ -]?\d{1,4}$"
url_pattern = r"^(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})(\.[a-zA-Z0-9]{2,})?$"

print(bool(re.match(email_pattern, "ggilperezalcazar@gmail.com")))
print(bool(re.match(phone_pattern, "695847123")))
print(bool(re.match(url_pattern, "python.org")))
