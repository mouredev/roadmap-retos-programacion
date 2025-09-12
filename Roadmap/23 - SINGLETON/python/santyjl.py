#23 PATRONES DE DISEÑO: SINGLETON

"""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
"""

class sigleton:
    # Variable de clase que almacenará la única instancia de la clase
    __instancia = None

    # Método especial que se llama para crear una nueva instancia de la clase
    def __new__(cls, *args, **kwargs):
        # Si no existe ninguna instancia de la clase, se crea una
        if cls.__instancia is None:
            cls.__instancia = super(sigleton, cls).__new__(cls)
        # Se devuelve la instancia única de la clase
        return cls.__instancia

# Creación de dos variables que apuntan a la instancia única de la clase sigleton
instancia1 = sigleton()
instancia2 = sigleton()

# Comprobación de que ambas variables apuntan a la misma instancia
print("\n-----------------Comprobacion de que las instancias son las mismas-------------------")
print("instancia1 == instancia2:", instancia1 is instancia2, "\n")

## Extra

class seccionDeUsuario:
    # Variable de clase que almacenará la única instancia de la clase
    __instancia = None

    # Método especial que se llama para crear una nueva instancia de la clase
    def __new__(cls):
        # Si no existe ninguna instancia de la clase, se crea una
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
            cls.__instancia.datos_de_usuario = None  # Inicialización de la variable de instancia
        # Se devuelve la instancia única de la clase
        return cls.__instancia

    # Método para iniciar sesión con los datos del usuario
    def iniciar_seccion(self, id, username, nombre, email):
        self.datos_de_usuario = {
            "id": id,
            "username": username,
            "nombre": nombre,
            "email": email
        }

    # Método para recuperar los datos del usuario
    def recuperar_datos(self):
        if self.datos_de_usuario:
            return self.datos_de_usuario
        return "no hay datos"

    # Método para cerrar la sesión del usuario
    def cerrar_seccion(self):
        self.datos_de_usuario = None

# Creación de dos variables que apuntan a la instancia única de la clase seccionDeUsuario
usuario1 = seccionDeUsuario()
usuario1.iniciar_seccion(1, "santyjl", "santiago", "algo@gmail.com")
print(usuario1.recuperar_datos())
print(usuario1.cerrar_seccion())

usuario2 = seccionDeUsuario()
usuario2.iniciar_seccion(2, "shechiremark", "justin", "cosa@gmail.com")
print(usuario2.recuperar_datos())
print(usuario1.recuperar_datos())

print(usuario1 is usuario2)
