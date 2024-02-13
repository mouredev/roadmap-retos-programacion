## 1.VARIABLES POR VALOR Y REFERENCIA ##

# Voy a crear dos variables, un string y una lista.
variableUno: str = "Hola"
variableDos: list = ["Hola", "Pedro"]

# Ahora creo dos funciones que alteren un valor:
def añadirEspacio1(valor):
    valor += " "
def añadirEspacio2(valor):
    valor.append(" ")

# Ahora llamo a las respectivas funciones
añadirEspacio1(variableUno)
añadirEspacio2(variableDos)

# Escribo los resultados:
print(f"'{variableUno}'") # Como podemos ver gracias a las comillas, la variableUno no ha cambiado al pasar por la función
print(variableDos) # En cambio, la variableDos si ha mantenido el cambio después de pasar por la función ¿Por qué?
#Lo que sucede es que en el primer caso, dentro de la función se crea una copia del objeto inicial. Los cambios se realizan en la copia.
#En el segundo caso dentro de las funciones estaríamos modificando el objeto inicial.
#Si quisieramos devolver el cambio, utilizaríamos el return:

def añadirEspacio3(valor) -> str:
    valor += " "
    return valor
variableUno = añadirEspacio3(variableUno)
print(f"'{variableUno}'")
# Comprobamos que ahora sí que añade el espacio al pasar por la función. Tanto los int, str, float y Bools son de paso por valor.

#Si quisieramos que no se realizara el cambio, usamos la función con una copia:

def añadirEspacio4(valor):
    valor.append(" ")
añadirEspacio4(variableDos[:]) # Una forma de hacer la copia es mandado un slice[:] completo del original
print(variableDos)
# Comprobamos que ahora no se añade un segundo espacio al pasar por la función. Las listas, tuplas... son de paso por referencia.


## 2.DIFICULTAD EXTRA ##

def programaUno(valor1, valor2):
    valor3 = valor1
    valor1 = valor2
    valor2 = valor3
    return valor1, valor2

def programaDos(valor):
    valor1 = valor[0]
    valor[0] = valor[1]
    valor[1] = valor1
    return valor

datoUno = "Hola"
datoDos = "Adios"

datoUno2, doatoDos2 = programaUno(datoUno, datoDos)
print(f"Datos originales: {datoUno, datoDos}. Datos nuevos: {datoUno2, doatoDos2}")
# Resultado --> Datos originales: ('Hola', 'Adios'). Datos nuevos: ('Adios', 'Hola')


datoUno = ["Hola", "Adios"]

datoUno2 = programaDos(datoUno)
print(f"Datos originales: {datoUno}. Datos nuevos: {datoUno2}")
# Resultado --> Datos originales: ['Adios', 'Hola']. Datos nuevos: ['Adios', 'Hola']
