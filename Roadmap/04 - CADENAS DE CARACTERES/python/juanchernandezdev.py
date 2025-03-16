### Python Strings ###

my_first_str = 'Hello world, I\'m learning python'
my_second_str = 'My other string'

#! Multiline String
my_multi_str = '''Hello, this
is a multiline
string'''
print(my_multi_str)

#! Accessing a Character
print(my_first_str[6]) # Shows character at index 6

#! String Concatenation
print(my_first_str + ', ' + my_second_str)
print(f'{my_first_str}, {my_second_str}')

#! Substrings
#* Slicing
print(my_first_str[0:11])
print(my_first_str[-6:])

#! Length
print(len(my_first_str))

#! Repetition
print(my_first_str * 4)

#! Formatting
year = 2024
month = 'jun'
temp = 23.5

# f-string
print(f'The current year is {year}, the current month is {month}, and today temperature is {temp}celsius.')

# format() method
print('The current year is {}, the current month is {}, and today temperature is {}celsius.'.format(year, month, temp))

# % Operator
print('The current year is %s, the current month is %s, and today temperature is %.1fcelsius.' %(year, month, temp))

#! String Iteration
for char in my_first_str:
  print(char)
  
# Iteration with char index
for i, char in enumerate(my_first_str):
  print(i, char)

#! Methods
#* Uppercase
print(my_first_str.upper())

#* Lowercase
print(my_first_str.lower())

#* Title
print(my_first_str.title())

#* Capitalize
print(my_first_str.capitalize())

#* Replace
print(my_first_str.replace('Hello', 'Good bye'))

#* Find
print(my_first_str.find('python'))

#* Split
print(my_first_str.split(' '))

#* Join
print(''.join(my_first_str))

#! Escape Characters
#* Line Break
print('Jumping a\nline.')

#* Tab
print('first word\tsecond word')

#* Quote
print('The author said, \'Author quote here!\'')

#* Backslash
print('Hi, I\'m a backslash -> \\')

#! Verification
upper_str = 'UPPER WORDS'
digits_str = '123456'
empty_str = ''

# isupper
print(upper_str.isupper())

# islower
print(upper_str.islower())

# isdigits
print(upper_str.isdigit())
print(digits_str.isdigit())

# isalpha
print(upper_str.isalpha()) # Returns false because of the space
print(digits_str.isalpha())

# isalnum
print(upper_str.isalnum())
print(digits_str.isalnum())

# startswith
print(upper_str.startswith('Hello'))
print(digits_str.startswith('1'))

# endswith
print(upper_str.endswith('WORDS'))
print(digits_str.endswith('6'))

# check if the string is empty
if len(empty_str) == 0: print('the string is empty') 

#! Optional Challenge
print('---Optional Challenge---')

def word_checker(first_txt, second_txt):
  normalized_first_txt = first_txt.lower().replace(' ', '')
  normalized_second_txt = second_txt.lower().replace(' ', '')
  sorted_first = ''.join(sorted(normalized_first_txt)) 
  sorted_second = ''.join(sorted(normalized_second_txt))
  
  
  if normalized_first_txt == normalized_first_txt[::-1]:
    print(f'{first_txt.capitalize()} is a palindrome!!.')
    
  if normalized_second_txt == normalized_second_txt[::-1]:
    print(f'{second_txt.capitalize()} is a palindrome!!.')
    
  if sorted_first == sorted_second :
    print(f'The second word {second_txt} is an anagram of {first_txt}!!.') 
  
  my_first_set = set()
    
  for char in normalized_first_txt:
      counter = normalized_first_txt.count(char)
      my_first_set.add(counter)
      
  my_second_set = set()
    
  for char in normalized_second_txt:
      counter = normalized_second_txt.count(char)
      my_second_set.add(counter)

  if len(my_first_set) == 1:
    print(f'Your word {first_txt} is a isogram!!')
    
  if len(my_second_set) == 1:
    print(f'Your word {second_txt} is a isogram!!')
      
#* Palindrome    
word_checker('madam', 'kayak')
word_checker('car', 'Rotator')  
    
#* Aanagram
word_checker('angel', 'Glean')
word_checker('cried', 'cider')
word_checker('cat', 'act')

#* Isogram
word_checker('Caucasus', 'intestines')
