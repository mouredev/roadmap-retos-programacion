"""
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje: Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits... (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
"""
# Asignación
asignacion = 'valor' # Asignación (=) Asigna un valor a una variable
asignacion = 3
asignacion += 2 # Suma 2 valores a la variable
asignacion -= 1 # Resta 1 valor a la variable
asignacion *= 2 # Multiplica 2 valores a la variable
asignacion /= 4 # Divide 4 valores a la variable
asignacion %= 3 # Devuelve el resto de dividir 3 valores a la variable
asignacion **= 2 # Eleva 2 valores a la variable

print(asignacion)

# Aritméticos
suma = 1 + 1 # Suma (+) suma dos valores
resta = 5 - 3 # Resta (-) resta dos valores
multiplicacion = 2 * 4 # Multilicación (*) multiplica dos valores
division = 20 / 5 # División (/) divide dos valores
resto = 6 % 5 # Resto (%) de la división guarda el resto de la misma
exponente = 5 ** 2 # Exponente (**) Eleva el 5 al 2
division_entera = 11 // 3 # División Entera (//) Hace una división normal pero guarda su parte entera

# Cómparación
igualacion = suma == resta # Igualación (==) comprueba si 2 valores son iguales - Devuelve True
diferentes = multiplicacion != division # Diferentes (!=) comprueba si 2 valores son distintos - Devuelve True
mayor = resto > suma # Mayor que (>) Devuelve si un valor es mayor que otro - Devuelve False
menor = suma < resta # Menor que (<) Devuelve si un valor es menor que otro - Devuelve False
mayor_igual = multiplicacion >= resta # Mayor o igual que (>=) Devuelve si un valor es mayor o igual que otro - Devuelve True
menor_igual = multiplicacion <= division # Menor o igual que (<=) Devuelve si un valor es menor o igual que otro  - Devuelve False

# Lógicos
y = igualacion and diferentes # Y (and) Con que uno de los valores sea sea False todo es False - Devuelve True
o = mayor or menor # O (or) Con que uno de los valores sea True todo es True - Devuelve False
negacion = not mayor_igual # No (not) Devuelve el valor booleano contrario - Devuelve False

# Identidad
es = suma is resta # Es (is) Hace referencia al mismo objeto - Devuelve True
no_es = resta is not multiplicacion # No es (is not) Hace referencia a objetos distintos - Devuelve True

# Pertenencia
print('Dato' in 'Python es para Ciencias de Datos') # En (in) Evalúa si un objeto pertenece a otro - Devuelve True
print('Python' not in 'Python es para Ciencias de Datos') # No en (not in) Evalúa si un objeto no pertenece a otro - Devuelve False

# De bits
bit_y = 10 & 3 # Y (&) Compara bit a bit los 2 números si encuentra 2 unos devuelve un 1 sino un 0, el resultado será el decimal del binario resultante
bit_o = 10 | 3 # O (|) Compara bit a bit los 2 números si encuentra al menos un 1 devuelve 1 sino un 0, el resultado será el decimal del binario resultante
bit_xor = 10 ^ 3 # Xor (^) Compara bit a bit los 2 números si los bits son diferentes el resultado es 1 sino es 0
bit_not = ~10 # Not (~) Invierte los bits del numero
derecha = 10 >> 2 # Desplazamiento hacia la derecha (>>) Desplaza cada bit 2 posiciones hacia la derecha
izquierda = 10 << 1 # Desplazamiento hacia la izquierda (<<) Desplaza cada bit 1 posición hacia la izquierda

print(derecha) 

'''
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
Condicionales, iterativas, excepciones...
'''

# Condicionales

# if
if suma == resta: # Si la condición es verdadera ejecuta lo que hay después del :
    print ('La suma es igual a la resta')
elif resta != multiplicacion: # Si la primera condición es falsa evalua las condiciones de elif y si es verdadera ejecuta lo que hay después del :
    print ('La resta y la multipliación son diferentes')
else: # Si ninguna de las condiciones es verdadera ejecuta lo que hay despues del : del else
    print ('La suma no es igual a la resta ni la resta distinta a la multiplicación')
    
i = 0

# Iteraciones

# while
while i < 5: # Ejecuta la instrucción mientras la condición sea verdadera
    print (i)
    i += 1 # Se suma 1 a la variable porque i puede quedar siempre con su valor original asignado (0) y quedar en un bucle infinito, de esta manera i en algun momento dejará de ser menor que 5 y el bucle termina

for x in range(5): # Ejecuta un bucle hasta llegar a un valor en específico
    print(x)

# Excepciones
try: # Intentamos ejecutar un código
    print(10 / 1)
except: # Si encuentra un error ejecutará el siguiente código
    print('Opa, cuidao, está cometiendo un delito que puede tener una pena de 30 años como mínimo')
finally: # Ejecuta el siguiente código al finalizar la excepción
    print('Ha finalizado la excepción con éxito')
    
# ----------------------------------------------------------------
'''Extra'''
text = ''
for i in range(10, 55):
    if i != 16 and i % 2 == 0:
        text += f'{i}, ';
        
print(text);