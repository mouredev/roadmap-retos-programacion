#04 CADENAS DE CARACTERES

"""
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 */
"""

print("Hello") #String between "" or ''

text =  """ 
multiple
lines
and not limit
"""
print(text)

#access:
print(text[2])
print(text[2:6])

for x in "fruits":
  print(x)

str01 = "Hello my friends"
str02 = "Hello my friend"
str03 = "Hello my friends"

#compare strings:
print(str01 == str02)
print(str02 == str03)

#Join:
str05 = "hello "
str06 = "my friends"
strUnion = str05+str06

print(strUnion)

#Lenght:
print(len(str01))

#Membership 
print( "a" in "home")
print( "h" in "home")

#methods:
print("baLls".upper()) #converts the string to uppercase
print("baLls".lower()) #converts the string to lowercase
print("baLls".swapcase()) #converts all uppercase characters to lowercase and vice versa of the given string and returns it.
print("balls and sticks".partition("and")) #The partition method returns a 3-tuple containing:
someText = "Here you can find the dragons."
print(someText)
replaced = someText.replace("dragons",">>puppets") #replaces substring inside
print(replaced)
print(replaced.find("you")) #returns the index of first occurrence of substring
anotherText="Help me please.    "
print(anotherText.rstrip()) #returns a copy of the string with trailing characters removed (based on the string argument passed).
print(replaced.split()) #breaks down a string into a list of substrings using a chosen separator.
print(replaced.startswith("H")) #	checks if string starts with the specified string
print("126".isnumeric()) #checks numeric characters
print("126aa".isalnum()) #checks numeric and alphabet characters
print(replaced.index("n")) #returns the index of a substring inside the string (if found). If the substring is not found, it raises an exception.

#Escape Sequences
specialText = "Mariló can \"play\" guitar" # use the character: \ to skip special characters

# f-Strings
name = "Camela"
surname = "Analisais"
print(f'{name} is from {surname}') #Python f-Strings make it really easy to print values and variables.
del name # delete whole string

# format
String1 = "{} {} {}".format('Help', 'Me', 'Baby') 
print(String1) 

# Formatting of Integers
number = 16
String1 = "{0:b}".format(number) 
print(f"\nBinary representation of {number} is: {String1}") 
  
# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print(f"\nExponent representation of 165.6458 is: {String1}") 
  
# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print(f"\nOne-sixth is : {String1}")

#sort strings:
surname = "Analisais"
sorted = sorted(surname)
print(sorted)

#Count currents
print(surname.lower().count("a"))


print()
print()

def cleanWords(word: str)-> str:
    """clean special characters and transform to lowercase"""
    from unidecode import unidecode
    # Remove special characteres, spaces and punctuation
    cleanStr = ''.join(filter(str.isalpha, word))
    cleanStr = unidecode(cleanStr)
    # Convert to lowercase
    lowerStr = cleanStr.lower()

    return lowerStr


def checkPalindromes(word1: str, word2: str) -> bool:
  """function to detect if 2 words are palindromes ( is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as madam or racecar)"""
  #Check palindrome
  if cleanWords(word1) != cleanWords(word2)[::-1]:
    return False
  else:
    return True

def checkAnagrams(word1: str, word2: str) -> bool:
  """function to detect if 2 words are anagrams (An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.)"""
  #sort the letters in the string
  list1 = list(cleanWords(word1))
  list1.sort()

  list2 = list(cleanWords(word2))
  list2.sort()

  if list1 != list2:
    return False
  else:
    return True
  
def checkIsograms(word: str) -> bool:
  """function to detect if 2 words are isograms (A word or phrase in which each letter occurs the same number of times.)"""
  listOfWord = list(cleanWords(word))
  listOfWord.sort()
  
  for i in range(0,len(listOfWord)-1):
    if listOfWord[i] == listOfWord[i+1]:
      return False
    else:
      return True

def checkIsogramsMoure(word: str) -> bool:
  """function to detect if 2 words are isograms (A word or phrase in which each letter occurs the same number of times.)"""
  listOfWord = cleanWords(word)
  
  wordDict = dict()
  for character in listOfWord:
    wordDict[character] = wordDict.get(character,0) + 1

  isogram = True
  values = list(wordDict.values())
  isogramLen = values[0]
  for wordCount in values:
    if wordCount != isogramLen:
      isogram = False
      break
  
  return isogram


def checkWords(word1: str, word2: str) -> str:
  """check 2 words if they are: palindromes, anagrams or/and isograms"""
  print(f"{word1} and {word2} Palindormes: ", checkPalindromes(word1, word2))
  print(f"{word1} and {word2} Anagrams: ", checkAnagrams(word1,word2))
  print(f"Isograms: {word1}: {checkIsograms(word1)}, {word2}: {checkIsograms(word2)}") 

checkWords("ratoN", "notar")
checkWords("camAc", "cAmÁc")
checkWords("diálogo", "cÄmero")
checkWords("Diálogo", "caMero")


