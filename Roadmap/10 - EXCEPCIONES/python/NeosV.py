

try:
 print(10/0)

except:
 print("error")

try:
 lista = [1,2,3,4,5]
 print (lista[4])
except Exception as e:
 print(f"error {e}")




class StrError(Exception):
   pass 


def errores(parameters:list):
    
   if len(parameters)<3:
    raise IndexError()
   elif parameters[1] == 0:
    raise ZeroDivisionError()
   elif type(parameters[2]) == str:
    raise StrError("La lista no puede contener cadenas de texto")

   print(parameters[2])
   print (parameters[0]/parameters[1])
   print (parameters[2] + 5)
   print(parameters[2])
 
 
 
 

try:
 errores([1,2,"carro",4])
except IndexError as e:
 print("Se necesitan al menos 3 parametros")
except ZeroDivisionError as e:
 print("El segundo elemento de la lista no puede ser 0")    
except StrError as e:
 print(f"{e}")
else:
 print("ejecucion terminada sin errores")
finally:
 print("ejecucion finalizada")
 



