# Funciones:

def imprimir_mensaje():
    print("Aprendiendo Python desde cero con el profe Mouredev\n")

# Definimos una funcion que sera pasada como parametro
def saludar(nombre):
    return f"Hola, {nombre}!"

# Definimos otra funcion que recibe una función como parametro
def ejecutar_funcion(funcion, argumento):
    return funcion(argumento)

# Usamos la funcion
resultado = ejecutar_funcion(saludar, "lPassword012")
print(resultado)  # Salida: Hola, lPassword012!
imprimir_mensaje()

# Variables locales y globales:
nombre_usuario = "lPassword012"

def modificar_primer_mensaje():
    usuario_incorrecto = "lPassword123" # Variable local.
    return usuario_incorrecto

def modificar_segundo_mensaje():
    global nombre_usuario  # Permite modificar la variable global dentro de la función
    print("Comprobando nombre de usuario: ",nombre_usuario) # Comprobamos que valor tiene nombre_usuario.
    print("Usuario registrado.\n")
    nombre_usuario =  modificar_primer_mensaje()
    print("Incorrecto, usuario no registrado.",nombre_usuario)
    print("Intente nuevamente!\n")

print("Incorrecto, usuario no registrado.",modificar_segundo_mensaje()) # La funcion no retorna ningun valor.
print("\nComprando si el usuario existe.",nombre_usuario)
print("Intente nuevamente!\n")


# Primero se llama a la funcion modificar_segundo_mensaje(), dentro de la funcion se llama a otra funcion.
# modificar_primer_mensaje() que retorna un valor que se asigna a nombre_usuario (global).
# pero modificar_segundo_mensaje() no retorna nada y devuelve None. Por ultimo.
# imprimimos un el valor de la variable global.

# Ejercicio extra:
def imprimir_numeros(cadena1: str, cadena2: str) -> list[int]:
    contador = 0
    numeros_sin_remplazos: list[int] = []
    
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            continue
        elif numero % 3 == 0:
            continue
        elif numero % 5 == 0:
            continue
        else:
            contador += 1
            numeros_sin_remplazos.append(numero)  # Se almacena el numero, no el contador

    return numeros_sin_remplazos

# Imprimo el arreglo y muestro la longitud
cantidad_impresa = imprimir_numeros("numero1", "numero2")
print(f"\nColeccion de numeros sin reemplazo:\n\n{cantidad_impresa}\n\nCantidad total de numeros: {len(cantidad_impresa)}")

# Nota: Para resolver el ejercicio ademas de obtener la solucion, aprendi sobre el tipado estricto en Python. 
# Usando 'mypy strict mode'. Requiere anotaciones de tipo explicitas en funciones y variables.
# Ademas, modifique la solucion para retonar una lista de los n numeros y manipularlos en el futuro.
