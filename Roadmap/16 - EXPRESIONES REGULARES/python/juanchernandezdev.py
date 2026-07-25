### Python Regex ###
import re

pattern = r'\d+'
string = 'this is my test with numbers 1 2 12 45 48'
result = re.findall(pattern, string, re.IGNORECASE)
print(result)

#! Optional Challenge
#* Email

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'
email = 'johndoe@gmail.com'

if re.match(email_pattern, email):
  print('Your email is correct')
else:
  print('Wrong email format')

#* Phone number US format
phone_pattern = r'^\+?1?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
phone_number = '123 456 7890'

if re.match(phone_pattern, phone_number):
  print('Your phone is correct')
else:
  print('Wrong phone format')

#* URL  
url_pattern = r'^(https?:\/\/)?([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,6}(:\d+)?(\/[a-zA-Z0-9@:%._\+~#?&\/=-]*)?$'
url_number = "https://www.mytesturl.com"

if re.match(url_pattern, url_number):
  print('Your url is correct')
else:
  print('Wrong url format')
