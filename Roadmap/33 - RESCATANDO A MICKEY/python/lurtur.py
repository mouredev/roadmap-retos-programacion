####################################
# Author: Luis Rodriguez
# GitHub: https://github/lurtur
# Date: 15 August 2024
####################################

from abc import ABC, abstractmethod
import sys

class Direction: 
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Position:
    
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


class PositionChangeEvent:

    def __init__(self, direction: Direction = None):
        self.direction: Direction = direction


class Observer(ABC):
    
    @abstractmethod
    def update(self, event: PositionChangeEvent):
        pass


class Observable(ABC):
    
    @abstractmethod
    def subscribe(self, observer: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Character(Observable):
    
    def __init__(self):
        self.observers = []

    def subscribe(self, observer: Observer):
        self.observers.append(observer)
    
    def unsubscribe(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self, event: PositionChangeEvent):
        for observer in self.observers:
            observer.update(event)

    def move_up(self):
        event = PositionChangeEvent()
        event.direction = Direction.UP
        
        self.notify(event)

    def move_down(self):
        event = PositionChangeEvent()
        event.direction = Direction.DOWN 
        
        self.notify(event)
            
    def move_right(self):
        event = PositionChangeEvent()
        event.direction = Direction.RIGHT
        
        self.notify(event)
        
    def move_left(self):
        event = PositionChangeEvent()
        event.direction = Direction.LEFT

        self.notify(event)
    

class Board(Observer):
    
    def __init__(self):
        self.board = [ 
            ['Mickey', 'Vacio', 'Vacio', 'Obstaculo', 'Obstaculo', 'Obstaculo'], 
            ['Obstaculo', 'Obstaculo', 'Vacio', 'Vacio', 'Vacio', 'Vacio'], 
            ['Obstaculo', 'Obstaculo', 'Obstaculo', 'Obstaculo', 'Obstaculo', 'Vacio'], 
            ['Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio'], 
            ['Vacio', 'Obstaculo', 'Obstaculo', 'Obstaculo', 'Obstaculo', 'Obstaculo'], 
            ['Vacio', 'Vacio', 'Vacio', 'Vacio', 'Vacio', 'Salida'], 
            ]
        self.rows = 6
        self.cols = 6
        self.character_pos = Position(0, 0)
        self.character_escaped = False
        
    def update(self, event: PositionChangeEvent):
        new_pos = Position(self.character_pos.x, self.character_pos.y)

        if event.direction == Direction.UP:
            new_pos.y -= 1
        elif event.direction == Direction.RIGHT:
            new_pos.x += 1
        elif event.direction == Direction.DOWN:
            new_pos.y += 1
        elif event.direction == Direction.LEFT:
            new_pos.x -= 1

        if self.validate_position(new_pos):
            if self.is_exit(new_pos):
                self.board[new_pos.y][new_pos.x] = 'Mickey'
                self.board[self.character_pos.y][self.character_pos.x] = 'Vacio'

                self.character_pos = new_pos

                self.character_escaped = True

            else:
                # Swap the content between the current position of the character and the new position.
                self.board[self.character_pos.y][self.character_pos.x], self.board[new_pos.y][new_pos.x] = \
                    self.board[new_pos.y][new_pos.x], self.board[self.character_pos.y][self.character_pos.x]
                
                # Update the character position
                self.character_pos = new_pos

    def is_exit(self, position: Position) -> bool:
        return (self.board[position.y][position.x] == 'Salida')

    def show(self):
        print()

        # Determine the width of the columns since the content size varies
        col_widths = [max(len(str(item)) for item in col) for col in zip(*self.board)]
        for row in self.board:
            print(" ".join(str(item).ljust(width) for item, width in zip(row, col_widths)))
        print()

    def validate_position(self, position: Position) -> False:
        result = True
        
        # Check if the position is between the limits of the board
        if position.x < 0:
            position.x = 0
            result = False
        elif position.x >= self.cols:
            position.x = self.cols
            result = False
        
        if position.y < 0:
            position.y = 0
            result = False
        elif position.y >= self.rows:
            position.y = self.rows
            result = False

        # Check if the position has an obstacle
        if (self.board[position.y][position.x] == 'Obstaculo'):
            print("|*** [ Invalid request: There is an obstacle ] ***|")
            result = False

        return result

class Commands:
    UP = '1'
    RIGHT = '2'
    DOWN = '3'
    LEFT = '4'
    QUIT = '5'

def commands_menu() -> str:
    print("+++ { Commands menu } +++")
    print("[ UP   : 1 ]")
    print("[ RIGHT: 2 ]")
    print("[ DOWN : 3 ]")
    print("[ LEFT : 4 ]")
    print("[ QUIT : 5 ]")
    option = input("Select the direction you want Mickey to move: ")
    options = f"{Commands.UP}{Commands.RIGHT}{Commands.DOWN}{Commands.LEFT}{Commands.QUIT}"

    if option in options:
        return option
        
    return -1

def main():
    board = Board()
    mickey = Character()
    mickey.subscribe(board)

    while True:
        board.show()

        if board.character_escaped:
            print("!!! -o-{ Mickey has found the exit }-o- !!!")
            sys.exit(0)

        option = commands_menu()
        if option == -1:
            print()
            print("|*** [ Invalid option ] ***|")
            print()
            continue

        if option == Commands.UP:
            mickey.move_up()
        elif option == Commands.RIGHT:
            mickey.move_right()
        elif option == Commands.DOWN:
            mickey.move_down()
        elif option == Commands.LEFT:
            mickey.move_left()
        elif option == Commands.QUIT:
            sys.exit(0)
            

main()