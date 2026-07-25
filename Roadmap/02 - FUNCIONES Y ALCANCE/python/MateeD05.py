"""""
EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
"""""

km = 8

# Función sin parámetros ni retorno
def km_actual():
    print(f"Llevas {km}km.\n")


# Función con un parámetro sin retorno
def contador_letras(palabra):
    print(f"La palabra {palabra} tiene {len(palabra)} letras.\n")


# Función con dos parámetros sin retorno
def suma(num1, num2):
    print(f"{num1} + {num2} = {num1+num2}\n")


# Función con dos parámetros con retorno
def suma_retorno(num1, num2):
    return num1 + num2


# Esta es la función externa con retorno
def externa():

    def interna():
        # Esta es la función interna con retorno
        return "Hola desde la función anidada!"

    # Llamada a la función interna dentro de la función externa
    resultado = interna()
    return resultado


# Dificultad extra
def dificultad_extra(tex_1, tex_2):

    contador = 0

    for num in range(1, 101):

        if num % 3 == 0 and num %5 == 0:
            print(tex_1+tex_2)

        elif num % 3 == 0:
            print(tex_1)

        elif num % 5 == 0:
            print(tex_2)

        else:
            contador += 1
            print(num)

    resultado = contador

    print(f"\nSe ha impreso el número {resultado} veces en lugar de los textos\n")

    return resultado



dificultad_extra("Hola", "Mundo")

km_actual()

contador_letras("hola")

suma(1, 3)

var_suma_retorno = suma_retorno(1, 4)

print(var_suma_retorno)
print()

print(externa())

