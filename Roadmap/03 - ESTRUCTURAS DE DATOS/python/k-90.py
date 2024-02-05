### 03 Estructuras de Datos

### Listas

lenguajes = ["python","cobol","javascript","swift","java"]
lenguajes.append("python")
lenguajes.append("cobol")
lenguajes.pop(1)
lenguajes.pop(0)
lenguajes.sort()
print(lenguajes.index("python"))
print(len(lenguajes))
lenguajes.clear()
print(lenguajes)

### Listas de comprensión

cuadrados = []
for x in range(10):
    cuadrados.append(x**2)

print(cuadrados)

combinaciones = []
for x in [3,4,5]:
    for y in [1,7,9]:
        if x != y:
            combinaciones.append((x,y))

print(combinaciones)

### Listas de compresión anidadas

matriz = [
    [1,2,3,],
    [5,6,7,],
    [9,10,11,]
]
matrix = [[row[i] for row in matriz] for i in range (3)]
print(matrix)

print(list(zip(*matriz)))

### Tuplas

tuples = ("manzana","pera","8","platano","mango")
print("manzana" in tuples)
print(tuples[2])
tuples = tuple(sorted(tuples))
print(tuples)



### Set

fruits = {"naranja","melon","sandia","melocoton"}
fruits.add("albaricoque") 
fruits.remove("naranja")
print(fruits)



### Diccionario

mi_diccionario: dict = {
    "name":"Enrique",
    "Surname":"Castro",
    "Edad":"33",
    "e-mail":"kikedev@kikadev.com"
}
mi_diccionario["web"] = "losfijos.dev"
print(mi_diccionario)
del mi_diccionario["Surname"]
print(mi_diccionario)
print(mi_diccionario["e-mail"])
mi_diccionario["Edad"] = "34"
print(mi_diccionario)
mi_diccionario = dict(sorted(mi_diccionario.items()))
print(mi_diccionario)


### Extra

def agenda():

    agenda = {}

    def añadir_contacto():
        telefono = input("Introduce número de telefono:")
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 11:
            agenda[name] = telefono
        else:
            print("Debe introducir un numero de 11 digitos")
    
    while True:

        print("")
        print("1.Buscar Contacto")
        print("2.Insertar Contacto")
        print("3.Actualizar Contacto")
        print("4.Eliminar Contacto")
        print("5.Salir")

        opciones = input("\nEliga una opcion:")

        match opciones:
            case "1":
                name = input("Introduce nombre de contacto a buscar:")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe.")
            case "2":
                name = input("Introduce el nombre de contacto:")
                añadir_contacto()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar:")
                if name in agenda:
                    añadir_contacto()
                else:
                    print(f"El contacto {name} no existe.")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar:")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe.")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opción no valida. Eliga una opcion del 1 al 6.")

agenda()

