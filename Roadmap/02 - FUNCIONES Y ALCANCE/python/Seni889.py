"""
FUNCIONES DEFINITIVAS
"""

# def saludar():
#     print("Hola mundo")

# def saludar1(nombre):
#     print(f"Hola {nombre}")

# def caminar():
#      return "Luis"
 

# edad = int(input("Ingrese su edad: "))

# def mayor(edad):
#     if edad >= 45:
#         return "Tienes promociones 2x1"
#     elif edad >= 18:
#         return "Pasa con precio normal"
#     else:
#          return "Usted no puede ingresar"  


# nombre = input("Ingresa tu nombre: ") 
# edad = input("Ingresa tu edad: ")
# direccion = input("Ingrese su direccion: ")

# def usuarios(nombre, edad, direccion):
#     return {
#         "nombre": nombre,
#         "edad": edad,
#         "direccion": direccion 
#     }

# print(usuarios(nombre, edad, direccion))

# def cursos():
#     return ("python", "java")



# def usuario():
#     return {
#         "id": 1,
#         "nombre" : "Andy",
#         "apellido" : "Reyes",
#         "edad" : 18
#     }

# print(usuario())

# def restaurantes(usuarios, name ):
#     print(f"El nombre del restaurante es: {name} y el encargado es {usuarios["nombre"]} {usuarios["apellido"]}")
    
# usuarios = usuario()

# #
# def cliente():
#     return{
#         "id": 1,
#         "nombre": "Josue",
#         "apellido": "Reyes",
#         "ciudad": "Piura",
#         "edad": 20
#     }

# # def clientes(client, nomb):
# #     sms = f"Este cliente {client["nombre"]} {client["apellido"]} tiene este restaurante {nomb}"
# #     return sms

# def clientes(client, nomb):
    
#     sms = f"El restaurante es : {nomb}\n El cliente es {client["nombre"]}\n estos son los proveedores"
#     return sms
# client = cliente()

# res = clientes(client, "El buen sabor")

# print(res)

# print(restaurantes(usuarios, "El buen Sabor"))

# #con armuento predeterminado
# def personas (nam= "Bebe"):
#     print (f"Buenas, {nam}")


# personas("Jordy")
# personas()

# #con argumentos
# def person(enc, siti):
#     print(f"{enc}, {siti}") 

# person(siti = "Jose", enc ="Hola")
# person("Hola", "Andy")

# #Con return incluido

# def persons(encw, sitiw):
#     return f"{encw}, {sitiw}"

# print(persons("Hola", "Jose"))
# print(persons("Jose", "Hola"))


# def personsid ():
#     return  "Buenos" , "Malos"

# nombre, saludo = personsid()

# print(saludo)
# print(nombre)



def objetos(*names):
    for nombre in names:
        print(f"Muy buenas tardes {nombre}")

objetos("Luis", "Martin", "Jordy")


def objetoss(**names):
    for clave, nombre in names.items():
        print(f"Muy buenas tardes {nombre} ({clave})")

objetoss(
    id = 1,
    name = "Josue", 
    edad = 21
)

"""
FUNCIONES DENTRO DE FUNCIONES
"""

def saludos():
    def saludo():
        print("Esta es una funcion dentro de otra funcion")
    saludo()
saludos()



def saludoss(nombre):
    def salud(text):
        return text.upper()
    
    sms = f"Hola, {salud(nombre)}. Muy buenas tardes"
    return sms

print(saludoss("Andy"))


def fiesta(nombre):
    def direccion(str):
        return str.upper()
    mensaje = f"El nombre de la fiesta es: {direccion(nombre)}"
    return mensaje

print(fiesta("San Juan de Dios"))


def user_nombre(nombre, edad):
    def edad_user(edad):
        if edad >= 60:
            return "Usted si puede ingresar, con premios incluidos"
        elif edad >= 18:
            return "Usted si puede continuar, ya tiene 18 años"
        else:
            return "Ustede todavia es una wuawita "

    return  f"Bienvenid@ {nombre} {edad_user(edad)}"

print (user_nombre("Andy", 21))


"""
FUNCIONES DEL LENGUAJE
"""
print(len("Andy"))
print(type("AndyJosue"))
print(type(28))
# print(input("Ingresa tu nombre: ")) #Ingresa de datos por consola
print(int(5))
print(str("andyadrianzen".upper()))
      
"""
VARIABLE LOCALES Y GLOBALES
""" 

#variable global
variable_global = "Mundo"
print(variable_global)

#variable global y locales
def hola_mundo():
    variable_local = "Hola" 
    print(f"{variable_local}, {variable_global}")

hola_mundo()

#variable local
def buen_dia():
    dias = "Buenos dias"
    nombre = "Andy"
    print(f"{dias}, {nombre}")

buen_dia()

"""
EXTRA EJERCICIO
"""

def funcion_num(text_1, text_2) -> int:
    count = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(text_1 + text_2)
        
        elif num % 3 == 0:
            print(text_1)
        
        elif num % 5 == 0:
            print(text_2)
        
        else:
            print(num)
            count += 1
    return count 

print(funcion_num("text_1", "text_2"))  

    
        
    
# print(cursos())





# print(mayor(edad))

# print(caminar())
# saludar()
# saludar1("Josue")

