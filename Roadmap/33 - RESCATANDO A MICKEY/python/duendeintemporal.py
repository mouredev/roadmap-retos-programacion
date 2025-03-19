#33 { Retos para Programadores } RESCATANDO A MICKEY 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
* EJERCICIO:
 * ¡Disney ha presentado un montón de novedades en su D23!
 * Pero... ¿Dónde está Mickey?
 * Mickey Mouse ha quedado atrapado en un laberinto mágico
 * creado por Maléfica.
 * Desarrolla un programa para ayudarlo a escapar.
 * Requisitos:
 * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
 * 2. Los valores de las celdas serán:
 *    - ⬜️ Vacío
 *    - ⬛️ Obstáculo
 *    - 🐭 Mickey
 *    - 🚪 Salida
 * Acciones:
 * 1. Crea una matriz que represente el laberinto (no hace falta
 * que se genere de manera automática).
 * 2. Interactúa con el usuario por consola para preguntarle hacia
 * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
 * 3. Muestra la actualización del laberinto tras cada desplazamiento.
 * 4. Valida todos los movimientos, teniendo en cuenta los límites
 * del laberinto y los obtáculos. Notifica al usuario.
 * 5. Finaliza el programa cuando Mickey llegue a la salida.

"""

""" 
Note: If you are using Command Prompt(cmd or Shell in Windows), you may need to change the code page to UTF-8 to properly display emojis. You can do this by running the following command before executing your script:

chcp 65001

Also set the font type to: Segoe UI Emoji or Noto Color Emoji is available. (if this doesn't work you will need to install Windows Terminal to to properly display emojis)

"""

log = print

import random

# Constants for the maze
obstacle = '\u2B1B'  # ⬛️ Obstacle
empty_space = '\u2B1C'  # ⬜️ Empty space
mickey = '\U0001F42D'  # 🐭 Mickey
exit = '\U0001F6AA'  # 🚪 Exit

# Start position for Mickey
position = {'x': 0, 'y': 0}

# Function to generate a random maze with obstacles
def generate_random_maze(size):
    maze = [[obstacle if random.random() < 0.4 else empty_space for _ in range(size)] for _ in range(size)]
    maze[0][0] = mickey  # Start position
    maze[size - 1][size - 1] = exit  # Exit position
    return maze

# Function to carve a path in the maze using Dijkstra's algorithm
def dijkstra(maze):
    size = len(maze)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    distances = [[float('inf')] * size for _ in range(size)]
    previous = [[None] * size for _ in range(size)]
    distances[0][0] = 0  # Distance from the entrance is 0
    queue = [(0, 0, 0)]  # (x, y, distance)

    while queue:
        x, y, distance = queue.pop(0)

        if distance > distances[y][x]:
            continue  # If the distance is greater than the current distance, do nothing

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < size and 0 <= new_y < size:
                new_distance = distance + (10 if maze[new_y][new_x] == obstacle else 1)

                if new_distance < distances[new_y][new_x]:
                    distances[new_y][new_x] = new_distance
                    previous[new_y][new_x] = (x, y)
                    queue.append((new_x, new_y, new_distance))

    # Reconstruct the shortest path
    path = []
    x, y = size - 1, size - 1

    while (x, y) != (0, 0):
        if previous[y][x] is None:
            break  # No valid path found
        path.append((x, y))
        x, y = previous[y][x]
    path.reverse()  # Reverse the path to get it from start to exit

    # If a path is found, mark it
    if path:
        for x, y in path:
            maze[y][x] = empty_space  # Mark the path with an empty space

    maze[size - 1][size - 1] = exit  # Ensure exit is not overwritten
    return path

# Function to display the maze
def display_maze(maze):
    print('\nMaze:\n')
    for row in maze:
        print(' '.join(row))
    print('\n')

# Function to move Mickey
def move_mickey(direction, maze):
    global position
    new_position = position.copy()

    # Update new position based on the direction
    if direction == "w":
        new_position['y'] -= 1  # up
    elif direction == "s":
        new_position['y'] += 1  # down
    elif direction == "a":
        new_position['x'] -= 1  # left
    elif direction == "d":
        new_position['x'] += 1  # right

    # Check if the new position is within the bounds of the board
    if (0 <= new_position['x'] < len(maze[0]) and
            0 <= new_position['y'] < len(maze)):
        # Check if the new position is a wall or path
        if maze[new_position['y']][new_position['x']] == obstacle:
            print("Mickey 🐭 has hit a wall ⬛️, try moving in another direction.")
            return False  # Movement failed due to wall
        elif maze[new_position['y']][new_position['x']] == exit:
            print("\nCongratulations! You won! Mickey 🐭 has escaped the maze.")
            maze[position['y']][position['x']] = empty_space  # Empty the cell
            position = new_position
            maze[position['y']][position['x']] = mickey  # Move
            maze[position['y']][position['x']] = mickey  # Move 🐭 Mickey 
            return True  # Movement successful and game won
        else:
            # Update the position of the player
            maze[position['y']][position['x']] = empty_space  # Empty the cell
            position = new_position
            maze[position['y']][position['x']] = mickey  # Move 🐭 Mickey 
            return True  # Movement successful
    else:
        print("Mickey 🐭 cannot move outside the maze, try moving in another direction.")
        return False  # Movement failed due to out of bounds

# Main function to start the game
def main():
    maze_size = int(input('Enter the size of the maze (between 7 and 15): '))
    
    # Validate the maze size input
    if maze_size < 7 or maze_size > 15:
        print('Please enter a valid number between 7 and 15.')
        return
    
    # Generate the random maze
    maze = generate_random_maze(maze_size)
    
    # Carve a path in the maze using Dijkstra's algorithm
    dijkstra(maze)
    
    # Display the generated maze
    display_maze(maze)

    # Start the game loop
    while True:
        direction = input("Choose a direction to move (up - w, down - s, left - a, right - d): ").lower()
        if move_mickey(direction, maze):
            display_maze(maze)  # Display the maze after the move
            if maze[position['y']][position['x']] == exit:
                break  # Exit the loop if Mickey has reached the exit
        else:
            display_maze(maze)  # Display the maze after an unsuccessful move

if __name__ == "__main__":
    main()  # Start the game
