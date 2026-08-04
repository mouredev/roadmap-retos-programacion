#Funciones
#Sin parametros ni retorno
def Hola_Mundo():
    print("Hola Mundo")

Hola_Mundo()

#Con varios parametros y sin retorno
def suma(a, b):
    sumar=a+b
    print(sumar)

suma(3,5)

#Funciones sin parametros y con retorno
def year():
    x=2026
    return x
print (year())

#Funciones con parametros y con retorno
def rectangulo(ancho,largo):
    area=ancho*largo
    return area
print(rectangulo(10,3))

#Funciones anidadas
def calcular_calificaciones():
    cal_1=int(input("Primera calificacion: "))
    cal_2=int(input("Segunda calificacion: "))
    cal_3=int(input("Tercera calificacion: "))

    def promedio():
        return (cal_1+cal_2+cal_3)/3
    
    def estado():
        prom=promedio()
        if prom>=6:
            print("Aprobaste")
        else:
            print("Reprobaste")

    def mostrar_calificacion():
        print(promedio())

    mostrar_calificacion()
    estado()
    
calcular_calificaciones()
#Funciones integradas del lenguaje 
def persona_mayuscula(nombre,apellido, edad):
    return(nombre.upper(),apellido.upper(), edad)
print(persona_mayuscula("juan", "gutierrez", 25))

#Variable locales
def saludar():
    nombre = "Jess"   
    print("Hola", nombre)

saludar()

#Variables globales
iva=1.16
def precio_productos(precio):
    precio*=iva
    return round(precio, 2)

print(precio_productos(100))

#Funcion Recursiva
def sumar_cadena_numeros(n):
    if n ==0:
        return 0
    resultado=n
    resultado=n+sumar_cadena_numeros(n-1)
    return resultado

numero=int(input("Hasta que numero quieres contar "))
print(sumar_cadena_numeros(numero))

#Dificultad extra
def Contar_numeros(cadena_1, cadena_2):
    multiplos_3=0
    multiplos_5=0
    multiplos_3_5=0
    numeros_normales=0
    for numero in range (1, 101, 1):
        if numero%3==0 and numero%5==0:
            print(cadena_1+cadena_2)
            multiplos_3_5+=1
        elif (numero %3==0):
            print(cadena_1)
            multiplos_3+=1
        elif(numero%5==0):
            print(cadena_2)
            multiplos_5+=1
        else:
            print(numero)
            numeros_normales+=1
    print(f'Multiplos de 3:  {multiplos_3}\nMultiplos de 5:  {multiplos_5}\nMultiplos de 3 y 5: {multiplos_3_5}\nNumeros: {numeros_normales}')
Contar_numeros("Fizz","Buzz")