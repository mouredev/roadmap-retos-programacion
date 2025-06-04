import random

#operadores aritmeticos

#suma
a=12
b=12
suma=a+b
print("La suma es:",suma)

#resta
c=14
d=9
resta=c-d
print("La resta es:",resta)

#Multiplicacion
e=20
f=3
multiplicacion=e*f
print("La multiplicacion es: ",multiplicacion)

#Divison
g=12
h=0
if (h==0):
     print("Ojo el divisor no puede ser 0")  
else:
    division=g/h
    print("La division es:",division)

#modulo (residuo)
i=12
j=9
if (j==0):
     print("Ojo el divisor no puede ser 0")  
else:
    modulo=i%j
    print("El modulo es:",modulo)


#operadores logicos y condicionales

#operadores logicos
#saber si el numero elegido es igual al numero ingresado, y verificar si es positivo el numero
num=8
numElegido=4
if num==numElegido and num>0:
     print("El numero es igual al numero elegido, el numero es positivo:",num) 
else:
     print("El numero no es igual al numero elegido, el numero es negativo:",num)

#aqui tenemos el if else en logicos
#Saber si eres nayor de edad sabiendo que los 18 años ya eres mayor de edad
edad=12
if(edad>=18):
     print("Eres mayor de edad")
else:
     print("Eres menor de edad")



#Comparacion
'''
aqui tenemos los signos de comparacion:
<   mayor
>   menor
>=  mayor igual
<=  menor igual
==  igua igual
!=  diferente
'''
if(12>8): print("El numero",12,"es mayor")
if(8<12): print("El numero",8,"es menor")
if(12>=8): print("El numero",12,"es mayor o igual")
if(8<=12): print("El numero",8,"es menor o igual")
if(12==12): print("son iguales")
if(12!=8): print("son diferentes")

#asignacion
#Es simple y sencilo lo que se le asigna a una variable ejemplo
variable=12
print("mi varible tiene asignada",variable,"y su tipo de datos es",type(variable))

#identidad
#Simple y sencillo cuando es igual, pero a la vez tambien es igual el tipo de datos ejemplo
variableUno=120
variableDos=120
indentidad= variableUno is variableDos
print("Es identico?",indentidad)

#pertenencia
#Aqui vamos a ver si cierta consonante o vocal esta dentr del nombre ingresado
nombre="Brayan Trujillo" 

pertence= ("s" in nombre)
print("Pertence?",pertence) 

#iteratividad
for i in range(1,11):
     print(i)

#excepciones
try:
     dividir=12/0
except:
     print("Error, no se puede dividri en tre cero")

print("Ejercicio")
'''
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
'''
for i in range(10,56):
    if(i%2==0):
         if(i!=16 and i%3!=0):
              print(i)
          
