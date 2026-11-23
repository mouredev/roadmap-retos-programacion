"""
 String operations
"""

word1 = "Dragon"
word2 = "Slayer"

# Concatenation
print(word1 + " " + word2)

# Repetition
print(word1 * 3)

# Indexing
print(word1[0] + word1[1] + word1[2] + word1[3])

# Length
print(len(word2))

# Slicing
print(word2[2:6])
print(word2[2:])
print(word2[0:2])
print(word2[:2])

# Search
print("a" in word1)
print("z" in word1)

# Replacement
print(word1.replace("a", "e"))

# Split
print(word2.split("a"))

# Upper, lower, title and capitalise
print(word1.upper())
print(word1.lower())
print("elhdrond the dragon slayer".title())
print("elhdrond the dragon slayer".capitalize())

# Strip whitespace
print("  elhdrond  ".strip())

# Starts and ends with
print(word1.startswith("Dr"))
print(word1.startswith("Sl"))
print(word2.endswith("er"))
print(word2.endswith("on"))

word3 = "Elhdrond the Dragon Slayer"

# Find position
print(word3.find("Dragon"))
print(word3.find("dragon"))
print(word3.lower().find("dragon"))

# Count occurrences
print(word3.lower().count("e"))

# Format
print("Hero: {}, Weapon: {}!".format(word1, word2))

# Interpolation
print(f"Hero: {word1}, Weapon: {word2}!")

# Convert string to list of characters
print(list(word3))

# Join list into string
parts = [word1, " ", word2]
print("".join(parts))

# Numeric conversions
num_str = "42"
print(int(num_str))

float_str = "3.14"
print(float(float_str))

# String checks
print(word1.isalnum())
print(word1.isalpha())
print(num_str.isalpha())
print(num_str.isnumeric())


"""
 Extra Exercise 
"""


def analyse_words(word1: str, word2: str):

    # Palindrome 
    print(f"Is '{word1}' a palindrome?: {word1 == word1[::-1]}")
    print(f"Is '{word2}' a palindrome?: {word2 == word2[::-1]}")

    # Palindrome char by char
    def check_palindrome(word: str):
        is_palindrome = True
        for i in range(len(word) // 2):
            left = word[i]
            right = word[-(i + 1)]
            match = left == right
            print(f"  [{i}] '{left}' == '[{len(word) - 1 - i}]' '{right}' -> {match}")
            if not match:
                is_palindrome = False
                break
        print(f"'{word}' is {'a palindrome' if is_palindrome else 'not a palindrome'}.")

    check_palindrome(word1)
    check_palindrome(word2)

    # Anagram
    print(f"Is '{word1}' an anagram of '{word2}'?: {sorted(word1.lower()) == sorted(word2.lower())}")

    # Isogram
    def is_isogram(word: str) -> bool:
        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        values = list(word_dict.values())
        base = values[0]
        for count in values:
            if count != base:
                return False
        return True

    print(f"Is '{word1}' an isogram?: {is_isogram(word1)}")
    print(f"Is '{word2}' an isogram?: {is_isogram(word2)}")

    # Isogram using set - only works if all characters are unique
    def is_isogram_set(word: str) -> bool:
        return len(set(word)) == len(word)
    print(f"Is '{word1}' an isogram (unique chars only)?: {is_isogram_set(word1)}")
    print(f"Is '{word2}' an isogram (unique chars only)?: {is_isogram_set(word2)}")

    # Isogram using Counter
    from collections import Counter
    def is_isogram_counter(word: str) -> bool:
        counts = Counter(word)
        return len(set(counts.values())) == 1

    print(f"Is '{word1}' an isogram (counter)?: {is_isogram_counter(word1)}")
    print(f"Is '{word2}' an isogram (counter)?: {is_isogram_counter(word2)}")


analyse_words("radar", "radar")
analyse_words("racecar", "abcabc")
analyse_words("python", "java")

analyse_words("phytonpython", "abcde")
analyse_words("abcabc", "python")
analyse_words("java", "radar")

