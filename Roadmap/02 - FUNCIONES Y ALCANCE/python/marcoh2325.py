"""En python se puede escoger que retorna una función. En caso de no indicar que se retorna
('return <objeto a retornar>') al final del flujo de ejecución de una función se retorna None"""

# Ejemplo función sin parametros ni retorno
print("Ejemplo función sin parametros ni retorno")
def print_hola():
    print("Hola!")

print_hola()
print()

# Ejemplo función sin parametros con retorno
print("Ejemplo función sin parametros con retorno")
def get_adios():
    return "Adios!" #En este caso se retorna el string "Adios!"

print(get_adios())
print()

# Si un parametro tiene un valor por defecto nos referiremos en este fichero a dicho
# parametro como parametro opcional. Pues es opcional es pasarse el argumento
# correspondiente a dicho parametro al llamar a la función
# Si un parametro no tiene valor por defecto nos referiremos en este fichero a dicho
# parametro como parametro obligatorio. Pues es necesario pasar el argumento correspondiente
# a dicho parametro siempre que se llame a la función

# Ejemplo función con un número finito de parametros (en este caso 2) y sin retorno
print("Ejemplo función con un número finito de parametros (en este caso 2) y sin retorno")
def add_two_numbers(n_1, n_2):
    print(n_1 + n_2)

# A la hora de llamar a la función, pasar los argumentos es obligatorio, pues los parametros
# no tienen un valor por defecto y el resultado de las operaciones que lleva a cabo la función
# no se podría determinar (TypeError)
add_two_numbers(14, 15)
print()

# Ejemplo función con un número finito de parametros (en este caso 3) y con retorno
def add_three_numbers(n_1, n_2, n_3):
    return(n_1 + n_2 + n_3)

print(add_three_numbers(14, 15, 16))
print(add_three_numbers(14, n_3 = 16, n_2 = 15))
print()

# Notar que hasta este punto en todas las funciones se tiene que indicar el valor de los 
# los argumentos en el momento en el que se llamen. Además los valores que toman los argumentos
# depende del orden en el que se llamen estos
# por ejemplo en la función add_two_numbers(14, 15) -> n_1 = 14 y n_2 = 15 en cambio
# add_two_numbers(15, 14) -> n_1 = 15 y n_2 = 14
# Este orden sin embargo se puede modificar indicando el nombre del parametro al cúal queremos que se
# asigne el valor. Por ejemplo: calculate_sum(14, n_3 = 16, n_2 = 15)
"""Regla sintactica de Python : A la hora de llamar a una función los argumentos con unicamente valor (<valor>) no pueden ir a la
derecha de argumentos con nombre y valor (<nombre>=<valor>). Por ejemplo: calculate_sum(n_3 = 15, 14, n_1 = 15) es incorrecto """

# Ejemplo de función con un número finito de parametros en el cúal algunos o todos los parametros
# tiene un valor por defecto

"""Regla sintactica de Python: Un parametro sin valor por defecto (obligatorio) no puede ir a la derecha
de un parametro con valor por defecto (opcional) al definir una función
Por ejemplo: def print_fav_animal(animal = "Gato", sonido) es incorrecto """
print("""Ejemplo de función con un número finito de parametros en el cúal algunos o todos los parametros
tiene un valor por defecto""")
def print_fav_animal(sonido, animal = "Perro"):
    print(f"Tu animal favorito '{animal}' dice {sonido}")

# En este caso, Proporcionar el argumento correspondiente al/los parametro/s
# con valor por defecto al llamar a la función es opcional
print_fav_animal("Guau")
print_fav_animal("Guau", "Ardilla")
print_fav_animal(animal= "Vaca", sonido = "Muuuuh")
print()

# Para evitar alargar demasiado este fichero, se sobreentenderá que para 
# el resto de combinaciones se puede o no indicar un objeto a retornar 
# en cada una de las siguientes funciones de ejemplo

# Ejemplo de función utilizando el parametro especial *<nombre parametro>

# Este parametro que normalmente se nombra *args, permite pasar tantos argumentos
# (con únicamente valor ) como se desee a la hora de llamar a la función.
print("Ejemplo de función utilizando el parametro especial *<nombre parametro>")
def add_numbers(*args):
    total = 0
    #args es una tupla que contiene todos los argumentos que se han pasado
    for n in args:
        total += n
    print(total)

add_numbers(2, 5, 5, 6, 10, 17)

# Ejemplo de función utilizando un número finito de parametros además del 
# parametro especial *<nombre parametro>
print("""Ejemplos de función utilizando un número finito de parametros además del 
parametro especial *<nombre parametro>""")
def concat_2_or_more(n_1, n_2, *args):
    full_concat = str(n_1) + str(n_2)
    for n in args:
        full_concat += str(n)
    print(full_concat)
    
concat_2_or_more(5, 0, 0, 0, 5)

# En la definición el parametro *<nombre parametro> puede ir en cualquier posición, sin embargo
# si no va el final (a la derecha del todo), a la hora de llamar a la función
# será necesario indicar por su nombre de los argumentos obligatorios
# Ejemplo:
def concat_2_or_more(n_1, *args, n_2):
    full_concat = str(n_1) + str(n_2)
    for n in args:
        full_concat += str(n)
    print(full_concat)
    
concat_2_or_more(5, 0, 0, 0, n_2 = 5)
# Ejemplo con retorno
def concat_2_or_more(*args, n_1, n_2):
    full_concat = str(n_1) + str(n_2)
    for n in args:
        full_concat += str(n)
    return full_concat
print(concat_2_or_more(3, 2, 1, n_1 = 5, n_2 = 4))
print()

# Ejemplo función con algunos parametros con valor por defecto y usando el parametro
# especial *<nombre parametro>
print("""Ejemplo función con algunos parametros con valor por defecto y usando el parametro
especial *<nombre parametro>""")
from random import choice
# El parametro especial *<nombre parametro> puede estar en cualquier posición
def who_washes_the_dishes(*args, host="Marco"):
    people = list(args)
    people.append(host)
    print("El que lava los platos es: ", choice(people))

who_washes_the_dishes("Juan", "Mateo", "Pedro", host="Horacio")

# Ejemplo con retorno:
def make_team(first_member="Steve Rodgers", *args):
    team = list(args)
    team.append(first_member)
    print("El primer integrante es: ", first_member)
    return team
print(make_team("Clark Kent", "Bruce Wayne"))

# Ejemplos de funciones con parametros finitos, teniendo alguno de estos
# valor por defecto y utilizando el parametro especial *<nombre parametro>
print("""Ejemplos de funciones con parametros finitos, teniendo alguno de estos
valor por defecto y utilizando el parametro especial *<nombre parametro>""")
def show_car(price, n_wheels = 4, *extra_features):
    print("Precio:", price)
    print("Número de ruedas: ", n_wheels)
    print("Otras características: ", extra_features)

# Utilizando lo visto anteriormente acerca del orden: los parametros con valores
# por defecto deben ir después de todos los parametros obligatorios, el parametro especial
# *<nombre parametro> puede ir en cualquier posición en este caso.
# Puede ser mejor declarar los parametros con valor por defecto después de *<nombre parametro>
# para así poder aprovechar el valor por defecto, en caso contrario
# el primer argumento pasado en la llamada a la función después de los obligatorios
# corresponderá al parametro con valor por defecto y no a *<nombre parametro>
# Ejemplo en este caso no podríamos aprovechar el valor por defecto de n_wheels
# porque si no indicamos un valor para este argumento (en este caso 6), el valor "electrico" corresponderá a
# n_wheels
show_car(10000, 6, "electrico", "color rojo", "año 2022")

#Ejemplo con retorno y con orden conveniente para aprovechar las características de los parametros
def show_car_2(price, *extra_features, n_wheels = 4):
    print("Precio:", price)
    print("Número de ruedas: ", n_wheels)
    print("Otras características: ", extra_features)
show_car_2(9000, "diesel", "color blanco", "año 2019")
show_car_2(12000, "diesel", "color amarillo", "año 2021", n_wheels = 8)
print()

# Ejemplo: Uso del parametro especial **<nombre parametro>
# Este parametro permite pasar como argumentos tantos objetos como se desee
# y además especificar los nombres con los que se hará referencia a dichos objetos
print("Ejemplo: Uso del parametro especial **<nombre parametro>")
def print_grocery_list(**kargs):
    #kargs es diccionario, cuyas claves son los nombres de los argumentos y los valores, los valores de estos 
    for k, v in kargs.items():
        print(f"{v} {k}")

print_grocery_list(Melon=1, Patatas=6, Lentejas_1kg=1)
# El uso del parametro **<nombre parametro> es opcional a la hora de llamar la función

# Ejemplo: Uso del parametro especial **<nombre parametro> y parametros obligatorios
print("""Ejemplo: Uso del parametro especial **<nombre parametro> y parametros obligatorios""")
# En este caso el único orden posible para los parametros en la definición es con **<nombre parametro> al final
def get_supermarket_codes(supermarket_name, **kargs):
    print("Nombre supermercado: ", supermarket_name)
    for k, v in kargs.items():
        print(f"{k}: {v}")
get_supermarket_codes("El badulaque", S990 = "Guindillas", S130= "Patatas fritas", S220= "Boleto loteria")
print()

# Ejemplo: Uso del parametro especial **<nombre parametro> y parametros opcionales
print("""Ejemplo: Uso del parametro especial **<nombre parametro> y parametros opcionales""")
# En este caso el único orden posible para los parametros en la definición es con **<nombre parametro> al final
def get_supermarket_codes_2(supermarket_name = "Agora", **kargs):
    """Muestra el nombre de un supermercado y la clave y nombre de algunos productos de este"""
    print("Nombre supermercado: ", supermarket_name)
    for k, v in kargs.items():
        print(f"{k}: {v}")
get_supermarket_codes_2(Y54 = "Pizza 4 quesos", AP7= "Helado", N64= "Cebollas")
"""Regla de sintaxis de Python: Cuando se usa **<nombre parametro> en una función. A la hora
de llamarla se podrá etiquetar los valores con cualquier nombre (los argumentos que hacen referencia
a **<nombre parametro>). Excepto los de los parametros obligatorios o opcionales, ya que estos
nombres siempre harán referencia los parametros con el mismo nombre"""
"""Regla: **<nombre parametro> tiene que ir siempre al final en la definición de la función en caso de usarse"""
# En este caso esto significaría que supermarket_name = "El badulaque" hace referencia al parametro supermarket_name
# y no **kargs
get_supermarket_codes_2(Y54 = "Pizza 4 quesos", AP7= "Helado", N64= "Cebollas", supermarket_name = "El badulaque")
print()

# Ejemplo de función utiliando el parametro especial **<nombre parametro>, parametros obligatorios
# y opcionales
# En este caso **<nombre parametro> no puede ser el primer parametro en la definición
# porque como se menciono anteriormente tanto los parametros obligatorios o opcionales
# tienen que ir antes que **<nombre parametro>
# Unico orden posible para este caso:
# (<parametros obligatorios>, <parametros opcionales>, **<nombre parametro>)
# Ejemplo de caso sin retorno
print("""Ejemplo de función utiliando el parametro especial **<nombre parametro>, parametros obligatorios
y opcionales""")
def show_dictionary(dictionary_name, language = "Español", **dictionary):
    print(dictionary_name)
    print("Lenguaje: ", language)
    for k, v in dictionary.items():
        print(f"{k}: {v} ")

# A la hora de llamar a la función el argumento que corresponde al parametro obligatorio como
# ya se ha mencionado puede ocupar cualquier posición siempre y cuando se mencione junto al valor el
# parametro al cúal hace referencia (ejemplo: dictionary_name="Diccionario de la RAE"). 
show_dictionary("Diccionario de la lengua Española", manzana="fruta roja", coche= "vehiculo de 4 ruedas")
show_dictionary(banana="fruit of color yellow", language = "English", dictionary_name = "English dictionary",
                 mathematician= "machine that transforms coffee into mathematics")
print()

# Ejemplo de función utilizando los parametros especiales **<nombre parametro> y *<nombre parametro>
# Unico orden posible
# (*<nombre parametro>, **<nombre parametro>)
print("Ejemplo de función utilizando los parametros especiales **<nombre parametro> y *<nombre parametro>")
def get_translation(*words, **translator):
    """Traduce una lista de palabras a partir de un diccionario cuyas
    claves son las palabras en el idioma de origen y los valores su traducción
    en el idioma objetivo"""
    print("El resultado de la traducción es: ")
    for word in words:
        if(word in translator.keys()):
            print(word, ":", translator[word])
        else:
            print(f"La traducción de {word} se desconoce")

# Al llamar a la función no hay forma de hacer referencia al parametro *<nombre parametro> indicando
# el nombre. Unicamente se puede entonces pasar los valores de los argumentos que se asignaran a *<nombre parametro>
# A la hora de llamar a la función el único orden posible es:
# (<argumentos *<nombre parametros>, <argumentos **nombre parametro>)
get_translation( "hola", "manzana", "car", "words", hola="hello", cebolla="onion", manzana="apple", words="palabras")
print()
# Notar que se puede utilizar el nombre del parametro especial *words, 
# como una de las etiquetas de los pares <nombre>=<valor> que se asignarán a **translator

# Ejemplo de función utilizando los parametros especiales *<nombre parametro>, **<nombre parametro>
# además de parametros obligatorios

def get_letter_encrypted(alphabet, key, c):
    """Dado un carácter retorna el caracter encriptado
    utilizando cifrado cesar"""
    base_i = 0
    found = False
    if (c not in alphabet): #Si el carácter no esta en el alfabeto no se modifica
        return c
    while ((base_i < len(alphabet)) and (not found)): #Si se llega a este punto
        # realmente la condición base_i < len(alphabet) no es necesaria porque
        # ya se sabe que el carácter esta en el alfabeto
        if(c == alphabet[base_i]):
            found = True
        else: 
            base_i += 1
    final_i = (base_i + key) % len(alphabet) # Se obtiene el nuevo índice

    return alphabet[final_i]

print("""Ejemplo de función utilizando los parametros especiales *<nombre parametro>, **<nombre parametro>
# además de parametros obligatorios""")
# En este caso el parametro **<nombre parametro> siempre tiene que ir al final
# El orden de los parametros obligatorios y *<nombre parametro> pueden estar en cualquier posición
# siempre **<nombre parametro> este al final.

# El sustituir números por letras puede dar problemas a la hora de desencriptar el mensaje si el
# mensaje original contiene números también. Se ignoro esta posibilidad
# al únicamente haberse creado esta función como ejemplo
def get_encrypted_messages(key: int, *input_messages, **extra_cypher):
    """Cifra mensajes utilizando el cifrado Cesar y retorna el resultado
    key: clave del cifrado
    input_messages: mensajes que se quieren codificar
    extra_cypher: sustituye ciertas letras por números
    retorna los mensajes cifrados"""
    from string import ascii_lowercase
    encrypted_messages = []
    for message in input_messages:
        encrypted_message = ""       
        # Process
        for c in message:
            c_encrypted = get_letter_encrypted(ascii_lowercase, key, c.lower())
            # notar que porque como el alfabeto y el caracter estan en mayúscula
            # c_encrypted siempre estará en minúscula
            if ((c_encrypted in extra_cypher.keys())):
                c_encrypted = str(extra_cypher[c_encrypted])
            elif (c_encrypted.upper() in extra_cypher.keys()):
                c_encrypted = str(extra_cypher[c_encrypted.upper()])

            encrypted_message += c_encrypted

        encrypted_messages.append(encrypted_message)
    return encrypted_messages

encrypted_messages = get_encrypted_messages(0, "Hola mundo!", "Come verduras!", i=1, o=0)
print(encrypted_messages)
encrypted_messages = get_encrypted_messages(29, "Hipopotamo", "Rinoceronte", a=4,e=3, i=2, o=1, u=0)
print(encrypted_messages)
encrypted_messages = get_encrypted_messages(a=4,e=3, i=2, o=1, u=0, key=29)
print(encrypted_messages)
print()

# Ejemplo de función utilizando los parametros especiales *<nombre parametro>, **<nombre parametro>
# además de parametros opcionales
print ("""Ejemplo de función utilizando los parametros especiales *<nombre parametro>, **<nombre parametro>
además de parametros opcionales""")
# el parametro **<nombre parametro> tiene que ir siempre al final
# los parametros opcionales o *<nombre parametro> pueden ocupar cualquier otra posición
def get_encrypted_messages_2(*input_messages, key: int = 29, **extra_cypher): #en este caso key tiene valor por defecto
    """Cifra mensajes utilizando el cifrado Cesar y retorna el resultado
    key: clave del cifrado
    input_messages: mensajes que se quieren codificar
    cypher: sustituye ciertas letras por números
    retorna los mensajes cifrados"""
    from string import ascii_lowercase
    encrypted_messages = []
    for message in input_messages:
        encrypted_message = ""       
        # Process
        for c in message:
            c_encrypted = get_letter_encrypted(ascii_lowercase, key, c.lower())
            if (c_encrypted.lower() in extra_cypher.keys()):
                c_encrypted = str(extra_cypher[c_encrypted])
            encrypted_message += c_encrypted
        encrypted_messages.append(encrypted_message)
    return encrypted_messages

encrypted_messages = get_encrypted_messages_2("Hola mundo!", "Come verduras!", i=1, key=0, o=0)
print(encrypted_messages)
encrypted_messages = get_encrypted_messages_2("Hipopotamo", "Rinoceronte", a=4,e=3, i=2, o=1, u=0)
print(encrypted_messages)
encrypted_messages = get_encrypted_messages_2(a=4,e=3, i=2, o=1, u=0, key=29)
print(encrypted_messages)
print()

# Ejemplo de función utilizando los parametros especiales *<nombre parametro>, **<nombre parametro>
# además de parametros obligatorios y opcionales
print("""Ejemplo de función utilizando los parametros especiales *<nombre parametro>, **<nombre parametro> 
además de parametros obligatorios y opcionales""")
def print_info_developer(name, *fav_languages, age = 30, **lang_time):
    """Función que imprime por pantalla el nombre, edad, lenguages de programación
    favoritos, y el tiempo que se le ha dedicado a cada lenguage.
    argumentos:
    name: nombre del desarrollador
    age: edad del desarrollador
    fav_languages: lenguajes favoritos del desarrollador
    lang_time: nombres del lenguaje de programación y el tiempo (en años) que se le ha dedicado"""
    print("Nombre:", name)
    print("Edad: ", age)
    print("Lenguages favoritos: ", fav_languages)
    for lang, time in lang_time.items():
        print(f"{time} año/s trabajando con {lang}")

print_info_developer("Grigori", "C", "Ruby", age = 50, C= 10, Ruby=3, R=4, Python= 1)
print()

print("Prueba funciones dentro de funciones")
# Prueba funciones dentro de funciones:
def say_goodbye():
    def put_exclamation_mark(str_1):
        return str_1 + "!"
    print(put_exclamation_mark("Goodbye"))

say_goodbye()
# Si se puede definir una función dentro de otra
print()

# Ejemplo de función ya creada en el lenguaje:
# La función sum que suma todos los elementos de un iterable
# siempre y cuando estos sean int, boolean, float o complex
print("Ejemplo de función ya presente en el lenguaje")
total = sum(range(1,101))
total = sum([3 + 4j, True])
print(total)
print()

# Variables locales y globales en python
# La diferencia entre una variable local y una global radica en el alcance (scope)
# Una variable local solo esta definida dentro de una función, método o clase
# mientras que el alcance de una variable global abarca desde la línea en la que se
# definió hasta el final del programa


print("Primer ejemplo uso variables locales y globales")
factor = 30
print(f"Valor: {factor}, id: {id(factor)}") # Con el identificador del objeto podemos ver
#si el objeto es el mismo

def get_double(n):
    """Observación: Dada una variable global de llamada <v>.
    Si dentro de una función se realiza una asignación a una variable
    con el mismo nombre y antes no se ha declarado que se hará referencia
    a la variable global <v> (global <v>). La variable global <v> deja de estar
    definida en la función y desde ese momento se crea una variable local
    con el mismo nombre."""
    # Luego si se trata de imprimir factor en este caso incluso antes de la asignación
    # se producirá un error
    # print(f"Valor: {factor}, id: {id(factor)}") # produce un error por lo mencionado antes
    """Observación: Si dentro de la función no se realiza ninguna asignación a una variable
    llamada <v>, <v> hará referencia a la variable global <v>"""    
    factor = 2 #variable local a la que se le asigna el 2
    """Observación: Si dada una variable global <nombre variable global> se realiza una asignación dentro de una función
    a una variable con el mismo nombre (<nombre variable global>) antes de declarar 'global <nombre variable global>'
    ya no se podrá utilizar 'global <nombre variable global>' en el resto de la función a partir de esa asignación.
    En la función, <nombre variable global> hará referencia a una variable local y no a la variable global del mismo nombre."""
    # global factor # Esta declaración es incorrecta a partir de la asignación de factor
    print(f"Valor: {factor}, id: {id(factor)}") # id distinto al de la variable global
    print(factor)
    return factor * n

print(get_double(10))
print(f"Valor: {factor}, id: {id(factor)}") # id distinto al del objeto asignado a la variable local en la función

"""Si se quiere modificar el valor de una variable global dentro de una función
se debe utilizar la palabra clave 'global'
si se hace una asignación a una variable con el mismo nombre de la variable global
sin utilizar la palabra 'global' python creara una variable local con el mismo nombre que la
variable global y no modificará la variable global"""
#Ejemplo
print("Segundo ejemplo uso variables locales y globales")
factor = 30
print(f"Valor: {factor}, id: {id(factor)}")

def get_double_2(n):
    global factor #primero se tiene que hacer la declaración 'global'
    print(f"Valor: {factor}, id: {id(factor)}") #mismo id que variable global
    factor= 2
    print(f"Valor: {factor}, id: {id(factor)}") #nuevo id por la asignación de nuevo objeto
    return factor * n


get_double_2(10)
print(f"Valor: {factor}, id: {id(factor)}") #mismo id que en la última asignación (factor = 2)

# DIFICULTAD EXTRA
print("Ejercicio de dificultad extra")
def special_n_list(str_1, str_2):
    count = 0
    for n in range(1, 101):
        if((n % 3 == 0) and (n % 5 == 0)):
            print (str_1 + str_2)
        elif(n % 3 == 0):
            print (str_1)
        elif(n % 5 == 0):
            print (str_2)
        else:
            print(n)
            count += 1
    return count

count = special_n_list("fizz", "buzz")
print("El número de veces que no se han imprimido numeros es: ", count)
