# operadores basicos
aritmeticos=5+12-2*1/1
caracter=" de"+" operadores"+" caracteres"
imprime2= "Ejemplo {}, ejemplo aritmetico {}".format(caracter, aritmeticos)
imprime=f"Ejemplo {caracter}, ejemplo aritmetico {aritmeticos}"

print (imprime)
print(imprime2)
print(f"Ejemplo modulo {11 % 3}")
print(f"Ejemplo exponencial {15 ** 3}")
print(f"Ejemplo div entera {11 // 3}")

# otros operadores
print(f"Ejemplo comparacion {'a' == 'b'}")
num1=10
num2= 11
print (f"Ejemplo de desplazamiento bit {num1 >> num2 }" )

uno=3
dos=3
tres=4
print (f"Ejemplo de operador identidad {uno is dos}")
#Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.

l1=[10,20,30]
l2=[10,20,30]
print (f"Ejemplo de operador identidad en Listas {l1 is l2}")

t1=(1, 2.5, "prueba")
t2=(1, 2.5, "prueba")
print (f"Ejemplo de operador identidad en Tuplas {t1 is t2}")
#Tuplas soninmutables

print (f"Ejemplo de operador de pertenencia {'u' in 'universida'}")

# Estructuras de Control 

if aritmeticos > 15:
    print ("es mayor a 15")
elif aritmeticos < 10:
   print ("es menor a 10")
else:
    print ("es otro numero")
    
numeroletras=0
while numeroletras <= 10:
     print (numeroletras) 
     numeroletras += 1

for l in l1:
    print (l)     

for t in t1:
    print (t)     

# try

try:
    print (10 /0)
except:
    print (" se produce un error")
finally:
    print ( " se ha ejeuctado el manejo de error")     

# Dificultad Extra 
 
inicial=10
ultimo= 55       
negado=16

while inicial <= ultimo:
    if  (inicial % 2) == 0  :
        if  (inicial % 3 ) == 0 :
            if inicial != negado :
                print (inicial)
    inicial += 1
