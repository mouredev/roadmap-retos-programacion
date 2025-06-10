# Simulación de navegador web con pilas
def navegador_web():
    historial_atras = []
    historial_adelante = []
    pagina_actual = None

    while True:
        accion = input("Ingresa una página web, 'atrás', 'adelante' o 'salir': ").strip().lower()

        if accion == "salir":
            print("Saliendo del navegador...")
            break
        elif accion == "atrás":
            if historial_atras:
                historial_adelante.append(pagina_actual)
                pagina_actual = historial_atras.pop()
                print(f"Yendo atrás a: {pagina_actual}")
            else:
                print("No hay páginas anteriores.")
        elif accion == "adelante":
            if historial_adelante:
                historial_atras.append(pagina_actual)
                pagina_actual = historial_adelante.pop()
                print(f"Yendo adelante a: {pagina_actual}")
            else:
                print("No hay páginas siguientes.")
        else:
            if pagina_actual:
                historial_atras.append(pagina_actual)
            pagina_actual = accion
            historial_adelante.clear()
            print(f"Navegando a: {pagina_actual}")

navegador_web()