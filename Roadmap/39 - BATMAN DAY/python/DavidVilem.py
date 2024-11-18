import numpy as np
import matplotlib.pyplot as plt
import datetime

# Función para calcular Batman Day
def obtener_batman_day(anio):
    # Fecha del 1 de septiembre de cada año
    fecha_base = datetime.date(anio, 9, 1)
    # Día de la semana de esa fecha (0 es lunes)
    dia_de_la_semana = fecha_base.weekday()
    # Si no es sábado (5), nos movemos a la tercera semana (15 días más el ajuste para el sábado)
    dias_a_sumar = 14 + (5 - dia_de_la_semana)
    # El Batman Day cae en el sábado de la tercera semana de septiembre
    batman_day = fecha_base + datetime.timedelta(days=dias_a_sumar)
    return batman_day

# Función para celebrar el Batman Day hasta su 100 aniversario
def celebrar_batman_day():
    anio_actual = datetime.date.today().year
    anio_batman = 1939
    for anio in range(anio_actual, anio_batman + 101):  # Hasta el año 2039
        print(f"Batman Day en el año {anio}: {obtener_batman_day(anio)}")

# Ejecutar celebración de Batman Day
celebrar_batman_day()

# Función para encontrar el área más amenazada
def encontrar_area_critica(sensor_data, umbral):
    # Crear una matriz 20x20 para representar el mapa de Gotham
    gotham_map = np.zeros((20, 20), dtype=int)
    
    # Colocar los niveles de amenaza en la matriz
    for sensor in sensor_data:
        x, y, amenaza = sensor
        gotham_map[x, y] = amenaza
    
    # Variables para guardar el área más crítica
    max_amenaza = 0
    coord_centro_max = (0, 0)
    zona_critica = None
    
    # Recorrer la cuadrícula buscando la zona 3x3 con mayor sumatorio de amenazas
    for i in range(18):  # 18 porque estamos buscando áreas de 3x3
        for j in range(18):
            # Extraer el área 3x3
            submatriz = gotham_map[i:i+3, j:j+3]
            suma_amenazas = np.sum(submatriz)
            
            # Verificar si es la mayor suma encontrada
            if suma_amenazas > max_amenaza:
                max_amenaza = suma_amenazas
                coord_centro_max = (i+1, j+1)  # El centro de la cuadrícula 3x3
                zona_critica = (i, j)  # Guardar coordenadas superiores izquierdas del área 3x3
    
    # Calcular la distancia a la Batcueva (0,0)
    distancia_batcueva = abs(coord_centro_max[0]) + abs(coord_centro_max[1])
    
    # Verificar si se debe activar el protocolo de seguridad
    activar_protocolo = max_amenaza > umbral
    
    # Mostrar resultados
    print(f"Centro de la zona más amenazada: {coord_centro_max}")
    print(f"Suma de amenazas en la zona: {max_amenaza}")
    print(f"Distancia a la Batcueva: {distancia_batcueva}")
    if activar_protocolo:
        print("¡Protocolo de seguridad activado!")
    else:
        print("No es necesario activar el protocolo de seguridad.")
    
    # Visualizar el mapa
    visualizar_mapa(gotham_map, coord_centro_max, zona_critica, max_amenaza, activar_protocolo)

# Función para visualizar el mapa de Gotham
def visualizar_mapa(mapa, centro, zona_critica, suma_amenazas, activar_protocolo):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Mostrar la cuadrícula con el mapa de Gotham
    ax.imshow(mapa, cmap='magma', origin='upper', alpha=0.8)
    
    # Marcar los puntos de los sensores
    for i in range(20):
        for j in range(20):
            if mapa[i, j] > 0:
                ax.text(j, i, str(mapa[i, j]), ha='center', va='center', color='black', fontsize=12)
    
    # Resaltar el área más crítica (zona 3x3)
    if zona_critica:
        rect = plt.Rectangle((zona_critica[1]-0.5, zona_critica[0]-0.5), 3, 3, linewidth=5, edgecolor='red', facecolor='none')
        ax.add_patch(rect)
    
    # Título con los resultados
    titulo = f"Zona más crítica: Centro en {centro}, Amenazas = {suma_amenazas}"
    if activar_protocolo:
        titulo += " (Protocolo activado)"
    else:
        titulo += " (Protocolo no activado)"
    ax.set_title(titulo)
    
    # Configuración del gráfico
    ax.set_xticks(np.arange(20))
    ax.set_yticks(np.arange(20))
    ax.grid(True)
    ax.set_xticklabels(np.arange(20))
    ax.set_yticklabels(np.arange(20))
    
    # Mostrar el gráfico
    plt.show()

# Datos de prueba (coordenadas de sensores y su nivel de amenaza)
sensor_data = [
    (5, 5, 8), (6, 7, 8), (5, 6, 8), (14, 4, 9), (10, 3, 4),
    (15, 9, 10), (13, 5, 5), (16, 2, 7), (8, 8, 9), (12, 4, 3)
]

# Umbral de activación del protocolo de seguridad
umbral_activacion = 20

# Ejecutar el sistema de seguridad
encontrar_area_critica(sensor_data, umbral_activacion)