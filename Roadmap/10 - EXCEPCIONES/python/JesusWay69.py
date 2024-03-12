import os
os.system('clear')

primer_numero = 4
segundo_numero = 0
cero = 0

#Comentar y descomentar la siguiente asignación de segundo_numero para ver cambios
#segundo_numero = "5"

### TRY-EXCEPT
try:
  print(primer_numero + segundo_numero)
  print("operación correcta\n")
except:
    print("operación incorrecta\n")
print("")

### TRY-EXCEPT-ELSE
try:
   print(primer_numero + segundo_numero)
   print("operación correcta\n")
except: #Obligatorio para completar try
    print("operación incorrecta\n")
else: # Opcional para continuar sin excepciones, sólo entrará si la operación dentro de try es correcta
    print ("la ejecución continúa\n")
print("")
### TRY-EXCEPT-ELSE-FINALLY

try: 
   print(primer_numero + segundo_numero)
   print("operación correcta\n")
except: #Obligatorio para completar try
    print("operación incorrecta\n")
else: # Opcional para continuar sin excepciones, sólo entrará si la operación dentro de try es correcta
    print ("la ejecución contitúa\n")
finally: #Finally se suele usar si queremos ejecutar algún tipo de acción de limpieza.
#Si por ejemplo estamos escribiendo datos en un fichero pero ocurre una excepción,
 #tal vez queramos borrar el contenido que hemos escrito con anterioridad, para no dejar datos inconsistenes en el fichero.
    print("la ejecución continúa pero puede haber errores\n")
print("")

###PREVENCIÓN DE EXCEPCIONES POR TIPO DE DATO
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta\n")
except TypeError: #TypeError limita la excepción al tipo de dato
    print("tipos de dato incompatibles para esta operación\n")
print("")

###PREVENCIÓN DE EXCEPCIONES POR DIVISIÓN ENTRE CERO
try: 
   print(primer_numero / cero)
   print("operación correcta\n")
except ZeroDivisionError: #ZeroDivisionError limita la excepción a un divisor con valor 0
    print("no se puede dividir entre 0\n")
print("")

###PREVENCIÓN DE EXCEPCIONES POR TIPO DE DATO Y/O POR VALOR
try: 
   print(primer_numero + segundo_numero)
   print("operación correcta")
except ValueError: #ValueError limita la excepción al valor del dato
    print("valores incompatibles con esta operación")
except TypeError: #TypeError limita la excepción al tipo de dato
    print("tipos de dato incompatibles para esta operación")
print("")

###PREVENCIÓN Y CAPTURA DE FALLO GENÉRICO O CONCRETO
try: 
   print(primer_numero / segundo_numero)
   print("operación correcta")
except Exception as fallo: #Exception nos permite capturar cualquier excepción en una variable
    print(fallo, "\n")

 
