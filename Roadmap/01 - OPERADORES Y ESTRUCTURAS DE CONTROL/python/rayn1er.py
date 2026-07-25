# /*
#  * EJERCICIO:
#  * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#  *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#  *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#  * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#  *   que representen todos los tipos de estructuras de control que existan
#  *   en tu lenguaje:
#  *   Condicionales, iterativas, excepciones...
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa que imprima por consola todos los números comprendidos
#  * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  *
#  * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
#  */


#artimeticos
sum_operator = 2 + 2 #operador logico de suma
sub_operator = 4 - 2 #operador logico de la resta
div_operator = 10 / 2 #operador logico de division
mul_operator = 5 * 2 #operador logico de la multiplicacion
exp_operator = 5 ** 2 #operador de potencia
float_div_operator = 55 /2 #operador para dividir redoneando

print(sum_operator,sub_operator,div_operator,mul_operator,exp_operator,float_div_operator)
#comparacion 

greater_than =  5 > 2 #operador logico mayor que, devuelve un boleano (en este caso true)
less_than = 2 < 5 #Operador logico menor que, devuelve un boleano (en este caso true)
equal_to = 2 == 5 #operador logico de igual que, devuelve booleano (en este caso false)
not_equal_to = 2 != 5 #operador logico de no igual que, en este caso devuelve true
greater_than_or_equal_to = 2 >= 5 #operador logico de igual o mayor que, devuelve false
less_than_or_equal_to = 2 <=5 #operador logico de menor o igual que, devuelve true

#logicos

# El operador and evalua ambos y valores y si los dos son true, devuelve true, en caso de uno de los valores sea false, entonces el resultado sera false

print(True and True) #imprime true
print(True and False) #imprime false

#por su parte el operador or nos devuelve true siempre y cuando uno de los valores sea true

print(True or True) #imprime True
print(True or False) #tambien imprime true
print(False or False) #imprime False

#finalmente tenemos el operador nor el cual nos invierte el valor de nuestro booleano

print(not True) #imprime False
print(not False) #imprime true


#asignacion

variable = 10 # utilizamos el simbolo = para asignar un valor a nuestra variable
print(variable)
variable += 10 #utilizamos += 10 para aumentar en 10 nuestro valor
print(variable) #imprimimos para ver los cambios
variable -= 10 #lo mismo con el operador -= que en este caso nos ayuda a restar
print(variable) #volvemos a imprimir para ver los cambios
variable *= 10 # *= para multiplicar
print(variable) #volvemos a imprimir para ver los cambios
variable /= 10 # para dividir
print(variable) #volvemos a imprimir para ver los cambios
variable **= 10 # **= para el exponencial
print(variable) #volvemos a imprimir para ver los cambios
variable //= 10 # //= para dividir redondeando 
print(variable) #volvemos a imprimir para ver los cambios
variable %= 10 # %= para el modulo
print(variable) #volvemos a imprimir para ver los cambios

#identidad

#supongamos que tenemos dos variables y queremos verificar si ambas son iguales, para ello utilizariamos los operadores de identidad, que nos devuelve un booleano positivo si el valor ambos elementos es igual

value_a = 100
value_b = 100
print(value_a is value_b) #el operador is nos arroja true si el objeto vale lo mismo, en este caso true

#el operador is not devuelve true si el elemento no es el mismo
value_c = 10

print(value_a is not value_c) #en este caso nos arroja tambien true

#el funcionamento de esto es diferente si lo aplicamos en listas que contengan los mismos objetos, debido a que a pesar de que los elementos contenidos dentro de la lista son los mismos, dichas listas se almacenan en lugares diferentes de la memoria

list_a = [1,2,3]
list_b = [1,2,3]

print(list_a is list_b) #en este caso arroja false, puesto que son listas distintas
print(list_a is not list_b) #como las listas no son las mismas, devuelve un true

#pertenencia
#aqui tenemos los operadores in y not in, que se utilizan para verificar si un elemento se encuentra o pertenece a otro
string = "soy una cadena de textos de python!"

print('i' in string) #en este caso nos arrojara false, puesto que "i" no esta comprendido en la cadena de texto
print('i' not in string) #todo lo contrario aca, nos arroja true porque la letra en cuestion no esta comprendida en la variable

#operadores bitwise
#estos son los operadores que utilizamos para trabajar a nivel binario

bit_a = 10
bit_b = 3

print(bit_a & bit_b) # & (and) compara cada bit de los operandos y devuelve uno si ambos bit son 1, de lo contrario devuelve 0
print(bit_a | bit_b) # | (or) compara cada bit de los operandos y devuelve 1 si al menos uno de ambos es 1 
print(bit_a ^ bit_b) # ^ (xor) compara ambos y devuelve uno si uno de los bit es 1, pero no ambos
print(~bit_a) # ~ (not) invierte los bits del operando
print(bit_a >> 2) # >> (desplazamiento a la derecha) reemplaza los bits hacia la derecha segun lo indiquemos, en este caso 2 digitos
print(bit_a << 2 ) # << (desplazamiento hacia la izquierda) reemplaza los bits hacia la izquierda segun lo indiquemos, en este caso dos digitos


#estructuras de control

#utilizamos if para verificar si una condicion se cumple o no y en base a ello ejecutar un codigo u otro

town = 'megalovania' #estableceremos esta variable para verificar si la misma contiene la letra "a"

if 'a' in town:
    print("la letra se encuentra") #codigo que se ejecutara, puesto que la letra esta en la variable
#aca podriamos colocar un elif en caso de querer agregar otro comportamiento para otra condicion dada
else:
    print("la letra no se encuentra") #codigo que se ejecutara en caso de que la letra no este en la variable

#tambien tenemos la palabra reservada while, que utilizamos para ejecutar codigo siempre y cuando se cumpla una condicion

counter = 0 #estableceremos un contador para ir aumentando su numero gradualmente

while counter < 10: #si el contador es menor a 10, ejecutamos codigo
    counter += 1 #agregamos uno a la variable
    print(counter) #imprimimos por consola

#tambien tenemos el bucle for, el cual se ejecutara un numero dado de veces, a diferencia del while que podria ejecutarse de manera infinita

for i in range(0,counter): #imprimimos desde el uno cantidad de veces hasta el valor de contador el cual se ha incrementado a diez
    print(f'hola #{i}')

#finalmente tenemos la estructura de control try, la cual nos sirve para detectar posibles errores y ejecutar un codigo alternativo con el objetivo de que el error no rompa el flujo de ejecucion de nuestro programa

try:
    print(2/0) #realizar esta operacion derivara en un error, puesto que no podemos dividir un numero entre 0

except:
    print("el programa ha presentado un error puesto que no se puede dividir por 0") #utilizamos except para continuar el flujo de la aplicacion

finally:
    print("el programa ha continuado exitosamente") #utilizamos finally para ejecutar codigo luego de realizar el except

#programa extra

for i in range(10,56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
        