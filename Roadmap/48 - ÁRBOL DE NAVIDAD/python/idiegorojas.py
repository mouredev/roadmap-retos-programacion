"""
# 48 - Arbol de navidad
"""
# Desarrolla un programa que cree un árbol de Navidad
# con una altura dinámica definida por el usuario por terminal. 
# Ejemplo de árbol de altura 5 (el tronco siempre será igual):

#     *
#    ***
#   *****
#  *******
# *********
#    |||
#    |||

# El usuario podrá seleccionar las siguientes acciones: 
    # Añadir o eliminar la estrella en la copa del árbol (@)
    # Añadir o eliminar bolas de dos en dos (o) aleatoriamente
    # Añadir o eliminar luces de tres en tres (+) aleatoriamente
    # Apagar (*) o encender (+) las luces (conservando su posición)
    # Una luz y una bola no pueden estar en el mismo sitio

# Sólo puedes añadir una estrella, y tantas luces o bolas como tengan cabida en el árbol. El programa debe notificar cada una de las acciones (o por el contrario, cuando no se pueda realizar alguna).

import random

class ArbolNavidad:
    def __init__(self, altura):
        self.altura = altura
        self.estrella = False  # Sin estrella inicialmente
        self.luces = []        # Lista de tuplas (fila, columna, encendida)
        self.bolas = []        # Lista de tuplas (fila, columna)
    
    def posicion_ocupada(self, fila, columna):
        """Comprobar si una posición ya tiene una decoración"""
        if self.estrella and fila == 0 and columna == self.altura - 1:
            return True
        
        for luz_fila, luz_col, _ in self.luces:
            if luz_fila == fila and luz_col == columna:
                return True
                
        for bola_fila, bola_col in self.bolas:
            if bola_fila == fila and bola_col == columna:
                return True
                
        return False
    
    def agregar_estrella(self):
        """Añadir una estrella a la copa del árbol"""
        if self.estrella:
            print("Ya hay una estrella en el árbol")
            return False
        
        self.estrella = True
        print("Estrella añadida")
        return True
        
    def quitar_estrella(self):
        """Quitar la estrella de la copa del árbol"""
        if not self.estrella:
            print("No hay estrella para eliminar")
            return False
            
        self.estrella = False
        print("Estrella eliminada")
        return True
    
    def agregar_bolas(self):
        """Añadir dos bolas aleatoriamente al árbol"""
        posiciones_disponibles = []
        
        # Encontrar posiciones disponibles para bolas
        for fila in range(self.altura):
            ancho = 2 * fila + 1
            for col in range(ancho):
                col_real = col + (self.altura - fila - 1)
                if not self.posicion_ocupada(fila, col_real):
                    posiciones_disponibles.append((fila, col_real))
        
        if len(posiciones_disponibles) < 2:
            print("No hay suficiente espacio para añadir más bolas")
            return False
            
        # Seleccionar dos posiciones aleatorias
        posiciones = random.sample(posiciones_disponibles, 2)
        self.bolas.extend(posiciones)
        print("Dos bolas añadidas aleatoriamente")
        return True
        
    def quitar_bolas(self):
        """Quitar dos bolas aleatoriamente del árbol"""
        if len(self.bolas) < 2:
            print(f"Solo hay {len(self.bolas)} bolas para eliminar")
            return False
            
        for _ in range(2):
            if self.bolas:
                posicion = random.choice(self.bolas)
                self.bolas.remove(posicion)
        
        print("Dos bolas eliminadas aleatoriamente")
        return True
    
    def agregar_luces(self):
        """Añadir tres luces aleatoriamente al árbol"""
        posiciones_disponibles = []
        
        # Encontrar posiciones disponibles para luces
        for fila in range(self.altura):
            ancho = 2 * fila + 1
            for col in range(ancho):
                col_real = col + (self.altura - fila - 1)
                if not self.posicion_ocupada(fila, col_real):
                    posiciones_disponibles.append((fila, col_real))
        
        if len(posiciones_disponibles) < 3:
            print("No hay suficiente espacio para añadir más luces")
            return False
            
        # Seleccionar tres posiciones aleatorias
        posiciones = random.sample(posiciones_disponibles, 3)
        self.luces.extend([(fila, col, True) for fila, col in posiciones])  # Luces comienzan encendidas (+)
        print("Tres luces añadidas aleatoriamente")
        return True
        
    def quitar_luces(self):
        """Quitar tres luces aleatoriamente del árbol"""
        if len(self.luces) < 3:
            print(f"Solo hay {len(self.luces)} luces para eliminar")
            return False
            
        for _ in range(3):
            if self.luces:
                posicion = random.choice(self.luces)
                self.luces.remove(posicion)
        
        print("Tres luces eliminadas aleatoriamente")
        return True
    
    def cambiar_luces(self, encender):
        """Encender o apagar las luces"""
        if not self.luces:
            print("No hay luces en el árbol")
            return False
            
        nuevo_estado = []
        for fila, col, _ in self.luces:
            nuevo_estado.append((fila, col, encender))
            
        self.luces = nuevo_estado
        print(f"Luces {'encendidas' if encender else 'apagadas'}")
        return True
    
    def dibujar(self):
        """Dibujar el árbol con todas las decoraciones"""
        arbol = []
        
        # Generar la forma básica del árbol
        for fila in range(self.altura):
            linea = [' '] * (2 * self.altura - 1)
            ancho = 2 * fila + 1
            col_inicio = self.altura - fila - 1
            
            for col in range(ancho):
                linea[col_inicio + col] = '*'
                
            arbol.append(linea)
        
        # Añadir el tronco
        for _ in range(2):
            linea = [' '] * (2 * self.altura - 1)
            inicio_tronco = self.altura - 2
            linea[inicio_tronco:inicio_tronco+3] = ['|', '|', '|']
            arbol.append(linea)
        
        # Añadir estrella si está presente
        if self.estrella:
            arbol[0][self.altura - 1] = '@'
        
        # Añadir luces
        for fila, col, encendida in self.luces:
            if 0 <= fila < self.altura and 0 <= col < len(arbol[fila]):
                arbol[fila][col] = '+' if encendida else '*'
        
        # Añadir bolas
        for fila, col in self.bolas:
            if 0 <= fila < self.altura and 0 <= col < len(arbol[fila]):
                arbol[fila][col] = 'o'
        
        # Convertir a cadenas y devolver
        return '\n'.join([''.join(linea) for linea in arbol])

def main():
    print("Bienvenido al generador de árboles de Navidad")
    
    while True:
        try:
            altura = int(input("Introduzca la altura del árbol (3-20): "))
            if 3 <= altura <= 20:
                break
            print("La altura debe estar entre 3 y 20")
        except ValueError:
            print("Por favor, introduzca un número válido")
    
    arbol = ArbolNavidad(altura)
    
    while True:
        print("\n" + arbol.dibujar() + "\n")
        print("Seleccione una acción:")
        print("1. Añadir estrella (@)")
        print("2. Eliminar estrella")
        print("3. Añadir bolas (o) aleatoriamente")
        print("4. Eliminar bolas aleatoriamente")
        print("5. Añadir luces (+) aleatoriamente")
        print("6. Eliminar luces aleatoriamente")
        print("7. Encender luces (+)")
        print("8. Apagar luces (*)")
        print("9. Salir")
        
        opcion = input("Elección: ")
        
        if opcion == '1':
            arbol.agregar_estrella()
        elif opcion == '2':
            arbol.quitar_estrella()
        elif opcion == '3':
            arbol.agregar_bolas()
        elif opcion == '4':
            arbol.quitar_bolas()
        elif opcion == '5':
            arbol.agregar_luces()
        elif opcion == '6':
            arbol.quitar_luces()
        elif opcion == '7':
            arbol.cambiar_luces(True)
        elif opcion == '8':
            arbol.cambiar_luces(False)
        elif opcion == '9':
            print("¡Feliz Navidad!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()