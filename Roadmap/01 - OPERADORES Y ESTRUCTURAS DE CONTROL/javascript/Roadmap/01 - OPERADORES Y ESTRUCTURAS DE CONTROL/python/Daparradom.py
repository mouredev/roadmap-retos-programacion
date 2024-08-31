### 01-Operadores y Estructuras de Control ###

#Operadores Aritmeticos

print(5 + 1, "suma") #suma
print(5 - 1, "resta") #resta
print(5 * 1, "Multiplicacion") #multiplicación
print(5 / 1, "Division") #División
print(10 % 2, "Modulo") #modulo ---> da el remanente
print(5 // 3, "floor division") #floor division --> division sin remanente o sin flotante
print(3**4, "Operacion con exponente") #Exponente

#Operadores comparativos

(5 == 4) # igual que 
(5 > 4) # mayor que
(5 < 4) # menor que
(5 >= 4) # mayor o igual que
(5 <= 4) # menor o igual que
(5 != 4) # diferente que

# Operadores logicos 

print( 5==3 and 1>0.5) 
print( 1==2 or 3>5) 
print(not (7<6)) 

# Condicionales

resul = 5

if resul>0:
    print (f"la variable resul cuyo valor es {resul} es positiva ")
elif resul == 0:
    print (f"La variable resul cuyo valor es {resul} es igual a 0")
else:
    print(f"La variable resul cuyo valor es {resul} es negativa")

#loops
    
while resul < 30 :
    print(resul)
    resul+=2
else:
    print("mi variable resul es mayor a 30")
    
numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    print(number)

for i in range(1,50,10):
    print(i)
else:
    print("se ha terminado el for")

## Programa 

print("Se comienza el programa\n")
for number in range(10,56,1):
    if number%2 == 0 and number!=16 and number%3!=0:
        print(number)