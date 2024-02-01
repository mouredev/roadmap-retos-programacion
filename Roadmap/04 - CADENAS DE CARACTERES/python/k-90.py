### Cadena de caracteres

name = "Enrique"
surname = "Castro"

### Concatenación
name_complete = name + " " + surname
print(name_complete)

### Repetición 

print(name * 3)

### Longitud
 
print(len(name))

### Indexación

print(surname[0]+surname[1]+surname[2]+surname[3]+ surname[4]+ surname[5])

### Busqueda

print("e" in name)
print("a" in surname)

### Division

print(name.split("r"))

### Slicing

print(name[2:4])
print(name[::2])
print(name[2:])

### Reemplazo

print(surname.replace("s","r" ))

### Mayusculas

print(name.upper())
print(surname.capitalize())
print(surname.title())
print(name.lower())

### Strip --> Elimina espacios al principio al final de un string

r1 = "Mi Lenguaje favorito es Python"
print(r1.strip())

### Busqueda en principio y final

print(r1.startswith("Mi"))
print(r1.startswith("El"))
print(r1.endswith("Python"))
print(r1.endswith("python"))

### Busqueda de ocurrencias

print(r1.lower().count("e"))

### Transformación en lista

print(list(r1))

### Interpolación

print(f"Hola {name}, ¿Cuál es tu apellido?. Es {surname}")

### Busqueda de posición

print(r1.find("Python"))
print(r1.find("len"))

### Formateo

print("Nombre: {} Apellido: {}".format(name,surname))

### Transformaciones númericas

n1 = "1234567"
n1 = int(n1)
print(n1)

### Transformación de lista en cadena

s1 = [name, " ", surname]
print("".join(s1))

### Extra

def find_out(word1:str, word2:str):
    ### Anagrama
    print(f"{word1} es anagrama de {word2}? {sorted(word1) == sorted(word2)}")
    
    ### Palíndromo 

    print(f"{word1} es palindromo?{word1 == word1[::-1]}")
    print(f"{word2} es palindromo?{word2 == word2[::-1]}")

    ### Isograma

    def isIsogram(word:str) -> bool:
        word_dict = dict()
        for char in word:
            word_dict[char] = word_dict.get(char, 0) + 1
        
        isograma = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isograma = False
                break
        return isograma
    
    print(f"{word1} es isograma?: {isIsogram(word1)}")
    print(f"{word2} es isograma?: {isIsogram(word2)}")
    
        
find_out("amor", "radar")









