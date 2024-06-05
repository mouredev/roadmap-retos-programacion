"""
*Pilas y Colas
"""
#*Pilas

pila = [1,2,3,4]
pila.append(5)
print("Pilas\n",pila) #Agrego elemento al final(LI)
pila.pop()
print(pila) #Quito el ultimo elemento agregado(FO)

#*Colas

cola = [1,2,3,4]
cola.append(5) #agrego un elemento al final
print("Colas\n",cola)
cola.pop(0) #quito el primer elemento 
print(cola)

"""
!Extra
"""

dir_web = ["www.twitch.tv","www.twitch.tv/mouredev","www.twitch.tv/mouredev/videos","www.twitch.tv/mouredev/videos/2162695381"]

def navegador(dir):
    op = 1
    while op != 0:
        print("Ingrese la opcion deseada")
        print("1: pagina siguiente")
        print("1: Pagina anterior")
        op = input("Opcion: ")

def pagina_anterior():
    pass

def pagina_siguiente():
    pass

def pagina_nueva():
    pass