"""
* EJERCICIO:
* Explora el patrón de diseño "singleton" y muestra cómo crearlo
* con un ejemplo genérico.
*
* DIFICULTAD EXTRA (opcional):
* Utiliza el patrón de diseño "singleton" para representar una clase que
* haga referencia a la sesión de usuario de una aplicación ficticia.
* La sesión debe permitir asignar un usuario (id, username, nombre y email),
* recuperar los datos del usuario y borrar los datos de la sesión.
"""

class Singleton:
    __instance = None  

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
            
            cls.__instance.data = "Singleton Data"
        return cls.__instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()
    
    print(s1 is s2)  
    
    print(s1.data)  # Salida: Singleton Data
    print(s2.data)  # Salida: Singleton Data
    
    s1.data = "New Singleton Data"
    print(s2.data)  # Salida: New Singleton Data


############### ------------------------------ EXTRA --------------------------------- #######################


class UsserSession:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(UsserSession, cls).__new__(cls)
            cls.__instance.user_data = {}
        return cls.__instance

    def set_user(self, id, username, name, email):
        self.user_data["id"] = id
        self.user_data["user_name"] = username
        self.user_data["name"] = name
        self.user_data["email"] = email

    def get_user(self):
        return self.user_data
    
    def cler_session(self):
        self.user_data = {}

if __name__== "__main__":
    session1 = UsserSession()

    session1.set_user(id=1, username="jhon00", name="Jhon", email="john.doe@example.com")

    user_info = session1.get_user()
    print(user_info)

    session2 = UsserSession()
    print(session1 is session2)

    user_info = session2.get_user()
    print(user_info)

    session2.cler_session()

    user_info = session1.get_user()
    print(user_info)