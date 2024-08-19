import os, platform

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" 
* EJERCICIO:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico."""


def make_title(func):#Función decoradora a la que le pasamos la función principal
    def wrapper()->str:#Subfunción decoradora (envolvente)
        return func().title()#La subfunción decora la función principal y la devuelve
    return wrapper#La función decoradora devuelve la subfunción envolvente

def add_javascript(func):
    def wrapper()->str:
        return func() + " y jAVasCrIpT"
    return wrapper

def hello_world_es()->str:#Función principal a decorar
    return "hOlA mUnDo"
hello_world_es = make_title(hello_world_es)  #Llamada a la función decoradora pasándole la función a decorar
print(hello_world_es)#Si llamamos a la función sin paréntesis nos devolverá sólo la referencia de la función decoradora
                     # con su función interna y su posición en memoria
print(hello_world_es())#Al ponerle los paréntesis nos devuelve la función original decorada


@make_title #Anotando antes de la función a decorar el nombre de la función decoradora precedido de @ nos ahorramos la llamada
def hello_python_es()->str:#Función principal a decorar
    return "hOLa pYThON"
print(hello_python_es())

def hello_java_es()->str:#La anotación solo servirá para la primera función bajo esta, en la siguiente no se aplica
    return "hOLA jaVA"
print(hello_java_es())


@add_javascript#Se pueden anotar varios decoradores pero estos se aplicarán en modo FIFO
@make_title#Este se aplica primero su decoración que formatea el texto a .title y luego el @add_javascript
           # que añade ' y jAVasCrIpT' al texto ya formateado por @make_title pero sin decorar por este.
def hello_java_es_2()->str:
    return "hOLA jAvA"
print(hello_java_es_2())
print()


""" 
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección."""


def call_counter(fun):
    calls=[]
    def counter(a:int, b:int)->str:
        calls.append(fun)
        calls_counter = len(calls)
        return '{:<25}'.format(fun(a, b)) + ", Llamada Nª: " + (str(calls_counter))
    return counter
    
@call_counter  
def my_call(a:int, b:int)->str:
    result = a + b
    return f"Resultado de {a} + {b} = {result}"

print(my_call(3, 8))
print(my_call(14, 9))
print(my_call(9, 7))
print(my_call(42, 4))
print(my_call(6, 13))
