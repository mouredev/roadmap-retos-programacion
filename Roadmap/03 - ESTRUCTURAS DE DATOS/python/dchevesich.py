def my_agenda():
    diccionario = {}

    def agregar_usuario():
        telefono = input(
            "Ingrese numero de telefono no debe superar los 11 caracteres")
        if telefono.isdigit() and len(telefono) < 11:
            diccionario[usuario] = telefono
        else:
            print("numero no cumple condiciones")

    while True:
        print("Bienvenido a la terminal")
        print("1. Ingresar usuario: ")
        print("2. Para Buscar usuario: ")
        print("3. Para Eliminar usuario: ")
        print("4. Para Actualizar usuario: ")
        print("5. Para salir.")
        opcion_usuario = input("Ingrese una opción: ")
        match opcion_usuario:
            case "1":
                usuario = input("Ingrese usuario: ")
                agregar_usuario()
            case "2":
                usuario = input("Ingrese usuario a buscar: ")
                if usuario in diccionario:
                    print(
                        f"El número de teléfono de {usuario} es {diccionario[usuario]}.")
                else:
                    print(f"Usuario {usuario} no encontrado")
            case "3":
                usuario = input("Introduce el usuario a eliminar: ")
                if usuario in diccionario:
                    del diccionario[usuario]
                    print("Usuario eliminado correctamente")
                else:
                    print("Usuario no existe")
            case "4":
                usuario = input("Introduce el usuario a actualizar: ")
                if usuario in diccionario:
                    agregar_usuario()
                else:
                    print("Usuario no existe")
            case "5":
                print("Saliendo del programa")
                break
            case _:
                print("Opcion invalida favor de leer las intrucciones")


my_agenda()
