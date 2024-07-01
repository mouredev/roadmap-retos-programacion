"""
EJERCICIO: #01 OPERADORES Y ESTRUCTURAS DE CONTROL

- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
  que representen todos los tipos de estructuras de control que existan
  en tu lenguaje:
  Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

 DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
"""

# 1. Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)

"""
Variables para los ejemlos:
"""

X = 5
Y = 4
Z = 2

print(f"Valor de las variables para los ejemplos X = {X}, Y = {Y}, Z = {Z}")
print(f"Valores negativos -X = {-X}, -Y = {-Y}, -Z = {-Z}")

"""
Tipos de operadores Aritméticos: "+, -, /, //, %, *, **" 
Se usan para ejecutar operaciones matematicas simples con datos o variables devueven integers o floats.
"""

suma = X + Y
print(f"La suma total entre {X} + {Y} = {suma}")
# La suma se usa con el signo "+" realiza una suma en este caso entre la variable X y Y.
# devuelve un valor de tipo integer(entero) si los valores sumados son integer(entero) y floats(decimales) si son floats(decimales). 

resta = X - Y
print(f"La diferencia entre {X} - {Y} = {resta}")
# La resta se una con el signo "-" realiza una resta en este caso la diferencia entre X y Y.
# devuelve un valor de tipo integer(entero) si los valores sumados son integer(entero) y floats(decimales) si son floats(decimales).

multiplicación = Y * Z
print(f"El producto resultado de {Y} * {Z} = {multiplicación}")
# La multiplicación se usa con el signo "*" realiza una multiplicación en este caso da el producto de Z y Y.
# devuelve un valor de tipo integer(entero) si los valores sumados son integer(entero) y floats(decimales) si son floats(decimales). 

división = Y / Z
print(f"El cociente de {Y} / {Z} es {división}")
# la división se usa con el signo "/"  realiza una división en este caso da el cociente de Y entre Z.
# devuelve un valor de tipo float(decimal) aunque los valores sean integers(enteros) se le agregara .0 al final.

resto_ent = X % Z 
print(f"El resto de la división entera {X} / {Z} = {resto_ent}")
# La opración de signo "%" devuelve un resto de una división entera en este caso X y Z.
# devuelve un valor de tipo integer(entero) si los valores sumados son integer(entero) y floats(decimales) si son floats(decimales).

potencia = Y ** Z
print(f"La potencia que resulta de elevar {Y} al exponente {Z} = {potencia}" )
# La potecia se usa con los signos "**" en este caso eleva la base Y a la potencia Z.
# devuelve un valor de tipo integer(entero) si los valores sumados son integer(entero) y floats(decimales) si son floats(decimales). 

división_ent = X // Z
print(f"El cociente entero de {X} // {Z} es = {división_ent}")
# la operación de signo "//" hace una división en este caso Y entre Z.
# devuelve un valor de tipo integer(entero).

"""
Tipos de operadores Lógicos: "and = &; or = ||; not = !"
se usan de manera que realacionan un valor booleano(True o False) con otro booleano(True o Falso)
y devuelven otro valor booleano(True o Falso) que depende del operador.
"""

# Ejemplo con el operador logico "And".
print(f"Si True and True = {True and True}, Si True and False = {True and False} y Si False and False = {False and False}")
print(f"Si True and True = {True & True}, Si True and False = {True & False} y Si False and False = {False & False}")
# El operador "and" necesita que ambos valores relacionados sean verdaderos(True) para devolver verdadero(True).

# Ejemplo con el operador logico "Or"
print(f"Si True or True = {True or True}, Si True or False = {True or False} y Si False or False = {False or False}")
print(f"Si True or True = {True | True}, Si True or False = {True | False} y Si False or False = {False | False}")
# El operador "or" necesita que uno de los valores relacionados sea verdadero(True) para devolver verdadero(True).

# Ejemplo con el operador logico "Not"
print(f"Si not True = {not True}, Si not False = {not False}")
# El operador "not" necesita que el valor sea falso(false) para devolver verdadero(true).

"""
Tipos de operadores de comparación: "==(igualdad), !=(diferente), <(menor que), >(mayor que), <=(menor o igual que), >=(mayor o igual que)"
conparan todos los tipos de datos primitivos con otros datos del mismo tipo y devuelven un valor de tipo booleano(True y False).
"""

# Ejemplo con el operador de comparación "igualdad(==)"
print(f"10 == 10 entonces {10 == 10}, si 10 == 5 entonces {10 == 5}") #Ejemplo con Integers
print(f"1.5 == 1.5 entonces {1.5 == 1.5}, si 1.8 == 0 entonces {1.8 == 0}") #Ejemplo con Floats
print(f"Verdadero == Verdadero entonces {'Verdadero' == 'Verdadero'}, si Verdadero == Falso entonces {'Verdadero' == 'Falso'}") #Ejemplo con Strings
print(f"True == True entonces {True == True}, si True == False entonces {True == False}") #Ejemplo con Booleanos
# Si despues de comparar determina ambos valores iguales devuelve un True caso contrario False.

# Ejemplo con el operador de comparación "diferente(!=)"
print(f"10 != 10 entonces {10 != 10}, si 10 != 5 entonces {10 != 5}") #Ejemplo con Integers
print(f"1.5 != 1.5 entonces {1.5 != 1.5}, si 1.8 != 0 entonces {1.8 != 0}") #Ejemplo con Floats
print(f"Verdadero != Verdadero entonces {'Verdadero' != 'Verdadero'}, si Verdadero != Falso entonces {'Verdadero' != 'Falso'}") #Ejemplo con Strings
print(f"True != True entonces {True != True}, si True != False entonces {True != False}") #Ejemplo con Booleanos
# Si despues de comparar determina ambos valores diferentes devuevle un True caso contrario False.

# Ejemplo con el operador de comparación "menor que(<)"
print(f"Si 1 < 2 entonces {1 < 2}, si 2 < 1 entonces {2 < 1}") #Ejemplo con Integers
print(f"Si 1.5 < 2 entonces {1.5 < 2}, si 2 < 1.5 entonces {2 < 1.5}") #Ejemplo con Floats
# Si despues de comparar determina que el primer valor es menor que el segundo entoces devuelve un True caso contrario False.
# Por su naturaleza aritmetica solo trabajo con Integers y Floats no con Strings ni con Booleanos.

# Ejemplo con el operador de comparación "mayor que(>)"
print(f"Si 2 > 1 entonces {2 > 1}, si 1 > 2 entonces {1 > 2}") #Ejemplo con Integers
print(f"Si 2 > 1.5 entonces {2 > 1.5}, si 1.5 > 2 entonces {1.5 > 2}") #Ejemplo con Floats
# Si despues de comparar determina que el primer valor es mayor que el segundo entoces devuelve un True caso contrario False.
# Por su naturaleza aritmetica solo trabajo con Integers y Floats no con Strings ni con Booleanos.

# Ejemplo con el operador de comparación "menor igual que(<=)"
print(f"Si 1 <= 2 entonces {1 <= 2}, si 2 <= 1 entonces {2 <= 1}") #Ejemplo con Integers
print(f"Si 2.5 <= 2.5 entonces {2.5 <= 2.5}, si 4.5 <= 2 entonces {4.5 <= 2}") #Ejemplo con Floats
# Si despues de comparar determina que el primer valor es mayor que el segundo entoces devuelve un True caso contrario False.
# Por su naturaleza aritmetica solo trabajo con Integers y Floats no con Strings ni con Booleanos.

# Ejemplo con el operador de comparación "mayor igual que(>=)"
print(f"Si 2 >= 1 entonces {2 >= 1}, si 1 >= 2 entonces {1 >= 2}") #Ejemplo con Integers
print(f"Si 2 >= 1.5 entonces {2 >= 1.5}, si 1.5 >= 2 entonces {1.5 >= 2}") #Ejemplo con Floats
# Si despues de comparar determina que el primer valor es mayor que el segundo entoces devuelve un True caso contrario False.
# Por su naturaleza aritmetica solo trabajo con Integers y Floats no con Strings ni con Booleanos.

"""
Tipos de operadores de asignación: "=, +=, -=, /=, //=, %=, *=, **="
se usan de forma comun cuando se quiere asginar un valor a una variable
o alterar de forma corta el volar a una variable mediante operaciones
aritmeticas siendo que se pone el signo de la operación aritmetica luego 
el signo de asignación(=) y despues el numero que conduce la operación.
"""

# Operador de asignacion: "="
variable = 2
print(f"definimos el valor de la variable con el signo '=' = {variable}")
# Le asigna un valor a una varible de la misma manera se puede canbiar el valor de la variable.

# Operador de suma y asignacion: "+="
variable += 2
print(f"despues de usar el operador '+=' con el numero 2 el valor queda = {variable}")
# Le suma la cantidad escrita despues de el signo de "+=" y le asgina el resultado a la variable.

# Operador de resta y asignacion: "-="
variable -= 3
print(f"despues de usar el operador '-=' con el numero 3 el valor queda = {variable} ")
# Le resta de la cantidad escrita despues del signo de "-=" y le asina el resultado a la variable.

# Operador de division y asignacion: "/="
variable /= 2
print(f"despues de usar el operador '/=' con el numero 2 el valor queda = {variable}")
# La division del valor sobre la cantidad escrita despues del signo "/=" y le asina el resultado a la variable.

# Operadaor de multipliacion y asignacion: "*="
variable *= 10 
print(f"despues de usar el operador '*=' con el numero 10 el valor queda = {variable}")
# Le multiplica la cantidad escrita despues del signo "*=" y le asigna el resultado a la variable.

# Operador de division entera y asignacion: "//="
variable //= 2
print(f"despues de usar el operador '//=' con el numero 2 el valor queda = {variable}")
# Divide la cantidad del valor sobre la cantidad escrita despues del signo "//=" y asigna el resultado a la variable.
# Si el cociente es un float cambia el valor despues del punto a 0(pero no lo combierte en un int).

# Operador de potenciacion y asignacion: "**="
variable **= 3
print(f"despues de usar el operador '**=' con el numero 3 el valor queda = {variable}")
# Potencia el valor de la variable al numero escrito despues del signo "**=" el resultado se asigna a la variable.

# Operador de resto y asignacion: "%="
variable %= 3
print(f"despues de usar el operador '%=' con el numero 3 el valor queda = {variable}")
# Divide el valor de la variable sobre el numero escrito despues del signo "%=" devievel el resto de haber
# si no devuelve 0 y la asigna a la variable


"""
Tipos de operadores de identidad: "Is , Is not"
Compara si dos variables tienen el mismo valor y devuelve un booleano(True o False)
dependiendo el operador las condiciones son opuestas.
"""
# Variables para los ejemplos

A = 4
B = 4
C = "Ejm"
D = "Ejm"

# Operador de identidad: "Is"
print(f"Si A y B tienen el mismo valor entonces = {A is B}")
print(f"Si B y C tienen no mismo valor entonces = {B is C}")
# Si despues de la comparacion determina que tienen el mismo valor devolvera True caso contrario False.

# Operador de identidad: "Is Not"
print(f"Si A y B tienen el mismo valor entonces = {A is not B}")
print(f"Si B y C tienen no mismo valor entonces = {B is not C}")
# Si despues de la comparacion determina que no tienen el mismo valor devolvera True caso contrario False.

"""
Tipos de operadores de pertenencia: "In, Not In"
Identifica si un valor puede ser econtrado dentro de otro valor estos valores tienen que ser de tipo String 
y devuelve un valor de tipo booleano. (No aceptan un Integer normales)
"""

# Varables para los ejemplos

Ejemplo_1 = "Ej"
Ejemplo_2 = "Ejemplo"

# Operador de pertenencia: "In"
print(f"Si {Ejemplo_1} esta en {Ejemplo_2} = {Ejemplo_1 in Ejemplo_2}") 
print(f"Si {Ejemplo_2} esta en {Ejemplo_1} = {Ejemplo_2 in Ejemplo_1}")
# si la primera cadena de texto esta dentro la segunda devolver True caso contrario devolvera False.

# Operadores de pertenencia: "Not In"
print(f"Si {Ejemplo_2} no esta en {Ejemplo_1} = {Ejemplo_2 not in Ejemplo_1}")
print(f"Si {Ejemplo_1} no esta en {Ejemplo_2} = {Ejemplo_1 not in Ejemplo_2}") 
# Si la primera cadena de texto no esta dentro de la segunda devolvera True caso contrario devolvera False.

"""
Tipos de operadores de bits: "& = and, | = or, ~ = not, << = desplazarce a la derecha, >> = desplazarce a la izquierda"
Cuando se trabajan con  estos operadores se trabaja con numeros, nosostros ingresamos numeros en el sistema decimal
pero se transfoman al sistema binario para ejecutar los operadores y se devuelve el resultado en sistema decimal.
El resutado depende del operador usado pero en la mayoria de casos compara los numeros de las mismas posiciones 
como es sistema binario solo 1 y 0 en las posiciones que no tengan un numero se completaran con 0.
"""

# Podemos transformar del sistema decimal al sistema binario con la funcion bin() cuando se ejecute antes del numero estara 0b
# Esto es una señal que el numero esta en sistema binario.

print(f"En el sistema decimal 10 en sistema binario {bin(10)}")
# 1010
print(f"En el sistema decimal 3 en sistema binario {bin(3)}")
# 11

# Operador de bits: "&"
print(f"10 & 3 = {10 & 3}")
# Como vimos antes 10 = 0b1010 y 3 = 0b11 el resultado de la funcion es 0b10 osea 2.
# El resultado es asi porque al comparar cada numero si en ambas posiciones los numeros tienen 1 el numeor resultante tendra 1 en esa 
# posicion caso contrario sera 0 en la posicion.

# Operador de bits: "|"
print(f"10 | 3 = {10 | 3}")
# Como sabemos 10 = 0b1010 y 3 = 0b11 el resultado de la funcion es 0b1011 osea 11.
# El resultado es asi porque al comparar cada umero si en una de los numeros almenos un 1 ocupa esa posicion devolvera un 1 en caso
# ningun 1 ocupa la posicion devolvera 0.

# Operador de bits: "~"
print(f"~10 = {~10}")
# El comportamineto normal deveria ser el intercambiar los valores del codigo binario correspodiente cada 0 a 1 y 1 a 0.
# Pero en python el resultado es el producto del numero con -1 seguido de restarle 1 al resultado por eso:
# el resutado de esta funcion siendo ingresado el numero 10 es -11

# Operador de bits: "^"
print(f"10 ^ 3 = {10 ^ 3}")
# Como sabemos 10 = 0b1010 y 3 = 0b11 el resultado de la funcion es 0b1001 osea 9
# Devuelve 9 por que despues de comporar cada numero si tiene un 0 y un 1 en la misma posicion devuelve 1 si ambos son 0 o 1
# devuelve 0.

# Operador de bits: ">>"
print(f"3 >> 2 = {3 >> 2}")
# Como sabemos 3 = 0b11 el resultado de la funcion es 0b0 osea 0.
# Es asi porque desplaza los numeros la cantidad de veces espesificado luego del signo ">>" 
# en este caso devuelve 0 porque si despalaza dos digitos como los 3 en binario solo tiene 2 digitos 
# y ambos estan en el extremo derecho la desplazr dos digitos a la derecha y no haber espacio los elimina.

# Operador de bits: "<<"
print(f"10 << 2 = {10 << 2}")
# Como sabemos 10 = 0b1010 el resutado de la funcion es 0b101000 osea 40.
# Es asi porque desplaza los digitos hacia la izquierda al contrario de su operador analogo >> envez de 
# elminar los dumeros que esten al extremo izquierdo agrega 0 al extremo derecho.

"""
Operador walrus: ":=" 
Un operador muy criticado y dificil de utilizar porque se usa para definir una variable dentro de un funcion.
"""

# Ejemplo Operador walrus:
print(k := 2)
# Como se obesarva en la terminal imprime k y k fue definida en la misma funcion print esto puede ser util para
# reducir el numero de lineas de codigo en un funcion pero es criticada porque es dificil de interpretar para el resto de personas.

# 2. Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#    que representen todos los tipos de estructuras de control que existan
#    en tu lenguaje:
#    Condicionales, iterativas, exepciones...

"""
Tipos de estructuras de control
"""

# Variables para los ejemplos:
Ejm_int_1 = 5
Ejm_int_2 = 2
Ejm_string_1 = "str"
Ejm_string_2 = "stg"

# Codicionales:

# Condicional "If":
if Ejm_int_1 == 5 :
    print(f"Ejm_int_1 = {Ejm_int_1}")
# Al usar el condicional If de esta manera definimos una accion que se tiene que realizar en caso la condicion sea True.
# Si la condicion definida no es True no pasara nada, pero si la accion no esta definida devolvera un error de sintaxys
# para evitar eso se puede poner "pass" en la accion y y el codigo compilara de forma normal sin hacer nada cuando se ejecute el condicional.
# Si bien el condicional tiene ese formato definido se puede escribir en una sola liena de ser necesario definiendo la accion seguido de los
# dos puntos y para agregar otra accion separarlas con punto y como sera suficiente. 

# Extension de if "Else"
if Ejm_int_1 == 2 :
    print(f"Ejm_int_1 = {Ejm_int_1}")
else : 
    print(f"Ejm_int-1 no es = {2}")
# AL usar esta extension "else" lagragamos una accion que se ejecutara si el caso definido con if no es True.

# Extension de if "ELif" esto renplaza de cierta manera "Switch" esto no existe en python pero es es util saberlo. 
if Ejm_string_1 == "str" :
    print(f"Ejm_string_1 = {Ejm_string_1}")
elif Ejm_string_1 == "stg" : 
    print(f"Ejm_string_1 = {Ejm_string_2}")
elif Ejm_string_1 == 5 :
    print(f"Ejm_string_1 = {Ejm_int_1}")
elif Ejm_string_1 == 2 :
    print(f"Ejm_string_1 = {2}")
else:
    print("No sabemos")
# Al usar esta extension "elif" conseguimos detallar mas condiocnes esto nos permite detallar tambien acciones diferentes en caso
# se cumplan diferentes condiciones y esta extension puede funcionar de manera igual con else en caso ninguna condicion se cumpla.

# Operador terniario: El operador terniario es otra manera de usar el condicional If:
P = 5
print("es 5" if P == 5 else "no es 5")  
# de esta forma la estructura de la condicional es:
# [codigo si cumple] if [condicion] else [codigo si no cumple]

# Iterativas:

"""
Iterables e Iteradores son conceptos que tenemos que tener claros para usar de forma eficaz las siguientes funciones.

Iterables:
Si usamos la funcion isinstance() podemos saber si la variable es iterable.
Al usar la funcion devuelve True o False para indicar si la variable es iterable.
"""
# print(isinstance("Python", type("Python"))) True
"""
de la siguiente forma podremos saber si un objeto es iterable.

Iteradores:
Si bien sabemos como identificar si una variables es iterable podemos saber su clase de forma que podremos utilizar mejor los iteradores 
que se ajustan a esa clase y sabler cuando un iterador no sera conveniente depedinedo el caso.
Esta forma es usando la funcion iter() dentro va el nombre de la variable.
"""
# print(iter("Python")) str_ascii_iterator object at 0x0000023E90943FD0
"""
Si el uso de la funcion da un error significa que no esta dentro de la lista de clases esta lista incluye: str_iterator para cadenas,
list_iterator para sets, tuple_iterator para tuplas, set_iterator para sets, dict_keyiterator para diccionarios.
"""
# Bucle "For":
for i in "Python":
    print(i)
# En el bucle "For" la i(variable) representa uno de los valores de la varaible interable.
# En este caso toma cada una de las letras de la cadena "Python" y las imprime en una linea cada letra, si pusieras un numero como string
# lo imprime de la misma manera.

# Funcion "Range":
for i in range(5,50,5):
    print(i) # 5 10 15 20 25 30 35 40 45
# Range es una forma de generar una sucesion de numeros por defecto esta enpieza en 0 y salta de 1 hasta el numero definido en el parentesis.
# El orden de los parametros de la funcion es Range([Inicio],[Fin],[Salto])
# El inicio es abierto lo que significa que utilza el numero que se define dentro de la sucesion.
# El fin es cerrado lo que signica que excluye el numero definido dentro de la sucesion.
# Y el salto solo es la diferencia que abra entre los numeros de la sucesion.

# Bucle "While": 
x = 5
while x > 0:
    x -= 1
    print(x) # 4 3 2 1
# importante diferencia
x = 5
while x > 0:
    print(x) # 5 4 3 2 1 
    x -= 1
# El bucle while tambien necestia una variable aqui utilizamos un operador de asignacion para modificar esa variable esta funciona como una condicion que mentras se cumpla
# seguira repitiendo la accion (esto puede generar un error en la ejecucion) Una ejecucion completa del codigo se llama iteracion.

# Else en while:
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")
# Se puede usar el else en while aqui el else se ejecuta cuando la condicion del while se deja de cumplirn osea cuando el bucle se termina.

# Modificadores "Break" y "Continue" : Son modificadores de comportamiento para los bucles se usan de la siguiente manera.

# "Break":
for l in "Break":
    if l == "a":
        print("Econtro la a")
        break
    print(l)
# De esta forma cuando "l" sea igual a "a" el bucle parara pero antes se ejecutara el codigo que lo precede.

# "Continue":
num = 5
while x > 0:
    num -= 1
    if num == 3:
        continue
    print(num)
# De esta forma cuando "num" sea igual a 3  el bucle omitira y pasara a la siguiente operacion.

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
# lo que hay dentro del try es la sección del código que podría lanzar la excepción que se está capturando en el except. 
# Por lo tanto cuando ocurra una excepción, se entra en el except pero el programa no se para.
# finally Este bloque se suele usar si queremos ejecutar algún tipo de acción de limpieza.
# Dicho bloque se ejecuta siempre, haya o no haya habido excepción.

# 3. Debes hacer print por consola del resultado de todos los ejemplos. (Cumplida)

# 4. Crea un programa que imprima por consola todos los números comprendidos
#  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo. (Opcional)

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
        
# Fin.