# /*
#  * EJERCICIO:
#  * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
#  * un ejemplo con cada nivel de "severidad" disponible.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
#  * y listar dichas tareas.
#  * - Añadir: recibe nombre y descripción.
#  * - Eliminar: por nombre de la tarea.
#  * Implementa diferentes mensajes de log que muestren información según la 
#  * tarea ejecutada (a tu elección).
#  * Utiliza el log para visualizar el tiempo de ejecución de cada tarea. 
#  */

import logging

print("Logging in File (F) or Display (D)")
op = input()
if op == "F":
    logging.basicConfig(filename="log_my.log",level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
else :
     logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

 
logging.debug("Mensaje de Error en Debug")
logging.warning("Esto es una Warning")
logging.critical("Esta critica la cosa")
logging.info("Solo es info")
logging.error("Error se formo el despelote")


# EXTRA
import time, datetime, random

class Dutty:

     
    
    def __init__(self):
        self.dutty = {}
        

    def create(self, dutty: str, desc: str ):
            if dutty in self.dutty:
                 logging.error(f"Tarea {dutty} is already created")
            else:
                 
                self.dutty[dutty] = desc
                logging.info(f"Tarea {dutty} Succesfully created ")
            logging.debug(f"Numero de tareas {len (self.dutty)}")
            

    def delete(self,name: str):
          
         if name in self.dutty:
              
              del self.dutty[name]
              logging.info(f"Tarea {name} Delete succesfully")
         else:
              logging.error(f"Tarea {name} Not Found")
         logging.debug(f"Numero de tareas {len (self.dutty)}")
          

    def display(self):
         logging.info("Lista de tareas")
         for i,v in   self.dutty.items():
                logging.info(f" Tarea {i} Descripcion {v}")

   
    
    def execute (self,name):
        if name in self.dutty:
              logging.debug(f"Tarea {name} executandose... ")
              start = datetime.datetime.now()
              logging.warning(f"Tarea {name} Inicio {start.strftime("%H:%M:%S")} ")
              time_exec = random.randint(1,10)
              logging.warning(f"duracion estimada  {time_exec}s")
              time.sleep(time_exec)
              end = datetime.datetime.now()
              logging.warning(f"fin {end.strftime("%H:%M:%S")} ")
              logging.debug(f"Tarea {name} terminada")
              
        else:
             logging.error(f"Tarea {name} Not found")\
             

     
list_dutty = Dutty()

list_dutty.create("t1","asasasass")
list_dutty.create("t2", "asasasass")
list_dutty.create("t2", "asasasass")
list_dutty.delete("t10")
list_dutty.create("t3", "asasasass")
list_dutty.delete("t1")
list_dutty.create("t4", "asasasass")
list_dutty.create("t5", "asasasass")
list_dutty.create("t6", "asasasass")
list_dutty.create("t7", "asasasass")

list_dutty.execute("t3" )
list_dutty.execute("t2" )
list_dutty.execute("t1" )
list_dutty.execute("t5" )
list_dutty.execute("t11" )

list_dutty.display()

         

  
 
 


