# EJERCICIO:
# - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
# - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#   que representen todos los tipos de estructuras de control que existan
#   en tu lenguaje:
# Condicionales, iterativas, excepciones...
# - Debes hacer print por consola del resultado de todos los ejemplos.

# DIFICULTAD EXTRA (opcional):
# Crea un programa que imprima por consola todos los números comprendidos
# entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 
# Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.


# SOLUCIÓN

# Operadores Aritméticos
    a = 10
    b = 3
    print("Suma:", a + b)         # Suma
    print("Resta:", a - b)        # Resta
    print("Multiplicación:", a * b)  # Multiplicación
    print("División:", a / b)     # División
    print("División entera:", a // b) # División entera
    print("Módulo:", a % b)       # Residuo de la división
    print("Potencia:", a ** b)    # Potencia

# Operadores de Comparación
    print("¿Igual?", a == b)      # Igualdad
    print("¿Diferente?", a != b)  # Desigualdad
    print("¿Mayor?", a > b)       # Mayor que
    print("¿Menor?", a < b)       # Menor que
    print("¿Mayor o igual?", a >= b) # Mayor o igual
    print("¿Menor o igual?", a <= b) # Menor o igual

# Operadores Lógicos
    x = True
    y = False
    print("AND lógico:", x and y) # AND lógico
    print("OR lógico:", x or y)   # OR lógico
    print("NOT lógico:", not x)   # NOT lógico

# Operadores de Asignación
    c = 5
    c += 2  # c = c + 2
    print("Asignación += :", c)
    c -= 1  # c = c - 1
    print("Asignación -= :", c)
    c *= 3  # c = c * 3
    print("Asignación *= :", c)
    c /= 2  # c = c / 2
    print("Asignación /= :", c)
    c //= 2  # c = c // 2
    print("Asignación //= :", c)
    c %= 2  # c = c % 2
    print("Asignación %= :", c)
    c **= 3  # c = c ** 3
    print("Asignación **= :", c)

# Operadores de Identidad
    print("¿Es el mismo objeto?", a is b)   # `is`
    print("¿No es el mismo objeto?", a is not b) # `is not`

# Operadores de Pertenencia
    lista = [1, 2, 3, 4, 5]
    print("¿Está en la lista?", 3 in lista)     # `in`
    print("¿No está en la lista?", 6 not in lista) # `not in`

# Operadores a Nivel de Bits
    p = 5  # 0101 en binario
    q = 3  # 0011 en binario
    print("AND a nivel de bits:", p & q)   # AND bit a bit
    print("OR a nivel de bits:", p | q)    # OR bit a bit
    print("XOR a nivel de bits:", p ^ q)   # XOR bit a bit
    print("Complemento a nivel de bits:", ~p) # Complemento
    print("Desplazamiento a la izquierda:", p << 1) # Desplaza bits a la izquierda
    print("Desplazamiento a la derecha:", p >> 1)  # Desplaza bits a la derecha

# Estructuras Condicionales (if, else, elif)
    x = 10
    y = 20

    if x > y:
        print("x es mayor que y")
    elif x == y:
        print("x es igual a y")
    else:
        print("x es menor que y")

# Bucles Iterativos (for, while)

    numeros =[1, 2, 3, 4, 5]
    for numero in numeros: # Itera sobre cada elemento de la lista
        cuadrado = numero**2
        print(f'El cuadrado de {numero} es {cuadrado}')

    
    contador = 1
    while contador <=5: # Condición lógica
        print(f'contador: {contador}')
        contador += 1

# Excepciones (try, except, else, finally)

    numerador = 10
    denominador = 0

    try:
        resultado = numerador / denominador  # División por cero
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Bloque finalmente ejecutado.")

# Estructura implícita

    cuadrados_pares = [n ** 2 for n in range(1, 11) if n % 2 == 0]  
    print("Cuadrados de números pares:", cuadrados_pares)

# Estructura con break y continue
    
    for i in range(10):
        if i % 2 == 0:  # Saltar números pares
            continue
        f"Número impar: {i}"
        if i == 5:
            print("Se alcanzó el valor 5. Salida del bucle.")
            break
        print(i)

# Estructura con match

    operador = "+"
    a, b = 10, 5

    match operador:
        case "+":
            print(f"Suma: {a + b}")
        case "-":
            print(f"Resta: {a - b}")
        case "*":
            print(f"Multiplicación: {a * b}")
        case "/":
            print(f"División: {a / b}")
        case _:
            print("Operador no válido.")

# Ejercicio opcional:

    pares = [n for n in range(10, 56) if n != 16 and n % 2 == 0 and n % 3 != 0]
    print(pares)
