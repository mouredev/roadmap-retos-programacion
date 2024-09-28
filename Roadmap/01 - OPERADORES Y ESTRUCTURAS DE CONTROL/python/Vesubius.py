""" 
EJERCICIO:
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


# ****************************************** OPERADORES *******************************************************************
#========================================= Operadores aritmeticos =========================================
print("========================================= Operadores aritmeticos =========================================")
# Suma
a = 5
b = 3
resultado_suma = a + b
print("Suma de", a, "y", b, "es:", resultado_suma)  

# Resta
a = 7
b = 2
resultado_resta = a - b
print("Resta de", a, "y", b, "es:", resultado_resta)  

# Multiplicación
a = 4
b = 6
resultado_multiplicacion = a * b
print("Multiplicación de", a, "y", b, "es:", resultado_multiplicacion)  

# División
a = 10
b = 2
resultado_division = a / b
print("División de", a, "y", b, "es:", resultado_division)  

# División entera
a = 10
b = 3
resultado_division_entera = a // b
print("División entera de", a, "y", b, "es:", resultado_division_entera)  

# Módulo
a = 10
b = 3
resultado_modulo = a % b
print("Módulo de", a, "y", b, "es:", resultado_modulo)  

# Potencia
a = 2
b = 3
resultado_potencia = a ** b
print("Potencia de", a, "a la", b, "es:", resultado_potencia)  



#================================================== Operadores Logicos ===========================================
print("================================================== Operadores Logicos ===========================================")
# Operador AND (and)
x = 5
y = 10
z = 15
resultado_and = (x < y) and (y < z)
print("Operador AND:", resultado_and) 

# Operador OR (or)
edad = 25
nacionalidad = "Mexicana"
es_adulto = (edad >= 18) or (nacionalidad == "Mexicana")
print("Operador OR:", es_adulto)  

# Operador NOT (not)
llueve = False
print("Operador NOT:", not llueve)  

# Operador XOR (^)
a = True
b = False
resultado_xor = a ^ b
print("Operador XOR:", resultado_xor)  

#================================================== Operadores de comparacion ===========================================
print("================================================== Operadores de comparacion ===========================================") 
# Operador de igualdad (==)
a = 5
b = 5
resultado_igual = a == b
print("Operador de igualdad:", resultado_igual) 

# Operador de desigualdad (!=)
x = 10
y = 20
resultado_desigual = x != y
print("Operador de desigualdad:", resultado_desigual) 
# Operador de mayor que (>)
num1 = 15
num2 = 10
resultado_mayor = num1 > num2
print("Operador de mayor que:", resultado_mayor)  

# Operador de menor que (<)
num3 = 5
num4 = 8
resultado_menor = num3 < num4
print("Operador de menor que:", resultado_menor)  

# Operador de mayor o igual que (>=)
x = 10
y = 10
resultado_mayor_igual = x >= y
print("Operador de mayor o igual que:", resultado_mayor_igual)  

#================================================== Operadores de asignacion ===========================================
print("================================================== Operadores de asignacion ===========================================") 
# Operador de asignación (=)
x = 5
print("Operador de asignación:", "x = 5:", x)  

# Operador de asignación con suma (+=)
y = 10
y += 5
print("Operador de asignación con suma:", "10 += 5:", y)  

# Operador de asignación con resta (-=)
z = 20
z -= 7
print("Operador de asignación con resta:", "20 -= 7:", z) 

# Operador de asignación con multiplicación (*=)
a = 3
a *= 4
print("Operador de asignación con multiplicación:", "3 *= 4:", a)  

# Operador de asignación con división (/=)
b = 25
b /= 5
print("Operador de asignación con división:", "25 /= 5:", b)  

# Operador de asignación con módulo (%=)
c = 17
c %= 5
print("Operador de asignación con módulo:", "17 %= 5:", c)  

# Operador de asignación con exponente (**=)
d = 2
d **= 3
print("Operador de asignación con exponente:", "2 **=3", d)  

# Operador de asignación con división entera (//=)
e = 25
e //= 4
print("Operador de asignación con división entera:", "25 //= 4:", e) 


#================================================== Operadores de identidad ===========================================
print("================================================== Operadores de identidad ===========================================") 

# Operador de identidad (is)
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("La lista x:",x)
print("La lista y:",y)
print("La lista z es una compia de la x",z)

print("Operación: x is y =", x is y)
print("Operación: x is z =", x is z)

# Operador de no identidad (is not)
print("Operación: x is not y =", x is not y)


# #================================================== Operadores de Pertenencia ===========================================
print("================================================== Operadores de Pertenencia ===========================================") 
# Operador de pertenencia (in)
lista = [1, 2, 3, 4, 5]
print(lista)
print("Operador de pertenencia 3 (in) lista :", 3 in lista)

# Operador de no pertenencia (not in)
print("Operador de no pertenencia 6 (not in) lista:", 6 not in lista)


# #================================================== Operadores de bits ===========================================
print("================================================== Operadores de bits ===========================================") 

# Operador AND a nivel de bits (&)
resultado_and = 15 & 7
print("Operación: 15 & 7 =", resultado_and)

# Operador OR a nivel de bits (|)
resultado_or = 15 | 7
print("Operación: 15 | 7 =", resultado_or)

# Operador XOR a nivel de bits (^)
resultado_xor = 15 ^ 7
print("Operación: 15 ^ 7 =", resultado_xor)

# Operador NOT a nivel de bits (~)
resultado_not = ~15
print("Operación: ~15 =", resultado_not)

# Operador Desplazamiento a la izquierda (<<)
resultado_despl_izq = 15 << 2
print("Operación: 15 << 2 =", resultado_despl_izq)

# Operador Desplazamiento a la derecha (>>)
resultado_despl_der = 15 >> 2
print("Operación: 15 >> 2 =", resultado_despl_der)



# ****************************************** ESTRUCTURAS DE CONTROL *******************************************************************

# ====================================== Condicionales ==========================================
x = 10
if x > 0:
    print("x es positivo")
elif x == 0:
    print("x es igual a cero")
else:
    print("x es negativo")

# Iterativa con for
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)


# ======================================== Iterativa con while ==================================
contador = 0
while contador < 5:
    print("El contador es:", contador)
    contador += 1


#========================================== Manejo de excepciones ===========================
"""try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
finally:
    print("El programa ha terminado de ejecutar el bloque try-except")
"""



 #======================================DIFICULTAD EXTRA (opcional) ========================================
""" Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3."""
for num in range(10,56):
    if num % 2 == 0:
        if num is not 16:
            if not num  % 3 == 0:
                print(num)