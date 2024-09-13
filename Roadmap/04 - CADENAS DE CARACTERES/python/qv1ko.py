def program(word1, word2):
    print(f"The word {word1} is a palindrome" if is_palindrome(word1) else f"The word {word1} is not a palindrome")
    print(f"The word {word2} is a palindrome" if is_palindrome(word2) else f"The word {word2} is not a palindrome")
    print(f"The words {word1} and {word2} are anagrams" if are_anagrams(word1, word2) else f"The words {word1} and {word2} are not anagrams")
    print(f"The word {word1} is an isogram" if is_isogram(word1) else f"The word {word1} is not an isogram")
    print(f"The word {word2} is an isogram" if is_isogram(word2) else f"The word {word2} is not an isogram")

def is_palindrome(word):
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - i - 1]:
            return False
    return True

def are_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False
    letters_word1 = sorted(word1)
    letters_word2 = sorted(word2)
    return letters_word1 == letters_word2

def is_isogram(word):
    letters = []
    for letter in word:
        if letter in letters:
            return False
        letters.append(letter)
    return True

program("solution", "loose")
