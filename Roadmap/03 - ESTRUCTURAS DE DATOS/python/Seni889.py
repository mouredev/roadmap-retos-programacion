
mylista = ["Andy", "Josue", "Josue"]
print(mylista)

# mylista.append("Jordy")
# print(mylista)

# mylista.extend("papa")
# print(mylista)

# mylista.insert(1, "Reyes")
# print(mylista)

# mylista[1] = "Maria"
# print(mylista)

# mylista.sort()
# print(mylista)

# mylista.reverse()
# print(mylista)

# mylista.copy()
# print(mylista)

print(mylista.count("Josue"))

#listas
reseta = ["arroz", "aceite", "camote", "cebolla", "arroz", "aceite"]
alimento = ["ceviche", "arroz con pollo", "sudado"]
animales= ["Leon", "caballo", "tigre", "perro"]

print(reseta)
print(alimento)
print(animales)

#contamos
print(reseta.count("arroz"))

print(reseta.count("camote"))

print(reseta.index("aceite"))

alimento.append("arroz chaufa")
print(alimento)
alimento.insert(3, "arroz con pato")
print(alimento)

alimento.sort()
print(alimento)

alimento.pop()
print(alimento)
# animales.remove("")
# animales.clear("")

#usar listas
numeros = [3, 4, 5, 6]
numeros.append(7)
numeros.append(8)
numeros.append(10)

numeros.insert(6, 9)
print(numeros)

numeros.pop()
print(numeros)

numeros.pop()
print(numeros)

numeros.remove(8)
print(numeros)

numeros.reverse()
print(numeros)

print(numeros.index(5))
print(numeros.index(5, 1 ))
print(numeros)

#usar listas como colas

#tuplas
datos = ("Jose", "Rey", "21")

print(datos)
print(datos[1])

datos = tuple(sorted(datos))
print(type(datos))

#set
alimentos = {"pan", "aceite", "verduras"}

alimentos.add("queso")
alimentos.update(["queso", "leche", "galletas"])
alimentos.remove("verduras")
alimentos.pop()
alimentos.discard("Kevin")
alimentos = set(sorted(alimentos)) #Se intenta ordenar pero no se puede
print(type(alimentos))
print(alimentos)

#diccionario

comidas = {"ceviche" : "nombre", "cebolla" : "ingrediente", 
           "arroz": "implemento"}
comidas["limon"] = "necesario" #insersion
comidas["ceviche"] = "plato" #actualizacion

del comidas["cebolla"]  #eliminacion datos

# comidas = sorted(comidas) #solo regresa los items

comidas = dict(sorted(comidas.items())) #un diccionario que se ordeno 


print(comidas)


"""
EXTRA
"""

def agendas():

    agenda = {}

    while True:

    

        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. actualiza contacto")
        print("4. elimina contactos")
        print("5. salir")
        


        opcion = input("Ingresa la operacion que deseas 1 ... 5: ")

        match opcion:
            case "1":
                nombre = input("Ingrese el nombre que desea buscar: ")
                if nombre in agenda:
                    print(f"El usuario con el nombre: {nombre} y su numero es : {agenda[nombre]}")
                    print("La busqueda fue exitosa")

                else:
                    print(f"El usuarios: {nombre} no se encuentra")

            case "2":
                nombre = input("Ingrese contacto: ")
                telefono = input("Ingrese numero de telefono: ")
                if telefono.isdigit() and len(telefono) > 0 and len(telefono) <=9:
                    agenda[nombre] = telefono
                else:
                    print("Ingrese un numero que no sobrepase los 9 digitos")

            case "3":
                
                nombre = input("Ingrese el nombre que desea actualizar: ")
                if nombre in agenda:
                    telefono = input("Ingrese el contacto que desea actualizar: ")
                    if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 9:
                        agenda[nombre] = telefono
                    else:
                        print("Ingrese un numero valido")
                else:
                    print("El contacto no existe")



            case "4":
                nombre = input("Ingresa el contacto que deseas eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print("Eliminacion exitosa")
                else:
                    print(f"El contacto {nombre} no existe")
            
            case "5":
                print("Saliendo del programa")
                break



   

agendas()

