def obtener_numero(mensaje):
    """
    Solicita al usuario que ingrese un número y lo devuelve.
    """
    while True:
        try:
            return float(input(f"{mensaje}: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def imprimir_resultado(nombre_operacion, resultado):
    """
    Imprime el resultado de una operación con su nombre.
    """
    print(f"{nombre_operacion}: {resultado}")

def imprimir_comparacion(nombre_operacion, comparacion):
    """
    Imprime el resultado de una comparación con su nombre.
    """
    print(f"{nombre_operacion}: {comparacion}")

def operador_de_identidad(a, b):
    """
    Verifica la identidad entre dos variables y devuelve el resultado como cadena.

    Parameters:
    - a (float): Primer variable.
    - b (float): Segunda variable.

    Returns:
    str: Cadena que indica si las dos variables son iguales o distintas.
    """
    return "Las dos variables son iguales" if a is b else "Las dos variables son distintas"

def operador_de_pertenencia(a):
    """
    Verifica si un número pertenece a un rango y devuelve el resultado como cadena.

    Parameters:
    - a (float): Número a verificar.

    Returns:
    str: Cadena que indica si el número está en el rango o no.
    """
    return f"{a} {'está' if a in range(10, 20) else 'no está'} en el rango"

def comparadores(a, b):
    """
    Realiza comparaciones entre dos números y devuelve el resultado como cadena.

    Parameters:
    - a (float): Primer número.
    - b (float): Segundo número.

    Returns:
    str: Cadena que describe el resultado de las comparaciones.
    """
    resultado = []
    if a == b:
        resultado.append("a = b")
    if a != b:
        resultado.append("a != b")
    if a > b:
        resultado.append("a > b")
    if a < b:
        resultado.append("a < b")
    if a >= b:
        resultado.append("a >= b")
    if a <= b:
        resultado.append("a <= b")
    return ", ".join(resultado)
# Solicitar números al usuario
a = obtener_numero("Escribe un numero")
b = obtener_numero("Escribe otro numero")

# Operaciones
imprimir_resultado("suma", a + b)
imprimir_resultado("resta", a - b)
imprimir_resultado("multiplicacion", a * b)
imprimir_resultado("exponente", a ** b)
imprimir_resultado("division", a / b)
imprimir_resultado("division_entera", a // b)
imprimir_resultado("resto_division", a % b)

# Comparaciones
imprimir_comparacion("comparador_and", int(a) & int(b))
imprimir_comparacion("comparador_or", int(a) | int(b))
imprimir_comparacion("comparadores", comparadores(a, b))
imprimir_comparacion("operador_de_pertenencia", operador_de_pertenencia(int(a)))
imprimir_comparacion("operador_de_identidad", operador_de_identidad(a, b))




for numero in range(10, 56):
    if numero == 16:
        continue
    elif numero%3 == 0:
        continue
    elif numero%2 == 0:
        print(numero)
