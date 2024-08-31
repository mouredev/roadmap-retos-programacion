'''
EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):

 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
 *   conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
'''

my_string = "  I wanna be a full stack developer  "

# Acceso al caracter en el indice 2:
print(my_string[2])
# Subcadena
sub_string = my_string[2:9]
print(sub_string)
# Longitud
print(len(my_string))
# Concatenación
string_result = my_string + sub_string
print(string_result)
# Búsqueda de ocurrencias
## Dime cuantas veces se repite el caracter "a" dentro del string sin usar ningún método
character = "a"
num = 0
for i in my_string:
    if character == i:
        num += 1
print(f"En nuestro string [{character}] aparece un total de: {num} veces")

## Ahora puedes usar métodos
print(my_string.count("a"))
# Conversión
string_upper = my_string.upper()
print(string_upper)
# Reemplazo
print(my_string.replace("a","A"))
# Multiplicación de caracteres
print(my_string[2].upper() * 3)
#División
print(my_string.split())
# Eliminación de espacios al principio y al final
print(my_string.strip())
# Búsqueda al principio y al final
print(my_string.startswith("  I"))
print(my_string.endswith("  "))
# Búsqueda de posición
print(my_string.find("w"))
# Formateo 
print("{} --> era mi string inicial. {} \n --> es mi string concatenado".format(my_string.strip(),string_result.strip()))
# Interpolación
print(f"En nuestro string [{character}] aparece un total de: {num} veces")
# Cambio de dato a lista
my_list = list(my_string)
print(my_list)
# Comprobaciones varias
s4 = "123456"
print(s4.isalnum())
print(s4.isalpha())
print(s4.isnumeric())


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
"""

def son_palindromos(str1:str,str2:str)->bool:
    print(f"¿Es {str1} palindroma con ella misma? {str1 == str1[::-1]}")
    print(f"¿Es {str2} palindroma con ella misma? {str2 == str2[::-1]}")
    return


def son_anagramas(str1:str,str2:str)->bool:
    print(f"Es {str1} anagrama de {str2}: {sorted(str1) == sorted(str2)}")


def son_isogramas(str1:str,str2:str):
        
    def isogram(word:str)->bool:
        # Creo un diccionario vacío para ir agregando el número de veces que se repite cada letra de la palabra
        world_dict= dict() 
        # Recorro cada letra de la palabra
        for letra in word:
            # Agrego al diccionario el total de repeticiones teniendo por defect el valor igual a 0
            world_dict[letra] = world_dict.get(letra,0) + 1
        
        isIsogram = True
        list_values = list(world_dict.values()) # Para trabajar con los indices me quedo con una lista SOLO con los valores del diccionario
        longitud_de_isogram = list_values[0]    # Calculo la longitud de cualquiera de los valores
                                                # Sabemos que para ser isograma todas las letras se tienen que repetir el mismo número de veces
        # Ahora voy a recorrer la lista de el número de repeticiones
        for count_word in list_values:
            if count_word != longitud_de_isogram:
                isIsogram = False
                break
        return isIsogram
    

    print(f"Es {str1} un isograma?: {isogram(str1)}")
    print(f"Es {str2} un isograma?: {isogram(str2)}")


# Ejemplos! 
son_palindromos("pera","radar")
son_anagramas("roma","amor")
son_isogramas("pera","radarmou")