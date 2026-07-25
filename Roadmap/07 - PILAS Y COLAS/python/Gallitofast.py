#Ejercicio 07 
"""
Pilas (Stacks)
"""

"""
Operaciones clave:
push(): Añade un elemento a la parte superior (top) de la pila.
pop(): Elimina y devuelve el elemento superior.
peek() (o top()): Observa el elemento superior sin eliminarlo.
isEmpty(): Verifica si la pila está vacía.
"""
stack = []
stack.append(1)  # push(1)
stack.append(2)  # push(2)
stack.append(3)  # push(3)
print(stack.pop())  # Devuelve 3 (último elemento)


"""
Colas (Queue)
"""
"""
enqueue(): Añade un elemento al final (rear) de la cola.
dequeue(): Elimina y devuelve el primer elemento (front).
front(): Observa el primer elemento sin eliminarlo.
isEmpty(): Verifica si la cola está vacía.
"""
from collections import deque
dq = deque()
dq.appendleft(1)  # Añade al frente
dq.append(2)      # Añade al final
print(dq.popleft())  # Elimina del frente

list_web=[]
index=0
def list_empty(list_web):
    if len(list_web)==0:
        print ("The list is empty.")
        return True
    else:
        return False

def web_navigator():
    while True:
        action=input(" 1 Search web | 2 Back | 3 Forward | 4 Weblist | 5 Remove web from list | 6 Exit")
        global index
        match action:
            case "1":
                web = input("Enter the website:")
                list_web.append(web)
                index+=1
                print(list_web)

            case "2":
                if not list_empty(list_web):
                    if index ==1:
                        print(f"you are on the very first page: {list_web[index-1]}")
                    else:
                        index-=1
                        print(list_web[index-1])

            case "3":
                if  not list_empty(list_web):
                        if index == (len(list_web)):
                            print(f"You are on the last web on the list:{list_web[index-1]}")
                        else:
                            index+=1
                            print(list_web[index-1])
            case "4":
                print(f"Weblist{list_web}")
            case "5":
                if not list_empty(list_web):
                    list_web.pop()
                    print(list_web)
                    index-=1
            case "6":
                print("exit succesfully")
                break
            case _:
                print("Invalid entry | Select from 1 to 5")
web_navigator()
doc_print = deque() 

index_2=0 
doc=0
printed_doc=[]

