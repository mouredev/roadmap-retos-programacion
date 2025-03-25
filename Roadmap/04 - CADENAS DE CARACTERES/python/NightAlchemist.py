#Operations on strings

string1 = "This is my year!"
string2 = "I will make it count!"

#Concatenation

string3 = string1 + " " + string2
print(string3)  #This is my year! I will make it count!

#Repetition

string4 = string1 * 3
print(string4)  #This is my year!This is my year!This is my year!

#Indexing

print(string1[0])  #T
print(string1[5])  #i
print(string1[-3]) #a

#Slicing

print(string1[0:4])  #This
print(string1[5:])   #is my year!
print(string1[:4])   #This
print(string1[:])    #This is my year!
print(string1[0:10:2])  #Ti sm

#Membership

print("year" in string1)  #True
print("year" not in string1)  #False

#Built-in functions

print(len(string1))  #15
print(min(string1))  
print(max(string1))
print(string1.index("i"))  #2
print(string1.count("i"))  #2

#String methods

print(string1.lower())  #this is my year!
print(string1.upper())  #THIS IS MY YEAR!
print(string1.title())  #This Is My Year!
print(string1.capitalize())  #This is my year!
print(string1.swapcase())  #tHIS IS MY YEAR!
print(string1.center(30))  #   This is my year!
print(string1.find("is"))  #2
print(string1.replace("is", "was"))  #Thwas was my year!
print(string1.split())  #['This', 'is', 'my', 'year!']
print(string1.split("i"))  #['Th', 's ', 's my year!']
print(string1.strip())  #This is my year!
print(string1.lstrip())  #This is my year!
print(string1.rstrip())  #This is my year!
print(string1.startswith("This"))  #True
print(string1.endswith("year!"))  #True
print(string1.isalnum())  #False
print(string1.isalpha())  #False
print(string1.isdigit())  #False
print(string1.islower())  #False
print(string1.isupper())  #False
print(string1.istitle())  #False

#String formatting

name = "John"
age = 25

print("My name is %s and I am %d years old." % (name, age))  #My name is John and I am 25 years old.
print("My name is {} and I am {} years old.".format(name, age))  #My name is John and I am 25 years old.    
print(f"My name is {name} and I am {age} years old.")  #My name is John and I am 25 years old.

#Escape characters

print("This is a backslash: \\")  #This is a backslash: \
print("This is a tab: \t")  #This is a tab:
print("This is a newline: \n")  #This is a newline:

#Raw strings

print(r"This is a raw string: \n")  #This is a raw string: \n
print("This is a raw string: \\n")  #This is a raw string: \n


#Extra

first_word = input("Give me a word: ").strip()
print(f"Your first word is {first_word}")
second_word = input("Give me another word: ").strip()
print(f"Your second word is {second_word}")

def analize(word1, word2): #palindrome, anagram or isogram?
    #palindromes
    reversed_word1 = word1[::-1]
    reversed_word2 = word2[::-1]
    
    if word1 == reversed_word1:
        print("The first word is a palindrome")
    else:
        print("The first word is not a palindrome")
    
    if word2 == reversed_word2:
        print("The second word is a palindrome")
    else:
        print("The second word is not a palindrome")
        
    #anagrams
    
    if len(word1) == len(word2) and sorted(word1) == sorted(word2):
        print("These words are anagrams")
    else:
        print("These words are not anagrams")
    
    #isograms
    def isogram(word):
        used_characters = set()
        for character in (word):
            if character in used_characters:
                return False
            else:
                used_characters.add(character)
        
        return True

    if isogram(word1):
        print("The first word is an Isogram")
    else:
        print("The first word is not an Isogram")
        
    if isogram(word2):
        print("The second word is an Isogram")
    else:
        print("The second word is not an Isogram")

analize(first_word, second_word)