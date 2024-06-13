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
print("#######Navegacion########")
def navegador_web():
    my_navigation = []
    my_back_urls=[]
    
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
               url_actual = input("Introduce la url:")
               my_navigation.append(url_actual)
           case "2":
               if len(my_back_urls) > 0:
                   my_navigation.append(my_back_urls.pop())
           case "3":
                if len(my_navigation) > 0:
                    my_back_urls.append(my_navigation.pop())
       if len(my_navigation) > 0:
           print(f"URL actual: {my_navigation[len(my_navigation)-1]}") 
       else:
           print(f"URL actual: None")
               
navegador_web()

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
         



