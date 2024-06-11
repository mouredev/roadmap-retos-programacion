#PILAS Y COLAS

#PILAS 
#Last Input First Output
my_list = [10,20,30,40]

my_list.append(50)
my_list.append(60)
#LIFO
my_list.pop()

print(my_list)

#COLAS
#First Input First Output
my_list = [10,20,30,40]

my_list.append(50)
my_list.append(60)

##FIFO
my_list.pop(0)

print(my_list)


print("DIFICULTAD EXTRA")
def navegador_web():
    my_navegacion = []
    while True:
       print("Selecciona la opcion:")
       print("1-Navegar a url")
       print("2-Adelante")
       print("3-Atras")
       print("4-Salir")
       option = input("Selecciona la opcion:")
       match option:
           case "4":
               break
           case "1":
               doc = input("Introduce la url:")
               my_navegacion.append(doc)
           case "2":
               if len(my_prints) > 0:
                   print(f"Imprimiendo documento.... {my_prints.pop(0)}")
                   print("Documento impreso")
               else:
                   print("No existen documentos para imprimir")


print("#######Impresion########")
def impresion():
    my_prints = []
    while True:
       print("Selecciona la opcion:")
       print("1-Introducir documento")
       print("2-Imprimir")
       print("3-Salir")
       option = input("Selecciona la opcion:")
       match option:
           case "3":
               break
           case "1":
               doc = input("Introduce el documento:")
               my_prints.append(doc)
           case "2":
               if len(my_prints) > 0:
                   print(f"Imprimiendo documento.... {my_prints.pop(0)}")
                   print("Documento impreso")
               else:
                   print("No existen documentos para imprimir")

impresion()
         



