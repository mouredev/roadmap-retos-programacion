
string = "This is a string with multiple characters"

#Access to element

print("Element at position 2 is: ", string[1])

#Sub string

print("Substring: ", string[0:15])

#Length

print("Length of the string is: ", len(string))

#Concatenate 

string1 = "This is a string"
string2 = " and another string"

print("Concatenate: ", string1+string2)

#Repeat string

print("Repeat string: ", 2*string1)

#Loop over string

for character in string1:
    print(character)

# Uppercase

print("Uppercase: ", string1.upper())  

#Lowercase

print("Lowercase: ",string1.lower())  

#Replace

string_new = string1.replace(' ','_')
print("Replace: ", string_new)

#Split

list = string1.split(" ")
print("Split: ", list)

#Join

list2 = ["Join", "string"]

print("Join: ", " ".join(list2))

#Verification

string_numeric = "12"
print("Is numeric: ", string_numeric.isdigit())

#Extra exercise

def isPalindrome(input:str)-> bool:
    reverse = input.lower()
    return input == reverse[::-1]

#Palindorme

string_palindrome = "ana"

print("Is palindrome:", isPalindrome(string_palindrome))

#Anagram

def is_anagram(value1:str,value2:str):
    return sorted(value1) == sorted(value2)


string3 = "roca"
string4 = "caro"

print("Anagram: ",is_anagram(string3,string4))

#Isogram

def is_isogram(input:str)->bool:
    letter_set = set(input.lower())
    return len(letter_set) == len(input)

string5="pan"
print("Is isogram: ", is_isogram(string5))