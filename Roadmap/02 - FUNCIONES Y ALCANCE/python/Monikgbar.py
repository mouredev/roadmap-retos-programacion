# Función sin parámetros
def suma():
    suma = 3 + 2
    print(suma)

# Función con uno parámetro
def suma(a=3):
    suma = a + 2
    print(suma)

# Función con dos parámetros y retorno
def suma(a=3,b=2):
    suma = a + b
    print(suma)
    return suma

# Función dentro de función
def funcion():
   def dentro_funcion():
      return "Función dentro de función"
   return "Función principal"
funcion()

# Ejemplo de función ya creada en el lenguaje
print(len("Hola Mundo")) # len: Obtiene la longitud de la cadena

# Variable Local y global
def suma():
   var_local = 5
   print("Esto es una variable local", var_local)
   print("Esto es una variable global", var_global)

if __name__ == "__main__":
    var_global = 5
    print("Imprimo la variable global desde el main", var_global)
    suma()

# DIFICULTAD EXTRA:

def imprimir_numeros(num1,num2):
    contador = 0
    for num in range(1, 101):
        if num % 3 == 0:
            print(num1)
        elif num % 5 == 0:
            print(num2)
        elif num % 3 == 0 and num % 5 == 0:
            print(num1 + num2)
        else:
            print(num)

    print("Hola", "Python")
    
