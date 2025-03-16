#Excepciones

try:
    print("Iniciando ejecucion")
    num = 10/0
except Exception as ex:
    print(f"Error {ex}")
finally:
    print("Ejecucion finalizada")
    

#Dificultad Extra
print("Dificultad Extra \n")
class MiExcepcion(Exception):
    pass

def genera_excepciones(param1, param2):
    if int(param1) == 10:
        raise MiExcepcion("1º Valor no puede ser 10 ")
    num = int(param1) / int(param2)
    print(f"Resultado Division:{num}")


try:
    num1 = input("Introduce el primer valor para hacer la division:")
    num2 = input("Introduce el segundo valor para hacer la division:")
    genera_excepciones(num1,num2)
except MiExcepcion as ex:
    print(f"Mi Excepcion {ex}")
except ValueError as ex:
    print(f"Excepcion division 0 {ex}")
except Exception as ex:
    print(f"Excepcion {ex}")
finally:
    print("Ejecucion finalizada")