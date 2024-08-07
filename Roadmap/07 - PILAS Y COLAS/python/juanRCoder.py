lista = []

# PILA - LIFO
# Los primeros en entrar son los ultimos en salir
for i in range(1, 5):     
    lista.append(i)     # -> apilando elementos en la lista comienza con 1, 2, 3, 4
    
# print(lista)          # [1, 2, 3, 4]

for _ in range(1, 5):  
    lista.pop()          # -> eliminando elementos en la lista comienza con 4, 3, 2, 1

# print(lista) # []



# COLA - FIFO:
# Los primeros en entrar son los primeros en salir
for i in range(1, 5):
    lista.append(i)     # -> apilando elementos en la lista comienza con 1, 2, 3, 4
    
# print(lista)          # [1, 2, 3, 4]

for i in range(1, 5):
    lista.remove(i)     # -> removiendo elementos de la lista comienza con 1, 2, 3, 4
    # print(lista)
    
# print(lista) # []


#  * DIFICULTAD EXTRA (opcional):
# Simulacion de las flechitas de una pagina web
def left_rigth():
    webs = ['home', 'services', 'products',  'contact']
    current = webs
    i = 0
    while i < 4:
        if (i != 3):
            print(f'Pagina Actual: {current[i]}')
        else:
            print(f'Pagina Actual: {current[i]} (ultimo)')
           
        eleccion = input(' < | > : ')
        
        if (eleccion == '>'):
            current[i+1]
            i+=1
        else:
            current[i-1]
            i-=1
            
left_rigth()