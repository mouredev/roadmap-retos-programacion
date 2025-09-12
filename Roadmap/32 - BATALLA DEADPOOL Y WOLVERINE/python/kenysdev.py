# ╔═════════════════════════════════════╗
# ║ Autor:  Kenys Alvarado              ║
# ║ GitHub: https://github.com/Kenysdev ║
# ║ 2024 -  Python                      ║
# ╚═════════════════════════════════════╝

# ---------------------------------------
# 32 * BATALLA DEADPOOL Y WOLVERINE
# ---------------------------------------
"""
 * EJERCICIO:
 * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
 * Crea un programa que simule la pelea y determine un ganador.
 * El programa simula un combate por turnos, donde cada protagonista posee unos
 * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
 * de regeneración y evasión de ataques.
 * Requisitos:
 * 1. El usuario debe determinar la vida inicial de cada protagonista.
 * 2. Cada personaje puede impartir un daño aleatorio:
 *    - Deadpool: Entre 10 y 100.
 *    - Wolverine: Entre 10 y 120.
 * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
 * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
 * 4. Cada personaje puede evitar el ataque contrario:
 *    - Deadpool: 25% de posibilidades.
 *    - Wolverine: 20% de posibilidades.
 * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
 * Acciones:
 * 1. Simula una batalla.
 * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
 * 3. Muestra qué pasa en cada turno.
 * 4. Muestra la vida en cada turno.
 * 5. Muestra el resultado final.
"""

# NOTA: Estoy intentando practicar los principios SOLID. XD 😂

#__________________________
from abc import ABC, abstractmethod
from typing import Type
from typing import Dict, List, Tuple, Any
import random
import time

# ---------------------------------------
# ABSTRACIONES
# ---------------------------------------
#__________________________
class AbcGlobalConfig(ABC):
    """Contrato sobre las constantes globales"""
    @property
    @abstractmethod
    def turn_interval(self) -> int:
        """Tiempo de espera en segundos entre cada turno."""
        pass

    @property
    @abstractmethod
    def minimun_hp(self) -> str:
        """Mínima cantidad de vida inicial permitida."""
        pass

    @property
    @abstractmethod
    def characters(self) -> Dict[str, Dict]:
        """
        Diccionario de personajes, con sus habilidades, Daño posible, Probabilidad de defensa.
        {"Character": {"attacks": ["Attack1", "Attack2"], "damage_range": (10, 100), "defense_chance": 0.25}}
        """
        pass

    @property
    @abstractmethod
    def menu(self) -> str:
        """Acciones del menú principal."""
        pass

#__________________________
class AbcInput(ABC):
    """Contrato sobre la entra de datos."""
    def get(self, msg: str, type_: str) -> str | int:
        """Retornará un dato que no debe ser None y garantizará el tipo de dato solicitado."""
        pass

#__________________________
class AbcCharacter(ABC):
    """Contrato sobre los datos y metodos de un personaje que participara en la batalla."""
    def __init__(self, name: str, hp:int, attributes: Dict[str, Any]) -> None:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Nombre del personaje."""
        pass

    @property
    @abstractmethod
    def attacks(self) -> List[str]:
        """Lista de ataques disponibles para el personaje."""
        pass

    @property
    @abstractmethod
    def damage_range(self) -> Tuple[int, int]:
        """Rango de daño que el personaje puede infligir."""
        pass

    @property
    @abstractmethod
    def defense_chance(self) -> float:
        """Probabilidad de que el personaje se defienda de un ataque."""
        pass
    
    @property
    @abstractmethod
    def hp(self) -> int:
        """Puntos de vida del personaje."""
        pass

    @property
    @abstractmethod
    def can_attack(self) -> bool:
        """Indica si el personaje puede atacar en el turno actual."""
        pass

    @hp.setter
    @abstractmethod
    def hp(self, value: int) -> None:
        """Modifica los puntos de vida del personaje."""
        pass

    @can_attack.setter
    @abstractmethod
    def can_attack(self, value: bool) -> None:
        """Modifica la capacidad del personaje para atacar."""
        pass

    @abstractmethod
    def attack(self) -> int:
        """
        Verifica si puede atacar usando '@can_attack.setter'.
        Imprime el ataque realizado y cantidad de daño.
        Realiza un ataque y devuelve el daño infligido.
        """
        pass

    @abstractmethod
    def defend(self) -> bool:
        """Determina si el personaje puede defenderse."""
        pass

#__________________________
class AbsBattleStrategy(ABC):
    """Lógica para la batalla."""
    @abstractmethod
    def execute(self, attacker: 'AbcCharacter', defender: 'AbcCharacter') -> bool:
        """Ejecutará la estrategia """
        pass

#__________________________
class AbcFeatures(ABC):
    """Contrato sobre las caracteristicas del programa las cuales usaran(AbcGlobalConfig, AbcInput, AbcCharacter y AbsBattleStrategy)."""
    def __init__(self, gc: Type[AbcGlobalConfig], input_: Type[AbcInput], 
    character: Type[AbcCharacter], battle_strategy: Type[AbsBattleStrategy]) -> None:
        pass

    @abstractmethod
    def get_character(self, msg: str) -> Tuple[str, int, Dict[str, Any]]:
        """
        Retorna los personajes y su vida.
        """
        pass
    
    @abstractmethod
    def show_hp(self) -> None:
        """Mostrara la vida de ambos personajes."""
        pass

    @abstractmethod
    def battle(self) -> None:
        """
        Llevará a cabo el turno de la batalla. Utilizando actions() y show_hp()
        También será donde se establezca el tiempo de espera de cada turno.
        """
        pass

    @abstractmethod
    def start_simulation(self) -> None:
        """Creará la simulación, utilizando get_character() y battle()."""
        pass

# ---------------------------------------
# IMPLEMENTACIÓN DE ABSTRACCIONES
# ---------------------------------------
#__________________________
class DefaultConfig(AbcGlobalConfig):
    """Constantes globales"""
    TIME: int = 2 # segundos

    MINIMUM_HP = 200

    CHARACTERS: Dict[str, Dict] = {
        "Deadpool": {
            "attacks": ["Con arma.", "Cuerpo a cuerpo.", "Con ataque imprudente."],
            "damage_range": (10, 100),
            "defense_chance": 0.25
        },
        "Wolverine": {
            "attacks": ["Con garras de adamantium.", "Con arma.", "Cuerpo a cuerpo."],
            "damage_range": (10, 120),
            "defense_chance": 0.20
        }

        # Sí, se desea incorporar más personajes, disponibles.
    }

    MENU: str = """
SIMULADOR DE BATALLAS:
------------------------------------------
| 1. Simular una batalla | 2. Salir      |  
------------------------------------------"""

    @property
    def turn_interval(self) -> int:
        return self.TIME

    @property
    def minimun_hp(self) -> str:
        return self.MINIMUM_HP

    @property
    def characters(self) -> dict:
        return self.CHARACTERS

    @property
    def menu(self) -> str:
        return self.MENU

#__________________________
class DefaultInput(AbcInput):
    """Solicitud de entrada."""
    def get(self, msg: str, type_: str) -> str | int:
        while True:
            txt = input(msg)
            
            if type_ == 'str':
                if isinstance(txt, str) and len(txt) > 0:
                    return txt
                else:
                    print("La entrada no puede estar vacía.")
            
            elif type_ == 'int':
                if txt.isdigit():
                    return int(txt)
                else:
                    print("Por favor, ingresa un número entero válido.")
            
            else:
                print("Tipo de dato no soportado.")

#__________________________
class DefaultCharacter(AbcCharacter):
    """Datos y metodos de un personaje que participara en la batalla."""
    def __init__(self, name: str, hp:int, attributes: Dict[str, Any]) -> None:
        self._name: str = name
        self._hp: int = hp
        self._attacks: List[str] = attributes.get('attacks', [])
        self._damage_range: Tuple[int, int] = attributes.get('damage_range', (0, 0))
        self._defense_chance: float = attributes.get('defense_chance', 0.0)
        self._can_attack: bool = True
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def attacks(self) -> List[str]:
        return self._attacks

    @property
    def damage_range(self) -> Tuple[int, int]:
        return self._damage_range

    @property
    def defense_chance(self) -> float:
        return self._defense_chance

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, value: int) -> None:
        self._hp = value

    @property
    def can_attack(self) -> bool:
        return self._can_attack

    @can_attack.setter
    def can_attack(self, value: bool) -> None:
        self._can_attack = value
    
    def attack(self) -> int:
        if self.can_attack:
            selected_attack = random.choice(self.attacks)
            damage: int = random.randint(self.damage_range[0], self.damage_range[1])
            print(f"|'{self._name}' ataca '{selected_attack}' Produciendo un: '-{damage}' 👊|")
            return damage
        else:
            print(f"|'{self._name}' se está regenerando y no ataca. 😴|")
            return 0

    def defend(self) -> bool:
        # random.random() genera un número decimal entre 0.0 y 1.0
        # tendra un self._defense_chance % de poder defenderse.
        if random.random() < self.defense_chance:
            print(f"|'{self.name}' logró defenderse. 🛡️|")
            return True
        else:
            print(f"|'{self.name}' no pudo bloquear el ataque. 🤕|")
            return False

#__________________________
class DefaultBattleStrategy(AbsBattleStrategy):
    def execute(self, attacker: 'AbcCharacter', defender: 'AbcCharacter') -> bool:
        damage = attacker.attack()
        
        if damage == attacker.damage_range[1]:
            print(f"|'{defender.name}' 🚨recibió un ataque crítico y no podrá atacar.🚨|")
            defender.can_attack = False
        
        if attacker.can_attack:
            if not defender.defend():
                defender.hp -= damage
        else:
            attacker.can_attack = True
        
        if defender.hp <= 0:
            print("\n____________________________")
            print(f"|'{attacker.name}' 🏆 gana la batalla. 🏆|")
            return False
        
        return True

#__________________________
class DefaultFeatures(AbcFeatures):
    """Caracteristicas del programa."""
    def __init__(self, gc: Type[AbcGlobalConfig], input_: Type[AbcInput], 
    character: Type[AbcCharacter], battle_strategy: Type[AbsBattleStrategy]) -> None:
        super().__init__(gc, input_, character, battle_strategy)
        self._gc: AbcGlobalConfig = gc()
        self._input: AbcInput = input_()
        self._new_character: AbcCharacter = character
        self._battle_strategy = battle_strategy()
        self.character1: AbcCharacter = character
        self.character2: AbcCharacter = character

    def get_character(self, msg: str) -> Tuple[str, int, Dict[str, Any]]:
        while True:
            #________
            index: int = self._input.get(msg, type_="int")
            keys: list = list(self._gc.characters.keys())

            #________
            if not (0 <= index < len(keys)):
                print("Número de personaje incorrecto.")
                continue  # Volver a solicitar
            
            #________
            if keys[index] == self.character1.name:
                print("El personaje ya fue utilizado.")
                continue
            
            #________
            hp: int = self._input.get(f"Establecer una vida >= que '{self._gc.minimun_hp}' : ", "int")
            if hp < self._gc.minimun_hp:
                print(f"La vida debe ser mayor a '{self._gc.minimun_hp}'.")
                continue
            
            #________
            name: str = keys[index]
            attributes: Dict[str, Any] = self._gc.characters[name]
            return name, hp, attributes

    def show_hp(self) -> None:
        print("____________________________")
        print(f"|{self.character1.name}: ❤️ {self.character1.hp}| |{self.character2.name}: ❤️ {self.character2.hp}|")

    def battle(self):
        turn: int = 1
        while True:
            print(f"\n----------------------------\nTurno #{turn}\n----------------------------")

            # Ataque de personaje #1 hacia #2
            self.show_hp()
            if not self._battle_strategy.execute(attacker=self.character1, defender=self.character2):
                break
            
            # Ataque de personaje #2 hacia #1
            self.show_hp()
            if not self._battle_strategy.execute(attacker=self.character2, defender=self.character1):
                break

            turn += 1
            time.sleep(self._gc.turn_interval)
        
        self.show_hp()

    def start_simulation(self) -> None:
        #________
        print("Personajes disponibles:")
        for i, name in enumerate(self._gc.characters):
            print(f"{i}. {name}")

        #________
        dt = self.get_character("'Primer' personaje: ")
        name, hp, attributes = dt
        self.character1 = self._new_character(name, hp, attributes)

        #________
        dt = self.get_character("'Segundo' personaje: ")
        name, hp, attributes = dt
        self.character2 = self._new_character(name, hp, attributes)

        #________
        # Iniciar batalla
        self.battle()

        #________
        self.character1 = self._new_character # Sin instancia
        self.character2 = self._new_character
        print(self._gc.menu)

# ---------------------------------------
# INYECCIÓN DE DEPENDENCIAS Y UTILIZACIÓN
# ---------------------------------------
#__________________________
class Program():
    def __init__(self) -> None:

        self.__gc: AbcGlobalConfig = DefaultConfig
        self.__input: AbcInput = DefaultInput
        self.__Character: AbcCharacter = DefaultCharacter
        self.__battle_strategy: AbsBattleStrategy = DefaultBattleStrategy
        self._ft: AbcFeatures = DefaultFeatures(self.__gc, self.__input, self.__Character, self.__battle_strategy)
        
    def run(self) -> None:

        print(self._ft._gc.menu)
        while True:
            option: int = self._ft._input.get(msg="\nOpción: ", type_="int")
            match option:
                case 1: self._ft.start_simulation()
                case 2: print("Adios"); break
                case _: print("Seleccionar de '1 a 2'")

#__________________________
if __name__ == "__main__":
    program = Program()
    program.run()

# NOTA: Solo estoy intentando practicar los principios SOLID. XD 😂

