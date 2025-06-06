
lista = [1, 2, "text", True]
diccionario = {"llave": "valor", "llave2": "valor"}
conjunto = {'se', 'puede', 'definir', 'con', 'set'}
tupla = (1,"Texto", lista)

# Operaciones de Insercion
lista.append("nuevo")
lista.extend('abc')
lista.insert(0, "primero")

diccionario['nuevo'] = 'nuevo2'

conjunto.add('nuevo')

# borrado
lista.remove('a')
lista.pop(1)
lista.clear()

diccionario.pop('nuevo')

conjunto.remove('nuevo')

# Actualizacion
lista[1] = 'valor'

diccionario['llave'] = 'Nllave'

conjunto2 = {1,2,3}
conjunto.update(conjunto2)

# ordenacion
lista.sort()
lista.reverse()

# Extra

def agregar(nombre: str, numero: str):
    if nombre not in contactos:
        contactos[nombre]=numero
        print(f"Contacto '{nombre}' agregado.")
    else:
        print("\nEl contacto ya existe.")

def buscar(nombre: str):
    if nombre in contactos:
        for key, value in contactos.items():
            if key == nombre:
                print(key,":",value)
    else:
        print("\nEl contacto no existe.")

def actualizar(nombre: str, numero: str):
    if nombre in contactos:
        contactos[nombre]=numero
        print(f"Contacto {nombre} actualizado.")
    else:
        print("\nEl contacto no existe.")
    

def eliminar(nombre: str, numero=None):
    if nombre in contactos:
        contactos.pop(nombre)
    else:
        print("\nEl contacto no existe.")
    
contactos = {'pepe': 1231234, 'chuy': 555555}

def main():
    while True:
        print("\n----- Agenda -----")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Ver contactos")
        print("6. Salir")
        opcion = input("Selecciona una opcion: ")
         
        if opcion == "1":
            print("\nAgregar")
            nombre, numero = input("Ingresa el nombre y numero: ").split()
            agregar(nombre, numero)
        elif opcion == "2":
            print("\nBuscar")
            nombre = input("Nombre: ")
            buscar(nombre)
        elif opcion == "3":
            print("\nActualizar")
            nombre, numero = input("Ingresa el nombre y numero: ").split()
            actualizar(nombre, numero)
        elif opcion == "4":
            print("\nEliminar")
            nombre = input("Nombre: ")
            eliminar(nombre)
        elif opcion == "5":
            print("\nContatos")
            for key, value in contactos.items():
                print(f"{key}:{value}")
        elif opcion == "6":
            break
        else:
            print("Opcion incorrecta")
