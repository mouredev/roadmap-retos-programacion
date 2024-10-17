# /*
#  * EJERCICIO:
#  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
#  * con un ejemplo genérico.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el patrón de diseño "singleton" para representar una clase que
#  * haga referencia a la sesión de usuario de una aplicación ficticia.
#  * La sesión debe permitir asignar un usuario (id, username, nombre y email),
#  * recuperar los datos del usuario y borrar los datos de la sesión.
#  */

class PaternSin:

    _inst = None
    

    def __new__(qq):
        if qq._inst == None:
            qq._inst = super(PaternSin,qq).__new__(qq)
            qq._inst.name = ["tiburcio"] #name es variable de instancia
         
        return qq._inst
    
    def SetName(self, name):
        self.name.append(name)

p1 = PaternSin()
p2 = PaternSin()
p3 = PaternSin()

print(p1,p2,p3)
print(p1 is p2 is p3)
print("p1", p1.name)
p1.SetName("segundo")
print("p2", p2.name)
p3.SetName("tercero")
print("p3", p3.name)
print("p1", p1.name)
print("p2", p2.name)

# EXTRA 

class User:

    _instance = None

    def __new__(cls):
        if cls._instance == None:
            cls._instance = super(User,cls).__new__(cls)
            cls._instance.ID = 1001
            cls._instance.Name = "Federico"
            cls._instance.User_Name = "fedrico_makiavelo"
            cls._instance._instance.email = "fede@gmail.com"
        return cls._instance
    
    def Get_User(self):
        return f" Name {self.Name} User {self .User_Name} ID {self.ID} email {self.email}"

    def Delete_User(self):
        self.ID = None
        self.Name = None
        self.User_Name = None
        self.email = None
    
    

U1 = User()
U2 = User()

print(U1.Get_User())
print(U2.Get_User())
U1.Delete_User()
print(U1.Get_User())
print(U2.Get_User())
    