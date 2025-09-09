# #tipos de operadores
# #Aritmeticos: Usados para realizar operaciones matematicas
# suma=5+3
# print("La suma es:",suma)
# resta=5-3
# print("La resta es:",resta)
# multiplicacion=5*3
# print("La multiplicacion es:",multiplicacion)
# division=5/3   
# print("La division es:",division)    
# division_entera=5//3
# print("La division entera es:",division_entera)
# exponente=5**3  
# print("El exponente es:",exponente)  
# modulo=5%3 
# print("El modulo es:",modulo)   

# #Comparacion:  Usados para comparar dos valores y devuelven un valor booleano (True o False)
# igualdad=(5==3)
# print("La igualdad es:",igualdad)
# desigualdad=(5!=3)
# print("La desigualdad es:",desigualdad)
# mayor_que=(5>3)
# print("Mayor que:",mayor_que)
# menor_que=(5<3) 
# print("Menor que:",menor_que)
# mayor_igual_que=(5>=3)
# print("Mayor o igual que:",mayor_igual_que) 
# menor_igual_que=(5<=3)    
# print("Menor o igual que:",menor_igual_que)

# #Logicos: Usados para combinar expresiones booleanas
# and_logico=(5>3 and 3<5) #tiene que cumplirse las dos condiciones
# print("AND logico:",and_logico)
# or_logico=(5>3 or 3<5) #tiene que cumplirse lcualquiera de las dos condiciones o ambas
# print("OR logico:",or_logico)  
# not_logico=not(5>3 and 3<5) #invierte el valor de la expresion
# print("NOT logico:",not_logico)

# #Asignacion: Usados para asignar valores a variables
# asignacion=5
# print("Asignacion:",asignacion) 
# asignacion_suma=5
# asignacion_suma+=3 #suma 3 al valor inicial de la variable
# print("Asignacion suma:",asignacion_suma)
# asignacion_resta=5
# asignacion_resta-=3 #resta 3 al valor inicial de la variable 
# print("Asignacion resta:",asignacion_resta)  
# asignacion_multi=5
# asignacion_multi*=3 #multiplica por 3 el valor inicial de la variable
# print("Asignacion multiplicacion:",asignacion_multi)
# asignacion_div=9
# asignacion_div/=3 #divide por 3 el valor inicial de la variable
# print("Asignacion division:", asignacion_div)

# #Identidad (is): Usados para comparar si dos variables son el mismo objeto en memoria
# a = [1, 2, 3]
# b = a  # b es el mismo objeto que a en memoria
# c = [1, 2, 4]  # c es un objeto diferente con el diferente contenido   
# print(a is b)                 
# print(a is c)                 
# print(b is c)   

# #De Pertenencia (in) y condicionales(if): Usados para verificar si un valor existe dentro de una secuencia (como una lista, tupla o cadena)
# lista = [1, 2, 3, "a", 5]
# elemento= "a"
# verificacion= elemento in lista
# if elemento in lista:
#     print(f"El elemento {elemento} esta en la lista")
# else:
#     print(f"El elemento {elemento} no esta en la lista")

# #iterativas
# for i in range(8):
#     i+=1
#     print(i)
# i=1
# while i<=8:
#     print(i)
#     i*=2

# #Control y manejo de excepciones
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("Error: Division por cero no permitida")
# finally:
#     print("Ha finalizado el control de excepciones")

#EXTRAS
for i in range (10,56): #lista del 10 al 55
    if (i%2==0 and i%3!=0 and i!=16) or i == 55:  #solo imprime pares, no multiplos de 3 y que sea diferente a 16 e incluido el 55
        print(i)
    