
### Pilas
lista = []
lista.append('1')
lista.append('2')
lista.append('3')
print(f'Para adicionar elementos usamos el metodo append. El ultimo elemento agregado ha sido {lista[-1]}')
print(lista)
print(f'Para eliminar elementos utilizamos el metodo pop. Sin argumento Pop elimina el ultimo elemento de la lista -> {lista[-1]}')
lista.pop()
print(lista)
print('Usando Append y Pop Las listas se comportan como Pilas, Last Input First Output')


### Colas
print('----------------------------------------------')
print('Para hacer un sistema First Input First Output podemos usar append y pop con el argumento 0')
print('Vamos a agregar elementos a ListaCola 1, 2, y 3 ')
listaCola = []
listaCola.append('1')
listaCola.append('2')
listaCola.append('3')
print(listaCola)
print(f'Vamos a eliminar el primer elemento -> {listaCola[0]} ')
listaCola.pop(0)
print(listaCola)
print(f'Vamos a adicionar un  elemento -> 4 ')
listaCola.append('4')
print(f'Vamos a eliminar el primer elemento -> {listaCola[0]} ')
listaCola.pop(0)
print(listaCola)

### Difucultad Extra
def safari():
    print('--------------Dificultad Extra 1 ----------------------')
    navegador = []
    index = len(navegador) - 1
    while True:
        accion = input('Precisa si quieres ir adelante o atras o quieres visitar una nueva pagina ')
        if accion not in ('atras', 'adelante'):        
            if index == len(navegador) -1 :
                navegador.append(accion)
                index = len(navegador) - 1
                print(f'nueva pagina agregada -> {accion}')            
                print(index)
            else:                                
                for i in range(index+1, len(navegador)): 
                    navegador.pop()
                navegador.append(accion)
                index = len(navegador) - 1
                print(f'nueva pagina agregada -> {accion}')            
                print(index)
        elif accion == 'atras':
            if index > 0:
                index -= 1
                print(f'la pagina es {navegador[index]}')
            else:
                print('Pagina de Inicio')
            print(f'atras index is {index}')       
        elif accion == 'adelante':
            if index < len(navegador) - 1:
                index += 1
                print(f'la pagina es {navegador[index]}')
            else:
                print('Has llegado al final del navegador ')
            
        print(navegador)

def canon():
    impresora = []
    while True:
        action = input('Que quieres hacer? ')
        if action == 'imprimir':
            if len(impresora) > 0:
                print(f'Imprimiendo el archivo {impresora[0]}')
                impresora.pop(0)
                print(impresora)
            else:
                print('La cola de impresion esta vacia')
        elif action == 'salir':
            break
        else:
            impresora.append(action)
            print(impresora)
        
#safari()
#canon()
            








