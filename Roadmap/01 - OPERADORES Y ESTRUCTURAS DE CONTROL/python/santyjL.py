##01 - OPERADORES Y ESTRUCTURAS DE CONTROL
"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

#Aritméticos
suma : int = 3 + 4
resta : int = 3 - 4
multiplicacion : int = 3 * 4
division : float = 3 / 4                                    #siempre regresa un float
potencia : int = 3 ** 5
Division_baja : int = 3 // 3                                #las divisiones bajas regresan un valor entero , el mas bajo por ejemplo si la resuesta es 4.9 regresara 4 int
resto : float = 3 % 4                                       #regresa el restante de una division

print("------------Aritméticos----------------")
print(f"""
        suma  3 + 4 = {suma}
        resta  3 - 4 = {resta}
        multiplicacion  3 * 4 = {multiplicacion}
        division  3 / 4 = {division}
        potencia  3 ** 5 = {potencia}
        Division_baja   3 // 3 = {Division_baja}
        resto  3 % 3 = {resto}
      """)

#logicos
print("------------logicos----------------")

print("True and True = " , True and True)                #para que and sea sierto las 2 opciones tienen que ser verdaderas si no false
print("True and False = " , True and False)

print("True or False = " , True or False)                #con que una sea verdadera regresara verdadero si no false
print("False or False = ", False or False)

print("not False = ",not False)                         #retorna >true
print("not True = ",not True)                           #retorna < false

#comparación
print("------------comparación----------------")

mayor_que : bool = 3 > 4
menor_que : bool= 3 < 4
igual_que : bool = 3 == 4
diferente_que : bool = 3 != 4
mayor_o_igual : bool = 3 >= 4
menor_o_igual : bool = 3 <= 4

print(f"""
        mayor_que  3 > 4 {mayor_que}
        menor_que  3 < 4 {menor_que}
        igual_que  3 == 4 {igual_que}
        diferente_que  = 3 != 4 {diferente_que}
        mayor_o_igual  = 3 >= 4 {mayor_o_igual}
        menor_o_igual  = 3 <= 4 {menor_o_igual}
      """)

#asignación
print("------------asignación----------------")

variable_vacia : int = 12
variable_vacia += 3
variable_vacia -= 4
variable_vacia *= 2
variable_vacia /= 2
variable_vacia **= 3
variable_vacia //= 6
variable_vacia %= 4

print("""
    VARIABLE += 3
    VARIABLE -= 4
    VARIABLE *= 2
    VARIABLE /= 2
    VARIABLE **= 3
    VARIABLE //= 6
    VARIABLE %= 4
     """)

#identidad
print("------------asignación----------------")

mayor_que is True
not menor_que is False

print("""
        is
        not is""")

#pertenencia
print("------------pertenencia----------------")
my_variable = "hola mundo"

resultado1 = "hola" in my_variable
resultado2 = "hola" not in my_variable
print("""
        in
        not in""")

#bits
print("------------bits----------------")#este no se usa casi nunca por no decir nunca
num1 = 0b101
num2 = 0b011

resultado_and = num1 & num2
resultado_or = num1 | num2
resultado_xor = num1 ^ num2
resultado_izquierda = num1 << 2
resultado_derecha = num1 >> 2

print(f"""
        resultado_and = {resultado_and}
        resultado_or = {resultado_or}
        resultado_xor = {resultado_xor}
        resultado_izquierda = {resultado_izquierda}
        resultado_derecha = {resultado_derecha}
      """)

"""
#control de flujo
#bucles
#range para repetir una cantidad de veces definida
"""

for i in range(1 , 4):
    print(f"------------{i}----------------")

#for para iterar cada elemento de la lista
for i in [1 , 2 , 4 ,6]:
    print(i)


print("------------while----------------\n")
i = 0

#while se ejecuta mientras la condicion se cumpla , cuidado con los bucles infinitos
while i < 5:
    print(i)
    i += 1


#Condicionales
print("------------Condicionales_&_excepciones----------------\n")

clave = 1234

try: #manejo de excepciones
    clave_introducida = int(input("introduce la contraseña numerica : "))

    if clave == clave_introducida: #si retorna un True se ejecuta si no se ejecutara el else
        print("contraseña correcta")

    else :
        print("contraseña incorrecta")

except ValueError as error:
    print("el valor no es numerico")


print("------------Condicionales_&_comparadores_logicos----------------\n")

for number in range(1, 46):

    if number % 3 == 0 and number % 5 == 0:
        print(number , "fizzbuzz")

    elif number % 3 == 0:
        print(number , "fizz")

    elif number % 5 == 0:
        print(number , "buzz")

#EXTRA

print("------------reto_extra----------------\n")
for i in range(10 , 56):

    if i == 16:
        continue

    if i % 2 == 0 :
        if i % 3 != 0 :
            print(i)
    else :
        continue