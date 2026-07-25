# EJERCICIO:
# Explora el patrón de diseño "singleton" y muestra cómo crearlo
# con un ejemplo genérico.
from typing import Optional


class Singleton:
    _instance = None

    def __new__(cls, name: Optional[str] = None):
        if cls._instance is None:
            if name is None:
                raise ValueError("El primer Singleton debe tener un nombre")
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.name = name
        elif name is not None:
            raise ValueError(
                "El Singleton ya esta inicializado, no puedes pasar nuevos parametros"
            )
        return cls._instance

    def __init__(self, name: Optional[str] = None):
        pass  # la inicializacion se hace en __new__

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return f"Singleton instance: {self.name}"


singleton = Singleton(name="Cristian Floyd")
print(singleton.get_name())
print(singleton)
singleton2 = Singleton()
print(f"Singleton2 nombre: {singleton2.get_name()}")
print(f"¿Son la misma instancia? {singleton is singleton2}")


#
# DIFICULTAD EXTRA (opcional):
# Utiliza el patrón de diseño "singleton" para representar una clase que
# haga referencia a la sesión de usuario de una aplicación ficticia.
# La sesión debe permitir asignar un usuario (id, username, nombre y email),
# recuperar los datos del usuario y borrar los datos de la sesión.


class UserSession:
    """
    Clase que representa la sesión de usuario de una aplicación ficticia.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserSession, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self) -> None:
        # inicializar solo una vez
        if not self._initialized:
            self._initialized = True
            self.id = None
            self.username = None
            self.name = None
            self.email = None
        
    def set_user(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email

    def get_user(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "email": self.email
        }

    def clear_session(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None
        print("Sesión limpiada")

    def is_active(self):
        """
        Verifica si la sesión está activa.
        """
        return self.id is not None

if __name__ == "__main__":
    # Primera instancia
    session1 = UserSession()
    session1.set_user(1, "cristianfloyd", "Cristian Floyd", "cristian@example.com")
    
    # Segunda "instancia" (realmente es la misma)
    session2 = UserSession()
    
    # Verificar que son la misma instancia
    print(f"¿Son la misma instancia? {session1 is session2}")  # True
    
    # Los datos están disponibles desde cualquier referencia
    print(f"Datos desde session2: {session2.get_user()}")
    
    # Limpiar sesión
    session1.clear_session()
    print(f"Sesión activa: {session2.is_active()}")  # False