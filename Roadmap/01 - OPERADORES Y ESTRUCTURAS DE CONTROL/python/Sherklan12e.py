"""
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
"""
print('==================================================')
## Operadores de Aritmeticos
print(f'''
    Operadores de Aritmeticos
        1 + 1 = {1+1}) suma
        1 * 2 = {1*2}) multiplicacion
        1 / 3 = {1/3}) division
        1 ** 4 = {1**4}) Exponente
        1 // 5 = {1//5}) Conciente 
        1 % 6 = {1%6}) Modulo residuo
''')
print('===============================================')
## Operadores de Asignacion
print('''
    Operadores de Asignacion
    
    x = 5  
    y = 2
    x += 5                  # Suma
    x -= 1                  # resta
    x  *= 2                 # x = x * 2
    x /= 4                  # x = x / 4
    x %= 2                  # x = x % 2 
    x //= 5                 # x = x // 5
    x **= 5                 # x = x ** 5

    # bit a bit asigninacion
    x &= 5                  # x = x & 5
    x !=6                   # x = x ! 6
    x ^=4                   # a = a ^ 4
    x >>=3                  # a = a >> 3 
    x <<=3                  # a = a << 3

    ''')
a =True
b= False
print('==============================================')
print(f'''
    Operadores Logicos
    a = True
    b = False  
    
    a and b = {a and b}
    a or b = {a or b}
    not b = {not  b}
    not a = {not a}
    ''')
print('==================================================')
a = 5
b = 3
print(f'''
    Operadores Bitwise
    a = 5
    b = 3
    a & b = {a&b}
    a | b = {a|b}
    a ^ b = {a^b}
    ~a = {~a}
    a >> 2 = {a>>2}
    b << 1 = {b<<1}
    
    ''')

print('====================================================')
a = 3
b = 7
c = 3
print(f"""
      Operadores de Identidad
     a = 3
     b = 7
     c = 3
     a is b = {a is b}
     a is not b = {a is not b}
     a is c = {a is c} 
     
      """)

print('===================================================')

variable= 'como estas'

print(
    f""""
    
    Pertenencia
    variable = 'como estas'
    
    nombre = 'como' in variable               {'como' in variable}
    nombre2 = 'g' in variable                  {'g' in variable}
    nombre3 = 'g'  not in variable              {'g' not in variable}
    
    
    
    """
)

print('=====================================================')


print('''
      
    Condiciones y excepciones
    
    number = int(input('Escribe el numero 2: '))
    
    try:
        nombre = input('escribe tu nombre: ')
    except ValueError as error:
        print("caracteres!")
        
    
    if number == 2:
        print('es el ' , number)
    else:
        print('No es el 2')
    
    
    
    
    ''')

print('Extra:')
for i in range(10 , 56):

    if i == 16:
        continue

    if i % 2 == 0 :
        if i % 3 != 0 :
            print(i)
    else :
        continue

