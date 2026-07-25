"#[número] - [lenguaje_utilizado]"
# 
# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).
# 
# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.
# - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#   impresora compartida que recibe documentos y los imprime cuando así se le indica.
#   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#   interpretan como nombres de documentos.
# 
def serparacion(cadena):
    print('{}'.format(cadena * 20))

palabras_aleatorias = [
    "Abismo", "Brújula", "Cántaro", "Delicado", "Ébano", "Fervor", "Gema", "Horizonte", "Ímpetu", "Joven",
    "Kilogramo", "Laberinto", "Mármol", "Nácar", "Órbita", "Papiro", "Quirúrgico", "Radiante", "Sutil", "Tímpano",
    "Utopía", "Vértigo", "Xenofobia", "Yacimiento", "Zócalo", "Armonía", "Bohemio", "Céfiro", "Diligencia", "Efímero",
    "Furtivo", "Grácil", "Hélice", "Ígneo", "Jolgorio", "Kiosco", "Lánguido", "Melancolía", "Nostalgia", "Ópalo",
    "Pálido", "Quimera", "Risueño", "Solitario", "Tácito", "Umbral", "Voraz", "Xilófono", "Yunque", "Zodiaco",
    "Algoritmo", "Bitácora", "Cristal", "Destello", "Espejismo", "Fractal", "Glaciar", "Hechizo", "Ilusión", "Jíbaro",
    "Karma", "Lunar", "Magia", "Nebulosa", "Ocre", "Panacea", "Quijote", "Relámpago", "Sigilo", "Tundra",
    "Ukelele", "Vaina", "Walabi", "Yoga", "Zafiro", "Ágora", "Bizarro", "Crisálida", "Diáfano", "Efusión",
    "Fugaz", "Gárgola", "Hada", "Inmune", "Júbilo", "Kaolín", "Límpido", "Metamorfosis", "Nítido", "Onírico",
    "Peregrino", "Quórum", "Rostro", "Súbito", "Trémulo", "Usurpador", "Voluble", "Xilografía", "Yodo", "Zambullida",
    "Abnegación", "Botella", "Cataclismo", "Desván", "Enigmático", "Filosofía", "Girasol", "Hilera", "Invierno", "Jerarquía",
    "Koala", "Licor", "Mirada", "Néctar", "Obsequio", "Pócima", "Quijada", "Ráfaga", "Sombrío", "Talismán",
    "Universo", "Vaho", "Waflera", "Yegua", "Zepelín", "Acentuar", "Binario", "Clavícula", "Desidia", "Énfasis",
    "Fantasma", "Glamour", "Horizonte", "Incandescente", "Jazmín", "Kaleidoscopio", "Luminoso", "Monolito", "Nudillo", "Óleo",
    "Polvo", "Quieto", "Rompecabezas", "Silencio", "Transparente", "Ulterior", "Vertiente", "Xiita", "Yacimiento", "Zaguán",
    "Anacronismo", "Bombilla", "Colmena", "Divagar", "Esmeralda", "Flecha", "Galaxia", "Hongo", "Idolatría", "Joya",
    "Kayak", "Letargo", "Melodía", "Nido", "Ocaso", "Palabras", "Quetzal", "Rumor", "Sabor", "Trama",
    "Urna", "Viento", "Wombat", "Yate", "Zarpa", "Altruista", "Bamba", "Célula", "Despertar", "Escarcha",
    "Farol", "Gaveta", "Hiena", "Incierto", "Jacarandá", "Kilo", "Lápiz", "Máscara", "Neón", "Olla",
    "Pluma", "Querubín", "Rinoceronte", "Sombra", "Tijera", "Útil", "Vacío", "Whisky", "Yacaré", "Zafarrancho"
]
def fifo():
    my_lista = []
    for element in palabras_aleatorias:
        if len(my_lista) <= 10:
            my_lista.append(element)
        else:
            output = my_lista.pop(0)
            print(output, end=", ")
            my_lista.append(element)
    restante = len(my_lista)
    for element in range(restante):
        output = my_lista.pop(0)
        if element == restante - 1:
            print(output)
        else:
            print(output, end=", ")

def lifo():
    my_lista = []
    for element in palabras_aleatorias:
        if len(my_lista) <= 10:
            my_lista.append(element)
        else:
            output = my_lista.pop(-1)
            print(output, end=", ")
            my_lista.append(element)
    restante = len(my_lista)
    for element in range(restante):
        output = my_lista.pop(-1)
        if element == restante - 1:
            print(output)
        else:
            print(output, end=", ")

def navegacion():
    my_lista = []
    my_lista_fow =[]
    cururl = ''
    while True:
        print('Por favor indica la url a la que quieres navegar, o si quieres ir "atras" o "adelante", o "salir"')
        url = input('>').lower()
        match url:
            case "salir":
                return
            case "atras":
                if len(my_lista) > 0:
                    my_lista_fow.insert(0, cururl)
                    cururl = my_lista.pop()
                    print(f'{"-"*50}\nhttp://{cururl}\n{"-"*50}')
                else:
                    print("No hay datos de web anteriores")
            case "adelante":
                if len(my_lista_fow) > 0:
                    my_lista.append(cururl)
                    cururl = my_lista_fow.pop(0)
                    print(f'{"-"*50}\nhttp://{cururl}\n{"-"*50}')
                else:
                    print('No hay ninguna web guardada')
            case _:
                my_lista.append(cururl)
                cururl = url
                print(f'{"-"*50}\nhttp://{cururl}\n{"-"*50}')
                if len(my_lista_fow) > 0: my_lista_fow.clear()

def imprimir():
    my_lista_impr = []
    while True:
        print('Por favor envía el archivo, dale a "imprimir" o "salir"')
        document = input('>').lower()
        match document:
            case "salir":
                return
            case "imprimir":
                if len(my_lista_impr) == 0:
                    print(f'{"-"*50}\nNúmero de documentos que hay en la cola de impresión: {len(my_lista_impr)}\n{"-"*50}')
                else:
                    printdocument = my_lista_impr.pop(0)
                    print(f'{"-"*50}\nImprimiento el documento: {printdocument} \nNúmero de documentos que quedan en la cola de impresión: {len(my_lista_impr)}\n{"-"*50}')
            case _:
                my_lista_impr.append(document)
                print(f'{"-"*50}\nNúmero de documentos en la cola de impresión: {len(my_lista_impr)}\n{"-"*50}')

def main():
    fifo()
    serparacion('.-')
    lifo()
    serparacion('.-')
    navegacion()
    serparacion('.-')
    imprimir()
    serparacion('.-')

main()
