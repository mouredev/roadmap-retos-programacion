# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
# Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
# - Comprueba si puedes crear funciones dentro de funciones.
# - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# - Pon a prueba el concepto de variable LOCAL y GLOBAL.
# - Debes hacer print por consola del resultado de todos los ejemplos.
# (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)


# Función sin parametros:

def fun_no_parametros():
    for i in range(5):
        print(i)

fun_no_parametros()

# Función con un parametro

def fun_con_parametro(nombre):
    print("¡Hola, "+nombre+"!")

fun_con_parametro("sergio")

# Función con dos parametros

def fun_con_return(num1, num2):
    numeros_pares = []
    i = num1
    print("Estos son los numeros pares entre "+str(num1)+" y "+str(num2))
    while i < num2:
        if i%2 == 0:
            numeros_pares.append(i)
        i +=1
    print(numeros_pares)
    
    
fun_con_return(1, 100)

# Función con return y tres parametros

def fun_return(a=5, b=8, c = 3):
    return (a*b)/c

print(fun_return())

#Diferencia variable local y variable global
var = "Esto es una variable global"
def fun_var():
    var = "Esto es una variable local"
    return var
print(var)
print(fun_var())
def fun_var_glob():
    global var
    var = var + " bis"
    return var
print(fun_var_glob())

# Una función ya creada de python es print que se ha utilizado más arriba varias veces pero existen muchas más, a continuación se muestran algunos ejemplos:
len(var) #imprime la longitud de un string
letra = "a"
letra = ord(letra) #devuelve el codigo ascii de una letra
print(letra)
letra = chr(letra) #convierte codigo ascii en su correspondiente simbolo
print(letra)

# DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def fun_dif_extra(var1 :str, var2 :str):
    contador = 0
    for i in range(100):
        if i%3 == 0:
            if i%5 == 0:
                print(var1+var2)
            print(var1)
        elif i%5 == 0:
            print(var2)
        else:
            print(i)
            contador += 1
    return "El número se ha impreso "+str(contador)+" veces."
print(fun_dif_extra("¡Hola, ","mundo!"))


# Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
# Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
