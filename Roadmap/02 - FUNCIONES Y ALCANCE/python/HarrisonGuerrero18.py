import unicodedata

def quitar_tildes(texto):
    return ''.join(
    c for c in unicodedata.normalize('NFD', texto)
    if unicodedata.category(c) != 'Mn'
    )

def despedir(**datos):
    print(f"\nInteresante información, creo que será todo por hoy {datos['nombre']}.")

    respuesta_positiva = False

    while True:
        respuesta = input("Para finalizar, ¿Te gustó probar mi código? (s/n): ").lower() 
        respuesta = quitar_tildes(respuesta)
        if respuesta in ["s", "si"]:
            respuesta_positiva = True
            print("\n¡Genial!")
            break
        elif respuesta in ["n", "no"]:
            print("\nUuh, eso dolió:(")
            break
        else: 
            print("\nTienes que escribir un valor correcto, gil.")
    
    return print(f"""
    \nHasta luego {'amigo' if datos['genero'] == 'Masculino' else 'amiga'} {datos['nombre']},
espero hayas tenido buenas experiencias con los {datos['edad']} años que has vivido.
{'Me alegro que te haya gustado probar mi código 🥸, eso me motiva a seguir aprendiendo' 
    if respuesta_positiva 
    else 'Lamento que no te haya gustado probar mi código 😭, trabajaré en mi lógica'}
¡Cuidate mucho!    
    """)

def mostrar_informacion(**datos):
    print("\nOkey, tus datos son los siguientes: ")
    for clave, valor in datos.items():
        if clave=="genero":
            print(f"Género: {valor}")
        else:
            print(f"{clave.capitalize()}: {valor}")
    return despedir(**datos)

def pedir_informacion():
    nombre = input("\nIngresa tu Nombre: ")
    
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            break
        except ValueError:
            print("Debes ingresar un número válido")
        
    while True:
        genero = input("Género (M / F): ").lower()
        if genero not in ("m", "masculino", "f", "femenino"):
            print('Debes ingresar "M" o "F" para Masculino o Femenino')
            continue
        else:
            if genero == "m" or genero == "masculino":
                genero = "Masculino"
            elif genero == "f" or "femenino":
                genero = "Femenino"
        break  
    
    informacion = {
        "nombre": nombre,
        "edad": edad,
        "genero": genero 
    }
    
    return mostrar_informacion(**informacion)
    
print("Hola, en este ejercicio tendrás que ingresar tus datos personales")
print("\n¿Estas de acuerdo en que tomemos tus datos personales?")
permiso = str(input("Si/No: ")).lower()
permiso = quitar_tildes(permiso)

match permiso:
    case "si":
        pedir_informacion()
    case "no":
        print("De acuerdo. Fin del programa.")  
    case _:
        print("Falopero de mierd")      
        
        
"""
    Extra
"""

def impirimir_numeros(texto_1,texto_2)->int:
    contador = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0: 
            print(texto_1, texto_2)       
        elif numero % 3 == 0:
            print(texto_1)
        elif numero % 5 == 0:
            print(texto_2)
        else:
            print(numero)
            contador+=1
    return contador
        
text1=input("Ingresa el primer texto: ")
text2=input("Ingresa el primer texto: ")
impirimir_numeros(text1, text2)