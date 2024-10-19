# /*
#  * EJERCICIO:
#  * ¡El último videojuego de Dragon Ball ya está aquí!
#  * Se llama Dragon Ball: Sparking! ZERO.
#  *
#  * Simula un Torneo de Artes Marciales, al más puro estilo
#  * de la saga, donde participarán diferentes luchadores, y el
#  * sistema decidirá quién es el ganador.
#  *
#  * Luchadores:
#  * - Nombre.
#  * - Tres atributos: velocidad, ataque y defensa
#  *   (con valores entre 0 a 100 que tú decidirás).
#  * - Comienza cada batalla con 100 de salud.
#  * Batalla:
#  * - En cada batalla se enfrentan 2 luchadores.
#  * - El luchador con más velocidad comienza atacando.
#  * - El daño se calcula restando el daño de ataque del
#  *   atacante menos la defensa del oponente.
#  * - El oponente siempre tiene un 20% de posibilidad de
#  *   esquivar el ataque.
#  * - Si la defensa es mayor que el ataque, recibe un 10%
#  *   del daño de ataque.
#  * - Después de cada turno y ataque, el oponente pierde salud.
#  * - La batalla finaliza cuando un luchador pierde toda su salud.
#  * Torneo:
#  * - Un torneo sólo es válido con un número de luchadores
#  *   potencia de 2.
#  * - El torneo debe crear parejas al azar en cada ronda.
#  * - Los luchadores se enfrentan en rondas eliminatorias.
#  * - El ganador avanza a la siguiente ronda hasta que sólo
#  *   quede uno.
#  * - Debes mostrar por consola todo lo que sucede en el torneo,
#  *   así como el ganador.
#  */
import random

class Stat():
    """
        Clase que representa a los stats de un luchador.
    """
    def __init__(self, velocidad, ataque, defensa):
        self.velocidad = velocidad
        self.ataque = ataque
        self.defensa = defensa
        self.vida = 100

class Luchador():
    """
        Clase que representa a un luchador
    """

    def __init__(self, nombre:str, stats:Stat) -> None:
        self.nombre = nombre
        self.stats = stats

    def esquiva(self):
        return random.randint(1,100) <= 20

    def cal_defensa_mayor_que_ataque(self, luchador_2)-> bool:
        return True if self.stats.ataque < luchador_2.stats.defensa else False
    
    def restablecer_vida(self)-> None:
        self.stats.vida = 100
    def es_golpe_critico(self) -> bool:
        return random.randint(0,100) <= 15

class Batalla():
    """
        Clase que representa el esenario de una batalla.
    """
    __DANY_MINIM = 5
    def __init__(self, luchador_1: Luchador, luchador_2: Luchador) -> None:
        self.luchador_1 = luchador_1
        self.luchador_2 = luchador_2
        self.turno = True
        self.batalla = True
        self.mas_rapido()
        if self.turno:
            print(f"El luchador {self.luchador_1.nombre} es el más rápido y comienza atacando.")
        else:
            print(f"El luchador {self.luchador_2.nombre} es el más rápido y comienza atacando.")



    def mas_rapido(self)-> bool:
        self.turno = True if self.luchador_1.stats.velocidad >= self.luchador_2.stats.velocidad else False
    

    def cal_defensa(self)-> bool:
        atacante = self.luchador_1 if self.turno else self.luchador_2
        defensor = self.luchador_2 if self.turno else self.luchador_1
        if atacante.cal_defensa_mayor_que_ataque(defensor):
            contra_ataque = defensor.stats.ataque*0.1
            atacante.stats.vida -=contra_ataque
            print(f"La defensa de {defensor.nombre} supera el ataque de {atacante.nombre}.")
            print(f"{defensor.nombre} recibe {contra_ataque} puntos de daño por rebote.")
            return False
        return True



    
    def batallar(self)-> None:
        while self.batalla:
            if self.cal_defensa():
                atacante = self.luchador_1 if self.turno else self.luchador_2
                defensor = self.luchador_2 if self.turno else self.luchador_1

                if defensor.esquiva():
                    print(f"{defensor.nombre} ha esquivado el ataque de {atacante.nombre}.")
                else:
                    if atacante.es_golpe_critico():
                        daño = atacante.stats.ataque - defensor.stats.defensa*0.5
                        print(f"¡Golpe crítico! {atacante.nombre} ha infligido un golpe crítico a {defensor.nombre}.")
                    else:
                        daño = atacante.stats.ataque - defensor.stats.defensa
                        if daño <= 0:
                            daño = self.__DANY_MINIM
                    defensor.stats.vida -= daño
                    print(f"{atacante.nombre} ha atacado a {defensor.nombre}.")
                    print(f"{defensor.nombre} ha perdido {daño} puntos de vida. Vida restante: {defensor.stats.vida}")

                self.finalizar_batalla() if defensor.stats.vida <= 0 else None
                self.turno = not self.turno
            else:
                self.turno = not self.turno

    
    def finalizar_batalla(self)-> bool:

        if self.luchador_1.stats.vida <=0:
            print(f"El luchador {self.luchador_1.nombre} ha sido derrotado.")
        else:
            print(f"El luchador {self.luchador_2.nombre} ha sido derrotado.")

        self.batalla = False

    def estado(self)-> str:

        print(f'El luchador {self.luchador_1.nombre} tiene {self.luchador_1.stats.vida} puntos de vida y el luchador {self.luchador_2.nombre} tiene {self.luchador_2.stats.vida} puntos de vida.')


class Torneo():
    __LISTA_DE_PARTICIPANTES_DEL_TORNEO = [
        Luchador("Goku", Stat(velocidad=99, ataque=99, defensa=99)),
        Luchador("Vegeta", Stat(velocidad=90, ataque=95, defensa=85)),
        Luchador("Gohan", Stat(velocidad=85, ataque=90, defensa=80)),
        Luchador("Piccolo", Stat(velocidad=75, ataque=80, defensa=85)),
        Luchador("Krillin", Stat(velocidad=70, ataque=65, defensa=60)),
        Luchador("Bulma", Stat(velocidad=30, ataque=10, defensa=20)),
        Luchador("Trunks", Stat(velocidad=80, ataque=85, defensa=75)),
        Luchador("Freezer", Stat(velocidad=85, ataque=90, defensa=80)),
        Luchador("Cell", Stat(velocidad=85, ataque=95, defensa=85)),
        Luchador("Majin Buu", Stat(velocidad=70, ataque=90, defensa=95)),
        Luchador("Yamcha", Stat(velocidad=60, ataque=55, defensa=50)),
        Luchador("Tenshinhan", Stat(velocidad=65, ataque=60, defensa=55)),
        Luchador("Chaoz", Stat(velocidad=50, ataque=40, defensa=35)),
        Luchador("Videl", Stat(velocidad=55, ataque=50, defensa=45)),
        Luchador("Mr. Satán", Stat(velocidad=40, ataque=30, defensa=35)),
        Luchador("Chi-Chi", Stat(velocidad=50, ataque=45, defensa=40)),
        Luchador("Androide 18", Stat(velocidad=80, ataque=85, defensa=80)),
        Luchador("Androide 17", Stat(velocidad=80, ataque=85, defensa=80)),
        Luchador("Dende", Stat(velocidad=30, ataque=20, defensa=25)),
        Luchador("Shenlong", Stat(velocidad=100, ataque=100, defensa=100)),
        Luchador("Kaiō-sama", Stat(velocidad=70, ataque=75, defensa=70)),
        Luchador("Beerus", Stat(velocidad=100, ataque=100, defensa=100)),
        Luchador("Whis", Stat(velocidad=100, ataque=100, defensa=100)),
        Luchador("Jiren", Stat(velocidad=95, ataque=100, defensa=95)),
        Luchador("Zamasu", Stat(velocidad=90, ataque=95, defensa=90)),
        Luchador("Broly", Stat(velocidad=85, ataque=100, defensa=90)),
        Luchador("Raditz", Stat(velocidad=60, ataque=65, defensa=55)),
        Luchador("Nappa", Stat(velocidad=55, ataque=70, defensa=60)),
        Luchador("Zarbon", Stat(velocidad=65, ataque=60, defensa=55)),
        Luchador("Dodoria", Stat(velocidad=50, ataque=60, defensa=55)),
        Luchador("Ginyu", Stat(velocidad=65, ataque=70, defensa=65)),
        Luchador("Recoome", Stat(velocidad=60, ataque=65, defensa=60))
    ]
    __SIGUIENTE_RONDA = []
    __CAMPEON:Luchador = None
    __RONDA = 1


    def __init__(self):
        self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO = self.obtener_lista_participantes(self.seleccionar_participantes())

    def seleccionar_participantes(self)-> int:
        while True:
            try:
                num_participantes = int(input("Selecciona el tamaño del torneo (32, 16, 8, 4): "))
                if num_participantes in [32, 16, 8, 4]:
                    return num_participantes
                else:
                    print("Por favor, selecciona un número válido (32, 16, 8, o 4).")
            except ValueError:
                print("Entrada no válida. Por favor, introduce un número entero.")
    
    def obtener_lista_participantes(self, num_participantes)-> list:
        return random.sample(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO, num_participantes)

    def iniciar_torneo(self)->None:

        self.__SIGUIENTE_RONDA = []
        self.__CAMPEON = None
        self.__RONDA = 1

        if self.torneo_valido():
            print(f'Se inicia el torneo Dragon Ball: Sparking! ZERO.')
            while(self.__CAMPEON == None):
                self.siguiente_ronda()
            print(f'El ganador del torneo es {self.__CAMPEON.nombre}')
            
    
    def eliminatoria(self, duelo: Batalla):
        duelo.luchador_1.restablecer_vida()
        duelo.luchador_2.restablecer_vida()
        while(duelo.batalla ==True):
            duelo.batallar()
            yield(duelo.luchador_1, duelo.luchador_2)
        yield duelo.luchador_1 if duelo.luchador_1.stats.vida > 0 else duelo.luchador_2
    
    def siguiente_ronda(self) -> None:
        print(f'\nRonda {self.__RONDA}:\n')
        if len(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO) == 1:
            self.__CAMPEON = self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO.pop()
        else:
            while len(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO) > 1:
                luchadores = random.sample(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO, 2)
                luchador_1, luchador_2 = luchadores
                self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO.remove(luchador_1)
                self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO.remove(luchador_2)
                print(f"\nLuchadores seleccionados: {luchador_1.nombre} vs {luchador_2.nombre}")
                try:
                    # Llamamos a la eliminatoria como generador
                    respuesta = int(input(f"Presiona un número para simular el duelo entre {luchador_1.nombre} vs {luchador_2.nombre}\n"))
                    if not isinstance(respuesta, int):
                        raise TypeError("Haz de poner número para poder simular")

                    if respuesta == 1:
                        self.gestionar_duelo(luchador_1, luchador_2)
                    else:
                        self.gestionar_duelo(luchador_1, luchador_2)
                except ValueError as e:
                    print("Debes introducir un número válido. Saltamos la simulación")



            # Actualizar la lista para la siguiente ronda
            self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO = self.__SIGUIENTE_RONDA[:]
            self.__SIGUIENTE_RONDA = []
            self.__RONDA += 1
            self.print_ronda()



    def print_ronda(self) -> None:
        print(f"Lista de participantes de la ronda {self.__RONDA}")
        for index, luchador in enumerate(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO):
            print(f'{index+1}. {luchador.nombre}')

    def torneo_valido(self)->bool:
        num_participantes = len(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO)
        if num_participantes >= 2 and (num_participantes & (num_participantes - 1) == 0):
            print('Torneo válido')
            self.print_ronda()
            return True
        else:
            potencia = 1
            while potencia * 2 <= num_participantes:
                potencia *= 2
            while len(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO) > potencia:
                eliminado = self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO.pop(random.randint(0, len(self.__LISTA_DE_PARTICIPANTES_DEL_TORNEO) - 1))
                print(f'El luchador {eliminado.nombre} ha sido eliminado del torneo.')
            print('Ahora el número de participantes es una potencia de 2. Torneo válido.')
            self.print_ronda()
            return True


    def gestionar_duelo(self, luchador_1, luchador_2):
        """Gestiona el duelo entre dos luchadores y muestra el ganador."""
        duelo = Batalla(luchador_1, luchador_2)
        
        for index, estado in enumerate(self.eliminatoria(duelo)):
            if isinstance(estado, tuple):
                luchador_1, luchador_2 = estado
                print(f"Duelo entre {luchador_1.nombre} y {luchador_2.nombre} Finalizado.")
            else:
                ganador = estado
                print(f"Ganador del duelo: {ganador.nombre}")
                self.__SIGUIENTE_RONDA.append(ganador)
                break
        


def main():
    torneo = Torneo()
    torneo.iniciar_torneo()

if __name__ == '__main__':
    main()