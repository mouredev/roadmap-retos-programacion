
# /*
#  * EJERCICIO:
#  * ¡Disney ha presentado un montón de novedades en su D23! 
#  * Pero... ¿Dónde está Mickey?
#  * Mickey Mouse ha quedado atrapado en un laberinto mágico 
#  * creado por Maléfica.
#  * Desarrolla un programa para ayudarlo a escapar.
#  * Requisitos:
#  * 1. El laberinto está formado por un cuadrado de 6x6 celdas.
#  * 2. Los valores de las celdas serán:
#  *    - ⬜️ Vacío
#  *    - ⬛️ Obstáculo
#  *    - 🐭 Mickey
#  *    - 🚪 Salida
#  * Acciones:
#  * 1. Crea una matriz que represente el laberinto (no hace falta
#  * que se genere de manera automática).
#  * 2. Interactúa con el usuario por consola para preguntarle hacia
#  * donde se tiene que desplazar (arriba, abajo, izquierda o derecha).
#  * 3. Muestra la actualización del laberinto tras cada desplazamiento.
#  * 4. Valida todos los movimientos, teniendo en cuenta los límites
#  * del laberinto y los obstáculos. Notifica al usuario.
#  * 5. Finaliza el programa cuando Mickey llegue a la salida.
#  */

from abc import ABC, abstractmethod
from random import randint, choice 


class VirtualBoardGenerator(ABC):
#  clase virtual para generar tablero, puede ser generado manual,  automatico o de alguna forma diferente
    @abstractmethod
    def generator(self):
        pass
    

     

class VirtualShowBoard(ABC):
    # clase virtual para mostrar el tablero, puede ser mostrado en consola, en interfaz grafica, en archivo, impreso en db
    @abstractmethod
    def ShowBoard(self):
        pass

class VirtualValidator(ABC):
#  clase virtual para validar, pueden existir diferentes tipos de validaciones
    # @abstractmethod
    # def validator(self, XYuserMove : list, XYcurrent: list):
    #     pass
    @abstractmethod
    def validator(self, data):
         pass
    
         
class VirtualMenu(ABC):

    @abstractmethod
    def boardType(self):
        pass

    @abstractmethod
    def movement(self ):
        pass

    @abstractmethod
    def userMenu(self, op: list):
        pass

class CBoard:
    def __init__(self, board: VirtualBoardGenerator):
        self._board =  board.generator()
        
        self.mikyPosition = []
        self.exitPosition = []
         
        
        


    def getBoard(self):
        return self._board
    
    def isWinner(self, pos):
         if pos == self.exitPosition:
              return True
         return False
    
    def updatePos(self, new_pos: list):
            self._board[self.mikyPosition[0]][self.mikyPosition[1]] = '⬜️'
            self._board[new_pos[0]][new_pos[1]] = '🐭'
            self.mikyPosition = new_pos
            if self.isWinner(new_pos):
                 return True
            return False

    
    def getEmpty(self):
         listEmpty = []
         for i,vi in enumerate(self._board):
              for j, vj in enumerate(vi):
                   if self._board[i][j] == '⬜️':
                        listEmpty.append([i,j])
         self.emptyPos = listEmpty
    
    def newBoard(self, board: VirtualBoardGenerator):
        self._board =  board.generator()

    def getNextPosition(self, op: str):
         newPosition = None
          
         if self.mikyPosition != None :
            if op == 'w' :
                 newPosition = [self.mikyPosition[0]-1,self.mikyPosition[1]]
            elif op == 'a':
                 newPosition = [self.mikyPosition[0],self.mikyPosition[1]-1]
            elif op == 'd':
                 newPosition = [self.mikyPosition[0],self.mikyPosition[1]+1]
            elif op == 'x':
                 newPosition = [self.mikyPosition[0]+1,self.mikyPosition[1]]
         return newPosition
                 

class CValidatorBoard(VirtualValidator):
     
     def __init__(self):
          self.input = ["q","a","m" ]
     
     def validator(self, data):
           
          return data in self.input
     
class CValidatorMovement(VirtualValidator):
     
     def __init__(self):
          self.input = ["q","a","w","d","x"]
     
     def validator(self, data):
           
          return data in self.input
     
     def _isPositionValid(self, empty:list, newPosition : list ):
          
         if newPosition in empty :
              return True
         return False
               
                   

class CShowTerminalBoard(VirtualShowBoard):
#  clase para mostrar tablero por consola, la unica por el momento
# recibe una matriz, no le interesa que es solo la muestra en consola

    def ShowBoard(self, matriz: list):
        for i in matriz:
             print(i)

class ManualBoardGeneration(VirtualBoardGenerator ):
    #  clase para generar manualmente el tablerio con posiciones fijas
     
     
    def generator(self):
        
        return  [   ['🐭','⬜️','⬜️','⬜️','⬜️','⬜️'],
                    ['⬜️','⬛️','⬛️','⬜️','⬛️','⬜️'],
                    ['⬜️','⬛️','⬜️','⬜️','⬛️','⬜️'],
                    ['⬜️','⬛️','⬜️','⬛️','⬛️','⬛️'],
                    ['⬜️','⬜️','⬜️','⬛️','⬛️','⬛️'],
                    ['⬛️','⬜️','⬜️','⬜️','⬜️','🚪']]
         
          

class RandomBoardGenerator(VirtualBoardGenerator):
#  clase para generar el tablero aleatorio
#   recibe tamano
#  devuelve tamanno, posiciones d miky, obstaculos, de salida y de espacios en blanco

    def __init__(self, col, row : int):
        self.col, self.row = col,row
         
    def _mikeyPosition(self):
        self.mikyX = randint(0,self.col)
        self.mikyY = randint(0,self.row)
         

    
    def _getMikyPosition(self):
        return [self.mikyX, self.mikyY]
    
    def _exitPosition(self):
         
        self.exitX = randint(0,self.col)
         

        match self.exitX:
            case 0 | (self.col):
                    self.exitY = randint(0,self.row)
            case _:
                 self.exitY = choice([0,self.row])
         

    def _getExitPosition(self):
         return [self.exitX, self.exitY]

    def _obstaclePosition(self):
        self.obstacleX = []
        self.obstacleY = []

        for i in range(self.col*self.row//2):
            self.obstacleX.append(randint(0,6))
            self.obstacleY.append(randint(0,6))

    def _getObstaclePosition(self):
        return self.obstacleX, self.obstacleY
    
    def generator(self):
        mikyChar,exitChar, obstChar, emptyChar = '🐭','🚪','⬛️','⬜️'

        self._mikeyPosition()
        self._exitPosition()
        self._obstaclePosition()

        self.matriz = [[emptyChar]*(self.col+1)  for _ in range(self.row+1)] 
         
        for i, vi in enumerate(self.matriz):
             print(i, vi)

        self.matriz[self.mikyX][self.mikyY] = mikyChar
        self.matriz[self.exitX][self.exitY] = exitChar

        obstPosX, obstPosY = self._getObstaclePosition() 

        for i in range(len(obstPosX)-1):
                if self.matriz[obstPosX[i]][obstPosY[i]] == emptyChar:
                    self.matriz[obstPosX[i]][obstPosY[i]] = obstChar
        
    
        return self.matriz


class CMenu(VirtualMenu):

    def __init__(self):
        self.op = 0

    def boardType(self, validator: VirtualValidator):
        
        print("Seleccione tipo de Laberinto (Aleatorio / Manual) (A/M) and Q to exit")
        return self.userMenu(validator)
        
    def movement(self, validator: VirtualValidator):
        
        print("Seleciona un movimiento valido: ")
        print(" (A Left) (W Up) (D Right) (X Down) and Q to exit")
        return self.userMenu(validator)
         

    def userMenu(self, validator: VirtualValidator):
         
        while True: 
             
            self.op = input()
            if not validator.validator(self.op):
                    print("seleccione opcion valida")
                    continue
            return self.op    



class BoardFactory:
    
    def createBoard(self,op: str):

         
            if op == "a":
                gen  = RandomBoardGenerator(6,6)
                a = CBoard(gen)
                 

                return a,{'miky':gen._getMikyPosition(), 'exit':gen._getExitPosition()}
                 
            elif op ==  "m":
                gen  = ManualBoardGeneration()
                return CBoard(gen), {'miky':[0,0], 'exit':[5,5]}
            
            elif op == "q":
                return None
                 


class Game:
#  clase orquestadora
#  recibe un tablero, y las accions a implementar
#  no le interesa mas nada, solo recibe oredenes y decide cuando y sobre que ejecutarla

    def __init__(self,):
        self.state = "INICIAL"
        self.board = None
            
    def setState(self, op: str):
        if  op == "q" or op == "WINN":
             self.state = "FIN"
         
            
    def start(self, Menu: VirtualMenu, boardfactory: BoardFactory, validator: VirtualValidator) :
                
                op = Menu.boardType(validator)
                
                self.board, itemPosition = boardfactory.createBoard(op)
                self.board.mikyPosition = itemPosition.get('miky')
                self.board.exitPosition = itemPosition.get('exit')
                self.setState(op)


    def execute(self,ShowBoard: VirtualShowBoard, menu: VirtualMenu, validator: VirtualValidator):
            
            while self.state != "FIN":
                print(" Donde esta Mikey? ")
                print()
                print("Mapa Actual")
                ShowBoard.ShowBoard(self.board.getBoard())
                op = menu.movement(validator)
                #recibo la opcion validada
                # alguien debe de recibir esa opcion y analizar si el movimiento es posible
                new_position = self.board.getNextPosition(op)
                self.board.getEmpty()
                self.board.emptyPos.append(self.board.exitPosition)
                if validator._isPositionValid(self.board.emptyPos,new_position):
                     
                     if self.board.updatePos(new_position):
                          ShowBoard.ShowBoard(self.board.getBoard())
                          self.setState("WINN")
                          print(" You are te Winner")
                          continue
                          
                else :
                     print("Movimiento imposible")

                 
                self.setState(op)

        


showBoard = CShowTerminalBoard() # lo muestro por terminal
menu = CMenu()
bf = BoardFactory()
validator_board = CValidatorBoard()
validator_mov = CValidatorMovement()
g = Game()
 

g.start(menu, bf, validator_board)
g.execute(showBoard, menu, validator_mov)  


 
 
 

