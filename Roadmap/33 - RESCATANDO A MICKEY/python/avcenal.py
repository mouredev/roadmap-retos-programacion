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
#A pesar de que en el ejercicio no se pide, el programa genera el laberinto de manera automática
#Esto tiene varias limitaciones a nivel de cuántos obstáculos se pueden colocar para que el juego tenga solución

from abc import ABC,abstractmethod
from random import randint,shuffle
from math import ceil

#Clases Abstractas
class AbstractBoardGenerator(ABC):
    @abstractmethod
    def create_board(self):
        pass

class AbstractPlaceMickeyAndExit(ABC):
    @abstractmethod
    def place_mickey_and_exit(self,board:AbstractBoardGenerator):
        pass

class AbstractObstaclesGenerator(ABC):
    @abstractmethod
    def place_obstacles(self,board:AbstractBoardGenerator):
        pass

class AbstractBoardChecker(ABC):
    @abstractmethod
    def confirm_board(self,board:AbstractBoardGenerator):
        pass

class AbstractBoardPrinter(ABC):
    @abstractmethod
    def print_board(self,board:AbstractBoardGenerator):
        pass

class AbstractMickeyMove(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_right(self):
        pass

class AbstractMoveChecker(ABC):
    @abstractmethod
    def check_move(self,board:AbstractBoardGenerator):
        pass

#Clases del programa que implementan las abstractas

#Clase que se ocupa de colocar a Mickey y la Salida
class PlaceMickeyAndExit(AbstractPlaceMickeyAndExit):
    def place_mickey_and_exit(self,board:AbstractBoardGenerator):
        while True:
            mickey_row = randint(0,board.number_of_rows-1)
            mickey_column = randint(0,board.number_of_columns-1)
            if mickey_row == 0:
                out_row = 5
                out_column = randint(0,board.number_of_columns-1)
                break
            elif mickey_row == 5:
                out_row = 0
                out_column = randint(0,board.number_of_columns-1)
                break
            else:
                if mickey_column == 0:
                    out_column = board.number_of_columns-1
                    out_row = randint(0,board.number_of_rows-1)
                    break
                elif mickey_column == board.number_of_columns-1:
                    out_column = 0
                    out_row = randint(0,board.number_of_rows-1)
                    break

        board.board[mickey_row][mickey_column] = "🐭"
        board.board[out_row][out_column] = "🚪"
        return mickey_row,mickey_column,out_row,out_column

class ObstaclesGenerator(AbstractObstaclesGenerator):
    #Método privado que genera 2 obstáculos por cuadrante de manera aleatoria
    def __set_obstacles_in_cuadrant(self,board:AbstractBoardGenerator,rows_start:int,rows_limit:int,columns_start:int,columns_limit:int,number_of_obstacles:int):
        index = 0
        positions = [(row, col) for row in range(rows_start, rows_limit + 1) for col in range(columns_start, columns_limit + 1)]
        shuffle(positions)  # Mezclar posiciones para seleccionar aleatoriamente
        while index < number_of_obstacles:
            row, column = positions.pop()
            if board.board[row][column] == "⬜️":
                board.board[row][column] = "⬛️"
            index +=1
    #método que calcula cuántos obstáculos se han de colocar por cuadrante según el tamaño del tablero (2 en este ejercicio) y usa __set_obstacles_in_cuadrant para generarlos
    def place_obstacles(self,board:AbstractBoardGenerator):
        NUMBER_OF_OBSTACLES = ceil((board.number_of_rows*board.number_of_columns)*2/9/4) #la proporcion es 9/2, por cada 9 casillas se ponen un máximo de 2 obstáculos para que el laberinto tenga solución. El resultado se divide entre 4 cuadrantes
        #primer cuadrante
        rows_start = 0
        rows_limit = int(board.number_of_rows/2-1)
        colunms_start = 0
        columns_limit = int(board.number_of_columns/2-1)
        self.__set_obstacles_in_cuadrant(board,rows_start,rows_limit,colunms_start,columns_limit,NUMBER_OF_OBSTACLES)
        #segundo cuadrante
        rows_start = int(board.number_of_rows/2)
        rows_limit = board.number_of_rows-1
        colunms_start = 0
        columns_limit = int(board.number_of_columns/2-1)
        self.__set_obstacles_in_cuadrant(board,rows_start,rows_limit,colunms_start,columns_limit,NUMBER_OF_OBSTACLES)
        #tercer cuadrante
        rows_start = 0
        rows_limit = int(board.number_of_rows/2-1)
        colunms_start = int(board.number_of_columns/2)
        columns_limit = board.number_of_columns-1
        self.__set_obstacles_in_cuadrant(board,rows_start,rows_limit,colunms_start,columns_limit,NUMBER_OF_OBSTACLES)
        #cuarto cuadrante
        rows_start = int(board.number_of_rows/2)
        rows_limit = board.number_of_rows-1
        colunms_start = int(board.number_of_columns/2)
        columns_limit = board.number_of_columns-1
        self.__set_obstacles_in_cuadrant(board,rows_start,rows_limit,colunms_start,columns_limit,NUMBER_OF_OBSTACLES)

class BoardChecker(AbstractBoardChecker): #comprueba que ni Mickey ni la salida están bloqueados por obstáculos
    def __check_position(self,board:AbstractBoardGenerator,row:int,column:int): #este método privado revisa que Mickey o la Salida no estén rodeados por obstáculos devolviendo un boolean
        valid_position = True
        if row == 5:
            if board.board[row-1][column] == "⬛️" and board.board[row][column-1] == "⬛️" and board.board[row][column+1] == "⬛️":
                valid_position = False
        elif column == 5:
            if board.board[row-1][column] == "⬛️" and board.board[row+1][column] == "⬛️" and board.board[row][column-1] == "⬛️":
                valid_position = False
        elif row == 0:
            if board.board[row][column+1] == "⬛️" and board.board[row+1][column] == "⬛️" and board.board[row][column-1] == "⬛️":
                valid_position = False
        elif column == 0:
            if board.board[row-1][column] == "⬛️" and board.board[row+1][column] == "⬛️" and board.board[row][column+1] == "⬛️":
                valid_position = False
        elif row == 0 and column == 0:
            if board.board[row+1][column] == "⬛️" and board.board[row][column+1] == "⬛️":
                valid_position = False
        elif row == 5 and column == 5:
            if board.board[row-1][column] == "⬛️" and board.board[row][column-1] == "⬛️":
                valid_position = False
        elif row == 0 and column == 5:
            if board.board[row+1][column] == "⬛️" and board.board[row][column-1] == "⬛️":
                valid_position = False
        elif row == 5 and column == 0:
            if board.board[row-1][column] == "⬛️" and board.board[row][column+1] == "⬛️":
                valid_position = False
        else:
            if board.board[row-1][column] == "⬛️" and board.board[row+1][column] == "⬛️" and board.board[row][column-1] == "⬛️" and board.board[row][column+1] == "⬛️":
                valid_position = False

        return valid_position

    #Este método confirma el tablero apoyándose en __check_position. Si Mickey o la salida están rodeados, genera un nuevo tablero y lo comprueba de manera recursiva
    def confirm_board(self, board: AbstractBoardGenerator,place_mickey_and_exit:AbstractPlaceMickeyAndExit,obstacle_generator:AbstractObstaclesGenerator):
        if not self.__check_position(board,board.mickey_row,board.mickey_column) or not self.__check_position(board,board.out_row,board.out_column):
            board.create_blank_board()
            board.mickey_row,board.mickey_column,board.out_row,board.out_column = place_mickey_and_exit.place_mickey_and_exit(board)
            obstacle_generator.place_obstacles(board)
            self.confirm_board(board,place_mickey_and_exit,obstacle_generator)
        else:
            pass

class BoardPrinter(AbstractBoardPrinter): #imprime el tablero por consola
    def print_board(self,board:AbstractBoardGenerator):
        row_printed = ""
        index = 0
        for row in board.board:
            for index,column in enumerate(row):
                if index == len(row)-1:
                    row_printed += f"{row[index]}\n"
                else:
                    row_printed += f"{row[index]}  "
            print (row_printed)
            row_printed = ""

class BoardGenerator(AbstractBoardGenerator): #genera el tablero en blanco y usa el resto de métodos para generar los obstáculos y colocar a Mickey y la salida
    def create_blank_board(self):
        for i in range (0,self.number_of_rows):
            row = []
            for index in range(0,self.number_of_columns):
                row.append("⬜️")
            self.board.append(row)

    def create_board(self,number_of_rows:int,number_of_columns:int,place_mickey_and_exit:AbstractPlaceMickeyAndExit,place_obstacles:AbstractObstaclesGenerator,confirm_board:AbstractBoardChecker):
        self.number_of_rows:int = number_of_rows
        self.number_of_columns:int = number_of_columns
        self.board:list = []
        self.create_blank_board()
        self.mickey_row,self.mickey_column,self.out_row,self.out_column = place_mickey_and_exit.place_mickey_and_exit(self)
        place_obstacles.place_obstacles(self)
        confirm_board.confirm_board(self,place_mickey_and_exit,place_obstacles)
        return self.mickey_row,self.mickey_column,self.out_row,self.out_column

class MoveChecker(AbstractMoveChecker): #con este método comprueba que el movimiento es válido y si ha llegado a la salida o no.
    def check_move(self,board:AbstractBoardGenerator,move:AbstractMickeyMove):
        exit = False
        if move.up:
            if board.mickey_row == 0:
                print("Mickey no puede avanzar en esa dirección, se chocaría con la pared del laberinto\n")
                move.up = False
            else:
                row = board.mickey_row
                board.mickey_row -= 1
                if board.board[board.mickey_row][board.mickey_column] == "🚪":
                    board.board[row][board.mickey_column] ="⬜️"
                    print("¡Mickey ha conseguido salir del laberinto!\n")
                    exit = True
                elif board.board[board.mickey_row][board.mickey_column] != "⬛️":
                        board.board[board.mickey_row][board.mickey_column] = "🐭"
                        board.board[row][board.mickey_column] ="⬜️"
                        move.up = False
                else:
                    print("Mickey no se puede mover ahi, hay un obstáculo en el camino\n")
                    board.mickey_row = row
                    move.up = False
        elif move.down:
            row = board.mickey_row
            try:
                board.mickey_row +=1
                if board.board[board.mickey_row][board.mickey_column] == "🚪":
                    board.board[row][board.mickey_column] ="⬜️"
                    print("¡Mickey ha conseguido salir del laberinto!\n")
                    exit = True
                elif board.board[board.mickey_row][board.mickey_column] != "⬛️":
                        board.board[board.mickey_row][board.mickey_column] = "🐭"
                        board.board[row][board.mickey_column] ="⬜️"
                        move.down = False
                else:
                    print("Mickey no se puede mover ahi, hay un obstáculo en el camino\n")
                    board.mickey_row = row
                    move.down = False
            except IndexError:
                print("Mickey no puede avanzar en esa dirección, se chocaría con la pared del laberinto\n")
                move.down = False
        elif move.left:
            if board.mickey_column == 0:
                print("Mickey no puede avanzar en esa dirección, se chocaría con la pared del laberinto\n")
                move.left = False
            else:
                column = board.mickey_column
                board.mickey_column -= 1
                if board.board[board.mickey_row][board.mickey_column] == "🚪":
                    board.board[board.mickey_row][column] ="⬜️"
                    print("¡Mickey ha conseguido salir del laberinto!\n")
                    exit = True
                elif board.board[board.mickey_row][board.mickey_column] != "⬛️":
                    board.board[board.mickey_row][board.mickey_column] = "🐭"
                    board.board[board.mickey_row][column] ="⬜️"
                    move.left = False
                else:
                    print("Mickey no se puede mover ahi, hay un obstáculo en el camino\n")
                    board.mickey_column = column
                    move.left = False
        elif move.right:
            column = board.mickey_column
            try:
                board.mickey_column += 1
                if board.board[board.mickey_row][board.mickey_column] == "🚪":
                    board.board[board.mickey_row][column] ="⬜️"
                    print("¡Mickey ha conseguido salir del laberinto!\n")
                    exit = True
                elif board.board[board.mickey_row][board.mickey_column] != "⬛️":
                    board.board[board.mickey_row][board.mickey_column] = "🐭"
                    board.board[board.mickey_row][column] ="⬜️"
                    move.right = False
                else:
                    print("Mickey no se puede mover ahi, hay un obstáculo en el camino\n")
                    board.mickey_column = column
                    move.right = False
            except IndexError:
                print("Mickey no puede avanzar en esa dirección, se chocaría con la pared del laberinto\n")
                move.right = False
        return exit

class MickeyMove(AbstractMickeyMove): #clase para el movimiento de Mickey
    def __init__(self):
        self.up:bool = False
        self.down:bool = False
        self.right:bool = False
        self.left:bool = False

    def move_up(self):
        self.up = True
        return self

    def move_down(self):
        self.down = True
        return self

    def move_left(self):
        self.left = True
        return self

    def move_right(self):
        self.right = True
        return self

exit = False
NUMBER_OF_ROWS = 6 #se podría solicitar el tamaño del tablero por consola.
NUMBER_OF_COLUMNS = 6
board = BoardGenerator()
mickey_row,mickey_column,out_row,out_column = board.create_board(NUMBER_OF_ROWS,NUMBER_OF_COLUMNS,PlaceMickeyAndExit(),ObstaclesGenerator(),BoardChecker())
board_printer = BoardPrinter()
print("Te doy la bienvenida al Laberinto del D23 en el que tendrás que ayudar a Mickey a escapar\n")
board_printer.print_board(board)
print("\n")
mickey_move = MickeyMove()
move_checker = MoveChecker()
while not exit:
    input_move = input("¿Hacia donde quieres mover a Mickey?\n- Arriba (U)\n- Abajo (D)\n- Izquierda (L)\n- Derecha (R)\n Introduce el movimiento por favor: ").upper()
    if input_move == "U":
        move = mickey_move.move_up()
    elif input_move == "D":
        move = mickey_move.move_down()
    elif input_move == "L":
        move = mickey_move.move_left()
    elif input_move == "R":
        move = mickey_move.move_right()
    else:
        print("Vaya, parece que Mickey no puede hacer ese movimiento, probemos de nuevo...")
    exit = move_checker.check_move(board,move)
    board_printer.print_board(board)
    print("\n")

print("Enhorabuena y gracias por ayudar a Mickey a salir del laberinto. Hasta pronto.")
