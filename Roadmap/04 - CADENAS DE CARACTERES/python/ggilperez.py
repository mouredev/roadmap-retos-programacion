# Problem #04 Strings

my_string = "hello world"

# Access first char / index
print(f"{my_string[0] = }")

# Substring
print(f"{'hello' in my_string = }")

# Length
print(f"{len(my_string) = }")

# Concat
print(f"{my_string + ' Python' = }")

# Repeat
print(f"{my_string * 3 = }")

# Loop
print("Start loop")
for char in my_string:
    print(char)
print("End loop")

# Upper case
print(f"{my_string.upper() = }")

# Lower case
print(f"{my_string.lower() = }")

# Title
print(f"{my_string.title() = }")

# Capitalize
print(f"{my_string.capitalize() = }")


# Replace...
# Strings are immutable but can return new object with replaced string
print(f"{my_string.replace('world', 'Python') = }")

# Split
print(f"{my_string.split((' ')) = }")

# Slicing
print(f"{my_string[2:5] = }")

# Trimm / Strip
my_string = " " + my_string + " "
print('"' + my_string + '"')
print(f"{my_string.strip() = }")


my_string = "hello world"

# Search
print(f"{my_string.startswith('hello') = }")
print(f"{my_string.endswith('world') = }")
print(f"{my_string.find('w') = }")

# Count
print(f"{my_string.count('l') = }")

# Format
my_string = "Hello {0}"
print('"' + my_string + '"')
print(f"{my_string.format('Python') = }")

# Cast
my_string = "hello world"

# To list
print(f"{list(my_string) = }")

# From list
print(f"{''.join(['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']) = }")

# To int
print(f"{int('1234') = }")

# From int
print(f"{str(1234) = }")

# To float
print(f"{float('12.34') = }")

# From float
print(f"{str(12.34) = }")

# Checks
print(f"{my_string.isdigit() = }")
print(f"{my_string.isalpha() = }")
print(f"{my_string.isalnum() = }")
print(f"{my_string.isnumeric() = }")
print(f"{my_string.isascii() = }")
print(f"{my_string.isdecimal() = }")
print(f"{my_string.isidentifier() = }")
print(f"{my_string.islower() = }")
print(f"{my_string.isprintable() = }")
print(f"{my_string.isspace() = }")
print(f"{my_string.istitle() = }")
print(f"{my_string.isupper() = }")

# Extra

def is_palindrome(word) -> bool:
    return word[::-1] == word

def is_anagram(word_1: str, word_2: str) -> bool:
    return sorted(word_1) == sorted(word_2)

def is_isogram(word: str) -> bool:
    """
    An isogram must have the same count on each letter/char
    """
    innit_count = word.count(word[0])
    for letter in word:
        if word.count(letter) != innit_count:
            return False
    return True

def do_checks(word_1: str, word_2: str):
    print(f"is palindrome {word_1} {is_palindrome(word_1)}")
    print(f"is palindrome {word_2} {is_palindrome(word_2)}")

    print(f"is anagram {word_1} / {word_2} {is_anagram(word_1, word_2)}")

    print(f"is isogram {word_1} {is_isogram(word_1)}")
    print(f"is isogram {word_2} {is_isogram(word_2)}")

do_checks("hello", "world")
do_checks("badab", "dabab")
