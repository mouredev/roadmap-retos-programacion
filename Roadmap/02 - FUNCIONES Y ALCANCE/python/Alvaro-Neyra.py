# Funciones
# Sin parámetros ni retorno, con uno o varios parámetros, con retorno...

## Funcion sin parametros ni retorno
def funcion_normal():
    print("Hola, esta es una funcion sin parametros ni retorno")
# Se llama la funcion para ejecutarla
funcion_normal()

## Funcion con varios parametros sin retorno
def funcion_2_parametros(nombre, edad):
    print(f"Hola {nombre}, tu edad es: {edad}")
# Llamando la funcion
funcion_2_parametros("Alvaro", 19)

## Funcion con varios parametros con retorno
def funcion_con_parametros_con_retorno(examen, nota):
    if examen and nota:
        if nota >= 9 and not nota <= 9:
            return print(f"Muy bien! en {examen}")
        if nota <= 6 and nota >= 5:
            return print(f"Bien hecho! en {examen}")
        if nota <= 4 and nota > 1:
            return print(f"Puedes mejorar en {examen}")
        else:
            return print(f"A mejorar!")
nota = funcion_con_parametros_con_retorno("Matematicas", 1)
print(nota)

# Llama a una funcion con valor establecido por defecto
def saludar_a(nombre="Usuario"):
    return f"Hola, {nombre}"

saludar_a("Alvaro")
saludar_a()
saludar_a("Rebecca")

# Una funcion con parametros opcionales y uno obligatorio
def retornar_valores(nombre, apellido="No especificado", origen="No especificado"):
    if nombre:
        print(f"Tu nombre es: {nombre}")
    if apellido:
        print(f"Tu apellido es: {apellido}")
    if origen:
        print(f"Tu origen es: {origen}")

retornar_valores("Alvaro") # Si no pones el valor del argumento obligatorio lanzara error ❌

# Llama una funcion con sus argumentos en desorden
def cuenta_deudas(costo_de_la_deudamensual, meses_vencidos_a_pagar, meses_totales, meses_pagados):
    meses_pagados += meses_vencidos_a_pagar
    meses_restantes = meses_totales - meses_pagados
    print(f"Si el Costo de la deuda mensual es: {costo_de_la_deudamensual}")
    print(f"Y si tu meses vencidos que faltan pagar son: {meses_vencidos_a_pagar}")
    print(f"Entonces te falta pagar por ahora: {costo_de_la_deudamensual * meses_vencidos_a_pagar}")
    print(f"Al estar al dia te faltan esta cantidad de meses a pagar: {meses_restantes}")

cuenta_deudas(meses_vencidos_a_pagar=2, meses_pagados=8, costo_de_la_deudamensual=200, meses_totales=18)

## Funcion con parametros usando args:
def suma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado
# Usando la funcion
suma_grande = suma(1,2,3,4,5)
print(suma_grande)

# Crea funciones asincronas (necesitamos importar un objeto awaitable: asyncio.sleep())
import asyncio

async def corutina1():
    # Imprimiendo en consola un aviso que ya empezo la funcion asincrona 1
    print("Inicio de la funcion asincrona 1....")
    # Simulando la funcion asincrona
    await asyncio.sleep(5)
    # Cuando ya se haya ejecutado la corutina2 hasta el await, se continua con la ejecucion de la corutina1...
    print("Fin de la funcion asincrona 1.")

async def corutina2():
    # Iniciando la funcion asincrona 2....
    print("Inicio de la funcion asincrona 2....")
    # Simulando la funcion asincrona
    await asyncio.sleep(5)
    # Cuando ya se haya ejecutado por completo la corutina1 se continua con la ejecucion de esta funcion
    print("Fin de la funcion asincrona 2.")

async def ejecutar_funciones_asincronas():
    # Haciendo un try para administrar excepciones
    try:
        # Empezando a ejecutar las funciones asincronas
        print("Ejecutando funciones asincronas. Espere", end='', flush=True)
        # Mostrar puntos de espera
        for _ in range(5):
            await asyncio.sleep(0.5)
            print(".", end='', flush=True)

        print() # Nueva linea despues de los puntos

        # Ejecutando la funcion asincrona 1
        await corutina1()

        # Aviso de espera para ejecutar la funcion asincrona 2
        print("Esperando a la funcion asincrona 2", end="", flush=True)

        # Mostrar puntos de espera
        for _ in range(5):
            await asyncio.sleep(0.5)
            print(".", end="", flush=True)

        print() # Nueva linea despues de los puntos

        # Ejecutando la funcion asincrona 2
        await corutina2()
    # Si el try retorna un error, ejecuta el except
    except Exception as Error:
        print(f"Se produjo un error durante la ejecucion del programa: {Error}")

asyncio.run(ejecutar_funciones_asincronas())

#* - Comprueba si puedes crear funciones dentro de funciones.

def funcion_externa(numero):
    def funcion_interna(numero_al_doble):
        return numero_al_doble * 2
    numero_doblado = funcion_interna(numero)
    return numero_doblado

resultado_de_la_funcion_externa = funcion_externa(10)
print(resultado_de_la_funcion_externa)

#* - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
# dir() --> Devuelve todos los metodos y atributos del objeto pasado
objeto_numerico = 20
propiedades = dir(objeto_numerico)
print(propiedades)

# print() --> Imprimir datos en consola
print("Hola, estoy usando la funcion integrada print()")

# len() --> Devuelve la cantidad de elementos de un objeto iterable
objeto_iterable = [True, "Hola", 10, 10.4, ("Chau", "Mouse"), "Te amo Moure"]
cantidad_de_elementos = len(objeto_iterable)
print(cantidad_de_elementos)

# list() --> Convierte el objeto pasado a una lista
tupla_iterable = (True, False, 20, "Te amo MoureDev y Comunidad!")
tupla_a_lista = list(tupla_iterable)
print(tupla_a_lista)

#* - Pon a prueba el concepto de variable LOCAL y GLOBAL.
"""Ambito Local: Corresponde con el ambito de una funcion. No se puede acceder a las variables 
    de una función desde fuera de esa función o desde otra función."""
"""Ambito Global: Corresponde con el ámbito que existe desde el comienzo de la ejecución de un programa.
    Todas las variables definidas fuera de cualquier función corresponden al ámbito global, que es accesible 
    desde cualquier punto del programa, incluidas las funciones."""

variable_global = 20
def modificar_variable_global():
    variable_global = 10

print(f"La variable global es: {variable_global}") # 20
modificar_variable_global()
print(f"Luego de llamar a la funcion 'modificar_variable_global' el valor de la variable global es: {variable_global}" ) # 20

"""La variable Global no ha cambiado, ya que dentro del ambito de la funcion 'modificar_variable_global' no existe
la variable: 'variable_global' porque donde se ha declarado la variable global es de distinto ambito que el ambito de la funcion creada.
Si hubiesemos querido que 'variable_global' hubiese sido cambiada, deberiamos haberlo pasado como argumento. Otra cosa es que dentro
de la funcion hemos creado una nueva variable que no la usamos para nada."""

"""Existe una manera para tener acceso de modificacion para las variable globales dentro de una funcion, usando el 
modificador `global`. Con esto le estamos diciendo a Python que sabemos que vamos a utilizar una variable global
y que queremos modificarla"""

variable_global_a_modificar_en_funcion = 100
def dividir_entre_cien():
    global variable_global_a_modificar_en_funcion
    variable_global_a_modificar_en_funcion = 100/10

print(f"La variable global es: {variable_global_a_modificar_en_funcion}")
dividir_entre_cien()
print(f"Variable global modificada: {variable_global_a_modificar_en_funcion}")

"""En el caso de las funciones anidadas, como ya hemos visto antes el ambito de la funcion externa es diferente a la de la funcion
interna y las variables declaradas desde la funcion interna solo se podran usar en su ambito. Pero si queremos modificar el valor
de una variable local de una funcion externa dentro de una funcion interna tendriamos que usar el modificar `nonlocal`"""

"""
> `nonlocal` solo puede ser usado dentro de funciones anidadas
"""

"""En otras palabras la variable local actua como variable global para las funciones anidadas dentro de su mismo contexto"""

def funcion_externa2():
    variable_local_de_la_funcion_externa = 30

    def funcion_interna2():
        nonlocal variable_local_de_la_funcion_externa # Consiguiendo la variable de la funcion externa usando `nonlocal`
        variable_local_de_la_funcion_externa = 10
        print(f"Valor de la variable local de la funcion externa dentro de la funcion interna es: {variable_local_de_la_funcion_externa}")

    print(f"El valor de la variable local de la funcion externa antes de ser cambiada es: {variable_local_de_la_funcion_externa}")
    funcion_interna2()
    print(f"Valor de la variable local despues de la ejecucion de la funcion interna: {variable_local_de_la_funcion_externa}")

funcion_externa2()

"""Espero que con esta explicacion de los modificadores `global` y `nonlocal` hayas entendido lo que son"""


#* DIFICULTAD EXTRA (opcional):

def intercambiar_numeros(string1, string2):
    # Creando contadores para cada contexto:
    contador_de_valores_no_intercambiados = 0
    contador_de_string1 = 0
    contador_de_string2 = 0
    contador_de_string1_y_string2 = 0
    # Iterando numeros del 1 al 100
    for i in range(1, 101):
        # Si los numeros son multiplos de 3 y 5 intercambialos por la concatenacion de las dos cadenas de texto, imprimelos y aumenta el contador
        if i % 3 == 0 and i % 5 == 0:
            print(string1 + string2)
            contador_de_string1_y_string2 += 1
        # Si el numero es multiplo de 3 intercambialos por la primera cadena de texto, aumenta el contador e imprimelos
        elif i % 3 == 0:
            print(string1)
            contador_de_string1 += 1
        # Si el numero es multiplo de 5 intercambialos por la segunda cadena de texto, aumenta el contador e imprimelos
        elif i % 5 == 0:
            print(string2)
            contador_de_string2 += 1
        # Si el numero no es multiplo ni de 3 ni de 5 no intercambialos y aumenta el contador de los numeros no intercambiados
        else:
            contador_de_valores_no_intercambiados += 1

    # Imprimendo en consola los datos:
    print(f"Numero de veces que los numeros han sido intercambiados por la primera cadena de texto: {contador_de_string1}")
    print(f"Numero de veces que los numeros han sido intercambiados por la segundo cadena de texto: {contador_de_string2}")
    print(f"Numero de veces que los numeros han sido intercambiados por la primera y segunda cadena de texto: {contador_de_string1_y_string2}")
    print(f"Numero de veces que los numeros no han sido intercambiados: {contador_de_valores_no_intercambiados}")
        
intercambiar_numeros("Hola", "Mundo")