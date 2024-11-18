class Board():
    def __init__(self):
        # Valores de las celdas:
        self.emp = '⬜️'   # Celda vacía
        self.obs = '⬛️'   # Obstáculo
        self.mickey = '🐭' # Personaje
        self.exit = '🚪'  # Salida
        self.lifes = 3 # Vidas del mickey
        self.make_board() #crea el tablero
        self.mickey_pos = [0, 0] #Posicion inicial de mickey
    
    def make_board(self):
        # Crear un tablero 6x6 con celdas vacías
        self.board = []
        self.board.append([self.mickey, self.emp, self.emp, self.emp, self.obs, self.obs])
        self.board.append([self.obs, self.obs, self.obs, self.emp, self.emp, self.emp])
        self.board.append([self.emp, self.emp, self.emp, self.emp, self.obs, self.obs])
        self.board.append([self.emp, self.obs, self.obs, self.obs, self.emp, self.obs])
        self.board.append([self.emp, self.emp, self.emp, self.emp, self.obs, self.obs])
        self.board.append([self.obs, self.obs, self.obs, self.emp, self.emp, self.exit])  
    
    def print_board(self):        
        # Imprimir el tablero
        print('\nRESCATANDO A MICKEY')
        for fila in self.board:
            print(" ".join(fila))
        print()
    
    def move_mickey(self, direction):
        x, y = self.mickey_pos
        
        if direction == 'a': # izquierda
            new_x, new_y = x, y - 1
        
        elif direction == 'd': #derecha
            new_x, new_y = x, y + 1
        
        elif direction == 's': #abajo
            new_x, new_y = x + 1, y
        
        elif direction == 'w': #arriba
            new_x, new_y = x - 1, y
        
        elif direction == 'e': # salir
            print('Saliendo del juego...')
            return
                          
        else:
            print('\nError: Opcion incorrecta, porfavor seleccione una opción valida.\n')
        
        # verificar si la nueva posicion es correcta
        if 0 <= new_x < 6 and 0 <= new_y < 6 and self.board[new_x][new_y] != self.obs:
            # Sustituimos la casella de mickey por una vacia
            self.board[self.mickey_pos[0]][self.mickey_pos[1]] = self.emp
            # Cambiamos la posicion de mickey actual
            self.mickey_pos = [new_x, new_y]
            # Colocamos a mickey en la nueva posicion en el tablero
            self.board[new_x][new_y] = self.mickey
            # Dibujamos el tablero con la nueva posicion
            self.print_board()
        else:
            print('\nouch! Mickey se ha golpeado contra una pared!')
            self.lifes -= 1
            print(f'Pierdes una vida, vida actual: {self.lifes}\n')
                          


def play():
    # creamos el tablero
    board = Board()
    
    # Dibuja el tablero
    board.print_board()
    
    # Menu de movimientos permitidos 
    print('MOVIMIENTOS:\na = izquierda\nd = Derecha\ns = Abajo\nw = Arriba\ne = Salir\n')
    
    while True:                
        # Movemos a mickey
        move = input('Selecciona un movimiento: ')
        board.move_mickey(move)
        
        # Condiciones para terminar el juego.
        if board.mickey_pos == [5, 5]:
            print('\n¡FELICIDADES! ¡Has rescatado a Mickey!\n')
            break
        if board.lifes <= 0:
            print('¡Oh no! Mickey ha fallecido por tantos cabezazos contra la pared, lo siento.')
            break
        if move == 'e':
            break
        

if __name__ == '__main__':
    play()