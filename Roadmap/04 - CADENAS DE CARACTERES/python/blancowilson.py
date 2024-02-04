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
    print(f"{word1}", "NO" {if word1 == word1[::-1]} "es Palindromo")

verify_string('Amor','Roma')