# Pilas
pila = [1, 2, 3, 4, 5]

# Agregar elementos a una pila
pila.append(6)
pila.append(7)

print('Pila orignial: ', pila)

# Eliminar el ultimo elemento agregado a la pila
pila.pop()
print('Pila nueva: ', pila)


# Colas
cola = [2, 4, 6, 8, 10]

cola.append(12)
cola.append(14)

print('Cola original: ', cola)

# Eliminar el primer elemento agregado a la cola
cola.pop(0)

print('Cola nueva: ', cola)


# DIFICULTAD EXTRA

def navegador():
  
  history = []

  while True:
    print(
      """
            AGENDA:
            1. Agregar nueva url
            2. Adelante
            3. Atras
            4. Salir
      """
    )
    option = input('\nEscoger del menu: ')

    match option:
      case "1":
        print('Agregar nueva url')
        name = input('Agregar nueva url para navegar: ')
        history.append(name)
      case "2":
        print('Adelante')
        pass
      case "3":
        print('Atras')
        if(len(history) > 0):
          history.pop()
      case "4":
        print('Saliendo...')
        break
      case _:
        print('Opcion no valida. Intentar de nuevo.')
      
    if(len(history) > 0):
      print('Has navegado a la web: ', history[len(history) - 1])
    else:
      print('No hay nuevas urls')
    

# navegador()


def impresora():
  cola = []

  while True:
    print(
      """
            AGENDA:
            1. Agregar nuevo documento a la impresora
            2. Imprimir
            3. Salir
      """
    )
    option = input('\nEscoger del menu: ')

    match option:
      case "1":
        print('Agregar nuevo documento a la impresora')
        name = input('Nombre del documento: ')
        cola.append(name)

        if(len(cola) > 0):
          print('Cola de impresion: ', cola)
      case "2":
        print('Imprimir')
        if(len(cola) > 0):
          print("Imprimiendo documento: ", cola.pop(0))
        else:
          print("No hay documentos en cola.")
      case "3":
        print('Saliendo...')
        break
      case _:
        print('Opcion no valida. Intentar de nuevo.')

impresora()