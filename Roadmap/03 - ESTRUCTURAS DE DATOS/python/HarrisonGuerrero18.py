"""/*
* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
*   los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
*   (o el número de dígitos que quieras)
* - También se debe proponer una operación de finalización del programa.
*/"""

## Estructura - Listas

lista = []
print(f"Lista base: {lista}")

# Inserción en listas

while True:
    nombre = input("\nIngresa tu nombre: ")
    if nombre.replace(" ", "").isalpha() and len(nombre) > 1:
        lista.append(nombre.title())  # Inserción en la última posición de la lista
        break
    else:
        print("Debes ingresar un nombre válido (solo letras y espacios)")

while True:
    edad_input = input("\nIngresa tu edad: ")
    if edad_input.isdigit():
        edad = int(edad_input)
        if 0 <= edad <= 120:
            lista.append(edad)
            break
        else:
            print("La edad debe estar entre y 120 años")
    else:
        print("Debes ingresar un número válido")

lenguajes_programacion = ["Python", "JavaScript", "PHP", "TypeScript", "C", "C#", "C++"]
lenguajes_str = ", ".join(lenguajes_programacion)

while True:
    respuesta = (
        input(
            f"\n¿Usaste alguno de estos lenguajes para el reto? {lenguajes_programacion} (si/no): "
        )
        .strip()
        .lower()
    )

    if respuesta not in ["s", "n", "si", "no"]:
        print("Debes responder con 's' o 'n'")
    elif respuesta in ["s", "si"]:
        lenguaje_programacion = (
            input(f"\nPerfecto, escribe cual de ellos usaste ({lenguajes_str}): ")
            .strip()
            .lower()
        )

        lenguaje_normalizados = [l.lower() for l in lenguajes_programacion]

        if lenguaje_programacion in lenguaje_normalizados:
            lista.insert(1, lenguaje_programacion)  # Inserción en la posición 1
            break
        else:
            print("Debes ingresar uno de esos lenguajes de programación")
    else:
        print("De acuerdo, continuaremos con el programa")
        break
    
print(f"\n Lista con valores actuales: {lista}")

print(
    """
\nOkey ahora deberás digitar uno a uno los números de tu año de nacimiento en orden.
Ejemplo: 1-9-9-1 ó 2-0-0-1       
"""
)


def pedir_digito(mensaje):
    while True:
        num = input(mensaje)
        if num.isdigit() and len(num) == 1:
            return num
        print("Debes seleccionar un solo número válido")


num_1 = pedir_digito("\nIngresa el primer número de tu año de nacimiento: ")
num_2 = pedir_digito("\nIngresa el segundo número de tu año de nacimiento: ")
num_3 = pedir_digito("\nIngresa el tercer número de tu año de nacimiento: ")
num_4 = pedir_digito("\nIngresa el cuarto número de tu año de nacimiento: ")

lista.extend(
    ["Año de Nacimiento:", num_1, num_2, num_3, num_4]
)  # Agregar varios elementos

print(f"\nLista actualizada con año de nacimiento: {lista}")


# Actualización de listas

while True:
    nuevo_lenguaje = input(
        "\nIngresa un lenguaje que te gustaría aprender (distinto al de este reto): "
    )
    if nuevo_lenguaje.replace(" ", "").isalpha() and len(nuevo_lenguaje) > 1:
        lista[1] = nuevo_lenguaje
        break

print(
    f"\nLista actualizada reemplazando el lenguaje que estás usando con el que deseas aprender: {lista}"
)

# Borrado de listas

lista.clear()
print(f"Lista con elementos borrados: {lista}")
