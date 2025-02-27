##creacion de ejemplos con operadores de python
separador = "--------------------------------------------------------------"
'''
OPERADORES ARITMETICOS 
son para operaciones matematicas basicas [suma, resta, multiplcacion, division, division entera,
modulo y exponeciacion]
'''
print("OPERADORES ARITMETICOS",separador)
print("SUMA 3+5 = ",3+5)
print("RESTA 3-5 = ",3-5)
print("MULTIPLCACION 3*5 = ",3*5)
print("DIVISION 3/5 = ",3/5)
print("DIVISION ENETERA 3//5 = ",3//5)
print("MODULO 10%5 = ",10%3)
print("EXPONENCIACION 3**5 = ",3**5)


'''
OPERADORES DE COMPARACION 
se usan para comparar valores y devuleven un valor de tipo bool (true or false) [igual, distinto que,
mayor que, menor que, mayor o igual que, menor o igual que]
'''

print("OPERADORES COMPARACION",separador)
print("4 es = 2",4 == 2) #igual
print("4 !=(no igual) 2",4 != 2) #distinto 
print("4 es > 2 = ",4 > 2 ) #mayor que  
print("4 es < 2 = ",4 < 2 ) #menor que
print("3 es >= 3 = ",4 >= 2 )# mayor o igual que
print("4 es <= 2 = ",4 <= 2 ) #menor o igual que
'''
OPERADORES DE ASIGNACION 
se usan para asignar valores a variables y muchos de estos se combinan con operadores
aritmeticos 
'''
x = 56
print("OPERADORES ASIGNACION",separador)
print("[igual =]x es igual que", x )
x += 2 
print("[mas igual +=] x+=2 es igual a",x)
x *= 2
print("[por igual *=] x *=3 igual a", x )
x /= 3
print("[dividido igual /=] x /=2  igual a", x )
x //= 3
print("[divido entero igual *=]x //=2  igual a", x )

'''
OPERADORES LOGICOS
se usan para combinar expresiones boleanas o para compararlas y esta arroja resultado
de dato booleano [and, or, not]
'''
print("OPERADORES LOGICOS",separador)

print("false and true =" , False and True) #los dos deben ser TRUE para que arroje TRUE
print("false and true =" , False or True) #Cualquiera debe ser TRUE para que arroje TRUE
print("not false =" ,  not False) #devolvera lo opuesto a lo que se esta negando

'''
OPERADORES DE PERTENENCIA
se usa para verificar si un elemento se encuentra en una secuencia devuelve booleano[in, not in]
'''
print("OPERADORES DE PERTENENCIA",separador)

my_list = [1,2,3,4,5,"adios"]
print("esta es la lista 'my_list'", my_list)
print("4 se encuentra dentro de my_list", 4 in my_list)
print("hola no se encuentra dentro de my_list", "hola" not in my_list)

'''
OPERADORES DE IDENTIDAD
se usa para saber si dos variables apuntan al mismo objeto en memoria arroja un booleano
 [is, is not]
'''
print("OPERADORES DE IDENTIDAD",separador)

my_object = {"uno" : 1, "dos" : 2 , "tres" : 3}
print("my_object es mi diccionario de numeros", my_object)

copy_object = my_object
print("copy_object es una copia de mi diccionario de numero", copy_object)
print("es decir que esas dos variables ocupan el mismo espacio en memorio",copy_object is my_object)

my_book = (1,2,3,4)
print("my_book es mi libro que tiene su propio espacion en memoria", my_book)
your_book = (1,2,3,4)
print("your_book es tu libro que tiene su priopio espcio en memoria", your_book)
print("asi que your_book is not my_book", your_book is not my_book)

'''
ESTRUCTURAS DE CONTROL CONDICIONALES 
permiten ejecutar ciertas lineas de codigo si la condicion se cumplo o no [if, elif, else]

'''
edad = 18

if edad >= 18:
    print("eres mayor de edad")
elif edad == 17:
    print("te falta un año para ser mayor de edad")
else :
    print("eres menor de edad")
    
#los condicionales tiene un tipo de extructura de control de una sola linea que se llama 
#exprecion ternaria
mensaje = "eres mayor de edad " if edad >= 18 else "eres menor de edad" #condcion en una sola linea
print(mensaje)
'''
ESTRUCTURAS DE CONTROL BUCLES [while, for]

while se utiliza para repetir un bloque de codigo mientras la condicion se cumpla

for se utiliza para repetir un bloque de codigo sobre secuencias o entre un rango de iteraciones

'''
#while
contador = 1
while contador <= 2048:
    print(contador)
    contador += contador

#for

for i in range(1,18,1):
    print(i)
    i += i

#hay formas de controlar el control de flujo dentro de estas estructuras de control las cuales pueden ser
#[break, continue, else, ]estas se utilizan en bucles y hay un manejo de excepciones 
# tambien que se pueden utilizar en condiciones[try, except, finally]

#try, except y finally

for x in range(10,-1,-1):
    try:
        resultado = 10/x
        print(resultado)
    except:
        print("la divion por 0 no es posible")
    finally:
        print("el tryCatch finalizo")


#continue, else y brake

#tenemos una lista de numero y el for debe encontrar si tiene un numero primo y que 
# sea menor que 10 si no lo tiene debera imprimir que no hay numero primo

lista = [1,2,3,4,5,6,7,8,9]
for numero in lista:
    if numero < 10:
        continue
    prueba = numero%5
    if prueba == 0:
        print("el numero es= ", numero)
        break
else:
    print("no hay ningun numero mayor a 10 en esta lista que sea divisible por 5")



for j in range(10, 56, 2):
    modulo = j%3
    if j == 16 or modulo == 0:
        continue
    print(j)
    



    
        
