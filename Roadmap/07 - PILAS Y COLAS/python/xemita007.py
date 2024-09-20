"""ejercicio"""

#pila
var=[]


def añadir(elmento):
    var.append(elmento)
    print(f"Elemento añadido {elmento} a la lista")

def eliminar():
    ele_list= var[len(var)-1]
    del var[len(var)-1]
    print(f"Elemento eliminadao {ele_list} de la lista")
    


añadir(1)
añadir(2)
añadir(3)
añadir(4)
eliminar()
eliminar()
eliminar()
eliminar()

#cola
var=[]


def añadir(elmento):
    var.append(elmento)
    print(f"Elemento añadido {elmento} a la lista")

def eliminar():
    ele_list= var[0]
    var.pop(0)
    print(f"Elemento eliminadao {ele_list} de la lista")
    


añadir(1)
añadir(2)
añadir(3)
añadir(4)
eliminar()
eliminar()
eliminar()
eliminar()

"""
#Extra
"""""
def navegador():
    
    var=[]

    while True:   
        web=input("buscar, para introducir la paguina a la que desea navegar, para ir hacia atras escribir atras,"
                "y para volver: adelante , para salir pulse salir")
        
        if web== "salir":
            print("Saliendo del navegador web.")
            break
    
        elif web== "atras":
            if len(var) > 0 :
                ele_list= var[len(var)-1]
                var.pop()
                print(f" retrocediendo a  {var[len(var) - 1]} ")

            else:
                print("Estas en la paguina de inicio")
        
        elif  web== "adelante":
            pass

        else:
            var.append(web)
            print(f"Has navegado a la web: {var[len(var) - 1]}.")

navegador()

def cola_impresion():

    var=[]

    while True:
        screem=input("introducir documentos a imprimir, para imprimir pulse , imprimir y para salir , salir ")
        
        if screem== "salir":
            print("Saliendo de la impresión")
            break
    
        elif screem== "imprimir":
            if len(var) > 0 :
                print(f" imprimiendo  {var[0]} ")
                var.pop(0)
                if len(var) > 0:
                    print(f"siguiente hoja de impresión {var[0]}")
                else:
                    print("No hay más documentos para imprimir.")

            else:
                print("no existen documentos")
        
        else:
            var.append(screem)
            print(f"Has añadido el documento a la cola de impresión: {var[len(var) - 1]}.")

cola_impresion()


