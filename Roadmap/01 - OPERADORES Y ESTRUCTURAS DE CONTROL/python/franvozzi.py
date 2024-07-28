# Operadores aritméticos
def suma(a, b):
    result = a + b
    print("El resultado de la suma es: " + result)

def resta(a, b):
    result = a - b
    print("El resultado de la resta es: " + result)

def multiplicacion(a, b):
    result = a * b
    print("El resultado de la multiplicación es: " + result)
    
def division(a, b):
    result = a / b  # Corrección aquí: debe ser división en lugar de suma
    print("El resultado de la división es: " + result)

def modulo(a, b):
    result = a % b
    print("El resultado del modulo es: " + result)
    
def potencia(a, b):
    result = a ** b
    print("El resultado de la potencia es: " + result)
    
def divisionEntera(a, b):
    result = a // b
    print("El resultado de la división entera es: " + result)
    
# Operadores Relacionales (devuelve True o False)

print("12 es mayor a 3? " + str(12 > 3)) # Es mayor?
print("12 es menor a 3? " + str(12 < 3)) # Es menor?
print("Tres es igual a tres? " + str(3 == 3)) # Es igual?
print("Tres es lo mismo que 3? " + str("3" == 3)) # Tiene mismo operando?
print("3 es mayor o igual a 3.0000001? " + str(3 >= 3.0000001)) # Es mayor o igual?
print("2.999999998 es menor o igual a 2.999999999? " + str(2.999999998 <= 2.999999999)) # Es menor o igual?
print("2 es diferente a 1? " + str(2 != 1)) # Es diferente?



# Operadores Bit a Bit
def ANDFunction(a, b):
    resultado = a & b
    print("a AND b es:" + str(resultado)) # imprime entero

def ORFunction(a, b):
    resultado = a | b
    print("a OR b es:" + str(resultado)) # imprime entero

def XORFunction(a, b):
    resultado = a ^ b
    print("a XOR b es:" + str(resultado)) # imprime entero
    
def NOTFunction(a, b):
    a = ~a
    b = ~b
    print(a) # imprime A
    print(b)  # imprime B

# Operadores lógicos (and, or y not)
a = True
b = False
print(a or b) # Es True si al menos uno es verdadero
print(not a) # Invierte valor booleano
print(a and b) # Ambos deben ser el mismo valor booleano

# Operadores de pertenencia (in y not in)
a = [1,2,3,4,5]
print(3 in a) # Se encuentra el 3 en el array "a"?
print(12 in a) # Se encuentra el 12 en "a"?

frase = "Hola retos!"
print("Hola" in frase)
print("Mundo" not in frase)

# Condicionales
def esMayor(a, b):
    if (a > b):
        print ("es mayor: " + str(True))
    else:
        print ("es mayor: " + str(False))

esMayor(5,4)

# Iteraciones (Itera e imprime numeros del 1 al 10)
for numero in range (1, 11):
    print(numero)
    
# DESAFIO EXTRA
for numero in range(10, 56):
    if numero % 2 == 0:
        if numero != 16 and numero % 3 != 0:
            print(numero)
