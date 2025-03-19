''' Ejemplos de operacones con 
Cadenas de caracteres / strings 
'''
a = "Esto es una cadena de caracteres / str. "
print(a)
#esto es lo que seria una cadena de caracteres, string o str
b = """        Esto es string 
        que ocupa 
        varias lineas. """ # string en varias lineas
print(b)
#para imprimir un string en varias lineas lo escribimos en tres comillas
c = """Este esta STR \
        ocupa \
        varias lineas """
print(c)
#podemos poner '\' para que no aparezcan las tres linea y solo aparezcan con tres espacios en una sola linea

"unión"
d = "hola" + "mundo" 
print(d)
#Así podemos unir dos strings pero cuando se imprima salda 'holamundo' todo junto
#para evitar eso escribe "hola" + " mundo" dejando un espacio ya sea en el "hola " o en " mundo"

"acceder a un caracter"
e = "soy thezhizn"
print(e[0])
print(e[3])
print(e[6]) #
print(e[10])
#De esta forma podemos acceder a un caracter especifico
#El primer caracter siempre vale 0 como podemos ver "(e[0])" es el caracter s
#como podemos por con el "(e[3])" los espacios tambien cuentan como caracteres

"subcadenas"
print(e[:3])
print(e[2:7])
print(e[-5:])
#Subcadenas comienzan de izquierda a derecha comenzando desde el caracter 1
#En el medio vamos de izquierda a derecha poniendo el par ordenado en la izquierda donde queremos iniciar y en la derecha donde quiere terminar
#Para el final lo hacemos de derecha a izquierda comenzando desde el -1

"longitud"
f = "¿cuanto mide este STR?"
print(len(f))
#Usamos la funcion "len" "f" mide 22 caracteres, recordando que los espacios tambien se cuentan

"concatenacion"
name = "Migue Santiago"
surname = " Garbanzo Hernan"
print(name + surname)
#Para concatenar Strings es mas comun usar el + 
#los datos podemos sacarlos de variables con inputs
#Recuerda poner espacios en los strings para que no aparecan pegados

"repeticion"
g = "repeticion " 
print(g *2)
h = "hola " *2 
print(h)
#Esta es una forma de repetir funciones de una forma muy simple
#Python no tiene formas mas complejas, de querer hacer cosas mas complejas tienes que hacer tu propia logica en una funcion

"recorrido"
i = "python"
for i in i:
    print(i)
#Para recorrer un String utilizamos el "for" que tambien usamos para el famoso fizz buzz

"conversion"
j = "hola mundo"
print(j.capitalize)
#Este metodo vuelve la primera letra mayuscula
print(j.upper())
#Para convertir de minusculas a mayusculas usamos el metodo .upper
print(j.lower())
#Para convertir de mayusculas a minusculas usamos el metodo .lower
print(j.capitalize())
#Para convertir solo la primera letra en mayuscula usamos el metodo .capitalize
k = "Soy Un Titulo"
print(k.swapcase())
#Este metodo cambia las mayusculas en minusculas y viceversa 
print(k.lower())
print(k.title())
#El metodo .title funciona de de tal forma que crea mayusculas en cada palabra de forma que sea un Titulo
#La funcion hace eso apesar de que usamos en metodo .lower antes

"reemplazar"
l = "yo soy yhechizn"
print(l)
print(l.replace("yhechizn","thezhizn"))
#De esta forma podemos reemplazar un texto especifico en nuesto STR
m = "aaaaaa"
print(m)
print(m.replace("a", "b",3))
#de esta forma podemos reemplazar un numero de veces que queramos 

"dividir"
n = "Maria,Ana,Roger,Sandy,Michael"
print(n.split(","))
#El metodo .split nos dividira nuestro String y nos devolvera una lista con los parametros
#El metodo divide en base en lo que pongamos en medio de las comillas del .split, en este caso una ","

"union"
union_1 = "thezhizn"
union_2 = "zhizn98"
the_union = set(union_1).union(union_2)
print("la union es " + str(the_union))
#esto nos mandara un conjunto/set con las letras que aparecen en los str

"interpolar"

'%d = Integer'
'%f = Float'
'%s = String'
'%x = Hexadecimal'
'%o = Octal'
#cada uno representa que se usara para interpolar cada tipo de dato
o = 16
p = 3.14
q = "thezhizn"
print("La edad de Jose es de %d " % (o))
print("El valor de π creo que es %f" % (p))
print("Mi nombre es %s" % (q))
#De esta forma es la que podemos usar las sintaxis
o = "Maria"
p = 6.5
q = 2000 
r = 5500
print("Ayer vi a {} pasear por el parque" .format(o)) 
print("{} es el resultado de dividor 13 entre 2" .format(p))
print("La suma de {} + 3500 da resultado {}" .format(q,r))
#Tambien podemos interpolar usando el metodo .format 
#En este caso usamos {} para marcar la posicion a interpolar en lugas de los "%d, %s...etc"
print(f"Ayer {o} salio a la tienda")
print(f"la divición de 13 entre 2 es igual a {p}")
print(F"Sumar {q} + 3500 resulta en {r}")
#Este metodo es exclusivo de Python y se le conoce como cadenas formateadas o cadenas f
#al agregar f al principio crea un str interactivo en donde podemos poner variables o logica en la cadena de texto
from string import Template
example_1 = Template("$a + 12 = 18")
example_2 = Template("Hola $name que tal te fue ayer en $city")
print(example_1.substitute({"a" : 6}))
print(example_2.substitute({"name" : "thezhizn", "city" : "Cartago" }))
#Esta forma es la Clase Platilla en donde en el Template usamos "$" para crear una variable
#en el .substitute vamos a crear un diccionario con el nombre de la variable en el template y un valor para la variable

"verificación"
s = "holaa"
t = "holaa"
u = "Holaa"
print(s == t)
print(t == u)
#Asi podemos verificar si dos str son iguales (se toman en cuenta las mayusculas y los espacios)
v = "hola"
w = "hola34"
print(v.isalpha())
print(w.isalpha())
#usando el metodo .isalpha podemos verificar con un true y false si los caracteres en el str son solo letras o no
print(k.islower())
#El metodo .islower sirve para saber si todo el texto es todo minisculas y devolvera falso o cierto
print(k.isupper())
#El metodo .islower sirve para saber si todo el texto es todo mayusculas y devolvera falso o cierto
print(w.isdigit())
#sirve para saber si es solo digitos
#hay muchos mas pero son demaciados. solo pon .is al lado de la variable en Python

"DIFICULTAD EXTRA"
def my_extra():
    print("\nBienvenido al programa")
    
    while True:

        print("\n1. palindromos")
        print("2. anagramas")
        print("3. isogramas")
        print("4. salir del programa")
        print("")

        opciones = input("\nseleccione una opcion porfavor ")

        match opciones:
            case "1":
                palabra_1 = input("Bienvenido a Palidromos.\nPor favor ingresa una palabra. ").lower()
                palabra_2 = palabra_1[::-1]
                if palabra_1.isalpha() and palabra_1 == palabra_2:
                    print(f"La palabra {palabra_1} es un Palindromo".upper())
                else:
                    print(f"La palabra {palabra_1} no es un palindromo".upper())
            case "2":
                print("Bienvenido a anagramas.\nPorfavor incerte las palabras que quieras comparar. ")
                palabra_1 = input("Palabra 1. ")
                palabra_2 = input("Palabra 2. ")
                if (sorted(palabra_1) == sorted(palabra_2)):
                    print(f"Las palabras {palabra_1} y {palabra_2} son anagramas")
                else:
                    print(f"Las palabras {palabra_1} y {palabra_2} no son anagramas")
            case "3":
                palabra_1 = input("Bienvenido a isogramas.\nInserta la palabra que quieres probar. ")
                lista = list(palabra_1)
                conjunto = set(lista)
                if len(lista) == len(conjunto):
                    print(f"La palabra {palabra_1} es un isogramo")
                else:
                    print(f"La palabra {palabra_1} no es un isogramo")
            case "4":
                print("Saliendo del sistema")
                break
            case _:
                print("por favor seleciona una opcion valida")
my_extra()    
