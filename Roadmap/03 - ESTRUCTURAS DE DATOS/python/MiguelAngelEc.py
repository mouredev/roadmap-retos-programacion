
# DIFICULTAD EXTRA (opcional):
# Crea una agenda de contactos por terminal.

contac = [
    {
        "nombre": "Miguel Angel",
        "apellido": "Castillo", 
        "edad": 22,
        "numero": 123456789
    }
]

#Mostrar Menu
def mostrar_menu():
    print("\n=== AGENDA DE CONTACTOS ===")
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Ver contactos")
    print("4. Eliminar contacto")
    print("5. Editar contacto")
    print("6. Salir")
    print("=" * 27)

# Funcion de buscar contactos
def buscar_contacto():
    print("\n--- Buscar contacto ---")
    if not contac:
        print("No hay contactos en la agenda.")
        return
    
    search = input("Ingrese el valor a buscar: ").lower().strip()
    print("-" * 20)
    
    encontrados = []
    for i, contacto in enumerate(contac):
        for valor in contacto.values():
            if search in str(valor).lower():
                encontrados.append((i, contacto))
                break
    
    if encontrados:
        print(f"Se encontraron {len(encontrados)} contacto(s):")
        for i, contacto in encontrados:
            print(f"\nContacto #{i+1}:")
            print(f"Nombre: {contacto['nombre']}")
            print(f"Apellido: {contacto['apellido']}")
            print(f"Edad: {contacto['edad']}")
            print(f"Número: {contacto['numero']}")
    else:
        print("No se encontraron contactos con ese criterio.")

# Funcion de Agregar Contactos
def agregar_contacto():
    print("\n--- Agregar contacto ---")
    try:
        nombre = input("Ingrese el nombre: ").strip()
        apellido = input("Ingrese el apellido: ").strip()
        edad = int(input("Ingrese la edad: "))
        numero = input("Ingrese el número: ").strip()
        

        if not nombre or not apellido:
            print("Error: El nombre y apellido no pueden estar vacíos.")
            return
        
        if edad < 0 or edad > 150:
            print("Error: Edad inválida.")
            return
            
        nuevo_contacto = {
            "nombre": nombre.title(),  # Primera letra mayúscula
            "apellido": apellido.title(),
            "edad": edad,
            "numero": numero
        }
        
        contac.append(nuevo_contacto)
        print("✓ Contacto agregado con éxito.")
        
    except ValueError:
        print("Error: La edad debe ser un número válido.")
        
# Funcion de Ver Contactos
def ver_contactos():
    print("\n--- Ver contactos ---")
    if not contac:
        print("No hay contactos en la agenda.")
        return
    
    print("-" * 20)
    for i, contacto in enumerate(contac):
        print(f"\nContacto #{i+1}:")
        print(f"Nombre: {contacto['nombre']}")
        print(f"Apellido: {contacto['apellido']}")
        print(f"Edad: {contacto['edad']}")
        print(f"Número: {contacto['numero']}")

# Funcion de Eliminar Contactos
def eliminar_contacto():
    print("\n--- Eliminar contacto ---")
    if not contac:
        print("No hay contactos en la agenda.")
        return
    ver_contactos()
    try:
        indice = int(input(f"\nIngrese el número del contacto a eliminar (1-{len(contac)}): ")) - 1
        if 0 <= indice < len(contac):
            contacto_eliminado = contac.pop(indice)
            print(f"✓ Contacto {contacto_eliminado['nombre']} {contacto_eliminado['apellido']} eliminado.")
        else:
            print("Error: Número de contacto inválido.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        
# Funcion de Editar Contactos
def editar_contacto():
    print("\n--- Editar contacto ---")
    if not contac:
        print("No hay contactos para editar.")
        return
    
    ver_contactos()
    try:
        indice = int(input(f"\nIngrese el número del contacto a editar (1-{len(contac)}): ")) - 1
        if 0 <= indice < len(contac):
            contacto = contac[indice]
            print(f"\nEditando: {contacto['nombre']} {contacto['apellido']}")
            
            nuevo_nombre = input(f"Nuevo nombre ({contacto['nombre']}): ").strip()
            nuevo_apellido = input(f"Nuevo apellido ({contacto['apellido']}): ").strip()
            nueva_edad = input(f"Nueva edad ({contacto['edad']}): ").strip()
            nuevo_numero = input(f"Nuevo número ({contacto['numero']}): ").strip()
            

            if nuevo_nombre:
                contacto['nombre'] = nuevo_nombre.title()
            if nuevo_apellido:
                contacto['apellido'] = nuevo_apellido.title()
            if nueva_edad:
                contacto['edad'] = int(nueva_edad)
            if nuevo_numero:
                contacto['numero'] = nuevo_numero
                
            print("✓ Contacto actualizado con éxito.")
        else:
            print("Error: Número de contacto inválido.")
    except ValueError:
        print("Error: Valores inválidos ingresados.")
 
# Funcion Principal Ejecuta el Programa       
def main():
    print("¡Bienvenido a tu Agenda de Contactos!")
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            
            if opcion == 1:
                buscar_contacto()
            elif opcion == 2:
                agregar_contacto()
            elif opcion == 3:
                ver_contactos()
            elif opcion == 4:
                eliminar_contacto()
            elif opcion == 5:
                editar_contacto()
            elif opcion == 6:
                print("\n¡Gracias por usar la agenda! ¡Hasta luego! 👋")
                break
            else:
                print("Error: Opción inválida. Seleccione del 1 al 6.")
                
        except ValueError:
            print("Error: Debe ingresar un número válido.")
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        

        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()