"""
EJERCICIO:
Explora el concepto de "decorador" y muestra cómo crearlo
con un ejemplo genérico.

DIFICULTAD EXTRA (opcional):
Crea un decorador que sea capaz de contabilizar cuántas veces
se ha llamado a una función y aplícalo a una función de tu elección.
"""
from threading import Lock
from random import randint


def decora_string(fun_parametro):
    """ 
    Creo un decorador que adorna funciones que retornan un string de manera aleatorea.
    """
    def fun_interna():
        ladornos=['･｡+☆+｡･ﾟ･','○+●+○+●', '+* ﾟ ゜ﾟ *+', '♥｡･ﾟ♡ﾟ･｡♥｡･', '★・・・・・・・★']
        i= randint(0,len(ladornos)-1)
        a= fun_parametro()
        return ladornos[i]+a+ ladornos[i]
    return fun_interna

class SingletonMeta(type):
    _instancias = {}
    _lock: Lock = Lock()
    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instancias:
                instancia = super().__call__(*args, **kwargs)
                cls._instancias[cls]= instancia
        return cls._instancias[cls]

class ContadorSingleton(metaclass=SingletonMeta):
    valor: int = 0 
    def get(self):
        return self.valor
    def incrementar(self):
        self.valor+=1
    def decrementar(self):
        self.valor-=1


def decorador_cuenta(fun_parametro):
    def fun_interna(s):
        cont=ContadorSingleton()
        a=fun_parametro(s)
        cont.incrementar()
        print("Llamaste a la funcion {} veces.".format(cont.get())  )
        return a
    return fun_interna

@decora_string
def DameNombre():
    return "Juan"

@decora_string
def DameDia():
    return "Hoy es Navidad"

@decorador_cuenta
def DuplicaString(s):
    return s*2



def main():
    print("Hola " + DameNombre())
    print(DameDia())
    print()
    print(DameNombre())
    print()
    print(DuplicaString("CHAU"))
    print(DuplicaString("Nos Vemos!"))
    print(DuplicaString("PE"))


if __name__=="__main__":
    main()

