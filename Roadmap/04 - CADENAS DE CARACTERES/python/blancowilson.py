string1 = "Hi "
string2 = "Python"

string_result = string1 + string2

print(string_result)

print(string1*3)

for leter in string1:
    print(leter)

print(len(string_result))

# dividir
print(string_result[2:6])
print(string_result[2:])

print ('t' in string_result)
print (string_result.replace('Hi', 'Hello'))

print(string_result.split('P'))

print(string_result.upper())
print(string_result.lower())
print(string_result.capitalize())
print(string_result.title())

string_list = [string1,', ', string2]
print(string_list)

def verify_string(word1: str, word2:str ):
    print(f"{word1}  {'Is' if word1 == word1[::-1] else 'is Not'} a Palindromo")
    print(f"{word2}  {'Is' if word2 == word2[::-1] else 'is Not'} a Palindromo")

    print(f"{word1}  {'Is' if sorted(word1) == sorted(word2) else 'is Not'} Anagrama of {word2}")

verify_string('amor','roma')