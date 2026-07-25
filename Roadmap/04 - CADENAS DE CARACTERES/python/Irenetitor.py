#STRINGS
"Hi, everyone"
'Python'
""" This is also a String """

s1 = "Hello"
s2 = "World"


# #Concatenate
# print(s1 + ', ' + s2 + '!' )  #Hello, World !

# #Repetition
# Eco = "ha" * 3
# print(Eco)

# #Length
# print(len(Eco))    #6

# #Indentation
# print(s1[0] + s1[1] + s1[2] + s1[3] + s1[4])   #Hello
# print(s1[1])    #he

# #Slicing
# t = "If you can dream it"
# print(t[2:6])     #from position 2 to position 6 (not included)  - you
# print(t[:6])      #from the start to position 6 (not included)  -If you
# print(t[2:])      #from position 2 to all the way to the end   -you can dream it
# print(t[-7:-2])   #start counting from the end (from r to ' ' before it.)  -ream

# #Character search
# print("o" in s1)  #True
# print("i" in s1)  #False

# #Replace
# y = "Hi, ocean"
# print(y.replace("H", "J"))    #Ji, ocean

# #Split
# y = "Hi, ocean"
# print(y.split(","))      #['Hi', ' ocean']

# # Uppercase, lowercase, and title case
# print(s1.upper())    #HELLO
# print(s1.lower())    #hello
# print("better together".title())       #Better Together
# print("better together".capitalize())    #Better together

# # Removing spaces at the beginning and end
# print(" sparkling water ".strip())           #sparkling water

# #Search at the beginning and end
# print(s1.startswith("He"))  #True
# print(s1.startswith("Pi"))  #False
# print(s1.endswith("lo"))    #True
# print(s1.endswith(""))      #True

s3 = "Blood is thicker than water"

# Position search
print(s3.find("thicker"))  #9
print(s3.find("Than"))  #-1
print(s3.find("B"))  #0
print(s3.lower().find("w"))  #22

# Counting occurrences
print(s3.lower().count("a"))  #2

# Formatting
print("Greeting: {}, language: {}!".format(s1, s2))  #Greeting: Hello, language: World!

# Interpolation (f-strings)
print(f"Greeting: {s1}, language: {s2}!")  #Greeting: Hello, language: World!

# Transform string into a list of characters
print(list(s3))  #['B', 'l', 'o', 'o', 'd', ' ', 'i', 's', ' ', 't', 'h', 'i', 'c', 'k', 'e', 'r', ' ', 't', 'h', 'a', 'n', ' ', 'w', 'a', 't', 'e', 'r']

# Transform list into a string
l1 = [s1, ", ", s2, "!"]
print("".join(l1))  #Hello, World!

# Numeric transformations
s4 = "123456"
s4 = int(s4)
print(s4)   #123456

s5 = "123456.123"
s5 = float(s5)
print(s5)   #123456.123

# Various checks
s4 = "123456"
print(s1.isalnum())   #True
print(s1.isalpha())   #True
print(s4.isalpha())   #False
print(s4.isnumeric())   #True

#Extra exercise

def checking_word(word1: str, word2: str):
    # Palindrome checks
    print(f"Is '{word1}' a palindrome? {word1.lower() == word1[::-1].lower()}")
    print(f"Is '{word2}' a palindrome? {word2.lower() == word2[::-1].lower()}")

    # Anagram check
    if sorted(word1.lower()) == sorted(word2.lower()):
        print(f"'{word1}' and '{word2}' are anagrams")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams")

    # Isogram checks
    print(f"Is '{word1}' an isogram? {len(word1.lower()) == len(set(word1.lower()))}")
    print(f"Is '{word2}' an isogram? {len(word2.lower()) == len(set(word2.lower()))}")

