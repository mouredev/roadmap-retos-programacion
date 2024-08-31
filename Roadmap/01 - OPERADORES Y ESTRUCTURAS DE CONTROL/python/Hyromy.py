# ---- OPERADORES ----
# Aritmeticos
"""
+ suma
- resta
* multiplicacion
/ division
% modulo
// division redondeada
** potencia
"""

# Logicos
"""
and y
or o
not no
"""

# Comparacion
"""
== igual que
!= diferente que 
< menor que
<= menor o igual que
> mayor que
>= mayor o igual que
"""

# Asignacion
"""
= igual
+= agregar
-= disminuir
*= producto
/= repartir
%= sobrante
//= repartir (redondeado)
**= potenciar
"""

# Pertenencia
"""
is es
is not no es
"""

# Bits
"""
& y
| o
^ o exclusivo
<< desplazamiento izquierda
>> desplazamiento derecha
"""

# Adicionales
"""
+ concatenacion (strings)
* repeticion (strings)
[] idenxacion (arrays)
[:] slicing (arrays)
"""

# ---- EJEMPLOS DE OPERADORES ----

print("Modulo y Division redondeada")

# cociente de la division = 5
# residuo de la division = 3
print(23 % 4) # 3

# resultado de la division = 5.75
# cociente de la division = 5
print(23 // 4) # 5
print()

# ----

print("Asignacion")

var_1 = 15
var_1 += 2 # var_1 = var_1 + 2
print(var_1)

var_2 = 10
var_2 **= 3 # var_2 = var_2 ** 3
print(var_2)
print()

# ----

print("Pertenencia")

obj_1 = [1, 2, 3]
obj_2 = [1, 2, 3]
obj_3  = obj_1

print(obj_1 is obj_2) # aunque sus valores seas identicos, son objetos diferentes
print(obj_1 is obj_3) # obj_1 y obj_3 hacen referencia al mismo objeto
print()

# ----

print("Bits")

bit_1 = 5 # numero binario      0101
bit_2 = 12 # numero binario     1100

print(bit_1 & bit_2) # salida   0100
print(bit_1 | bit_2) # salida   1101
print(bit_1 ^ bit_2) # salida   1001
print(bit_1 << 1) # salida      1010
print(bit_1 << 3) # salida    101000
print(bit_1 >> 2) # salida      0001
print()

# ----

print("Adicionales")

str_1 = "Hola"
str_2 = "Python"

str_3 = str_1 + str_2
print(str_3)

str_4 = (str_1 + "_") * 3
print(str_4)

list_1 = [55, 1.77, "Hyromy", True]
print(list_1[2])
"""
list_1[0] = 55
list_1[1] = 1.77
list_1[2] = "Hyromy"
list_1[3] = True
"""

print(list_1[1:3]) # selecciona desde el primer indice hasta el ultimo (sin inluirlo)

moure_dev = "MoureDev"
print(moure_dev[0:5])
print()

# ---- EJEMPLOS DE ESTRUCTURAS DE CONTROL ----
print("Estructuras de control")


# Condicion si (if)
edad = 19
condicion = edad >= 18 # True

if condicion: # Si la condicion se cumple...
    
    # hacemos esto
    print("Eres mayor de edad")
    print("Eres mayor de edad") 


# Condicion de lo contrario (else)
if False:
    print("Este es en caso de que la condicion no se haya cumplido")
else: # En caso de que nada se cumpla
    print("La condicion no se cumplió")
    print("Pero aun asi puedo hacer algo")
  
    
# Condicion de lo contrario si (else if)
nombre = "Hyromy"
if nombre == "MoureDev":
    print("Hola MoureDev :D")
elif nombre == "Hyromy": # Si lo anterior no se cumplió, voy a ver si esta condicion se cumple
    print("Hola yo ¿Como estas?")
else: # en caso de que nada se cumpla
    print("Hola " + nombre)
    
    
# Estructura de control de flujo condicional (if serial)
estrellas = 4
if estrellas == 1:
    print("es una estrella")
elif estrellas == 2:
    print("son dos estrellas")
elif estrellas == 3:
    print("son tres estrellas")
elif estrellas == 4:
    print("son cuatro estrellas")
elif estrellas == 5:
    print("son cinco estrellas")
else:
    print("solo se contar hasta 5")    


# if anidado (if paralelo)
coche_color = "rojo"
coche_ruedas = 6

if coche_color == "rojo":
    if coche_ruedas < 4:
        print("eso es una moto")
    elif coche_ruedas == 4:
        print("que bonito coche rojo")
    else:    
        print("¿por que tiene " + str(coche_ruedas) + " ruedas?")
else:
    print("no me gusta el color")


# manejo de errores (try except)
numero = 10
divisor = 0

try: # codigo que pueda dar errores durante su ejecucion
    resultado = numero / divisor
    print("el resultado es " + str(resultado))
    
except Exception as e: # accciones en caso de error y evitar que el programa se pare
    print("algo salió mal")
print()


# Sentencia mientras (while)
numero = 2.3
while numero < 100:
    print("el numero vale " + str(numero))
    numero *= 2
else: # acciones cuando el bucle termine de forma natural
    print("la sentencia while terminó")
    
    
# Sentencia while interrumpida
numero = 1

while numero != 10:
    if numero == 5:
        break 
    
    print("el numero vale " + str(numero))
    numero += 1
else: # no se ejecuta porque el bucle se interrumpió
    print("la sentencia while terminó de forma natural")
print()
    

# bucle for (iterar)
for i in range(0, 10): # itera la variable i del 0 hasta el 10 (sin incluirlo)
    print(i)
else: # acciones cuando el bucle termine
    print("el for terminó")
    
# bucle for interrumpido
for x in range(1, 100):
    if x == 12:
        break
    print(x)
else:
    print("el for terminó")
    
# sentencia continue
for y in range(0, 5):
    if y == 3:
        print("se omitió esta iteracion")
        continue # todo lo que vaya delante no se ejecuta pero el bucle continua
    print(y)
else:
    print("el for terminó")
    

# ---- DIFICULTAD ADICIONAL ----
print("DIFICULTAD ADICIONAL\n")

for i in range(10, 55):
    if i % 2 == 0 and i != 16 and not i % 3 == 0:
        print(i)
else:
    print(i + 1)