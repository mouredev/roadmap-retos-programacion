###############################################################################
### EJERCICIO
###############################################################################

# creamos un decorador singleton para nuestra clase.
# crear este decorador nos permitira reutilizarlo sin volver a escribir
def singleton(cls):
    """
    Decorador singleton que nos asegurara tener solo una instancia de una clase
    para aquella clases decoradas
    """
    __instances = dict() 
    
    def wrap(*args, **kwargs):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kwargs)
        
        return __instances[cls]
    
    return wrap

@singleton 
class User():    
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return self.username

@singleton
class Admin():
    def __init__(self, username):
        self.username = username
    def __str__(self):
        return f'{self.username}(Admin)'


# Creamos la primera instancia
instance_1 = User('Pepe Grillo')
print(f'Usuario = {instance_1}')
# La segunda instancia no se crea pues ya hay una creada
instance_2 = User('Naruto')
print(f'Usuario = {instance_1}, Usuario 2 = {instance_2}')


admin_1 = Admin('Vegeta')
admin_2 = Admin('Goku')
print(f'admin_1 = {admin_1}, admin_2 = {admin_2}')


###############################################################################
### DIFICULTAD EXTRA
###############################################################################
print('\nDificutad Extra:\n')


class Session:
    __instances = dict()
    
    def __new__(cls, *args, **kwargs):
        """
        Garantiza que solo se crea una instancia de la clase
        """
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__new__(cls)
        
        return cls.__instances[cls]  
    
    
    def __init__(self, id, username, name, email):
        self.user_data = {
            'id': id,
            'username': username,
            'name': name,
            'email': email
        }
    
    
    def __str__(self):
        """
        Imprime informacion del usuario
        """
        if self.user_data:
            return f"id:{self.user_data['id']}\nusername:{self.user_data['username']}\nname:{self.user_data['name']}\nemail:{self.user_data['email']}"
        else:
            return "Datos de usuario vacio."
    
    
    def delete_session(self):
        """
        borra los datos del usuario y elimina la instancia
        """
        self.user_data = {}
        del Session.__instances[self.__class__]
    
    
    def __del__(self):
        """
        Impremie mensaje despues de eliminar un objeto
        """
        print('Las sesion a sido eliminada')



# Creamos instancia con los datos de usuario
session_1 = Session(2, 'vegetta777', 'fran', 'fran@gmail.com')

# Obtenemos los datos del usuario
print("Datos del usuario:")
print(session_1)

# Borramos los datos del usuario
session_1.delete_session()

# Intentamos acceder a los datos del usuario
print("\nDespués de borrar la sesión:")
print(session_1)

