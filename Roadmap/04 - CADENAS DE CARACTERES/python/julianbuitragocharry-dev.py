my_string = 'Hello'
my_second_string = 'World!'

# Concatenation
print(my_string + ', ' + my_second_string)

# String as List --> You can slicing and using list methods 
for i in range(len(my_string)):
    print(my_string[i])

print(my_string[::-1])

# Search
print('W' in my_string)
print('W' in my_second_string)

# Some Methods 
my_new_string = my_string

my_new_string.capitalize()
print(my_new_string)

my_new_string.lower()
print(my_new_string)

my_new_string.replace('e', 'o')
print(my_new_string)

def is_palindromo(first_string: str, second_string: str):
    return (first_string == second_string[::-1])

def is_anagrama(first_string: str, second_string: str):
    return (first_string.sort() == second_string.sort())

def is_isograma(string):
    word_dict = dict()
    for character in string:
        word_dict[character] = word_dict.get(character, 0) + 1
    isogram = True
    values = list(word_dict.values())
    isogram_len = values[0]
    for word_count in values:
        if word_count != isogram_len:
            isogram = False
            break
    return isogram