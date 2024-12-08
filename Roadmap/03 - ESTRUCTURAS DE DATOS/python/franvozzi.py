# Lista (colección mutable y ordenada)
miLista = [1, 2, 3, 4, 5]
primerElementoLista = miLista[0] # Acceder al 1

miLista.append(6) # Agrega un sexto elemento
miLista.insert(2, 15) # Agrega en una posición específica

miLista.remove(3) # Eliminar elementos por valor

eliminaElemento = miLista.pop(1) # Elimina por índice

logitudLista = len(miLista) # Longitud lista

for elemento in miLista:
    print(elemento) # Recorrer e imprimir lista

# Tuplas (colección ordenada e inmutable)
miTupla = (1, 2, 3, 4, 5) 

primerElementoTupla = miTupla[0] # Acceder a primer elemento

longitudTupla = len(miTupla) # Longitud tupla

for elemento in miTupla:
    print(elemento) # Recorre tupla
    
# Conjuntos
miConjunto = {1, 2, 3, 4, 5}
miConjunto.add(6) # Añadir elementos
miConjunto.remove(3) # Remover elementos
estaPresente = 4 in miConjunto # Devuelve True, sí está presente

otroConjunto = {4, 5, 6, 7}

union = miConjunto | otroConjunto

interseccion = miConjunto & otroConjunto

diferencia = miConjunto - otroConjunto

diferenciaSimetrica = miConjunto ^ otroConjunto

for elemento in miConjunto:
    print(elemento) #recorre conjunto


miDiccionario = {"clave1": "valor1", "clave2": "valor2"}

valor = miDiccionario["clave1"] # Acceso a valor
miDiccionario["clave1"] = "nuevoValor1"
miDiccionario["clave3"] = "valor3"
del miDiccionario["clave2"] # Elimina clave-valor

claves = miDiccionario.keys() # Obtener claves
valor = miDiccionario.values() # Obtener valores

for clave, valor in miDiccionario.items():
    print(f"{clave}: {valor}")
    
# Desafío EXTRA
def myAgenda ():
    agenda = {}
    
    def insertContact():
        phone = input("Introduce el número del contacto: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else: 
            print("Debes introducir un número de teléfono con menos de 12 dígitos")
    
    while True:
        
        print("")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir") 
        
        option = input("\nSelecciona una opción: ")
        
        match option:
            case "1":
                name = input("Introduce el nombre del contacto: ")
                if name in agenda:
                    print(f"El número de teléfono de {name} es {agenda[name]}")
                else:
                    print("Usuario inexistente.")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                insertContact()
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insertContact()
                else:
                    print(f"El contacto {name} no existe")
            case "4":
                if name in agenda:
                    del agenda[name]
                else:
                    print("Usuario inexistente.")
            case "5":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción no valida. Elige una opción del 1 al 5.") 
                

myAgenda ()    