#4 { Retos para Programadores } CADENAS DE CARACTERES
# Short for log
log = print  # Using print as a logging function

# STRING TYPE
# The str type is the object representation of strings in Python.
string_object = str("hello girl")  # Creating a string object

# In Python, strings are immutable, but we can still access various methods for manipulating the data.

q = 'Did you know Internet start as a Pentagon project named ARPANET (Advanced Research Projects Agency Network)?'
q2 = q[12:]  # Slicing the string from index 12 to the end
log(q2)  # Logs: Internet start as a Pentagon project named ARPANET (Advanced Research Projects Agency Network)?

# The Python Character
# Python strings are sequences of Unicode characters. The len() function returns the number of characters in the string.
message = "Sometimes you make me smile..."

# Length of the message
log(len(message))  # Output: 30

# Character at index 10
log(message[10])  # Output: y

# Unicode code point of character at index 10
log(ord(message[10]))  # Output: 121

# First occurrence of 'm'
log(message.index('m'))  # Output: 2

# Last occurrence of 'm'
log(message.rindex('m'))  # Output: 23

# Last index of 's'
chart = message.rindex('s')  # Should be 22
log(chart)  # Log the value of chart (last index of 's')

# First index of '.'
chart2 = message.index('.')  # Should be 27
log(chart2)  # Log the value of chart2 (first index of '.')

# Substring from last index of 's' to the first index of '.'
log(message[chart:chart2])  # Output: smile (substring from index 27 to 29)

# Slicing from the end
log(message[-8:])  # Output: smile...

arr = list(message[:8])  # Convert the first 8 characters to a list
log(arr)  # ['S', 'o', 'm', 'e', 't', 'i', 'm', 'e'] (not inclusive of the last index)
log('-'.join(arr))  # S-o-m-e-t-i-m-e
log(arr[-1].replace('e', 'e-s'))  # e-s
log('-'.join(arr).replace('-', '') + 's')  # Sometimes

# Note: Some emojis may be represented by multiple code points, so consider this when evaluating lengths.

fragment = '   at this point in my life...  '
log(fragment.strip())  # Logs: at this point in my life... (without spaces at the beginning or end)

# Note: You can also use lstrip() or rstrip() for trimming.

name = 'anna'
log(name.upper())  # ANNA
othername = 'Luna'
log(othername.lower())  # luna

# We can also use the chr() function to get characters from Unicode code points.
log(''.join(chr(i) for i in [193, 48, 587, 482, 102, 107]))  # Á0ɋǢfk
log(chr(0x68fa))  # 棺

# Note: Using chr() may have performance implications if called frequently or with many characters.

# The normalize() method is not directly available in Python, but we can use the unicodedata module for normalization.
import unicodedata

# U+00C5: Latin capital letter A with ring above
log(chr(0x00C5))  # Å
# U+212B: Angstrom sign
log(chr(0x212B))  # Å
# U+0041: Latin capital letter A
# U+030A: Combining ring above
log(chr(0x0041) + chr(0x030A))  # Å

unnormalized_text = chr(0x0041) + chr(0x030A) + chr(0x212B) + chr(0x00C5)
log(ord(unnormalized_text[1]), ord(unnormalized_text[3]))  # 778 197
# Normalize the text and check its length before accessing indices
normalized_text = unicodedata.normalize('NFC', unnormalized_text)

# Check the length of normalized_text before accessing its indices
if len(normalized_text) > 3:
    log(ord(normalized_text[1]), ord(normalized_text[3]))  # Access safely
else:
    log("Normalized text is too short:", normalized_text)

# We can concatenate strings using the + operator or the join() method.
first_name = 'Patty'
last_name = ' Smith'
long_name = first_name + last_name  # Concatenation using +
log(long_name)  # Patty Smith
# Same as
log(first_name + last_name)  # Patty Smith

# Function to capitalize the first letter of a string
def capitalize(s):
    return s[0].upper() + s[1:]

log(capitalize(name))  # Anna

# Methods for locating substrings within another string: find() and rfind().
fragment2 = 'the fire is burned, the tables are turned...'
log(fragment2.find('is'))  # 9
# Searching for a substring that does not exist returns -1
log(fragment2.find('house'))  # -1
log(fragment2.rfind('t'))  # 35 (last occurrence of 't')

# String Inclusion Methods
log(fragment2.startswith("the"))  # True
log(fragment2.endswith("fire"))  # False

# Repeat a string using the * operator
say = 'oh'
log(say * 2 + '!')  # ohoh!

# Implementing a custom padStart function
def add_pad(s, width, pad='0'):
    result = str(s)  # Convert to string
    while len(result) < width:  # While the length is less than the desired width
        result = f"{pad}{result}"  # Prepend the padding character
    return result

log(add_pad(4, 3, '#'))  # ##4
log(add_pad(56, 3, '$'))  # $56
log(add_pad(7, 3))  # 007
log(add_pad('something', 3, '-'))  # ---something

# Function to add padding to a string
def add_pad(s, width, pad='0'):
    result = str(s)  # Convert to string
    while len(result) < width:  # While the length is less than the desired width
        result = f"{pad}{result}"  # Prepend the padding character
    return result

greeting = "tururuuu"
padded_string = add_pad(greeting, 11, "&")  # Padding the greeting string to a width of 11 with '&'
log(padded_string)  # Logs: &&&tururuuu

import re

# Function to convert various string formats to camelCase
def to_camel_case(input_str):
    # Replace kebab-case, snake_case, and spaces with a space
    # Handle PascalCase
    return (
        ''.join(
            part.capitalize() if i > 0 else part.lower()
            for i, part in enumerate(re.split(r'[-_\s]+', input_str))
        )
    )

log(to_camel_case('PascalCase'))  # pascalCase
log(to_camel_case('kebab-case-string'))  # kebabCaseString
log(to_camel_case('snake_case_string'))  # snakeCaseString
log(to_camel_case('string with spaces'))  # stringWithSpaces

# Simulating a window load event in a console environment
def on_load():
    body_style = {
        'background': '#000',
        'text-align': 'center'
    }
    
    title = 'Retosparaprogramadores #4.'
    title_style = {
        'font-size': '3.5vmax',
        'color': '#fff',
        'line-height': '100vh'
    }
    
    # Simulating setting styles (not applicable in console)
    log(f"Body styles: {body_style}")
    log(f"Title: {title} with styles: {title_style}")
    
    # Simulating a delay before showing an alert
    import time
    time.sleep(2)  # Wait for 2 seconds
    log('Retosparaprogramadores #4.')

on_load()  # Call the function to simulate the load event

# ADDITIONAL DIFFICULTY (optional):
# Create a program that analyzes two different words and performs checks
# to determine if they are: Palindromes, Anagrams, Isograms

# Palindrome: A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
def is_palindrome(w1, w2):
    if len(w1) != len(w2):
        return False
    return w1 == w2[::-1]  # Check if w1 is equal to w2 reversed

log('is palindrome: ', is_palindrome('roma', 'amor'))  # Logs: true

# Anagram: An anagram is a word or phrase formed by rearranging the letters of another word or phrase.
def is_anagram(w1, w2):
    if len(w1) != len(w2):
        return False
    return sorted(w1) == sorted(w2)  # Check if sorted characters of both words are equal

log('is anagram: ', is_anagram('nick', 'kinc'))  # Logs: True

# Isogram: An isogram is a word or phrase in which no letter occurs more than once.
def is_isogram(s):
    # Create a list to count occurrences of each letter
    count_letters = []
    for l in s:
        count_letters.append(s.count(l))  # Count occurrences of each letter in the string

    # Check if any letter occurs more than once
    for num in count_letters:
        if num > 1:
            return False
    return True

log('is isogram: ', is_isogram('background'))  # Logs: true

# Function to check if two strings are palindromes, anagrams, or isograms
def check_state(str1, str2):
    r_poli = is_palindrome(str1, str2)  # Check if they are palindromes
    r_anag = is_anagram(str1, str2)      # Check if they are anagrams
    f_iso = is_isogram(str1)              # Check if the first string is an isogram
    s_iso = is_isogram(str2)              # Check if the second string is an isogram
    result = ''
    bool_result = False

    if r_poli and r_anag and f_iso and s_iso:
        result = f'The words: "{str1}" and "{str2}" are palindromes, anagrams, and also isograms.'
        bool_result = True
    elif r_poli:
        result = f'The words: "{str1}" and "{str2}" are palindromes and anagrams but they aren\'t isograms.'
    elif r_anag and f_iso and s_iso:
        result = f'The words: "{str1}" and "{str2}" are anagrams and also isograms.'
        bool_result = True
    elif r_anag:
        result = f'The words: "{str1}" and "{str2}" are anagrams.'

    if not bool_result:
        if f_iso and s_iso:
            result = f'The words: "{str1}" and "{str2}" are isograms.'
        elif f_iso:
            result += f'The first word: "{str1}" is an isogram.'
        elif s_iso:
            result += f'The second word: "{str2}" is an isogram.'
        elif not r_poli and not r_anag:
            result = f'The words: "{str1}" and "{str2}" aren\'t palindromes, anagrams, or isograms.'

    log(result)

# Test cases
check_state('amor', 'mora')  # Logs: The words: "amor" and "mora" are anagrams and also isograms.
check_state('amor', 'roma')  # Logs: The words: "amor" and "roma" are palindromes, anagrams, and also isograms.
check_state('zeitgest', 'kaguabumga')  # Logs: The words: "zeitgest" and "kaguabumga" aren't palindromes, anagrams, or isograms.
check_state('pizza', 'background')  # Logs: The second word: "background" is an isogram.
