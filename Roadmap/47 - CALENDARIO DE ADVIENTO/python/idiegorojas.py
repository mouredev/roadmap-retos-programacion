""" 
# 47 - Calendario de adviento
"""
# Dibuja un calendario por terminal e implementa una funcionalidad para seleccionar días y mostrar regalos.
    # El calendario mostrará los días del 1 al 24 repartidos en 6 columnas a modo de cuadrícula.
    # Cada cuadrícula correspondiente a un día tendrá un tamaño de 4x3 caracteres, y sus bordes serán asteríscos.
    # Las cuadrículas dejarán un espacio entre ellas.
    # En el medio de cada cuadrícula aparecerá el día entre el 01 y el 24.#

# Ejemplo de cuadrículas:
    # **** **** ****
    # *01* *02* *03* ...
    # **** **** ****#

# - El usuario selecciona qué día quiere descubrir.
# - Si está sin descubrir, se le dirá que ha abierto ese día y se mostrará de nuevo el calendario con esa cuadrícula cubierta de asteríscos (sin mostrar el día).#

# Ejemplo de selección del día 1
    # **** **** ****
    # **** *02* *03* ...
    # **** **** ****#
# Si se selecciona un número ya descubierto, se le notifica al usuario.

def crear_calendario():
    # Crear un diccionario para representar el calendario
    # Días del 1 al 24, inicialmente todos sin descubrir (False)
    return {i: False for i in range(1, 25)}

def mostrar_calendario(calendario):
    # Mostrar el calendario en una cuadrícula de 6 columnas
    dias_por_fila = 6
    
    for fila in range(0, 24, dias_por_fila):
        dias_en_esta_fila = range(fila + 1, min(fila + dias_por_fila + 1, 25))
        
        # Primera línea de asteriscos (parte superior de las cuadrículas)
        for i, dia in enumerate(dias_en_esta_fila):
            print("****", end=" " if i < len(dias_en_esta_fila) - 1 else "")
        print()
        
        # Línea con los números
        for i, dia in enumerate(dias_en_esta_fila):
            if calendario[dia]:  # Si el día está descubierto
                print("****", end=" " if i < len(dias_en_esta_fila) - 1 else "")
            else:
                print(f"*{dia:02d}*", end=" " if i < len(dias_en_esta_fila) - 1 else "")
        print()
        
        # Tercera línea de asteriscos (parte inferior de las cuadrículas)
        for i, dia in enumerate(dias_en_esta_fila):
            print("****", end=" " if i < len(dias_en_esta_fila) - 1 else "")
        print()
        
        # Añadir una línea en blanco entre filas, excepto después de la última fila
        if fila + dias_por_fila < 24:
            print()

def seleccionar_dia(calendario, dia):
    if dia < 1 or dia > 24:
        print("Día inválido. Debe estar entre 1 y 24.")
        return calendario
    
    if calendario[dia]:
        print(f"El día {dia} ya ha sido descubierto.")
    else:
        calendario[dia] = True
        print(f"¡Has abierto el día {dia}!")
    
    return calendario

def main():
    calendario = crear_calendario()
    
    while True:
        mostrar_calendario(calendario)
        
        try:
            opcion = input("Selecciona un día (1-24) o 'q' para salir: ")
            
            if opcion.lower() == 'q':
                break
            
            dia = int(opcion)
            calendario = seleccionar_dia(calendario, dia)
            
        except ValueError:
            print("Entrada inválida. Ingresa un número entre 1 y 24 o 'q' para salir.")
        
        print("\n")

if __name__ == "__main__":
    main()