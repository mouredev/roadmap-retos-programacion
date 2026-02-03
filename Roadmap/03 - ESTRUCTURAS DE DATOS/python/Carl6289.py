print("Ejemplo con listas (list)")
print("Creación")
lista_de_compras = ["arroz", "frutas", "verduras", "leche", "huevos", "refresco", "carne"] # Creación
print(lista_de_compras)
print("Inserción")
lista_de_compras.append("pescado") # Insersión
print(lista_de_compras)
print("Borrado")
lista_de_compras.remove("refresco") # Borrado
print(lista_de_compras)
print("Actualización")
lista_de_compras[0] = "cereal" # Actualización
print(lista_de_compras)
print("Ordenación")
lista_de_compras.sort() # Ordenación
print(lista_de_compras)
print()

print("Ejemplo con diccionarios (dict)")
capitales_venezuela = {"Zulia": "Cabimas", "Lara": "Barquisimeto", "Carabobo": "Valencia"} # Creación
print("Creación")
print(capitales_venezuela)
print("Inserción")
capitales_venezuela["Distrito Capital"] = "Caracas" # Inserción
print(capitales_venezuela)
print("Borrado")
del capitales_venezuela["Lara"] # Borrado
print(capitales_venezuela)
print("Actualización")
capitales_venezuela["Zulia"] = "Maracaibo" # Actualización
print(capitales_venezuela)
print("Ordenación")
ordenadas = sorted(capitales_venezuela.keys()) # Ordenación
print(ordenadas)
print()

print("Ejemplo con conjuntos (set)")
print("Creación")
conjunto_numeros = {45, 34, 12} # Creación
print(conjunto_numeros)
print("Inserción")
conjunto_numeros.add(23)
print(conjunto_numeros)
print("Borrado")
conjunto_numeros.remove(12)
print(conjunto_numeros)
print("No aplica actualización")
print("Ordenación")
numeros_ordenados = sorted(conjunto_numeros)
print(numeros_ordenados)
print()

print("***AGENDA DE CONTACTOS***")
agenda_contactos = {"carlos": "04167209454", "norelys": "04241503333"}
def listar_agenda(agenda_contactos):
    for nombre, numero in agenda_contactos.items():
     print(f"{nombre}: {numero}")
listar_agenda(agenda_contactos)

def buscar_contacto(agenda_contactos): # Función buscar
   while True:
     nombre_buscado = input("Ingrese el contacto a buscar: ")
     if nombre_buscado in agenda_contactos:
       numero = agenda_contactos[nombre_buscado]
       print({nombre_buscado})
       print({numero})
       break
     else:
        print("Este contacto no existe")

def insertar_contacto(agenda_contactos): # Función insertar
   nuevo_nombre = input("Ingrese el nombre: ")
   while True:
    nuevo_numero = input("Ingrese el número (máx. 11 dígitos): ")
    if not nuevo_numero.isdigit():
       print("El número de teléfono solo debe contener dígitos (0-9)")
       continue
    elif len(nuevo_numero) > 11:
       print("El número debe tener 11 dígitos o menos")
       continue
    else:
       agenda_contactos[nuevo_nombre] = nuevo_numero
       print(f"El contacto {nuevo_nombre} a sido registrado")
       print(agenda_contactos)
       break

def actualizar_contacto(agenda_contactos): #Función actualizar
   while True:
    antiguo_nombre = input("Ingrese el nombre exacto a actualizar: ")
    if antiguo_nombre in agenda_contactos:
       while True:
          opcion = input("1-Actualizar nombre, 2-Actualizar número: ")
          if opcion == "1":
             nuevo_nombre = input(f"Ingrese el nuevo nombre para {antiguo_nombre}: ")
             nombre_original = agenda_contactos[antiguo_nombre]
             agenda_contactos[nuevo_nombre] = nombre_original
             del agenda_contactos[antiguo_nombre]
             print("¡El nombre a sido actualizado!")
             print(agenda_contactos)
             break
          elif opcion == "2":
             while True:
                nuevo_numero = input(f"Ingrese el nuevo número para {antiguo_nombre}: ")
                if not nuevo_numero.isdigit():
                   print("El número de teléfono solo debe contener dígitos (0-9)")
                   continue
                elif len(nuevo_numero) > 11:
                   print("El número debe tener 11 dígitos o menos")
                   continue
                else:
                   agenda_contactos[antiguo_nombre] = nuevo_numero
                   print("¡El número a sido actualizado!")
                   print(agenda_contactos)
                break
          else:
             print("Opción invalida")
             continue
          break      
    else:
       print("Este contacto no existe")
    break          

def eliminar_contacto(agenda_contactos): # Función eliminar
   while True:
      nombre = input("Ingrese el contacto a eliminar: ")
      if nombre not in agenda_contactos:
       print ("Este contacto no existe")
       break
      else:
       while True:
          opcion = input(f"¿Esta seguro que desea eliminar a {nombre} de la lista de contactos? (y ó n): ")
          if opcion == "y":
             del agenda_contactos[nombre]
             print("¡Contacto eliminado!")
             print(agenda_contactos)
             break 
          elif opcion == "n":
             break
          else:
             print("Opción invalida")
      break
       
while True:
 opcion = input("Elija una opción (1-Buscar, 2-Insertar, 3-Actualizar, 4-Eliminar, 5-Salir): ")
 if opcion == "1":
    buscar_contacto(agenda_contactos)
    continue
 elif opcion == "2":
    insertar_contacto(agenda_contactos)
    continue
 elif opcion == "3":
    actualizar_contacto(agenda_contactos)
    continue
 elif opcion == "4":
    eliminar_contacto(agenda_contactos)
    continue
 elif opcion == "5":
    print("***¡Agenda de contactos cerrada!***")
    break
 else:
    print("Opción invalida")