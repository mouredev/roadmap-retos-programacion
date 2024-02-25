# OPERACIONES CON CADENAS DE CARACTERES

# 1. Asignacion
saludo = "Hola, "
nombre = "Nico"

# 2. Concatenacion
sal = saludo + nombre
print(f'{sal}\n')

# 3. Operaciones "aritmeticas"
saludoTotal = saludo*3
print(f'{saludoTotal}\n')

# 4. Operaciones de partcion (Subcadena)
secuencia = "123456789"
primerCorte = secuencia[0:2:1] # Se toma -> 12
segundoCorte = secuencia[::2] # Se toma -> 13579
tercerCorte = secuencia[::3] # Se toma -> 147 
cuartoCorte = secuencia[::] #Se toma toda la cadena
print(primerCorte)
print(segundoCorte)
print(tercerCorte)
print(f'{cuartoCorte}\n')

# 5. Acceso a caracteres
caracter1 = sal[0]
caracter2 = sal[4]
print(caracter1)
print(f'{caracter2}\n')

# 6. Longitud
longitudString = len(sal)
print(f'La longitud de la cadena "{sal}" es de {longitudString}\n') # Interpolacion utilizando f-string y {}

# 7. Recorrido
for i in range(longitudString):
    print(sal[i])

# 8. Mayusculas y Minusculas
salMayus = sal.upper()
print(f'\n{salMayus}')
salMinus = sal.lower()
print(f'{salMinus}\n')

# 9. Reemplazo
salReplace = sal
print(f'Palabra Original -> {salReplace}') # Interpolacion utilizando f-string y {}
salReplace = salReplace.replace("o", "2") # Reemplaza todas las "o" por un "2"
print(f'Primer reemplazo de letra "0" por un "2" -> {salReplace}') # Interpolacion utilizando f-string y {}
salReplace = salReplace.replace("2", "o", 1) # Reemplaza el primer "2" por una "o"
print(f'Segundo reemplazo, primer "2" por una "o" -> {salReplace}\n') # Interpolacion utilizando f-string y {}

# 10. Divison o Separacion
salDiv = sal
print(f'Palabra Original -> {salDiv}') # Interpolacion utilizando f-string y {}
salDiv = salDiv.split(",") # Separa la cadena por el caracter "," y los deja en una lista
print(f'Separacion = {salDiv}') # Interpolacion utilizando f-string y {}
salDiv = sal + " Me llamo Johan, soy ingeneriero electronico, me gusta el futbol, la programacion y la f1"
print(f'Otra separacion de la siguiente cadena -> {salDiv}') # Interpolacion utilizando f-string y {}
salDiv = salDiv.split(",", 2) # Separa por comas solo las dos primeras comas
print(f'Separacion = {salDiv}\n') # Interpolacion utilizando f-string y {}

# 11. Union
myStringList = ["uno", "dos", "tres", "cuatro"]
print(f'Lista -> {myStringList}') # Interpolacion utilizando f-string y {}
myString = ", ".join(myStringList)
print(f'Lista unida en un string -> {myString}\n') # Interpolacion utilizando f-string y {}

# 12. Verificacion
letra = "a"
print(f"String Base -> {sal}")
if letra in sal:
    print(f"La letra {letra} si esta en {sal}\n")
else:
    print(f"La letra {letra} no esta en {sal}\n")


# DIFICULTAD EXTRA
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()

    numeros = ["0","1","2","3","4","5","6","7","8","9"]

    try:
        for index in numeros:
            if index in palabra:
                raise ValueError("Por favor ingresa una palabra, por lo menos hay un numero dentro de ella") 
        return palabra == palabra[::-1]
    
    except ValueError as ve:
        print(ve)
        return False
    

def anagrama(palabra1, palabra2):
    palabra1 = palabra1.replace(' ', '')
    palabra1 = palabra1.lower()
    palabra2 = palabra2.replace(' ', '')
    palabra2 = palabra2.lower()

    palabra1 = sorted(palabra1)
    palabra2 = sorted(palabra2)

    return palabra1 == palabra2


def isograma(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    setLetras = set()

    for letra in palabra:
        if letra in setLetras:
            print(f'Se repite la letra {letra}')
            return False
        else:
            setLetras.add(letra)

    return True


def run():
    palabra1 = input('Ingresa la primer palabra: ')
    palabra2 = input('Ingresa la segunda palabra: ')
    # Seccion Palindromo
    es_palindromo1 = palindromo(palabra1)
    es_palindromo2 = palindromo(palabra2)

    if es_palindromo1:
        print(f'{palabra1}, es palindroma')
    else:
        print(f'{palabra1}, NO es palindroma')
    
    if es_palindromo2:
        print(f'{palabra2}, es palindroma')
    else:
        print(f'{palabra2}, NO es palindroma')

    # Seccion Anagrama
    es_anagrama = anagrama(palabra1, palabra2)
    if es_anagrama:
        print(f'{palabra1} y {palabra2} son anagramas')
    else:
        print(f'{palabra1} y {palabra2} NO son anagramas')

    # Seccion Isograma
    es_isograma1 = isograma(palabra1)
    es_isograma2 = isograma(palabra2)

    if es_isograma1:
        print(f'{palabra1}, si es isograma')
    else:
        print(f'{palabra1}, NO es isograma')
    
    if es_isograma2:
        print(f'{palabra2}, es isograma')
    else:
        print(f'{palabra2}, NO es isograma')


if __name__ == "__main__":
    run()