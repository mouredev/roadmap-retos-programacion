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

paginas = ['wwww.musica.com','wwww.musica.com/artistas','wwww.musica.com/canciones','wwww.musica.com/downloads']
indice = 0
print(f'La pagina web actual es: {paginas[indice]}')
while True:
    
    
    opcion = input("Seleccione la opción deseada: ")

    if opcion == '1' and indice < len(paginas) - 1:
        indice += 1
        
    elif opcion == '2' and indice > -1 * len(paginas):
        indice -= 1
        
    if opcion == '3':
        print('ADIOS!')
        break
    print(f'Indice: {indice}')
    print(paginas[indice])

#IMPRESORA

documentos = ['Documento1',]
while True:
    print('MENU')
    print('1.- Imprimir')
    print('2.- Nuevo documento')
    print('3.- Salir')
    opcion = input('Seleccione la opcion deseada: ')
    if opcion == '1' and len(documentos) > 0:
        print(f'{documentos.pop(0)}...Imprimiendo')
    elif opcion == '2':
        documentos.append(input('Nombre documento: '))
    elif opcion == '3':
        print('Adios!')
        break
    else:
        print('Opción incorrecta')