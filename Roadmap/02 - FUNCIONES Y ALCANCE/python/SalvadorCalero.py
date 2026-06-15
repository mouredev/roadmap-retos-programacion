# Funciones básicas

# Esto viene de una función básica.




def función_básica():
    print("Esto viene de una función básica.")

función_básica()

print("\n"*0)

"""El número y la palabra viene determinada,
          por una función con argumentos."""
def función_arg(num,pal):
    print(num,pal,"""El número y la palabra viene determinada,
          por una función con argumentos.""")
    
función_arg(5,"hola.")

print("\n"*0)

"""Si no se conoce el número de argumentos, se puede poner un * antes
    del parámetro, e indicar el número de orden para mostrar el 
    argumento."""
def function(*obj):
    print("Mi color favorito del " + obj[0] + " es rojo")

function("coche","techo","barco")

print("\n"*0)

# Argumentos con palabras calve.

def function_pres(empl1,empl2,empl3,empl4):
    print("El presupuesto más bajo pertenece a " + empl1 )

function_pres(empl1="Juan",empl2="Pedro",empl3="Carmen",empl4="Olivia")

print("\n"*0)

# Parámetro predeterminado.

def funct_pred(color="Amarillo"):
    print("Mi color favorito es el " +color)

funct_pred("Rojo")
funct_pred("Verde")
funct_pred()

print("|n"*0)

# Usar una lista como argumento.

def funct_lis(objetos_cocina):
    for Xcocina in objetos_cocina:
        print(Xcocina)

utensilios = ["Cuchara","Cuchillo","Tenedor"]

funct_lis(utensilios)

print("|n"*0)

# Con retorno.

def funct_return(x):
    return 5 * x

print(funct_return(2))
print(funct_return(5))

print("|n"*0)

# Para que no de error una función vacia, se introduce "pass".

def mi_funct():
    pass

print("|n"*0)

# Recursividad

def funct_recur(x):
    if(x>0):
        resultado = x +funct_recur (x-1)
        print(resultado)
    else:
        resultado = 0
    return resultado

print("Resultado")
funct_recur(7)

print("|n"*0)

# Funciones dentro de otra función.Anidadas.

def funct_ext(numero):
    
    def doble():
        resultado = numero * 2 
        print(f"el doble de {numero} es {resultado}")
    
    def al_cuadrado():
        resultado = numero ** 2
        print(f"{numero} al cuadrado es {resultado}")

    doble()
    al_cuadrado()

funct_ext(5)

print("|n"*0)

#Funciones incorporadas a python.

Num = int("150")
print(Num)# Convierte un valor a entero.

mas_alto = max([25,48,2,12])
print(mas_alto)# Muestra el número más alto.

print("Hola,Salva")

print("|n"*0)

# Variable Local.

def funct_local():
    x = "Esta variable es local por estar dentro de una función"
    print(x)
    
funct_local()


# Variable Global.

x = "Esta variable es global por estar fuera de la función."

def funct_global():
    print(x)

funct_global()

x = "Se ha cambiado el valor de la variable x, en global."

funct_global()

print("|n"*0)

# EXTRA
"""
def sum_text(text1,text2):
    valor1 = len(text1)
    valor2 = len(text2)
    suma_valor = valor1 + valor2
    return suma_valor

text1 = "Hola"    
text2 = "Caracola"
resultado = sum_text(text1,text2)
print(resultado)
"""

def imprime_numeros(param1, param2):
    conteo_numeros = 0
    
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(param1 + param2)
        elif i % 3 == 0:
            print(param1)
        elif i % 5 == 0:
            print(param2)
        else:
            print(i)
            conteo_numeros += 1
    
    return conteo_numeros

param1 = "Hola"
param2 = "Caracola"
resultado = imprime_numeros(param1, param2)
print(f"Número de veces que se imprimió un número: {resultado}")
