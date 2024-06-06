import re

"""
    String operations...
"""

# Get length of a string
LENGTHSTR = len("Hello World!")
print("Get length of a string: len(<STRING NAME>)")
print(f'len("Hello World!") --> {LENGTHSTR}')

# Get char of a string
CHAR = "Hello World!"[3]
print("\nGet char of a string: <STRING NAME>[<INDEX OF THE CHAR>]")
print(f'"Hello World!"[3] --> "{CHAR}"')

# Get substring of a string
SUBSTRING = "Hello World!"[3:8]
print("\nGet substring of a string: <STRING NAME>[<START + 1>, <END>]")
print(f'"Hello World!"[3:9] --> "{SUBSTRING}"')

# String to uppercase
UPPERCASESTR = "Buenos Aires".upper()
print("\nString to uppercase: <STRING NAME>.uppercase()")
print(f'"Buenos Aires".upper() --> "{UPPERCASESTR}"')

# String to lowercase
LOWERCASESTR = "USA".lower()
print("\nString to lowercase: <STRING NAME>.lower()")
print(f'"USA".lower() --> "{LOWERCASESTR}"')

# Repeat a string
REPEATEDSTR = "Juana" * 2
print("\nRepeat a string: <STRING NAME> * <NUMBER OF REPEATS>")
print(f'"Juana" * 2 --> "{REPEATEDSTR}"')

# Concat two strings (first option)
CONCATEDSTROPT01 = "Lucas " + "Hoz"
print(
    "\nConcat two strings (first option): <FIRST STRING NAME> + <SECOND STRING NAME> + <'N' STRING NAME...>"
)
print(f'"Lucas " + "Hoz" --> "{CONCATEDSTROPT01}"')

# Concat two strings (second option)
CONCATEDSTROPT02 = " ".join(["Lucas", "Hoz", "-", "Argentina"])
print(
    "\nConcat two strings (second option): <SEPARATOR>.join([<FIRST STRING NAME>, <'N' STRING NAME...>])"
)
print(f'" ".join(["Lucas", "Hoz", "-", "Argentina"]) --> "{CONCATEDSTROPT02}"')

# Replace substring of a string
REPLACEDSTR = "Hello Python!".replace("Python", "TypeScript")
print(
    "\nReplace substring of a string: <STRING NAME>.replace(<SUBSTRING TO SEARCH>, <NEW SUBSTRING>)"
)
print(f'"Hello Python!".replace("Python", "TypeScript") --> "{REPLACEDSTR}"')

# Compare start of a string
COMPARESTART = "Lucas".startswith("ho")
print("\nCompare start of a string: <STRING NAME>.startswith(<SUBSTRING TO FIND>)")
print(f'"Lucas".startswith("ho") --> {COMPARESTART}')

# Compare end of a string
COMPAREEND = "Lucas".endswith("as")
print("\nCompare end of a string: <STRING NAME>.endswith(<SUBSTRING TO FIND>)")
print(f'"Lucas".endswith("as") --> {COMPAREEND}')

# Check if a string includes a substring
INCLUDES = "Lucas".find("c")
print("\nCheck if a string find a substring: <STRING NAME>.find(<SUBSTRING TO FIND>)")
print(f'"Lucas".find("c") --> {INCLUDES}')

# Check if a string matches a regex
REGEXSTR = re.match(r"/[uca]/", "Lucas")
print("\nCheck if a string matches a regex: re.match(r<REGEX>, <STRING NAME>)")
print(f're.match(r"/[uca]/", "Lucas") --> [{REGEXSTR}]')

# Check if a string is equal to another string
COMMONCOMPARISON = "Lucas" == "LuCaS"
print(
    "\nCheck if a string is equal to another string: <FIRST STRING NAME> == <SECOND STRING NAME>"
)
print(f'"Lucas" == "LuCaS" --> {COMMONCOMPARISON}')


print(
    "\n# ---------------------------------------------------------------------------------- #"
)

"""
    Additional challenge... 
"""


def get_palindrome_words(words: list[str]) -> list[str]:
    """Get palindrome words"""
    palindromes: list[str] = []

    for word in words:
        reversed_word: str = word[::-1]
        if word == reversed_word:
            palindromes.append(word)

    return palindromes


def get_anagram_words(pair_of_words: list[list[str]]) -> list[list[str]]:
    """Get anagram words"""
    anagrams: list[list[str]] = []

    for words in pair_of_words:
        [word_01, word_02] = words
        longest_word: str = word_01 if (len(word_01) > len(word_02)) else word_02

        are_anagrams: bool = True
        unique_chars: set[str] = set(list(longest_word))

        for char in longest_word:
            if char in unique_chars:
                continue
            are_anagrams = False
            break

        if are_anagrams:
            anagrams.append(words)

    return anagrams


def get_isogram_words(words: list[str]) -> list[str]:
    """Get isogram words"""
    isograms: list[str] = []

    for word in words:
        word_formatted = word.replace(" ", "")
        unique_chars = set(list(word_formatted))
        if len(word_formatted) == len(unique_chars):
            isograms.append(word)

    return isograms


ARR01 = [
    "level",
    "hello",
    "racecar",
    "world",
    "madam",
    "programming",
    "deed",
    "javascript",
]
PALINDROMEWORDS = get_palindrome_words(ARR01)
print(f"\nPalindrome words of {ARR01} --> {PALINDROMEWORDS}")

ARR02 = [
    ["listen", "silent"],
    ["hello", "world"],
    ["good", "dog"],
]
ANAGRAM_WORDS = get_anagram_words(ARR02)
print(f"\nAnagram words of {ARR02} --> {ANAGRAM_WORDS}")

ARR03 = ["hello", "world", "isogram", "javascript", "python", "algorithm"]
ISOGRAM_WORDS = get_isogram_words(ARR03)
print(f"\nIsogram words of {ARR03} --> {ISOGRAM_WORDS}")
