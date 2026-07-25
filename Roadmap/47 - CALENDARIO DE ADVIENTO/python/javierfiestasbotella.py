'''
/*
 * EJERCICIO:
 * ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
 * developers. Del 1 al 24 de diciembre: https://adviento.dev
 * 
 * Dibuja un calendario por terminal e implementa una
 * funcionalidad para seleccionar días y mostrar regalos.
 * - El calendario mostrará los días del 1 al 24 repartidos
 *   en 6 columnas a modo de cuadrícula.
 * - Cada cuadrícula correspondiente a un día tendrá un tamaño 
 *   de 4x3 caracteres, y sus bordes serán asteríscos.
 * - Las cuadrículas dejarán un espacio entre ellas.
 * - En el medio de cada cuadrícula aparecerá el día entre el
 *   01 y el 24.
 *
 * Ejemplo de cuadrículas:
 * **** **** ****
 * *01* *02* *03* ...
 * **** **** ****
 *
 * - El usuario seleccioná qué día quiere descubrir.
 * - Si está sin descubrir, se le dirá que ha abierto ese día
 *   y se mostrará de nuevo el calendario con esa cuadrícula
 *   cubierta de asteríscos (sin mostrar el día).
 *
 * Ejemplo de selección del día 1
 * **** **** ****
 * **** *02* *03* ...
 * **** **** ****
 *   
 * - Si se selecciona un número ya descubierto, se le notifica
 *   al usuario.
 */
'''


dias = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
regalos = [
    "Chocolatina",
    "Chicle",
    "Mini paquete de caramelos",
    "Nota con un mensaje positivo",
    "Calcetines navideños",
    "Llavero pequeño",
    "Bálsamo labial",
    "Velita aromática",
    "Mini juguete (tipo figurita)",
    "Bolsa de té o infusión",
    "Pegatinas decorativas",
    "Lápiz o bolígrafo bonito",
    "Pequeña libreta",
    "Imán decorativo",
    "Mini botellita de gel o crema",
    "Paquete de galletas pequeñas",
    "Mini figura de madera o cerámica (como una estrella o un árbol)",
    "Esponja de baño en forma navideña",
    "Pinza para el pelo o goma elástica decorativa",
    "Set de clips de papel bonitos",
    "Mini chocolate caliente en sobre",
    "Mini adorno para el árbol de Navidad",
    "Tattoo temporal decorativo",
    "Tarjeta para escribir deseos navideños"
]
def crea_calendario(dias):
    # Inicializamos un índice para recorrer la lista 'dias'
    index = 0

    # Crear la matriz con valores de 'dias'
    matriz = []
    for _ in range(6):  # 6 filas
        fila = []
        for _ in range(4):  # 4 columnas
            # Añadir el elemento actual de 'dias' a la fila
            fila.append(f'****\n*{dias[index]}*\n****')
            index += 1  # Pasar al siguiente día
        matriz.append(fila)  # Añadir la fila a la matriz

    # Mostrar la matriz
    for fila in matriz:
        print(fila)
if __name__ == "__main__":
    while True:
        crea_calendario(dias)
        print()
        seleccion=input('Quieres seleccionar un día: s/n: ').lower()
        if seleccion=='n':
            break
        elif seleccion=='s':
            dia_seleccionado=input('Selecciona el día del calendario: ')
            if len(dia_seleccionado)<2:
                dia_seleccionado='0'+dia_seleccionado
            while True:
                if dia_seleccionado not in dias:
                    print('El día ya ha sido abierto o no existe... prueba de nuevo: \n')
                    break
                else:
                    print(f'El Regalo para el dia {dia_seleccionado} es un : {regalos[int(dia_seleccionado)-1]}\n')
                    for i in range(len(dias)):
                        if dias[i] == dia_seleccionado:
                            dias[i] = '**'
                    break        
                