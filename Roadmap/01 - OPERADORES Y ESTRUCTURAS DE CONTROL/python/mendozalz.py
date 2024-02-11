'''
# Ejercicios de Programación

## Operadores

- [X] Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
  - Aritméticos
  - Lógicos
  - De comparación
  - Asignación
  - Identidad
  - Pertenencia
  - Bits

## Estructuras de Control

- [X] Utilizando las operaciones con operadores que tú quieras, crea ejemplos que representen todos los tipos de estructuras de control que existan en tu lenguaje:
  - Condicionales
  - Iterativas
  - Excepciones
- [X] Debes hacer print por consola del resultado de todos los ejemplos.

## Dificultad Extra (Opcional)

- [X] Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

- [X] Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''


##Operadores Aritméticos:

# Suma (+)
a = 15
b = 44 
print(f"Suma= {a+b}")

# Resta (-)
print(f"Resta= {a-b}")

# Multiplicación (*)
print(f"Multiplicación= {a*b}")

# División (/)
print(f"División= {b/a}")

# Módulo (%)
print(f"Mudulo= {b%a}")

# Potencia (**)
print(f"Potencia= {a**b}")

# División entera (//)
print(f"División entera= {b//a}")


#Operadores de Comparación:

# Igual (==)
print(f"Comparación= {a==b}")

# No igual (!=)
print(f"Desigualdad {a!=b}")

# Mayor que (>)
print(f"Mayor que= {a>b}")

# Menor que (<)
print(f"Menor que= {a<b}")

# Mayor o igual que (>=)
print(f"Mayor igual= {a>=b}")

# Menor o igual que (<=)
print(f"Menor igual= {a<=b}")


#Operadores Lógicos:

# AND (and)
print(f"AND= {True and True}")

# OR (or)
print(f"OR= {True or False}")

# NOT (not)
print(f"NOT= {not True}")


# Operadores de Asignación:

#Asignación (=)
c=44
print(f"Asignación= {c}")

# Suma y asignación (+=)
c+=1
print(f"Suma y asignación= {c}")

# Resta y asignación (-=)
c-=3
print(f"Resta y asignación= {c}")

# Multiplicación y asignación (*=)
c*=2
print(f"Multiplicación y asignación= {c}")

# División y asignación (/=)
c/=2
print(f"División y asignación= {c}")

# Módulo y asignación (%=)
c%=2
print(f"Modulo y asignación= {c}")


#Operadores de Identidad:

# is
print(f"IS= {a is b}")

# is not
print(f"IS NOT= {a is not b}")


# Operadores de Pertenencia:
nick = "Mendozalz"

# in
print(f"La M esta incluida en Mendozalz= {'M' in nick}")

# not in
print(f"La X esta incluida en Mendozalz= {'M' not in nick}")


# Operadores de Bits:

# AND a nivel de bits (&)
print(f"Bit AND= {a&b}")

# OR a nivel de bits (|)
print(f"Bit OR= {a|b}")

# XOR a nivel de bits (^)
print(f"Bit XOR= {a^b}")

# Complemento a nivel de bits (~)
print(f"Complemento a nivel de bit= {~b}")

# Desplazamiento a la izquierda (<<)
print(f"Desplazamiento a la izquierda= {a<<b}")

# Desplazamiento a la derecha (>>)
print(f"Desplazamiento a la derecha= {a>>b}")

## Estructuras de Control

# Condicionales

usuario = input("Por favor indica tu edad ")
edad = int(usuario)
if(edad<18):
    print("Eres menor de edad")
else:{
    print("Eres mayor de edad")
}
# Iterativas

for i in range(11):
    print(i)

# Excepciones

def div(a,b):
    try:
        result= a/b
    except:
        print("No se puede dividir por cero")
    finally:
        print("El programa a finalizado")

div(7, 0)

# Crea un programa que imprima por consola todos los números comprendidos entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

for i in range(10, 56):
    if i % 2 == 0 and i != 16 and 1 % 3 != 0:
        print(f"Imprimiendo entre 10 y 55 {i}")
    