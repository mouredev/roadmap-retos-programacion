### RESCATANDO A MICKEY
import random as rnd

def generate_maze() -> list :
    
    maze = []
    empty_row = ['obstaculo', 'vacio', 'vacio', 'vacio', 'vacio', 'obstaculo']
    border_sup_inf = ['obstaculo','obstaculo','obstaculo','obstaculo','obstaculo','obstaculo']

    # Generamos el maze vacío y con los obstáculos en los extremos.
    maze.append(border_sup_inf.copy())
    for i in range(1, 5):
        maze.append(empty_row.copy())
    maze.append(border_sup_inf.copy())
    
    #Dejamos también vacías las posiciones (1,0) y (0,1) para poder movernos
    maze[1][0] = 'vacio'
    maze[0][1] = 'vacio'

    # Elegimos de manera aleatoria donde vamos a colocar la salida
    row_out = 5 # Siempre tomaremos la última fila de momento.
    col_out = rnd.randint(1, 5)
    maze[row_out][col_out] = 'salida'

    # Colocamos de manera aleatoria a Mickey dentro del tablero
    row_mickey = rnd.randint(1, 4)
    col_mickey = rnd.randint(1, 4)
    maze[row_mickey][col_mickey] = 'mickey'
    
    # La posición 0,0 serla el punto de entrada
    maze[0][0] = 'vacio'
    
    return maze

def check_obstacle(x: int, y: int, matrix: list) -> bool:
    if matrix[x][y] == 'obstaculo':
        return True
    return False

def check_mickey(x: int, y: int, matrix: list) -> bool:
    if matrix[x][y] == 'mickey':
        return True
    return False

maze = generate_maze()

for row in maze:
    print(row)

exit = False
position = [0,0]
founded = False

while not exit:
    # Preguntamos al usuario qué acción quiere realizar.
    print(f"Tu posición actual es [{position[0]}, {position[1]}]")
    action = input("Indica la acción a realizar (u - arriba, d - abajo, l - izquierda, r - derecha, e - exit): ")
    while action[0].lower() not in ['u', 'd', 'l', 'r', 'e']:
        print("Error: Introduce un valor correcto para el movimiento")
        action = input("Indica la acción a realizar (u - arriba, d - abajo, l - izquierda, r - derecha): ")
    
    if action[0].lower() == 'e':
        exit = True
        break
    
    match action[0].lower():
        case 'u':
            if check_mickey(x=position[0] - 1, y=position[1], matrix=maze):
                founded = True
                print('¡Mickey está aquí!')
                position[0] -= 1
            else:
                if not check_obstacle(x=position[0] - 1, y=position[1], matrix=maze):
                    position[0] -= 1
                else:
                    print('Hay un obstáculo, no te puedes mover ahí')
        case 'd':
            if check_mickey(x=position[0] + 1, y=position[1], matrix=maze):
                founded = True
                print('¡Mickey está aquí!')
                position[0] += 1
            else:
                if not check_obstacle(x=position[0] + 1, y=position[1], matrix=maze):
                    position[0] += 1
                else:
                    print('Hay un obstáculo, no te puedes mover ahí')
        case 'l':
            if check_mickey(x=position[0], y=position[1] - 1, matrix=maze):
                founded = True
                print('¡Mickey está aquí!')
                position[1] -= 1
            else:
                if not check_obstacle(x=position[0], y=position[1] - 1, matrix=maze):
                    position[1] -= 1
                else:
                    print('Hay un obstáculo, no te puedes mover ahí')
        case 'r':
            if check_mickey(x=position[0], y=position[1] + 1, matrix=maze):
                founded = True
                print('¡Mickey está aquí!')
                position[1] += 1
            else:
                if not check_obstacle(x=position[0], y=position[1] + 1, matrix=maze):
                    position[1] += 1
                else:
                    print('Hay un obstáculo, no te puedes mover ahí')

if founded:
    print(f'Enhorabuena, pudiste rescatar a Mickey!!!')
print('Fin del juego')
### FIN RESCATANDO A MICKEY