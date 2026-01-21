def demostrar_operadores():
    print("\n--- 1. OPERADORES ---")
    
    # Aritméticos
    a, b = 10, 3
    print(f"Aritméticos (10 y 3): Suma={a+b}, Resta={a-b}, Mult={a*b}, Div={a/b:.2f}, Módulo={a%b}, Exp={a**b}, Div.Entera={a//b}")

    # Comparación
    print(f"Comparación: 10 > 3 es {10 > 3}, 10 == 10 es {10 == 10}, 10 != 3 es {10 != 3}")

    # Lógicos
    print(f"Lógicos: (True and False) es {True and False}, (True or False) es {True or False}, not True es {not True}")

    # Asignación (Mostrando el cambio)
    x = 5
    print(f"Asignación original: x={x}")
    x += 5  # x = x + 5
    print(f"Asignación compuesta (x+=5): x={x}")

    # Identidad (is vs ==) -> ¡Ojo aquí, importante en Python!
    lista_1 = [1, 2, 3]
    lista_2 = [1, 2, 3]
    lista_3 = lista_1
    print(f"Identidad (is): lista_1 is lista_2? {lista_1 is lista_2} (Son objetos distintos en memoria)")
    print(f"Igualdad (==): lista_1 == lista_2? {lista_1 == lista_2} (Tienen el mismo contenido)")
    print(f"Identidad (is): lista_1 is lista_3? {lista_1 is lista_3} (Apuntan al mismo espacio de memoria)")

    # Pertenencia
    fruta = "Manzana"
    print(f"Pertenencia: 'z' in 'Manzana'? {'z' in fruta}")

    # BITS (Muy importante para Ciberseguridad y redes)
    # 10 en binario es 1010
    # 3  en binario es 0011
    print(f"Bits AND (10 & 3): {10 & 3} (Binario: 0010)") 
    print(f"Bits OR  (10 | 3): {10 | 3} (Binario: 1011)")
    print(f"Bits XOR (10 ^ 3): {10 ^ 3} (Binario: 1001)") # XOR es clave en criptografía


def demostrar_estructuras_control():
    print("\n--- 2. ESTRUCTURAS DE CONTROL ---")

    # Condicionales
    user_role = "admin"
    if user_role == "admin":
        print("Condicional: Acceso total concedido (Admin).")
    elif user_role == "user":
        print("Condicional: Acceso limitado.")
    else:
        print("Condicional: Acceso denegado.")

    # Iterativa (Bucle For)
    print("Iterativa For:", end=" ")
    for i in range(1, 4):
        print(f"Intento {i}...", end=" ")
    print("Conectado.")

    # Iterativa (Bucle While)
    contador = 3
    print("Iterativa While (Cuenta regresiva):", end=" ")
    while contador > 0:
        print(contador, end="..")
        contador -= 1
    print("¡Boom!")

    # Excepciones (Try - Except - Finally)
    # Esto es vital para manejar errores sin que el programa colapse
    print("Excepciones:", end=" ")
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        print("¡Error! No puedes dividir por cero (Capturado correctamente).")
    finally:
        print("Este bloque 'finally' se ejecuta siempre, haya error o no.")


def reto_extra():
    print("\n--- 3. DIFICULTAD EXTRA (Filtrado de números) ---")
    
    # Solución "Pythonica" usando List Comprehension (En una sola línea)
    # Rango: 10 a 55 (inclusive, por eso range va hasta 56)
    numeros_filtrados = [
        n for n in range(10, 56) 
        if n % 2 == 0          # Que sea par
        and n != 16            # Que no sea 16
        and n % 3 != 0         # Que no sea múltiplo de 3
    ]
    
    print(f"Números resultantes: {numeros_filtrados}")


# --- EJECUCIÓN DEL PROGRAMA PRINCIPAL (Entry Point) ---
if __name__ == "__main__":
    demostrar_operadores()
    demostrar_estructuras_control()
    reto_extra()