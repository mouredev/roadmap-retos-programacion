#ESTRUCTURAS DE DATOS

#lISTAS

lista_frutas = ["manzana", "pera", "piña"]
print(f"lista inicial: {lista_frutas}")
#insercion
lista_frutas.append("naranja")
print(f"se inserta el elemento naranja al final de la lista: {lista_frutas}")

lista_frutas.insert(0, "fresa")
print(f"se inserta el elemento fresa en un indice especifico : {lista_frutas}")
#eliminacion
lista_frutas.remove("piña")
print(f"se elimina el elemnto piña de la lista: {lista_frutas}")
#actualizacion
lista_frutas[1] = "mandarina"
print(f"se actualiza el indice 1 de la lista de manzana a mandarina: {lista_frutas}")
#ordenacion
lista_frutas.reverse()
print(f"revierte el orden de la lista: {lista_frutas}")

lista_frutas.sort()
print(f"ordena la lista de forma ascendente: {lista_frutas}")

lista_frutas.sort(reverse=True)
print(f"ordena la lista de forma descendente : {lista_frutas}")

lista_frutas.sort(key=len)
print(f"ordena la lista por longitus de cadenas: {lista_frutas}")

lista_frutas_nueva = sorted(lista_frutas)

print(f"crea y ordena una nueva lista sin modificar a la original: {lista_frutas_nueva}")
print(f"lista original: {lista_frutas}")

#Tuplas

tupla_numeros = (1,  2, 3)

print(tupla_numeros)

#diccionario

notas_estudiantes = {"jesus": 20, "pedro": 16, "carlos": 10}
print(notas_estudiantes)

notas_estudiantes["jose"] = 5
print(f"agregar un par al diccionario: {notas_estudiantes}") #insercion

del notas_estudiantes["carlos"]
print(f"eliminar un par del diccionario: {notas_estudiantes}") #eliminar

notas_estudiantes["pedro"] = 4
print(f"se actualiza el valor de la clave carlos: {notas_estudiantes}") #actualizar


#extra

def agenda():

	def insertar_numero():
		phone = input("Ingrese el nuevo numero de telefono ")
		if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
			agenda_contactos[name] = phone
		else:
			print("Por favor ingresa un numero mayor que 0 e igual o menor que 11")


	agenda_contactos = {}

	while True:
		print("")
		print("1. Buscar contacto")
		print("2. Nuevo contacto")
		print("3. Actualizar contacto")
		print("4. Eliminar contacto")
		print("5. Salir")
		print("")
		
		sel = input("Selecciona una opcion: ")

		if sel == "1":
			name = input("Ingrese el contacto que desea buscar: ")
			if name in agenda_contactos:
				print(f"Este es el numero de telefono: {agenda_contactos[name]}")
			else:
				print("El contacto no existe")		
		
		elif sel == "2":
			name = input("Ingrese el nombre del nuevo contacto: ")
			if name in agenda_contactos:
				print("Este contacto ya existe")
			else:
				insertar_numero()

		elif sel == "3":
			name = input("Ingresa el nombre del contacto: ")
			if name in agenda_contactos:
				insertar_numero()
			else:
				print("Este contacto no existe")


		elif sel == "4":
			name = input("Ingrese el nombre del contacto que desee eliminar: ")
			if name in agenda_contactos:
			    del agenda_contactos[name]
			else:
			    print("Este contacto no existe")
		elif sel == "5":
			break             
			

agenda()