a = 1
b = 2
print("Dadas las variables a=1 y b=2:\n")

# Operadores aritméticos:
suma = a+b
resta = a-b
multiplicacion = a*b
division = a/b
modulo = a%b
div_entera = a//b
exponenciacion = a**b
print(f"""Las operaciones aritméticas realizables son:
      Suma: {suma}
      Resta: {resta}
      Multiplicación: {multiplicacion}
      Division: {division}
      Modulo: {modulo}
      Division entera: {div_entera}
      Exponenciacion: {exponenciacion}\n""")

# Operadores lógicos
y = a and b
o = a or b
no = not a
print(f"""Las operaciones lógicas básicas realizables son:
      AND: {y}
      OR: {o}
      NOT: {no}\n""")

# Operadores de comparacion
mayor_que = a>b
mayor_o_igual = a>=b
menor_que = a<b
menor_o_igual = a<=b
igualdad = a==b
desigualdad = a!=b
print(f"""Las operaciones de comparacion realizables son:
      Mayor que: {mayor_que}
      Mayor o igual que: {mayor_o_igual}
      Menor que: {menor_que}
      Menor o igual que: {menor_o_igual}
      Igualdad: {igualdad}
      Desigualdad: {desigualdad}\n""")

# Operadores de asignación
asignacion = "simbolo ="
a += b
a -= b
a *= b
print(f"""En principio la asignación se hace con {asignacion}
      Es posible agregar cualquier operación aritmética a la vez que se asigna valor de manera que se asignará a la variable su propio valor con la operación realizada""")

# Operadores de identidad
es = a is b
no_es = a is not b
print(f"""Las operaciones de identidad realizables son:
      Es: {es}
      No es: {no_es}""")

# Operadores de pertenencia
a = "gato"
b = "perro"
en = a in b
no_en = a not in b
print(f"""Las operaciones de pertenencia son para elementos iterables, tenemos que cambiar las variables a a="gato" y b="perro":
      En: {en}
      No en: {no_en}""")

# Operadores bitwise
a = 1
b = 2
bit_and = a&b
bit_or = a|b
bit_not = ~a
bit_xor = a^b
print(f"""Las operaciones bitwise (bit a bit) son con la forma binaria de las variables:
      AND: {bit_and}
      OR: {bit_or}
      NOT: {bit_not}
      XOR: {bit_xor}""")

# Estructuras de control

# Condicionales
if a<b:
    print("a es menor que b")
elif a>b:
    print("a es mayor que b")
else:
    print("deben ser iguales porque no se cumple ninguna condicion...")

# Bucle for
for i in range(1,4):
    print(f"Esta es la vez {i} de este bucle for")

# Bucle while
i=0
while i<5:
    print(f"Esta es la vez {i} del bucle while")
    i+=1

# EXTRA
for i in range(10,56):
    if (i%2==0) and (i!=16) and (i%3!=0):
        print(i)