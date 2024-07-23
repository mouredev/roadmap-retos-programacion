"""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 */
"""

# Singleton
class Singleton:
    _instancia = None
    def __new__(cls) -> _instancia:
        if cls._instancia == None:
            cls._instancia = super(Singleton,cls).__new__(cls)
        return cls._instancia

# Pruebas 
instancia_1 = Singleton()
instancia_2 = Singleton()
instancia_3 = Singleton()

print(f"1 es igual a 2: {instancia_1 == instancia_2}")
print(f"2 es igual a 3: {instancia_2 == instancia_3}")
print(f"3 es igual a 1: {instancia_3 == instancia_1}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
"""

class Sesion:
    _instancia = None
    nombre = None
    id = None
    username = None
    email = None

    def __new__(cls,nombre,id,username,email):
        if cls._instancia is None:
            cls._instancia = super(Sesion,cls).__new__(cls)
            cls.nombre = nombre
            cls.id = id
            cls.username = username
            cls.email = email
        return cls._instancia
    
    def mostrar_datos(self):
        if Sesion._instancia != None:
            print(f"Sesión activa por {Sesion.username}")
            print(f"Nombre: {Sesion.nombre}")
            print(f"ID sesión: {Sesion.id}")
            print(f"Email: {Sesion.email}\n")
        else:
            print("Sesión No Activa\n")
    
    def cerrar_sesion(self):
        print(f"Sesión cerrada: {Sesion.username}\n")
        Sesion._instancia = None
        Sesion.nombre = None
        Sesion.id = None
        Sesion.email = None
        Sesion.username = None

# Pruebas
sesion_1 = Sesion("Emmanuel",1,"SrMancoMan","example@email.com")
sesion_2 = Sesion("Emmanuel2",2,"SrMancoMan2","example2@email2.com")
sesion_3 = Sesion("Emmanuel3",3,"SrMancoMan3","example3@email3.com")

sesion_1.mostrar_datos()
sesion_2.mostrar_datos()
sesion_3.mostrar_datos()

sesion_1.cerrar_sesion()
sesion_1.mostrar_datos()

sesion_2 = Sesion("Emmanuel2",2,"SrMancoMan2","example2@email2.com")

sesion_1.mostrar_datos()
sesion_2.mostrar_datos()
