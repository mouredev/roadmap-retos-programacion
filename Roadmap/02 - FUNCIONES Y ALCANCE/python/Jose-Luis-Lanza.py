# EJERCICIO:
# - Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje:
# Sin parámetros ni retorno:

def saludo():
    print("Hello, World!")

saludo()

# Con uno o varios parámetros:

# Con un parametro:
def saludo_personal(mi_nombre):
    print("Hola mi nombre es:", mi_nombre)

saludo_personal("Jose Luis")

# Con varios parametros:

def area_triangulo(base, altura):
    area = (base * altura)/2
    print("El area del triangulo es igual a:", area)

area_triangulo(3, 4)

# con retorno:
def main():
    n = int(input("Ingrese un número: "))
    if par(n):
        print("El número es par!")
    else:
        print("El número es impar!")

def par(numero):
    if numero % 2 == 0:
        return True
main()

# - Comprueba si puedes crear funciones dentro de funciones.

def main():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    def nombre_completo(nom, ape):
        print("Un gusto conocerte", nom, ape)

    nombre_completo(nombre, apellido)

main()

# Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# Funcion round(number, ndigits=None)

number = 17.159753
print("El numbero redondeado con 2 digitos es: ", round(number, 2))

# Pon a prueba el concepto de variable LOCAL y GLOBAL.
"""
Una variable "GLOBAL" es la que se encuentra fuera de una funcion, la misma puede ser usada por otras funciones
definidas en el programa. En cambio una funcion "LOCAL" esta definida dentro de una funcion especifica y solo
puede ser usada por dicha funcion, esta variable "LOCAL" no puede ser utilizada por otras funciones en el programa.
"""
x = "espectacular"

def mi_funcion():
  y = "fantastico"
  print("Python es " + y)

mi_funcion()

print("Python es " + x) # Si yo quisiera utilizar la variable "y" que fue definida en la funcion "mi_funcion" en este print(), obtendria un error: "NameError: name 'y' is not defined",
                        # lo que nos indica que las variables locales solamente pueden ser utilizadas dentro de las funciones donde fueron definidas.

#DIFICULTAD EXTRA (opcional):
# Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
# - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
# - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
# - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
# - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
# - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

def function_numbers(string_1, string_2):
    count = 0
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(string_1 + string_2)

        elif number % 3 == 0:
            print(string_1)

        elif number % 5 == 0:
            print(string_2)

        else:
            print(number)
            count += 1
    return count

print(function_numbers("cat", "dog"))
