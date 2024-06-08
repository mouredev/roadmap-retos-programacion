
#FUNCIONES BÁSICAS

#función básica
def imprimir_saludo():
    print("Hola")

imprimir_saludo()

#función con parametros
def funcion_parametros(param1, param2):
    print(param1, param2)
funcion_parametros("Hola", "que tal")

#Función con Valor de Retorno
def funcion_con_retorno(a,b):
    return a + b
suma = funcion_con_retorno(4,3)
print(suma)

# Función con Parámetros por Defecto
def saludar(nombre="mundo"):
    print(f"Hola, {nombre}!")

saludar() 
saludar("Natalia")  

#Funciones Anidadas
def exterior():
    print("Esta es la función exterior.")
    
    def interior():
        print("Esta es la función interior.")
    
    interior()

exterior()

# Función Lambda
sumar = lambda x, y: x + y

resultado = sumar(10, 5)
print(f"El resultado de la suma lambda es: {resultado}")  

#FUNCIONES BUILT IN

print(type(3.14))
print(len("supercalifragilistico"))
numeros = [1, 2, 3, 4]
print(sum(numeros))  
print(min(numeros))  
print(max(numeros))  
for num in range(3):
    print(num)

#VARIABLE LOCAL Y GLOBAL

mensaje_global = "Soy una variable global"

def mi_funcion():
    mensaje_local = "Soy una variable local"
    print(mensaje_local)
    
    print(mensaje_global)
    
mi_funcion()







