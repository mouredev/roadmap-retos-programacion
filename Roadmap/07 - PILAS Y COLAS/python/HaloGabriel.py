# EJERCICIO:
# Implementa los mecanismos de introducción y recuperación de elementos propios de las
# pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
# o lista (dependiendo de las posibilidades de tu lenguaje).

'''Stacks'''

documentos_apilados = ['Documento 1', 'Documento 2', 'Documento 3', 'Documento 4']

print(f"Documentos disponibles: {documentos_apilados}")

error = False

for documento in documentos_apilados[::-1]:
    print(f"Revisando documento: {documento}")
    if documento == 'Documento 1':
        error = not error

    documento_retirado = documentos_apilados.pop()
    print(f"Documento retirado: {documento_retirado}")

    if error:
        print(f"Documento necesita corrección: {documento_retirado}")
        print(f"Reinsertando documento y deteniendo proceso...")
        documentos_apilados.append(documento_retirado)
        break
    print("Continuando proceso...")
print("¡Proceso terminado!")
print(f"Documentos disponibles: {documentos_apilados}")

'''Queue'''

tickets = []

tickets.append(10001)
tickets.append(10002)
tickets.append(10003)
tickets.append(10004)
tickets.extend([10005, 10006, 10007, 10008, 10009, 10010])

print(f"\nTickets disponibles: {tickets}")

error = False

for ticket in tickets.copy():
    print(f"Atendiendo ticket N°{ticket}...")
    if ticket == 10008:
        error = not error

    ticket_retirado = ticket
    tickets.remove(ticket)
    print(f"Ticket retirado: {ticket_retirado}")

    if error:
        print(f"Hubo un error con ticket N°{ticket_retirado}")
        print(f"Reinsertando ticket y deteniendo proceso...")
        tickets.insert(0, ticket_retirado)
        break
    print("Continuando proceso...")
print("¡Proceso terminado!")
print(f"\nTickets disponibles: {tickets}")
print()

# DIFICULTAD EXTRA (opcional):
# - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
#   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarles
#   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
#   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
#   el nombre de una nueva web.

print("=== Pila de páginas web ===")

paginas_web = []
pagina_web_retrocedida = None

while True:
    print(
        "\nUsted se encuentra en: "
        f"{paginas_web[-1] if len(paginas_web) > 0 else "Página de Inicio"}"
        )

    print("\nOpciones disponibles: ")
    print("1. 'adelante' para avanzar de página web.")
    print("2. 'atrás' para retroceder de página web.")
    print("3. 'salir' para salir del navegador.")
    print("4. Ingresar cualquier nombre de página para navegar.")

    accion = input("\n¿Qué deseas hacer? ").strip()

    if accion.lower() == 'adelante':
        if not pagina_web_retrocedida:
            print("\nNo hay páginas web a la que avanzar.")
        else:
            paginas_web.append(pagina_web_retrocedida)
            pagina_web_retrocedida = None
    elif accion.lower() in ['atras', 'atrás']:
        if len(paginas_web) > 0:
            pagina_web_retrocedida = paginas_web.pop()
        else:
            print("\nNo hay páginas web a la que retroceder.")
    elif accion.lower() == 'salir':
        print("\nGracias por navegar con nosotros. Vuelva pronto.")
        break
    else:
        paginas_web.append(accion)
        pagina_web_retrocedidad = None
print()

#  - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
#    impresora compartida que recibe documentos y los imprime cuando así se le indica.
#    La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
#    interpretan como nombres de documentos.

print("=== Cola de documentos ===")

documentos = []

while True:
    print(f"\nDocumentos que faltan imprimir: {len(documentos)}")

    print("\nOpciones disponibles:")
    print("1. 'imprimir' para imprimir el siguiente documento.")
    print("2. 'salir' para salir de la impresora.")
    print("3. Ingresar cualquier nombre de documento para imprimir.")

    accion = input("\n¿Qué desea hacer? ").strip()

    if accion.lower() == "imprimir":
        if len(documentos) != 0:
            documento_impreso = documentos[0]
            documentos = documentos[1:]
            print(f"\nDocumento '{documento_impreso}' impreso.")
        else:
            print(f"\nNo hay documentos para imprimir.")
    elif accion.lower() == "salir":
        print("\nCerrando impresora. Gracias y que vuelva pronto.")
        break
    else:
        documentos.append(accion)
        print(f"\nDocumento '{accion}' agregado a la cola.")