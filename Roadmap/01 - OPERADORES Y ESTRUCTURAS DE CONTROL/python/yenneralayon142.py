
# ===== > Operadores aritmeticos < ======

# suma

suma = 1 + 1
print("La suma es:  ", suma) #2

# resta

resta = 7 - 6
print("La resta es:  ",resta) #1

# multiplicación

multiplicación = 7 * 6
print("La multiplicación es:  ",multiplicación) #42

# División

division = 7 / 6
print("La división es:  ",division) #1.16


# División Interna

divisionI = 7 // 6
print("La división interna es: ",divisionI) #1


# Módulo

modulo = 7 % 6
print("El módulo es:  ", modulo) #1


# Potencia

potencia = 7 ** 6
print("La potencia es:  ",potencia) #117649

# ===== > Operadores logicos < ======

# Igual

logica1 =  1 == 2
print("El resultado del operador logico igual es: ", logica1) #False

# Diferente

logica2 = 1 != 2
print("El resultado del operador logico diferente es: ",logica2) #True


# más que

logica3 = 1 > 2
print("El resultado del operador logico más que es: ",logica3) #False


# menos que

logica4 = 1 < 2
print("El resultado del operador logico menos que es: ",logica4) #True

# más o igual que

logica5 = 1 >= 2
print("El resultado del operador logico más o igual que es: ",logica5) #False


# menos o igual que

logica6 = 1 <= 2 
print("El resultado del operador logico menos o igual que es: ",logica6) #True

# # ===== > Operadores de comparación < ======

# and

comp1 = 1 and 2 < 3
print("El resultado del operador de comparación and es: ",comp1) #True

# or

comp2 = (1 == 1) or (2 < 3)
print("El resultado del operador de comparación or es: ",comp2) #True

# not

comp3 = not 2 < 3
print("El resultado del operador de comparación not es: ",comp3) #False



# ===== > Operadores de asignación < ======

asignación = 10

#+=

asignación += 5
print("El resultado del operador asignación más es: ",asignación) #15

#-=

asignación -= 5
print("El resultado del operador asignación menos es: ",asignación) #10

# *=

asignación *= 5
print("El resultado del operador asignación por es: ",asignación) #50

# /=

asignación /= 5
print("El resultado del operador asignación división es: ",asignación) #10.0


# //=

asignación //= 5
print("El resultado del operador asignación división interna es: ",asignación) #2.0

# %=

asignación %= 5
print("El resultado del operador asignación módulo es: ",asignación) #2.0


#**

asignación **= 5
print("El resultado del operador asignación potenciación es: ",asignación) #32.0

# ===== > Operadores de identidad < ======

# is
identidad1 = 10
identidad2 = 10
print("El resultado del operador de identidad is es: ",identidad1 is identidad2) #True

# is not 

print("El resultado del operador de identidad is not es: ",identidad1 is not identidad2) #False


# ===== > Operadores de pertenencia < ======

#in

pertenencia1 = [1,2,3,4,5,6]
print("El resultado del operador de pertenencia in es: ",3 in pertenencia1) #True

#not in

print("El resultado del operador de pertenencia not in es: ",8 not in pertenencia1) #True


# ===== > Operadores Bit < ======

a,b = 15,3

#and bit
print("El resultado del operador & es :  ",a & b) #3

#OR bit
print("El resultado del operador | es :  ",a | b) #15

#XOR bit
print("El resultado del operador ^ es :  ",a ^ b) #12

#NOT
print("El resultado del operador ~ es :  ",~a) #-16

#Desplazamiento a la derecha

print(f"Desplazamiento a la derecha: 8 >> 2 = {8 >> 2}")  # 2

#Desplazamiento a la izquierda

print(f"Desplazamiento a la izquierda: 8 << 2 = {8 << 2}")  # 32


# ===== > Estructuras de control < ======

control = 10

#IF

if control < 11:
   print(True)
elif control < 12:
   print("El número es menor")
else:
   print(False)  #True


#FOR
numero = 5  
for i in range(1,11):
   tabla = numero * i
   print(tabla) #Valores de numero multiplicados


# WHILE
   
i = 0
while i <= 10:
    print(i)
    i += 1 #Numeros hasta 10

#TRY
    
try:
   print(8 / 2)
except:
   print("Se ha producido un error")
finally:
   print("Ha finalizado el manejo de excepciones")
   


#DIFICULTAD EXTRA
   
for i in range(10,56):
   if i % 2 == 0 and i != 16 and i % 3 != 0:
      print(i) 
   

