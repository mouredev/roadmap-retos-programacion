# --------- Strings

my_string: str = "Soy un String"

# I. Acceso
print("Acceso:", my_string[5])

# II. Subcadenas
my_sub_string = my_string[0:10]
print("Subcadenas:", my_sub_string)

# III. Longitud
print("Longitud:", len(my_string))

# IV. Concatenación
my_string = my_string + " :)"
print("Concatenación:", my_string)

# V. Repetición
print("Repetición:", my_string * 2)

# VI. Recorridio
print("Recorrido (for each): ", end='')
for letter in my_string:
  print(letter, end='')
print()


print("Recorrido (while): ", end='')
counter = 0
while counter != len(my_string):
  print(my_string[counter], end='')
  counter = counter + 1
print()

# VII. Mayusculas
print("Conversión a mayusculas:", my_string.upper())

# VIII. Minisculas
print("Conversión a minusculas:", my_string.lower())

# IX. Reemplazo
my_string = my_string.replace("un String", "una Cadena")
print("Reemplazo:", my_string)

# X. División
my_split_string = my_string.split()
print("División:", my_split_string)

# XI. Union
my_join_string = " ".join(my_split_string)
print("Union:", my_join_string)

# XII. Interpolación
print(f"Interpolación: {my_string}")

# XIII. Verificación
print("Verificación:")
print("String" in my_string)
print(my_string.isdigit())
print(my_string.islower())
print(my_string.startswith("Soy"))
print(not my_string.isalpha())


# --------- Extra
import re


def only_letters(string):
  return re.sub(r"[^a-z]", '', string.lower())


def is_palindrome(string):
  return only_letters(string) == string[::-1]


def is_anagram(string_1, string_2):
  return sorted(only_letters(string_1)) == sorted(only_letters(string_2))


def is_isogram(string):
  stack: dict = {}

  for letter in only_letters(string):
        if letter in stack:
            stack[letter] += 1

        else:
            stack[letter] = 1

  return len(set(stack.values())) == 1


print(is_palindrome("radar"))
print(is_palindrome("coco"))

print(is_anagram("cola", "loca"))
print(is_anagram("nona", "nono"))

print(is_isogram("carbon"))
print(is_isogram("carbonara"))
