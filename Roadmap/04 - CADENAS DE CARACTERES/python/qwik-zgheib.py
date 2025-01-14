# -- exercise --
string: str = "Hello, World!"

# access to specific characters
print(string[0])
print(string[-1])

# sub strings
print(string[1:5])
print(string[:4])
print(string[7:])

# long
print(len(string))

# concatenation
print(string + " How are you?")

# repetition
print(string * 2)

# route
for char in string:
    print(char)

# uppercase - lowercase
print(string.upper())
print(string.lower())

# replacement
print(string.replace("Hello", "Bye"))

# division
print(string.split(" "))

# union
list_i: list[str] = ["Hello", "World"]
print(" ".join(list_i))

# interpolation
name: str = "World"
print(f"Hello, {name}!")

# verification
print(string.startswith("Hello"))
print(string.endswith("!"))
print("World" in string)
print(string.isalpha())
print("Hello".isalpha())


print("\n----- extra challenge -----")


# -- extra challenge --
class WordAnalyzer:
    def __init__(self, word1: str, word2: str):
        self.word1 = word1
        self.word2 = word2

    def is_palindrome(self, word: str) -> bool:
        return word == word[::-1]

    def is_anagram(self, word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)

    def is_isogram(self, word: str) -> bool:
        return len(word) == len(set(word))

    def analyze(self):
        results = {
            "word1_is_palindrome": self.is_palindrome(self.word1),
            "word2_is_palindrome": self.is_palindrome(self.word2),
            "are_anagrams": self.is_anagram(self.word1, self.word2),
            "word1_is_isogram": self.is_isogram(self.word1),
            "word2_is_isogram": self.is_isogram(self.word2),
        }
        return results


def display_results(results):
    print(f"fist word is palindrome: {results['word1_is_palindrome']}")
    print(f"second word is palindromw: {results['word2_is_palindrome']}")
    print(f"the words are anagrams: {results['are_anagrams']}")
    print(f"first word is isogram: {results['word1_is_isogram']}")
    print(f"second word is isogram: {results['word2_is_isogram']}")


def main():
    word1 = input("enter the first word: ")
    word2 = input("enter the second word: ")

    analyzer = WordAnalyzer(word1, word2)
    results = analyzer.analyze()

    display_results(results)


if __name__ == "__main__":
    main()
