# 46 - X vs Bluesky
import datetime

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followed = []
        self.posts = []

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.id == other.id
    
    def __hash__(self):
        return hash((self.id,self.name))

    def follow_user(self, user):
        if user in self.followed:
            print(f"{self.name} ya esta siguiendo a esa cuenta ID[{user.id}]: {user.name}")
        else:
            self.followed.append(user)
            print(f"{self.name} ha comenzado a seguir a ID[{user.id}]: {user.name}!")

    def unfollow_user(self, user):
        if user in self.followed:
            self.followed.remove(user)
            print(f"{self.name} ha dejado de seguir a ID[{user.id}]: {user.name}!")
        else:
            print("Ese usuario no se encuentra en la lista de seguidos.")

    def show_followed(self):
        print(f"Lista de seguidos de {self.name}")
        if self.followed:
            for user in self.followed:
                print(f"{user.name}[ID:{user.id}]",end=" - ")
            print()
        else:
            print(f"{self.name} no sigue a nadie")

    def create_post(self, post_item):
        self.posts.append(post_item)

    def del_post(self, post_item):
        self.posts.remove(post_item)

    def show_feeds(self):
        list_feed_ordenate = sorted(self.posts, key = lambda x: x.create_date , reverse= True)
        count = 0
        for post in list_feed_ordenate:
            count += 1
            print(f"Post: {count}")
            post.show_post(self)
            if count >= 10:
                break
    
    def return_feeds(self):
        list_of_feeds = sorted(self.posts, key = lambda x: x.create_date , reverse= True)
        return list_of_feeds

    def show_followed_feeds(self):
        followed_feeds = [x.return_feeds() for x in self.followed]
        plain_followed_feeds = [x for sublist in followed_feeds for x in sublist]
        plain_followed_feeds.sort(key=lambda x: x.create_date, reverse= True)
        count = 0
        for post in plain_followed_feeds:
            count += 1
            print(f"Post: {count}")
            post.show_post(post.user)
            if count >= 10:
                break


class Post:
    def __init__(self,user: Person ,post_id: int, created_date: datetime.datetime, text : str):
        self.user = user
        self.post_id = post_id
        self.create_date = created_date
        self.text = text
        self.like_list = []

    def __eq__(self, other):
        if not isinstance(other, Post):
            return NotImplemented
        return self.user.id == other.user.id and self.post_id == other.post_id
    
    def __hash__(self):
        return hash((self.user.id,self.post_id))
    
    def add_like_post(self, user: Person):
        self.like_list.append(user)
    
    def remove_like_post(self, user: Person):
        self.like_list.remove(user)

    def show_post(self, user):
        if not user == self.user:
            print("Error: El usuario no es el que hizo este post")
            return
        print(f"Post [ID:{self.post_id}] de {user.name} [{user.id}]")
        print(f"Fecha: {self.create_date.strftime("%d/%m/%Y")}")
        print(f"Text: {self.text}")
        print(f"Likes: {len(self.like_list)}")
        if self.like_list:
            print(f"{[x.name for x in self.like_list]}")


class GreenXsky:
    def __init__(self):
        self.users = []
        self.posts = []
    # Funcion para saber si existe el usuario en la lista de usuarios
    def exist_user_ID(self, user_ID: int):
        if self.users:
            for user in self.users:
                if user.id == user_ID:
                    return True
            return False
        return False
    # Funcion para saber si existe el nombre
    def exist_user_name(self, user_name):
        if self.users:
            for user in self.users:
                if user_name == user.name:
                    return True
            return False
        return False
    # Funcion para obtener un usuario (Person) a partir de una ID
    def from_ID_obtain_user(self, user_id) -> Person|None:
        for user in self.users:
            if user.id == user_id:
                return user
        else:
            print("No existe usuario con esa ID!")
    # Realiza una validacion de si existen los usuarios y luego aplica un funcion dada en "metod_object",
    # que debe ser una funcion de la clase de user_ID (Person), dando como argumento other (Person), aunque
    # se le pase solo el ID de other (other_ID)
    def validate_and_run_user_un_follow(self, metod_object, user_ID, other_ID):
        if not self.exist_user_ID(user_ID) or not self.exist_user_ID(other_ID):
                print("Uno de los ID no existe.")
                return
        if user_ID == other_ID:
            print("No puede ser el mismo ID.")
            return
        other = self.from_ID_obtain_user(other_ID)
        for user in self.users:
            if user.id == user_ID:
                metod = getattr(user, metod_object, None)
                if callable(metod):
                    metod(other)
                else:
                    print(f"El método '{metod_object}' no existe.")
                return
    # Registra un usuario en la lista de usuario del objeto de clase GreenXsky
    def register_user(self,id ,name):
        if not self.exist_user_ID(id) and not self.exist_user_name(name):
            self.users.append(Person(id,name))
            print(f"Usuario [ID:{id}]: {name} creado exitosamente")
        else:
            print(f"Ya existe el ID:[{id}] y/o el nombre: {name}")

    def show_user_followed(self, user_ID):
        user = self.from_ID_obtain_user(user_ID)
        user.show_followed()
    # Funcion para verificar si el text es str y si tiene 200 caracteres como maximo
    def verify_text(self, text):
        if not isinstance(text,str):
            print("Valor invalido. Ingrese una cadena de texto")
            return None
        if not len(text)<=200:
            print("Error: El texto debe poseer como maximo 200 caracteres")
            return None
        return text
        
    def create_post(self, user_ID: int, post_ID: int, text: str, date: str):
        # Verifica si existe el usuario
        if not self.exist_user_ID(user_ID):
            print(f"No existe el usuario con ID: {user_ID}")
            return None
        user = self.from_ID_obtain_user(user_ID)
        print(f"Creando el post de {user.name} [ID: {user.id}]!")
        # Se verifica el texto
        verified_text = self.verify_text(text)
        if not verified_text:
            return None
        # Verificar si existe el id del post
        exist_post_id = next((u for u in self.posts if u.post_id == post_ID), None)
        if exist_post_id:
            print(f"Id del post ({post_ID}) ya existe!")
            return None
        # Si pasa las verificaciones se aplica el create post
        formated_date = datetime.datetime.strptime(date,"%d/%m/%Y")
        # Se crea el post
        post_greenxsky = Post(user, post_ID, formated_date, verified_text)
        # Se adhiere a las listas, del objeto de GreenXsky y al objeto de Person
        user.create_post(post_greenxsky)
        self.posts.append(post_greenxsky)
        print(f"Se ha creado el post exitosamente:\nPost: {verified_text}")

    def del_post(self, post_ID):
        # Se optiene el post
        post = next((x for x in self.posts if x.post_id == post_ID), None)
        # Se verifica si existe el post
        if not post:
            print(f"No existe post con ese ID: {post_ID}")
            return None
        # Se optiene el user
        user: Person = next((x for x in self.users if x == post.user), None)
        # Se verifica que existe el user
        if not user:
            print(f"No existe ese usuario con ID: {post.user.id}")
            return None
        # Se elimina el post de la lista de post general
        self.posts.remove(post)
        # Se elimina el post de la lista del post del usuario
        user.del_post(post)
        print(f"Se elimino el post de ID: {post_ID} exitosamente")

    def like_post(self, user_ID: int, post_ID: int):
        post: Post = next((x for x in self.posts if x.post_id == post_ID), None)
        user = next((x for x in self.users if x.id == user_ID), None)
        # Verifica si existen el user y el post
        if not post or not user:
            print(f"No existe el post de ID: {post_ID} o el user de ID: {user_ID} ")
            return None
        post.add_like_post(user)

    def unlike_post(self, user_ID: int, post_ID: int):
        # Verifica si existe el post en la lista de posts
        post = next((x for x in self.posts if x.post_id == post_ID), None)
        if not post:
            print(f"No existe el post de ID: {post_ID}")
            return None
        # Verifica si existe el user en la lista de likes del post
        user = next((x for x in post.like_list if x.id == user_ID), None)
        if not user:
            print(f"No existe el user de ID: {user_ID} en la lista de likes")
            return None
        # Elimina el like
        post.remove_like_post(user)

    def show_user_feed(self, user_ID: int):
        user = next((x for x in self.users if x.id == user_ID), None)
        if user:
            user.show_feeds()

    def show_user_followed_feed(self, user_ID: int):
        user: Person = next((x for x in self.users if x.id == user_ID), None)
        if user:
            print(f"Actualizacion de los feed de seguidos de {user.name}")
            user.show_followed_feeds()

# Instanciando la clase maestra
greenxsky = GreenXsky()
# Creando Usuarios
greenxsky.register_user(1,"Juan")
greenxsky.register_user(2,"Fran")
greenxsky.register_user(3,"Lau")
greenxsky.register_user(4,"Jaz")
greenxsky.register_user(5,"Carl")
greenxsky.register_user(6,"John")
greenxsky.register_user(3,"Juan") # Falla
greenxsky.register_user(3,"Clark") # Falla
# Probando el follow
greenxsky.validate_and_run_user_un_follow("follow_user",3,1)
greenxsky.validate_and_run_user_un_follow("follow_user",3,1) # Falla
greenxsky.validate_and_run_user_un_follow("follow_user",4,1)
greenxsky.validate_and_run_user_un_follow("follow_user",5,1)
greenxsky.validate_and_run_user_un_follow("follow_user",1,4)
greenxsky.validate_and_run_user_un_follow("follow_user",1,5)
greenxsky.validate_and_run_user_un_follow("follow_user",1,6)
# Viendo los followed
greenxsky.show_user_followed(1)
greenxsky.show_user_followed(2)
# Creando un post
greenxsky.create_post(
    4,
    1,
    "Hola mundo como estan!!",
    "07/05/2025"
)
greenxsky.create_post(
    4,
    2,
    "Hola mundo como estan 2 !!",
    "08/05/2025"
)
greenxsky.create_post(
    4,
    3,
    "Hola mundo como estan 3!!",
    "09/05/2025"
)
greenxsky.create_post(
    4,
    4,
    "Hola mundo como estan 4 en el pasado!!",
    "01/05/2025"
)
greenxsky.create_post(
    4,
    5,
    "Hola mundo como estan 5!!",
    "10/05/2025"
)
greenxsky.create_post(
    4,
    6,
    "Hola mundo como estan 6!!",
    "11/05/2025"
)
greenxsky.create_post(
    4,
    7,
    "Hola mundo como estan 7!!",
    "12/05/2025"
)
greenxsky.create_post(
    4,
    8,
    "Hola mundo como estan 8!!",
    "13/05/2025"
)
greenxsky.create_post(
    4,
    9,
    "Hola mundo como estan 9!!",
    "14/05/2025"
)
greenxsky.create_post(
    4,
    10,
    "Hola mundo como estan 10!!",
    "15/05/2025"
)
greenxsky.create_post(
    4,
    11,
    "Hola mundo como estan 11, el mejor!!",
    "16/05/2025"
)
greenxsky.create_post(
    4,
    12,
    "Hola mundo como estan 12!!",
    "17/05/2025"
)
# A partir de aca es de 5
greenxsky.create_post(
    5,
    13,
    "Hola mundo como estan 13!!",
    "12/05/2025"
)
greenxsky.create_post(
    5,
    14,
    "Hola mundo como estan 14!!",
    "15/05/2025"
)
greenxsky.create_post(
    5,
    15,
    "Hola mundo como estan 15!!",
    "20/05/2025"
)
greenxsky.create_post(
    5,
    16,
    "Hola mundo como estan 16!!",
    "19/05/2025"
)
# A partir de aca es el 6
greenxsky.create_post(
    6,
    17,
    "Hola mundo como estan 17!!",
    "20/05/2025"
)
greenxsky.create_post(
    6,
    18,
    "Hola mundo como estan 18!!",
    "19/05/2025"
)
greenxsky.create_post(
    3,
    19,
    "Hola mundo como estan 19!!",
    "20/05/2025"
)

# Borrando post
greenxsky.del_post(2)
# Dando like a los post
greenxsky.like_post(1,11)
greenxsky.like_post(2,11)
greenxsky.like_post(3,11)
greenxsky.like_post(4,1)
# Quitando like a los post
greenxsky.unlike_post(2,11)
greenxsky.unlike_post(4,5)
# Mostrado el los ultimos 10 feeds
# greenxsky.show_user_feed(4)
print()
greenxsky.show_user_followed_feed(1)