"""
- Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje: sin parámetros ni retorno, con uno o varios parámetros, con retorno...
- Comprueba si puedes crear funciones dentro de funciones.
- Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
- Pon a prueba el concepto de variable local y global.
- Debes hacer print por consola del resultado de todos los ejemplos.
"""

# Función sin parámetro ni retorno
def ejemplo():
    if 5 * 5 >= 8 * 4:
        print("Primera opción")
    else:
        print("Segunda opción")

ejemplo()

# Función con un parámetro
def parámetro(texto1):
    print(texto1)

parámetro("Algo de texto")

# Función con varios parámetros
def varios(x, y):
    while y < x:
        print("y < x")
        if y == x:
            break
        y += 1

varios(10, 2)

# Función con retorno
def retorno(a, b):
    multiplicar = a * b
    return multiplicar

print(retorno(11, 3))

# Función dentro de función

def primera_función():
    oración = "Raro, ¿verdad?"
    experimento = ""

    for letra in oración:
        experimento += letra
        print(experimento)

        def segunda_función():
            if oración == experimento:
                print("Más que raro, ¿no?")
        
        segunda_función()

primera_función()

# Funciones del lenguaje
# Lambda
x = lambda a, b: a % b
print(x(10, 3))

# Type, id
lenguaje = 6.9
print(type(lenguaje))
print(id(lenguaje))

# Suma, max, min
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(
    f"""
    Suma: {sum(lista)}
    Numero mayor: {max(lista)}
    Numero menor: {min(lista)}
    """
)


# Variable local
var_local = 100 # Variable local FUERA de la función

def var():
    var_local = 100 # Variable local DENTRO de la función
    print(var_local)
print(var_local)

var()

# Variable global
var_global = 111 # Variable global FUERA de la función

def var2():
    global var_global
    var_global = 111 # Variable global DENTRO de la función
    print(var_global)
print(var_global)

var2()


"""
DIFICULTAD EXTRA (opcional):
- Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
- La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
- Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
- Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
- Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
- La función retorna el número de veces que se ha impreso el número en lugar de los textos.
- Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
- Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def dif_extra(texto1, texto2):
    veces = 0

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(f"A {num} le corresponde: '{texto1 + " " + texto2}'")
        elif num % 3 == 0:
            print(f"A {num} le corresponde: '{texto1}'")
        elif num % 5 == 0:
            print(f"A {num} le corresponde: '{texto2}'")
        else:
            print(f"A {num} no le corresponde texto.")
            veces += 1
    return print(f"Veces que se ha impreso el numero en lugar del texto: {veces}")

dif_extra("Dificultad", "extra")