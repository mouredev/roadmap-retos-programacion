""" # #03 ESTRUCTURAS DE DATOS
> #### Dificultad: Media | Publicación: 15/01/24 | Corrección: 22/01/24

## Ejercicio

```
/*
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
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**. """

#LISTAS

listas = [1, 2, 3, 4]
print(listas)

listas.append(1)    #Inserción
print(listas)
listas.remove(2)    #Borrar
print(listas)
listas[1] = 5       #Actualizar
print(listas)
listas.sort()       #Ordenar
print(listas)

#TUPLAS

tuplas = (0, 1, 2, 3, 4)
print(tuplas)

tuplas = tuple(sorted(tuplas))  #Ordenar
print(tuplas)

#SETS

my_set = {"David", "Rodriguez", "@davidrguez98", "26"}
print(my_set)

my_set.add("ropeda98@gmail.com")    #Inserción
print(my_set)

my_set.remove("David")              #Borrar
print(my_set)

#DICCIONARIOS

diccionario = {
    "hola" : "1",
    "adios" : "2",
    "you" : "7"
}
print(diccionario)

print(diccionario["hola"])                          #Acceso

diccionario["hey"] = "3"                            #Incersión
print(diccionario)

diccionario["hey"] = "4"                            #Actualización
print(diccionario)

del diccionario["adios"]                            #Borrar
print(diccionario)

diccionario = dict(sorted(diccionario.items()))     #Ordenar
print(diccionario)

"""  * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */ """

def my_agend():

    agend = {}

    def insert_contact():
        phone_number = input("Introduce el número del contacto: ")
        if phone_number.isdigit() and len(phone_number) > 0 and len(phone_number) < 12:
            agend[name] = phone_number
            print(f"El contacto {name} con teléfono {phone_number} se ha añadido correctamente")
        else:
            print("\nEl teléfono marcado es incorrecto. Introduce un teléfono válido con un máximo de 11 dígitos")

    while True:

        print("")
        print("1. Buscar un contacto.")
        print("2. Añade un contacto.")
        print("3. Actualiza un contacto.")
        print("4. Elimina un contacto.")
        print("5. Salir de la agenda.")
        selection = input("\nSelecciona una de las opciones anteriores: ")


        match selection:
            case "1":
                name = input("Introduce el nombre del contacto que quiere buscar: ")
                if name in agend:
                    print(f"El número de teléfono del contacto {name} es {agend[name]}")
                else:
                    print("\nEl contacto que ha introducido no está en su agenda")
            case "2":
                name = input("Introduce el nombre del contacto que quiere añadir: ")
                insert_contact()
            case "3":
                name = input("Introduce el nombre del contacto que quiere actualizar: ")
                insert_contact()
            case "4":
                name = input("Introduce el nombre del contacto que quiere eliminar: ")
                if name in agend:
                    print(f"El contacto {name} ha sido eliminado")
                    del agend[name]
                else:
                    print(f"\nEl contacto {name} no está en su agenda.")
            case "5":
                break
            case "6":
                print("\nLa opción marcada no es correcta. Selecciona un número del 1 al 5.")

my_agend()
