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
def operate():
    print(f'''
    *******BIENVENIDO*******
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Comparar
    6. Bits
    7. Numeros divisibles por numero determinado
    8. Salir''')
    option = int(input('Ingrese una opcion para operar: '))    
    while True:
        try:
            while option != 8:
                a = int(input('Primer numero: '))
                b = int(input('Segundo numero: '))
                
                if option == 1:
                    print(f'La suma de los numeros es: {a+b}')
                
                if option == 2:
                    print(f'La resta de los numeros es: {a-b}')
                
                if option == 3:
                    print(f'El producto de los numeros es: {a*b}')
                    
                if option == 4:
                    try:
                        print(f'La division de los numeros es: {a/b}')
                    except ZeroDivisionError:
                        print('El segundo numero no puede ser 0')
                
                if option == 5:
                    if a == b:
                        print(f'Los datos ingresados son iguales')
                    if a < b:
                        print(f'{a} es menor a {b}')
                    if a > b:
                        print(f'{b} es menor a {a}') 
                
                if option == 6:
                    print(f'Operador or &: {a & b}')
                    print(f'Operador and |: {a|b}')
                    print(f'Operador xor ^: {a ^ b}')
                    print(f'Operador >>: {a >> b}')
                    
                if option == 7:
                    range_number = int(input('Que rango desea usar?: '))
                    a_even,b_even = 0,0
                    for num in range(1,range_number):
                        if num % a == 0:
                            a_even += 1
                        if num % b == 0:
                            b_even += 1
                    print(f'Los numeros divisibles por el primer numero ({a}) son {a_even} ')
                    print(f'Los numeros divisibles por el segundo numero ({b}) son {b_even} ')
                    
                option = int(input('Ingrese una opcion para operar: '))

        except ValueError:
            print('Ingrese numeros para operar')
            option = int(input('Ingrese una opcion para operar: '))
        else:
            print('Muchas Gracias')
            break    

def print_numbers():
    print('Los numeros son: ')
    for number in range(10,56):
        if number % 2 == 0 and number != 16 and number % 3 != 0:
            print(number)

print_numbers()
operate()

               
    
    