from os import system
system("cls")
# 01 - OPERADORES Y ESTRUCTURAS DE CONTROL

# OPERADOR DE ASIGNACIÓN ( = )
"""
    El signo = ( igual ) se utiliza para asignar el valor que se encuentra a su derecha ( 2do operando )
    a a la variable que se encuentra a su izquierda ( 1er operando )
"""

variable = "contenido por acá"
nombre = "pablo"
edad = "35"

# OPERADORES DE CONCATENACIÓN ( + , f" { } " )
print("=========================================================================")
print("OPERADORES DE CONCATENACIÓN")
"""
    El signo + ( mas ) ademas de que sirve como signo aritmetico para realizar sumas tambien se utiliza
    para realizar uniones de contenido

    f " { variables } " podemos unir usando variables de diferentes tipos de datos
"""

texto_concatenado_f = f"Mi nombre es { nombre }  y tengo  { edad } años "
print(texto_concatenado_f)
texto_concatenado_mas = "Mi nombre es " + nombre + "  y tengo  " + edad + " años "
print(texto_concatenado_mas)

# OPERADORES ARITMETICOS ( +, -, *, **, /, //, % )
print("=========================================================================")
print("OPERADORES ARITMETICOS")
"""
    Los operadores aritmeticos se utilizan para llevar al cabo calculos matematicos
"""

nro1 = 7
nro2 = 3
print(f"Suma ( + )                  { nro1 } +  { nro2 }  = { nro1 + nro2 }")       
print(f"resta ( - )                 { nro1 } -  { nro2 }  = { nro1 - nro2 }")       
print(f"multiplicar ( * )           { nro1 } *  { nro2 }  = { nro1 + nro2 }")       
print(f"potencia ( ** )             { nro1 } ** { nro2 }  = { nro1 ** nro2 }")       
print(f"División ( / )              { nro1 } /  { nro2 }  = { nro1 / nro2 }")       
print(f"Coinciente entero ( // )    { nro1 } // { nro2 }  = { nro1 // nro2 }")       
print(f"Resto de la división ( % )  { nro1 } %  { nro2 }  = { nro1 % nro2 }")      

# OPERADORES DE COMPARACIÓN O RELACIONALES
print("=========================================================================")
print("OPERADORES DE COMPARACIÓN")
"""
    Los operadores de comparación dan como resultado un valor booleano
"""

print(f"Igualdad            ( 33 == 16)  { 33 == 16 } ")
print(f"Desigual            ( 82 != 35)  { 83 != 35 } ")
print(f"Mayor que           ( 25 > 53 )  { 25 > 53 }")
print(f"Menor que           ( 17 < 50 )  { 17 < 50 }")
print(f"Mayor o igual que   ( 56 >= 56 ) { 56 >= 56 }")
print(f"Menor o igual que   ( 70 <= 73 ) { 70 <= 73 }")

# OPERADORES LÓGICOS
print("=========================================================================")
print("OPERADORES DE LÓGICOS")
"""
    Los operadores lógicos dan como resultado un valor booleano luego de realizar la comparación
    entreo otros 2 valores booleanos
"""

print(f"Pablo == Javier and 35 > 20     { "Pablo" == "Javier" and 35 > 20}")
print(f"Pablo != Javier and 35 > 20     { "Pablo" != "Javier" and 35 > 20}")
print(f"Pablo != Javier and 35 > 20     {not "Pablo" != "Javier" and 35 > 20}")
print(f"50 == 30 or 35 == 35            { 50 == 30 or 35 == 35 }")

# OPERADORES DE ASIGNACIÓN COMPUESTA
print("=========================================================================")
print("OPERADORES DE ASIGNACIÓN COMPUESTA")
"""
    Aplica el resultado de los operandos al primer operando
"""

numero1 = 10
numero1 += 4
print(f"10 += 4     { numero1 }")

numero1 = 10
numero1 -= 4
print(f"10 -= 4     { numero1 }")

numero1 = 10
numero1 *= 5
print(f"10 *= 5     { numero1 }")

numero1 = 10
numero1 **= 3
print(f"10 **= 9    { numero1 }")

numero1 = 10
numero1 /= 3
print(f"10 /= 3     { numero1 }")

numero1 = 10
numero1 %= 3
print(f"10 %= 3     { numero1 }")

numero1 = 10
numero1 //= 3
print(f"10 //= 3    { numero1 }")

# OPERADORES DE IDENTIDAD
print("=========================================================================")
print("OPERADORES DE IDENTIDAD")
"""
    Los operadores de identidad se usan para comparar si las variables ocupan
    la misma dirección en memoria
"""

numero2 = numero1
print(f"numero1 is numero2      { numero1 is numero2 }")
print(f"numero1 is not numero2  { numero1 is  not numero2 }")

# OPERADORES DE PERTENENCIA
print("=========================================================================")
print("OPERADORES DE PERTENENCIA")
"""
    El operador de pertencia su usa para saber si algo pertenece a algo
    por ejemplo si una letra esta dentro de una cadena de texto
"""

frase = "La pajara pinta a la sombra del verde limon"
print(f"'u' in { frase }          {'u' in frase} ")
print(f"'u' not in { frase }      {'u' not in frase} ")

# OPERADORES DE BIT 
nro  = 2    # 00010
nro1 = 10   # 01010
nro2 = 12   # 01100
nro3 = 16   # 10000
# El AND da como resultado 1 cuando los 2 bits a comprar es 1
print(f"AND: 10 & 12 ( 01010 & 01100 )      = { 10 & 12}  ( 01000 )")    # 01000

# El OR al menos 1 de los 2 bits a comparar tiene que ser 1
print(f"OR: 10 | 12  ( 01010 | 01100 )      = { 10 | 12 } ( 01110 )")    # 01110

# El XOR si los 2 bits a comparar son difierentes da como resultado 1
print(f"XOR 16 ^ 12  ( 10000 ^ 01100 )      = { 16 ^ 12 } ( 11100 )" )   # 11100

# El DEPLAZAMIENOT rellena de 0 hacia la izquierda o hacia la derecha la cantidad que le indiquemos
print(f"DESPLAZAR 12 << 2   ( 01010 << 2 )  = { 12 << 2 } ( 0110000 )" )     # 0110000
print(f"DESPLAZAR 16 << 12  ( 10000 << 4 )  = { 16 << 4 } ( 100000000 )" )   # 100000000


# ESTRUCTURAS DE CONTRO IF ELSEIF
print("=========================================================================")
print("ESTRUCTURAS DE CONTRO IF ELSEIF")
"""
    Se evaluan los 2 operandos y por medio de una respuestas booleana
    elige continuar por un lado o por el otro
"""

nombre = "Pablo"
if nombre == "Pablo":
    print("El nombre es Pablo")
elif nombre == "Romina":
    print("El nombre es Pablo")
else:
    print("El nombre es otro")


# CICLO FOR
print("=========================================================================")
print("CICLO FOR")
"""
    Se utiliza para repetir un bloque de codigo un X cantidad de veces
"""

# for variable_contadora in range(valor_inicial, valor_final, tamaño_paso:)
for i in range( 0, 31, 3 ):
    print(i)


# CICLO WHILE
print("=========================================================================")
print("CICLO WHILE")
"""
    Se repite un bloque de codigo mientras la condición sea TRUE
"""

i = 0
while i <= 12:
    print(i) 
    i += 2


# MANEJO DE ERRORES
print("=========================================================================")
print("MANEJO DE ERRORES")
"""
    El manejo de errores se utiliza para caputar el error en una parte del programa
    y luego seguir operando , por ejemplo un error del servidor
"""

try:
    print("aca no hay error")
except:
    print("Aca hay un error ")
finally:
    print("El finally es opcional y siempre se va a ejecutar")



# DIFICULTAD EXTRA
print("=========================================================================")
print("DIFICULTAD EXTRA")

for i in range( 10, 56 ):
    if ( i  == 55 ): print(i)
    if ( i % 2 != 0 or i == 16 or i % 3 == 0 ): continue
    print(i)
    
print("==================   FIN DEL RETO   =====================================")
print("\n")