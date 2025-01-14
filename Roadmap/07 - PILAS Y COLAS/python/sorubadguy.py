import time

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
    pagina = 0
    
    while op != 0:
        print("Ingrese la opcion deseada")
        print("1: pagina siguiente")
        print("2: Pagina anterior")
        print("0: Cerrar Navegador")
        op = input("Opcion: ")
        match op:
            case "1":
                pagina = pagina_siguiente(dir, pagina)
            case "2":
                pagina = pagina_anterior(dir, pagina)
            case "0":
                print("El navegador se cerrara")
                break
            case _:
                print("opcion incorrecta")

def pagina_anterior(dir: list, pag: int):
    if(pag != 0):
        pag -= 1
        print(dir[pag])
        return pag
    else:
        print(f"Usted se encuentra en: {dir[pag]}, no quedan paginas anteriores")

def pagina_siguiente(dir: list, pag: int):
    print(dir, pag)
    if(pag == len(dir)-1):
        op_sitio = input("este es el ultimo sitio visitado, desea visitar otro? s/n:\n")
        if (op_sitio == "s"):
            dir.append(input("Ingrese el nuevo sitio:\n"))
            pag += 1
            print(dir[pag])
            return pag
    else:
        pag += 1
        print(dir[pag])
        return pag
            
navegador(dir_web)
