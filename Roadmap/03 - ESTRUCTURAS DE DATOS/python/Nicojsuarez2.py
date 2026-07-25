'''
# #03 ESTRUCTURAS DE DATOS
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
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
```
#### Tienes toda la información extendida sobre el roadmap de retos de programación en **[retosdeprogramacion.com/roadmap](https://retosdeprogramacion.com/roadmap)**.

Sigue las **[instrucciones](../../README.md)**, consulta las correcciones y aporta la tuya propia utilizando el lenguaje de programación que quieras.

> Recuerda que cada semana se publica un nuevo ejercicio y se corrige el de la semana anterior en directo desde **[Twitch](https://twitch.tv/mouredev)**. Tienes el horario en la sección "eventos" del servidor de **[Discord](https://discord.gg/mouredev)**.
'''
lista = [1, 2, 3, 4, 5]
lista.append(6)
lista.remove(3)
lista[2] = 10
lista.sort()
lista.reverse()

print('-' * 100)

dict = {
    "nombre": "Nico",
    "edad": 23,
    "ciudad": "Bogotá"
}
dict["edad"] = 24
dict["profesion"] = "Desarrollador"
dict.pop("ciudad")


print('-' * 100)

tupla = (1, 2, 3, 4, 5)
tupla.count(2)
tupla.index(4)


set = {1, 2, 3, 4, 5}
set.add(6)
set.remove(3)
set.add(10)
set.pop()
set.clear()
set.add(1)
set.add(2)
set.add(3)

listadelista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
listadelista[0].append(4)
listadelista[1].remove(5)
listadelista[2][2] = 10
listadelista.sort()
listadelista.reverse()



dictofdict = {
    "persona1": {
        "nombre": "Nico",
        "edad": 23,
        "ciudad": "Bogotá"
    },
    "persona2": {
        "nombre": "Juan",
        "edad": 24,
        "ciudad": "Medellín"
    },
    "persona3": {
        "nombre": "Pedro",
        "edad": 25,
        "ciudad": "Cali"
    }
}
dictofdict["persona1"]["edad"] = 24
dictofdict["persona1"]["profesion"] = "Desarrollador"
dictofdict["persona1"].pop("ciudad")

print('-' * 100)

def agenda(): 
    agenda = {}
    while True:
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = int(input("¿Qué operación deseas realizar? "))

        match opcion:
            case 1:
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                if telefono.isdigit() and len(telefono) == 11:
                    agenda[nombre] = telefono
                else:
                    print("Número de teléfono no válido")
            case 2:
                nombre = input("Nombre: ")
                if nombre in agenda:
                    print(f"Teléfono: {agenda[nombre]}")
                else:
                    print("Contacto no encontrado")
            case 3:
                nombre = input("Nombre: ")
                if nombre in agenda:
                    telefono = input("Teléfono: ")
                    if telefono.isdigit() and len(telefono) == 11:
                        agenda[nombre] = telefono
                    else:
                        print("Número de teléfono no válido")
                else:
                    print("Contacto no encontrado")
            case 4:
                nombre = input("Nombre: ")
                if nombre in agenda:
                    agenda.pop(nombre)
                else:
                    print("Contacto no encontrado")
            case 5:
                break
            case _:
                print("Opción no válida")

agenda()