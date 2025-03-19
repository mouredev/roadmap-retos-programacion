# 21 - CALLBACKS

# Ejercicio

""" Un callback es una función que se pasa como argumento a otra función.
Esta función "callback" se invoca en algún punto de la ejecución de
la función que la recibe como argumento."""


import random
import time


def conversion_F_a_C(temperatura: float, funcion):
    # Funcion que pasa grados Farengheint a grados Centigrados
    resultado = temperatura-32 * 0.555
    funcion(resultado)


def mostrar_resultado(resultado):
    print(f"El resultado es: {resultado}")


conversion_F_a_C(46.5, mostrar_resultado)


# Dificultad Extra


def confirmar_menu(mensaje):
    while True:
        respuesta = input(f"{mensaje} (sí/no): ").strip().lower()
        if respuesta == "sí" or respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Respuesta no válida. Por favor responde 'sí' o 'no'.")


def pedido_listo(menu, cliente):
    print(f"El menú {menu} del cliente {
          cliente} está listo para ser entregado.")


def pedido_en_entrega(menu, cliente):
    print(f"El menú {menu} del cliente {cliente} fue entregado.")


def simulador_de_pedidos(confirmacion=pedido_listo, servicio=pedido_listo, entrega=pedido_en_entrega):
    print("Iniciando el procesamiento del pedido...")
    id = list(range(1, 11))
    try:
        menu = int(input("Seleccione un menú (1-10): "))
    except ValueError:
        print("Debes proporcionar un número válido para el menú.")
        return

    cliente = input("Indica el número de cliente: ").strip()

    if not cliente:
        print("Debes proporcionar un número de cliente.")
        return

    if menu in id:
        print(f"Ud. ha elegido el menú número {menu}.")
    else:
        print(f"Ud. ha elegido el menú número {
              menu} que no está dentro de nuestra carta, seleccione nuevamente.")
        return

    if confirmar_menu("¿Confirma su elección?"):
        print("Confirmando menú, se envía a cocina...")
        time.sleep(random.randint(1, 10))
        if confirmacion:
            confirmacion(menu, cliente)
    else:
        print("Acción cancelada")
        return

    print("Preparando el pedido...")
    time.sleep(random.randint(1, 10))
    if servicio:
        servicio(menu, cliente)

    print("Entregando el pedido...")
    time.sleep(random.randint(1, 10))
    if entrega:
        entrega(menu, cliente)


# Ejemplo de uso
simulador_de_pedidos()
