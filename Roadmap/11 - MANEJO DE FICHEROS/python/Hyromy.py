nombre = "Joel"
edad = 19
lenguaje = "Python"

lineas = [
    f"Nombre: {nombre}\n",
    f"Edad: {edad}\n",
    f"Lenguaje Fav: {lenguaje}\n"
]

file_path = "Roadmap/11 - MANEJO DE FICHEROS/python/Hyromy.txt"

# abrimos la ruta con permisos de escritura guardando como variable f
with open(file_path, "w") as f:
    f.writelines(lineas) # escribimos las lineas en f
    del lineas # borramos la variable lista

# abrimos el archivo (por defecto tiene permisos de lectura)
with open(file_path) as f:
    # leemos su contenido
    data = f.readlines()

# mostramos el contenido de la variable data
print(data)

for i in data: # iteramos cada linea
    print(i)

import os
os.remove(file_path) # eliminamos el archivo

# ---- DIFICULTAD EXTRA ----

class Ventas:
    def __init__(self):
        self.path = "Roadmap/11 - MANEJO DE FICHEROS/python/venta.txt"
        
        with open(self.path, "w") as f:
            f.write("")

    def create(self, producto:str, cantidad:int, precio:float):
        with open(self.path, "a") as f:
            f.write(f"{producto}, {cantidad}, {precio}\n")

    def read(self) -> list[str]:
        with open(self.path) as f:
            return f.readlines()

    def update(self, producto:str, nuevo_producto:str = None, nueva_cantidad:int = None, nuevo_precio:float = None) -> bool:
        file = self.read()

        i = 0
        for product in file:
            if product[:len(producto)] == producto:
                items = product.split(", ")

                if nuevo_producto == "":
                    nuevo_producto = items[0]

                if nueva_cantidad == -1:
                    nueva_cantidad = items[1]
                
                if nuevo_precio == -1:
                    nuevo_precio = items[2][:-2]
        
                break

            i += 1

        else:
            return False
        
        file[i] = f"{nuevo_producto}, {nueva_cantidad}, {nuevo_precio}\n"
        with open(self.path, "w") as f:
            f.writelines(file)

        return True

    def delete(self, producto) -> bool:
        file = self.read()

        i = 0
        for product in file:
            if product[:len(producto)] == producto:
                break
            
            i += 1

        else:
            return False
        
        file.pop(i)
        with open(self.path, "w") as f:
            f.writelines(file)

        return True
    
print("GESTION DE VENTAS\n")
ventas = Ventas()
while True:
    print("(C) Añadir producto\n" +
          "(R) Consultar productos\n" +
          "(U) Actualizar producto\n" +
          "(D) Eliminar producto\n" +
          "(X) SALIR")
    opt = input(" => ")

    if opt.casefold() == "c":
        nombre = input("Nombre del producto => ")
        cantidad = int(input(f"Cantidad de {nombre} => "))
        precio = float(input(f"Precio de {nombre} => "))

        ventas.create(nombre, cantidad, precio)

        print("\nPRODUCTO AGREGADO\n")

    elif opt.casefold() == "r":
        items = ventas.read()
        
        print()
        for item in items:
            print(item[:-1])
        print()
    
    elif opt.casefold() == "u":
        nombre = input("Nombre del producto a actualizar => ")
        nuevo_nombre = input(f"Nuevo nombre para {nombre} (deja en blanco para no modificarlo) => ")

        if nuevo_nombre == "":
            nuevo_nombre = nombre

        nueva_cantidad = int(input(f"Nueva cantidad para {nuevo_nombre} (escribe -1 para no modificarlo) => "))
        nuevo_precio = float(input(f"Nuevo precio para {nuevo_nombre} (escribe -1 para no modificarlo) => "))

        updated = ventas.update(nombre, nuevo_nombre, nueva_cantidad, nuevo_precio)
        if updated:
            print("\nPRODUCTO ACTUALIZADO\n")
        else:
            print("\nno se modifico porque el producto no existe xd\n")
    
    elif opt.casefold() == "d":
        nombre = input("Producto a eliminar => ")
        eliminado = ventas.delete(nombre)

        if eliminado:
            print("\nPRODUCTO ELIMINADO\n")
        else:
            print("\nNO ES POSIBLE ELIMINAR UN PRODUCTO INEXISTENTE\n")
    
    elif opt.casefold() == "x":
        os.remove(ventas.path)
        break

    else:
        print("\nOPCION NO VALIDA\n")