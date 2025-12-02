#23 - Python
# 
# EJERCICIO:
# Explora el patrón de diseño "singleton" y muestra cómo crearlo
# con un ejemplo genérico.
# 
# DIFICULTAD EXTRA (opcional):
# Utiliza el patrón de diseño "singleton" para representar una clase que
# haga referencia a la sesión de usuario de una aplicación ficticia.
# La sesión debe permitir asignar un usuario (id, username, nombre y email),
# recuperar los datos del usuario y borrar los datos de la sesión.
# 
class Counter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

def serparacion(cadena) -> str:
    global contador
    print(f'\nEjercicio {next(contador)}. {cadena * 20}')

contador = iter(Counter())

class Singleton:
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]
    
class Logger(Singleton):
    def log(self, message):
        print(f"LOG: {message}")

class UserSession(Singleton):

    def __init__(self):
        if not hasattr(self, 'user'):
            self.user = None

    def set_user(self, user_id, username, name, email):
        self.user = {
            'id': user_id,
            'username': username,
            'name': name,
            'email': email
        }

    def get_user(self):
        return self.user

    def clear_session(self):
        self.user = None

def excercise_singleton() -> None:
    serparacion('-:-')
    
    # Primera vez que se crea una instancia
    logger1 = Logger()
    logger1.log("Este es el primer mensaje")

    # Se crea otra instancia, pero se devuelve la misma que la primera
    logger2 = Logger()
    logger2.log("Este es el segundo mensaje")

    # Se verifica que ambas variables apuntan a la misma instancia
    print(f'Es logger1 = logger2: {logger1 is logger2}')  # Imprime: True

def extra_user_session() -> None:
    serparacion('-:-')
    
    # Crear una sesión de usuario
    print('\nCreando sesión de usuario...')
    session1 = UserSession()
    session1.set_user(1, 'jdoe', 'John Doe', 'jdoe@mail.com')
    print(f'Usuario en session: {session1.get_user()}')
    # Crear otra sesión de usuario
    print('\nCreando otra sesión de usuario...')
    session2 = UserSession()
    session2.set_user(2, 'mkart', 'Mikael Kart', 'mkart@mail.com')
    print(f'Usuario en session2 antes de borrar: {session2.get_user()}')
    # Verificar que ambas sesiones son la misma instancia
    print(f'\nEs session1 = session2: {session1 is session2}')  # Imprime: True
    # Borrar la sesión de usuario
    session2.clear_session()
    print('\nBorrando sesión de usuario...')
    print(f'Usuario en session1: {session1.get_user()}')
    print(f'Usuario en session2: {session2.get_user()}')
    
    
def main():
    excercise_singleton()
    extra_user_session()

if __name__ == "__main__":
    main()
