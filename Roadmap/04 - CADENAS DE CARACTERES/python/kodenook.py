
txt = 'hello, python!'

print(len(txt))
print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.replace('h', 'j'))
print(txt.split(','))
print(txt.capitalize())

def word_type(word: str, word2: str) -> None:

    if word == word[::-1]:
        print('is palindrome')

    if sorted(word) == sorted(word2):
        print('is an anagram')

    if len(word) == len(set((word))):
        print('is isogram')

word_type('amor', 'roma')