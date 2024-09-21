import csv,random
                
def cantidad_lineas():
    cantidad = 0

    with open ("mouredevpro.csv") as file:
        datos = csv.reader(file , delimiter ="|")
    
        for dato in datos:
            cantidad = cantidad + 1
        return cantidad -1 
    
def ganador(posicion):
    num = 0

    with open ("mouredevpro.csv") as file:
        lineas = csv.reader(file , delimiter ="|")
    
        for linea in lineas:
            if num == posicion:
                ganador = linea
            num = num + 1
        
        return ganador     
    
cantidad = cantidad_lineas()  

while True:
    posicion1 = random.randint (1,cantidad)
    subscripcion = ganador(posicion1)
    if subscripcion [2] == " activo":
        break

while True:
    posicion2 = random.randint (1,cantidad) 
    if not(posicion2 == posicion1):
        descuento = ganador(posicion2)
        if descuento [2] == " activo":
            break
        
while True:
    posicion3 = random.randint (1,cantidad) 
    if not(posicion3 == posicion2 or posicion3 == posicion1):
        libro = ganador (posicion3)
        if libro [2] == " activo":
            break 
         
print (f"EL GANADOR DE LA SUBSCRIPCION ES: {subscripcion[1]} . CON ID: {subscripcion[0]}.\n")
print (f"EL GANADOR DE LA DESCUENTO ES: {descuento[1]} . CON ID: {descuento[0]}.\n")
print (f"EL GANADOR DE LA LIBRO ES: {libro[1]} . CON ID: {libro[0]}.\n")
           
    