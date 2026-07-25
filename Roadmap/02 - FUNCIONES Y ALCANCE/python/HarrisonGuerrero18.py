import re, unicodedata

# Variables globales

opciones_si = ["s", "si"]
opciones_no = ["n", "no"]

while True:
    nombre = input("Hola, ¿Cómo te llamas?: ").strip().title()
    if nombre == "":
        print("No puedes dejar el nombre vacío 🙃")
        continue
    elif re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", nombre):
        break
    else: 
        print("\n❌ Debes ingresar un nombre válido")
        continue

"""
    Ejemplos básicos de funciones 
"""
# Sin parámetros ni retorno 

def saludar_basico()->str:
    print(
f""" 
¿Qué tal?, {nombre}, espero que el código de este archivo te agrade, consistirá en poner en practica todos los ejercicios planteados en el tercer reto de Mouredev. 
Recuerda que nunca dejamos de ser estudiantes en este rubro, pues no paramos de aprender.
""")
saludar_basico()

# Con un parámetro y retorno
    
def quitar_tildes(texto)->str:
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    ) 

"""
    Función dentro de función
"""

def pedir_numeros()->float:
    def sumar_numeros(*numeros):
        suma = sum(float(num) for num in numeros)
        return int(suma) if suma.is_integer() else suma

    print(
f"""
Bien, en este ejercicio te pediremos que digites al menos dos números para realizar sumas, pero podrás realizar la suma de todos los números que ingreses.
Esta función contiene una subfunción que se encargará de realizar la suma.
""")
    
    try:
        while True:
            respuesta = input(quitar_tildes("\n¿Deseas proceder a sumar números? (en caso de que no, finalizará el programa). (s/n): ")).lower().strip()
            
            if respuesta in opciones_si:
                print("Perfecto. Iniciando programa... 🖥️")
                lista_numeros = []
                
                while True:
                    try:
                        numero = float(input("\nIngresa un número: "))
                        lista_numeros.append(numero)
                    except ValueError:
                        print("❌ Debes ingresar un número válido.")
                        continue
                        
                    if len(lista_numeros) >= 2:
                            continuar = quitar_tildes(input("\n¿Deseas sumar más números? (s/n): ")).lower().strip()
                            if continuar in opciones_no:
                                print(f"\n✅ La suma de los números que ingresaste es la siguiente: {sumar_numeros(*lista_numeros)}")
                                return
                            elif continuar in opciones_si:
                                continue
                            else:
                                print("\n❌ Responde con 's' o 'n'.")
            elif respuesta in opciones_no:
                print(f"De acuerdo {nombre}, no sumaremos números 🥺")
                break
            else:
                print("\n❌ Responde con 's' o 'n'.")
    except Exception as e:
        print(f"\n⚠️ Ocurrió un error de la función principal: {e}")    
        
pedir_numeros()

"""
    Funciones propias del lenguaje (built-in)
"""

print(f"""\n
En esta sección veremos algunas funciones propias del lenguaje (built-in) de Python, no tienes que ingresar nada.
Para que entindas mejor ve a la línea 180 del archivo.
"""      
)

print((len("\nHola, estudiante")))
print((type(3.14)))
print((str.upper("hola")))
print((str.lower("HOLA")))

        
"""
    Ejercicio extra No.1 
"""

# Función con uno o varios parámetros (parámetro variable) y retorno

def imprimir_numeros(*textos)->int:
    contador = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0: 
            print(*textos)       
        elif numero % 3 == 0:
            print(textos[0])
        elif numero % 5 == 0:
            print(textos[1])
        else:
            print(numero)
            contador+=1
    return contador        

def pedir_textos():
    print(
    f"""\n
Hola de nuevo {nombre}, este es el primero de 2 ejercicios extra que realizaremos.

Consistirá en lo siguiente:

Escribirás dos cadenas de texto y retornaremos un número.
*   - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
*   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
*   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
*   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
*   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
    """
    )
    
    while True:
        permiso = quitar_tildes(input("\n¿Quieres iniciar el ejercicio? (s/n): "))
        
        if permiso in opciones_si:
            texto_1=input("\nIngresa el primer texto: ")
            texto_2=input("Ingresa el segundo texto: ")
            return imprimir_numeros(texto_1, texto_2)
        elif permiso in opciones_no:
            print("\n Okey, ejercicio finalizado 🥺🐒😭")
            break
        else:
            print("\n❌ Debes responder con 's' o 'n'")

pedir_textos()

"""

    Ejercicio extra No.2 (personal, no del reto)
"""    

def obtener_nombres_amigos()->str:
    print(f"\nGenial, ya casi llegamos al final {nombre}. En esta función saludaremos a todos tus amigos :D")
    while True:
        respuesta = quitar_tildes(input("¿Nos permites obtener los nombres de tus amigos? (s/n): ")).lower().strip()
       
        if respuesta in opciones_si:
            print("\nPerfecto, ahora deberás escribir uno por uno el nombre de tus amigos")
            lista_amigos = []
            i = 1
            try:
                while True:
                    amigo = input(f"\nIngresa el nombre de tu amigo {i}: ").strip().title()
                    if amigo == "":
                        print("No puedes dejar el nombre vacío 🙃")
                        continue
                    elif re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+", amigo):
                        lista_amigos.append(amigo)
                        i+=1
                    else: 
                        print("\nDebes ingresar un nombre válido")
                        continue
                        
                    continuar_ciclo = quitar_tildes(input("¿Deseas agregar más amigos? (s/n): ")).lower().strip()
                    if continuar_ciclo in opciones_si:
                        continue
                    elif continuar_ciclo in opciones_no:
                        saludar_amigos(*lista_amigos) 
                        return
                    else:
                        print("\nDebes responder con 's' o 'n'")
            except Exception as e:
                print(f"\nOcurrió un error: {e}") 
        elif respuesta in opciones_no:
                print("\nVale, no saludaremos a tus amigos 😔")
                break
        else:
            print("\nDebes responder con 's' o 'n'")

def saludar_amigos(*nombres)->str:    
    numero_amigos = len(nombres)
    if numero_amigos >= 10:
        print(f"\nWaos, {numero_amigos} son bastantes amigos.")
    elif numero_amigos >= 2:
        print(f"\nTienes {numero_amigos} amigos, pocos pero seguramente de calidad.")
    else:
        print(f"\nUn solo amigo, pero {nombres[0]} vale x1000")      
    for i, nombre in enumerate(nombres, start=1):
        print(f"{i}. ¡Hola, {nombre}!")

obtener_nombres_amigos()

def despedir(**datos)->str:
    print(f"\nInteresante información, con esto damos por terminado este ejercicio, {datos['nombre']}, gracias por tu tiempo.")

    respuesta_positiva = False

    while True:
        respuesta = quitar_tildes(input("Para finalizar, ¿Te gustó probar mi código? (s/n): ")).lower().strip()
        if respuesta in opciones_si:
            respuesta_positiva = True
            print("\n¡Genial!")
            break
        elif respuesta in opciones_no:
            print("\nUuh, eso dolió:(")
            break
        else: 
            print("\nTienes que escribir un valor correcto, gil.")
    
    return print(f"""
Hasta luego {'amigo' if datos['genero'] == 'Masculino' else 'amiga'} {datos['nombre']},
espero hayas tenido buenas experiencias con los {datos['edad']} años que has vivido.
{'Me alegro que te haya gustado probar mi código 🥸, eso me motiva a seguir aprendiendo' 
    if respuesta_positiva 
    else 'Lamento que no te haya gustado probar mi código 😭, trabajaré en mi lógica'}
¡Cuidate mucho!    
    """)

def mostrar_informacion(**datos)->str:
    print(f"\nOkey {nombre}, tus datos son los siguientes: ")
    for clave, valor in datos.items():
        if clave=="genero":
            print(f"Género: {valor}")
        else:
            print(f"{clave.capitalize()}: {valor}")
    return despedir(**datos)

def pedir_informacion()->str:
    while True:
        try:
            edad = int(input("\nIngresa tu edad: "))
            break
        except ValueError:
            print("Debes ingresar un número válido")
        
    while True:
        genero = input("\nGénero (M/f): ").lower().strip()
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

def pedir_permisos():
    while True:
        print(f"""\n
Muy bien {nombre}, este es el último ejercicio, lo prometo 😅
En este ejercicio tendrás que ingresar tus datos personales
        """)
         
        permiso = quitar_tildes(input("¿Estas de acuerdo en que tomemos tus datos personales? (s/n): "))
        if permiso in opciones_si:
            pedir_informacion()
            break
        elif permiso in opciones_no:
            print("\nDe acuerdo. Fin de la función.")
            break  
        else:
            print("\n❌ Debes responder con 's' o 'n'")
pedir_permisos() 