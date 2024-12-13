#01 OPERADORES Y ESTRUCTURAS DE CONTROL
# '''
# EJERCICIO:
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
# '''

def main():
    a = 1
    b = 2
    print()
    print("Operadores aritmeticos")
    print(a + b)
    print(a - b)
    print(a * b) 
    print(a / b)
    print(a // b)
    print(a % b)
    print(a ** b)

    print()

    print("Operadores logicos")
    print(a < b and b > a)
    print(a > b or b > a)
    print(not (a > b and b > a))

    print()

    print("Operadores de comparacion")
    print(a == b)
    print(a < b)
    print(a > b)
    print(a <= b)
    print(a >= b)
    print(a != b)

    print()

    print("Operadores de asignacion")
    # =   
    x = 3	
    print(x)
    # +=	
    x += 3		
    print(x)
    # -=	
    x -= 3	
    print(x)
    # *=	
    x *= 3
    print(x)		
    # /=	
    x /= 3
    print(x)	 
    # %=	
    x %= 3
    print(x)	
    # //=	
    x //= 3
    print(x)		
    # **=	
    x **= 3
    print(x)
    # :=  	
    print(x := 3)	
    print("(este es su equivalente)")
    x = 3  
    print(x)
    
    print()

    print("Operadores de identidad")
    print(a is b)
    print(a is not b)

    print()

    print("Operadores de pertenencia")
    lista1 = ["apple","orange"]

    print("apple" in lista1)
    print("orange" not in lista1)

    print()

    print("Operadores de bits")
    # AND
    print(a & b)	
    # OR
    print(a | b)	
    # XOR 
    print(a ^ b)	
    # NOT
    print(~b)	
    # Zero fill left shift
    print(a << 2)
    # Signed right shifT
    print(a >> 2)

    print()

    print("Operadores con estructuras de control")
    print()

    print("Condicional If")
    if a > b:
        print("a es mayor que b")
    elif a < b:
        print("a es menor que b")
    else:
        print("a y b son iguales")

    print()

    print("Inicia while loop")
    while a <= b:
        print(a)
        a += 1
        if a > b:
            break
    print("Termina el while loop")

    print()

    print("Inicia for loop")
    print("Lista 1 contiene:")
    lista2 = list()
    for i in (lista1):
        print(i)
        lista2.append(i)
    if "banana" not in lista2:
        lista2.append("banana")
    print(f"Nueva lista contiene: {lista2}")

    print()

    print("Comienza try/except")
    try:
        int(lista1)
    except TypeError:
        print("No se puede convertir lista 2 a int")
        
if __name__=="__main__":
    main()