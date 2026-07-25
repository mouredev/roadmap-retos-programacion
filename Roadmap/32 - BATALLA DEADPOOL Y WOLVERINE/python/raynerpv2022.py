# /*
#  * EJERCICIO:
#  * ¡Deadpool y Wolverine se enfrentan en una batalla épica!
#  * Crea un programa que simule la pelea y determine un ganador.
#  * El programa simula un combate por turnos, donde cada protagonista posee unos
#  * puntos de vida iniciales, un daño de ataque variable y diferentes cualidades
#  * de regeneración y evasión de ataques.
#  * Requisitos:
#  * 1. El usuario debe determinar la vida inicial de cada protagonista.
#  * 2. Cada personaje puede impartir un daño aleatorio:
#  *    - Deadpool: Entre 10 y 100.
#  *    - Wolverine: Entre 10 y 120.
#  * 3. Si el daño es el máximo, el personaje que lo recibe no ataca en el
#  * siguiente turno, ya que tiene que regenerarse (pero no aumenta vida).
#  * 4. Cada personaje puede evitar el ataque contrario:
#  *    - Deadpool: 25% de posibilidades.
#  *    - Wolverine: 20% de posibilidades.
#  * 5. Un personaje pierde si sus puntos de vida llegan a cero o menos.
#  * Acciones:
#  * 1. Simula una batalla.
#  * 2. Muestra el número del turno (pausa de 1 segundo entre turnos).
#  * 3. Muestra qué pasa en cada turno.
#  * 4. Muestra la vida en cada turno.
#  * 5. Muestra el resultado final.
#  */
from abc import ABC, abstractmethod

import random, time

class VirtualWarrior(ABC):
    @abstractmethod
    def __init__(self, initial_life: int, maximo: int,ae: int):
        self._initial_life = initial_life
        self._life = initial_life
        self._atack_damage = 0
        self._regeneration  = False
        self._atack_evation = ae
        self._winner = False
        self._maximo =  maximo
    
    
    def reset_warrior(self):
          self._life = self._initial_life
          self._atack_damage = 0
          self._regeneration  = False
          self._winner = False
          
                   
    def  evation(self):
            
           return  random.random() < self._atack_evation/100
            
    
     
    def attack(self):
         self._atack_damage = random.randint(10,self._maximo)
          
         
          


class DeadPool(VirtualWarrior):
    def __init__(self, initial_life: int, maximo: int,ae: int):
        super().__init__(initial_life,maximo, ae)
         
         
         

     
          

class Wolwerine(VirtualWarrior):
    def __init__(self, initial_life: int, maximo: int,ae: int):
        super().__init__(initial_life,maximo, ae)
         
         
         

    
class VirtualReport(ABC):
     @abstractmethod
     def __init__(self):
          pass
     @abstractmethod
     def reset(self):
          pass
     @abstractmethod
     def turn_report(self):
          pass
     @abstractmethod
     def show_winner(self):
          pass



    


class Report(VirtualReport):
     def __init__(self):
          self._message = {"attacker":None,
                          "defenser": None,
                          "winner": None,
                          "regeneration": None,
                          "evation": None,
                          "attackpower": None,
                          "maximalhit": None,
                          "turn": None,
                          "defenserlife":None,

                          }
           
     
     def reset(self):
           for  clave in self._message:
            self._message[clave] = None

    
     def turn_report(self):
          

          print(f"  Turno :{self._message["turn"]} -  Atacante : {self._message["attacker"]} Defensor :{self._message["defenser"]} Fuerza de Ataque: {self._message["attackpower"]}")
          
          if self._message["evation"] :
               print(f"    :{self._message["evation"]}")

          if self._message["maximalhit"] :
               print(f"    :{self._message["maximalhit"]}")

          if self._message["regeneration"] :
               print(f"    :{self._message["regeneration"]}")

          
            
               
          print(f"  Vide de  {self._message["defenser"]}  : {self._message["defenserlife"]}")
           

     def show_winner(self):
          
          print(f"  {self._message["attacker"]} is the WINNER")

     
class VirtualTurn(ABC):
     @abstractmethod
     def __init__(self, warriors: list[VirtualWarrior] ):
          pass
          
     @abstractmethod      
     def  choose_current_attacker(self, report: Report)    :
            pass

     @abstractmethod     
     def choose_current_defenser(self, report: Report) :
          pass
     
     @abstractmethod
     def turn_change(self, attacker: VirtualWarrior, defenser: VirtualWarrior,report: Report):
          pass

     @abstractmethod
     def turn_winner(self, attacker: VirtualWarrior, defenser: VirtualWarrior, report: Report): 
          pass
     
     
class Turn(VirtualTurn):
     def __init__(self, warriors: list[VirtualWarrior] ):
          self._warriors = warriors
          self._number_turn = 0
          self._current_attacker : VirtualWarrior
          self._current_defenser : VirtualWarrior
          self._message : VirtualWarrior
          
           
         
           
     def  choose_current_attacker(self, report: Report)    :
            self._current_attacker = random.choice(self._warriors)
            report._message["attacker"] = self._current_attacker.__class__.__name__
             
         
     
     def choose_current_defenser(self, report: Report) :
          self._current_defenser = (next(w for w in self._warriors if w is not self._current_attacker))
          report._message["defenser"] = self._current_defenser.__class__.__name__
     
     def turn_change(self, attacker: VirtualWarrior, defenser: VirtualWarrior,report: Report):
          
          if defenser._regeneration :
               defenser._regeneration = False
               report._message["attacker"], report._message["defenser"] = self._current_attacker.__class__.__name__, self._current_defenser.__class__.__name__
                 

               return
          else:
               self._current_attacker, self._current_defenser = defenser, attacker
               report._message["attacker"], report._message["defenser"] = self._current_attacker.__class__.__name__, self._current_defenser.__class__.__name__
                 
               

        
                
          

     def turn_winner(self, attacker: VirtualWarrior, defenser: VirtualWarrior, report: Report):
            
            if defenser._life <= 0:
                     attacker._winner = True
                     report._message["winner"] = f"{attacker.__class__.__name__} is the WINNER"
            
     
          
class VirtualAttackManager(ABC):
     @abstractmethod
     def turn_attack(self, attacker: VirtualWarrior, defenser: VirtualWarrior, report: Report):
               pass
               


class AttackManager(VirtualAttackManager):
               
     def turn_attack(self, attacker: VirtualWarrior, defenser: VirtualWarrior, report: Report):
     
         attacker.attack()
         report._message["attackpower"] = attacker._atack_damage
         report._message["defenserlife"] = defenser._life
         if defenser.evation():
            
            report._message["evation"] = f"{defenser.__class__.__name__} ha evadido el ataque"
            return
         
         defenser._life -= attacker._atack_damage
         report._message["defenserlife"] = defenser._life
         if attacker._atack_damage >= attacker._maximo   :
                defenser._regeneration = True
                report._message["maximalhit"] = f"   {attacker.__class__.__name__}  GOLPE MAXIMO !!!"
                report._message["regeneration"] =  f"   {defenser.__class__.__name__} Debe Regenerarse"
               
          
             
            
             

      
                 
            

class Battle:
     def __init__(self,warriors: list[VirtualWarrior], report: VirtualReport, attack: VirtualAttackManager):
          
          self._warriors = warriors
          self._report = report
          self._attack_manager = attack

     def reset(self):
            for i in self._warriors:   
                i.reset_warrior()
     

    
     def battle_simulator(self):
            self._turn = Turn(self._warriors)
            self._turn.choose_current_attacker(report)
            self._turn.choose_current_defenser(report)
            
            
            
            while True:
                           self._turn._number_turn +=1
                           self._report._message["turn"] = self._turn._number_turn
                             
                           self._attack_manager.turn_attack(self._turn._current_attacker, self._turn._current_defenser, report)
                           self._report.turn_report()

                           self._turn.turn_winner(self._turn._current_attacker, self._turn._current_defenser,report)
                           
                           
                           if self._turn._current_attacker._winner:
                                break
                           time.sleep(1)
                           self._report.reset()
                           self._turn.turn_change(self._turn._current_attacker, self._turn._current_defenser, report)
                 
            self._report.show_winner()
            self.reset()
   

class MenuUser:
    def __init__(self):
         self._option = 0

    def show_menu(self):
            
            print("Batalla Epica")
            print()
            print("1. Simula una batalla.") 
            print("2. Terminar.")

    def option_select(self, battle: Battle):
         while True:
            self._option = int(input("Option between 1 and 2 : "))
            print()
            1

            match self._option:
                        case 1:
                            battle.battle_simulator()
                        case 2:
                            break
                        case _:
                            print("Option not available, try again...")
                     
               


     


menu = MenuUser()
report = Report()
attack_manager = AttackManager()
 
warrior = [DeadPool(300,120, 20),Wolwerine(300, 100, 25)]
battle = Battle( warrior, report, attack_manager)
menu.show_menu()
menu.option_select(battle)
 




# ****************************************************************


# 🔍 Análisis revisado punto por punto con SOLID + OOP
# ✅ 1. S - Single Responsibility Principle (SRP)

# ✔ Bien aplicado, aunque con matices.
# Clase	Responsabilidad principal	¿Cumple SRP?
# Battle	Orquestar la batalla (simulación de alto nivel)	✅ Sí
# Report	Mostrar y gestionar los reportes de combate	✅ Sí
# AttackManager	Lógica del ataque: daño, evasión, efectos	✅ Sí
# Turn	Manejo de turnos, cambio de roles, orden	⚠ Parcial

# 🔧 Mejora sugerida para Turn:
# Actualmente mezcla:

#     Elección inicial de atacante/defensor

#     Cambio de turno

#     Determinar ganador

# 👉 Podrías separar la lógica de elección y la verificación del fin de combate en servicios distintos, si quieres escalar o testear.
# ✅ 2. O - Open/Closed Principle (OCP)

# ✔ Excelente cumplimiento.

#     Puedes agregar nuevos tipos de guerreros (como Hulk o Thanos) simplemente heredando de VirtualWarrior.

#     Nuevas reglas de batalla pueden ser incorporadas creando nuevos AttackManager o Turn.

# ✅ Todas las clases dependen de interfaces/abstracciones (VirtualAttackManager, VirtualReport, VirtualTurn), por lo que están cerradas para modificación, pero abiertas para extensión.
# ✅ 3. L - Liskov Substitution Principle (LSP)

# ✔ Muy bien.

#     Cualquier objeto DeadPool, Wolverine funciona correctamente donde se espera un VirtualWarrior.

#     Igual con Report, AttackManager, etc.

#     No se rompe el comportamiento esperado al sustituir instancias concretas por abstractas.

# ✅ 4. I - Interface Segregation Principle (ISP)

# ✔ Bien aplicado.

#     Las clases abstractas (VirtualTurn, VirtualWarrior, etc.) definen solo lo esencial.

#     No hay métodos innecesarios forzados a las clases hijas.

#     Muy adecuado para Python, aunque Python no requiere interfaces explícitas, tu diseño lo simula muy bien con ABC.

# ✅ 5. D - Dependency Inversion Principle (DIP)

# ✔ CUMPLIDO gracias a tu aclaración.

#     Battle no instancia directamente Report o AttackManager.

#     Los recibe como dependencias inyectadas a través de sus interfaces abstractas:

# battle = Battle(warrior, report, attack_manager)

#     Esto hace que Battle dependa de abstracciones, no de implementaciones concretas.

# ⚙️ Diseño General POO
# ✔️ Fortalezas

#     Modularidad: Cada componente está separado con una responsabilidad clara.

#     Extensibilidad: Fácil agregar personajes, reglas, tipos de ataque, nuevos reportes.

#     Reusabilidad: Puedes usar los mismos VirtualWarrior con otro AttackManager, etc.

#     Testabilidad: Gracias al uso de abstracciones, puedes mockear objetos para testing.

# 🔧 Mejoras posibles
# 1. Encapsulamiento real

#     Actualmente accedes directamente a atributos como report._message[...] desde otras clases.

#         🔧 Mejor usar set_data() y get_data() para no violar el encapsulamiento.

# 2. Separar responsabilidades del Turn

#     Como mencionamos, tiene múltiples roles.

# 3. Mejorar el input del usuario

#     Validaciones con try/except para evitar errores en consola.

# 4. Uso de propiedades (@property)

#     En vez de exponer _life, podrías tener @property def life() y @life.setter.

# 5. Añadir pruebas unitarias

#     La estructura está lista para testeo automático si desacoplas el input() / print().

# 📊 Conclusión en Puntos
# Criterio	Evaluación	Comentario breve
# SRP (Responsabilidad única)	✅ 80% cumplido	Turn tiene demasiadas tareas
# OCP (Abierto/cerrado)	✅ Excelente	Fácil de extender
# LSP (Sustitución)	✅ Sin problemas	Todo sustituible sin romper
# ISP (Interfaces claras)	✅ Bien aplicado	Sin métodos forzados
# DIP (Inversión de dependencias)	✅ ✔ Cumplido con abstracciones	Muy bien hecho