"""
*Excepciones
"""

try: #?Intenta realizar la/s tarea/s contenidas
    a = int(input("Ingrese un numero: "))
except Exception as ex:#?Si no las puede llevar a cavo, se ejecuta lo que contenga el except
    print("No es un numero")
    print(f"{ex} \n{type(ex).__name__}")
else:#?En caso de que el try se exitoso se ejecuta lo que contenga
    print(a)
finally:#?Se ejecuta al final del try, haya sido o no exitoso
    print("fin Try")

#?Raise

a = 2

if a < 0:
    raise Exception("No se admiten numeros menores a 0")#?Raise invoca la una excepcion y finaliza el programa. se muestran distintos mensajes segun el error invocado

"""
!Extra
"""

