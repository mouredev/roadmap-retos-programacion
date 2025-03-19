### Operadores Aritméticos ###

print("Suma '+'=", 7+4)
print("Resta '-'=", 7-4)
print("Multiplicación '*' =", 7*4)
print("Division '/' =", 7/4)
print("Modulo '%' = ", 7%4)
print("Division Entera '//' =", 7//4)
print("Exponenciación '**' =", 7**4)

### Operadores De Commparación ###

print("Igual '-'=", 7==4)
print("Diferente '!=' =", 7!=4)
print("Mayor que '>' =", 7 > 4)
print("Menor que '<' =", 7 < 4)
print("Mayor o igual que '>=' =", 7>=4)
print("Menor o igual que '<=' =", 7 <= 4)

### Operadores de Asignación ###
a=-2
print(f"Asignacion '=' = {a}", )
a += 2
print(f"Asignacion con suma +'=' = {a}" )
a -= 2
print(f"Asignacion con resta '-=' = {a}" )
a *= 2
print(f"Asignacion con multiplicación '*=' = {a}" )
a /= 2
print(f"Asignacion con división '/=' = {a}")
a //= 2
print(f"Asignacion con division entero '//=' = {a}")
a %= 2
print(f"Asignacion con modulo '%=' = {a}")
a **= 2
print(f"Asignacion con exponenciacion '**=' = {a}")

### Operadores Logicos ###

print("And =" ,(4 >2 and 145>=6 ))
print("Or =" ,(4 >2 or 145>=6 ))
print("Not =", not(4 >2 ))

### Operadores de Identidad ###

a= [1,3,5]
b= [1,3,5]
c= 5
d= 5
print(f"Hacen referencia al mismo objeto en memoria 'is' = {a is b} ")
print(f"No hacen referencia al mismo objeto en memoria 'is not' = {a is not b} ")
print(f"Hacen referencia al mismo objeto en memoria 'is not' = {c is d} ")
print(f"No hacen referencia al mismo objeto en memoria 'is not' = {c is not d} ")

### Operadores de Pertenencia ###
a= [1,3,5]

print(f"El valor esta presente en la secuencia 'in' = {c in a} ")
print(f"El valor no esta presente en la secuencia 'in' = {c is not a} ")

### Operadores De Bits ###

print(f"Operacion de AND entre bits '&' = {12 & 11} ")
print(f"Operacion de OR entre bits '|' = {12 | 11} ")
print(f"Operacion de comparacion entre bits, si son diferentes es 1, si son iguales 0 '^' = {12 ^ 11} ")
print(f"Operacion de dezplazamiento a la izquierda de bits '<<' = {12 << 2} ")
print(f"Operacion de dezplazamiento a la derecha de bits '>>' = {12 >> 2} ")

### Condicionales ###

x= 10

if x == 10:
    print("X es igual a 10")
elif x > 10:
    print("X es menor a 10")
else:
    print("X es no es igual o menor a 10")

### Iterativas ###

for i in range(10):
    print(i) 

cuenta = 0
while cuenta > 12:
    print(cuenta)
    cuenta += 1

### Excepciones ###

try:
    indefined = 10/0
except:
    print("Error al dividir con 0")
finally:
    print("Esto es una excepción")

### Ejercicio Extra ###

for i in range (10,56):
    if (i % 2)==0 and (i % 3) != 0 and i != 16:
        print(i)


