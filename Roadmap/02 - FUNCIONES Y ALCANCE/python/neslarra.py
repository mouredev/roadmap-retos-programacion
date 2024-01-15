"""
 EJERCICIO:
 - Crea ejemplos de funciones básicas que representen las diferentes
   posibilidades del lenguaje:
   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 - Comprueba si puedes crear funciones dentro de funciones.
 - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 - Debes hacer print por consola del resultado de todos los ejemplos.
   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)

 DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.

 Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""
numero_de_llamadas_por_funcion = dict()


def imprimir_llamadas_a_funcion() -> None:
    """
    Imprime la cantidad de veces que se ejecutó una función
    mostrando la variable global numero_de_llamadas_por_funcion.
    :return: None
    """
    global numero_de_llamadas_por_funcion

    def contador_de_ejecuciones():
        """
        Contabiliza la llamada
        :return: None
        """
        if "imprimir_llamadas_a_funcion" in numero_de_llamadas_por_funcion.keys():
            numero_de_llamadas_por_funcion["imprimir_llamadas_a_funcion"] += 1
        else:
            numero_de_llamadas_por_funcion["imprimir_llamadas_a_funcion"] = 1

    contador_de_ejecuciones()

    for k, v in numero_de_llamadas_por_funcion.items():
        print(f"La función {k} fue llamada {v} veces.")


def sumar(*args) -> int:
    """
    Suma los números recibidos
    :param args: numeros a sumar
    :return: suma
    """
    global numero_de_llamadas_por_funcion

    def contador_de_ejecuciones():
        """
        Contabiliza la llamada
        :return: None
        """
        if "sumar" in numero_de_llamadas_por_funcion.keys():
            numero_de_llamadas_por_funcion["sumar"] += 1
        else:
            numero_de_llamadas_por_funcion["sumar"] = 1

    contador_de_ejecuciones()

    suma = 0

    for sumando in args:
        suma += sumando

    return suma


def multiplicar(*args) -> int:
    """
    Multplica los números recibidos
    :param args: números a multiplicar
    :return: producto
    """
    global numero_de_llamadas_por_funcion

    def contador_de_ejecuciones():
        """
        Contabiliza la llamada
        :return: None
        """
        if "multiplicar" in numero_de_llamadas_por_funcion.keys():
            numero_de_llamadas_por_funcion["multiplicar"] += 1
        else:
            numero_de_llamadas_por_funcion["multiplicar"] = 1

    contador_de_ejecuciones()

    producto = 1
    for p in args:
        producto *= p
    return producto


def mail(*args) -> str:
    """
    Arma el mail con los datos recibidos
    :param args: Para, Copiar, Asunto y Texto
    :return: representación del mail
    """
    global numero_de_llamadas_por_funcion

    def contador_de_ejecuciones():
        """
        Contabiliza la llamada
        :return: None
        """
        if "mail" in numero_de_llamadas_por_funcion.keys():
            numero_de_llamadas_por_funcion["mail"] += 1
        else:
            numero_de_llamadas_por_funcion["mail"] = 1

    contador_de_ejecuciones()

    return f"To: {args[0]}\nCc: {args[1]}\nAsunto: {args[2]}\n{args[3]}\n"


def ejecutar(funcion, args):
    """
    Una manera de armar "reflexión" => recibe cadenas y evalúa para ejecutar una función.
    :param funcion: función a llamar
    :param args: argumentos a enviar
    :return: devuelve que lo que retorne cada función llamada
    """
    ejecutar = funcion + str(args)
    return eval(ejecutar)


def complejidad_extra(cadena1: str, cadena2: str) -> int:
    """
    Sigue los lineamientos indicados al ppio del reto.
    :param cadena1:
    :param cadena2:
    :return:
    """
    global numero_de_llamadas_por_funcion

    def contador_de_ejecuciones():
        """
        Contabiliza la llamada
        :return: None
        """
        if "complejidad_extra" in numero_de_llamadas_por_funcion.keys():
            numero_de_llamadas_por_funcion["complejidad_extra"] += 1
        else:
            numero_de_llamadas_por_funcion["complejidad_extra"] = 1

    contador_de_ejecuciones()

    numero_de_veces = 0

    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print(f"{cadena1} {cadena2}")
            else:
                print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(f"{i}")
            numero_de_veces += 1

    return numero_de_veces


tareas = {
    "suma 1": ["sumar", (1, 4, 7, 9)],
    "producto 1": ["multiplicar", (3, 3, 4)],
    "suma 2": ["sumar", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)],
    "suma 3": ["sumar", (1, 2, 3, 5, 8, 13, 21, 34)],
    "producto 2": ["multiplicar", (1, 2, 3, 4, 5,  6)],
    "correo": ["mail", ("neslarra@fibertel.com.ar",
                        "Brais.Moure@mouredev.com.es",
                        "Reto# 2 - funciones",
                        "Subiendo una versión python del reto."
                        )],
    "complejidad extra": ["complejidad_extra", ("Lorem Ipsum", "dolor sit amet")]
    }

for k, v in tareas.items():
    print(f"{k} =>  {ejecutar(v[0], v[1])}")

print(f"Otra suma: {sumar(1, 29, 30, 40, 50)}")
print(f"Otro producto: {multiplicar(1, 2, 4, 8, 16, 32, 64)}", end="\n\n")
print(f"Otro correo: {mail('neslarra@fibertel.com.ar', 'Brais.Moure@mouredev.com.es', 'Reto# 2 - funciones (2)', 'Agregué complejidad extra.')}")

imprimir_llamadas_a_funcion()
