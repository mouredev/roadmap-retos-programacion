# @Author Daniel Grande (Mhayhem)

# EJERCICIO:
# La alternativa descentralizada a X, Bluesky, comienza a atraer
# a nuevos usuarios. ¿Cómo funciona una red de este estilo?
# 
# Implementa un sistema que simule el comportamiento de estas
# redes sociales.
# 
# Debes crear las siguientes operaciones:
# - Registrar un usuario por nombre e identificador único.
# - Un usuario puede seguir/dejar de seguir a otro.
# - Creación de post asociado a un usuario. Debe poseer
#   texto (200 caracteres máximo), fecha de creación 
#   e identificador único.   
# - Eliminación de un post.
# - Posibilidad de hacer like (y eliminarlo) en un post.
# - Visualización del feed de un usuario con sus 10 publicaciones
#   más actuales ordenadas desde la más reciente.
# - Visualización del feed de un usuario con las 10 publicaciones
#   más actuales de los usuarios que sigue ordenadas 
#   desde la más reciente.
#   
# Cuando se visualiza un post, debe mostrarse:
# ID de usuario, nombre de usuario, texto del post, 
# fecha de creación y número total de likes.
# 
# Controla errores en duplicados o acciones no permitidas.

import datetime

class User:
    def __init__(self, nickname: str, password: str, id: int):
        self.nickname = nickname
        self.password = password
        self.id = id
        self.followings = set()
        self.posts = []
        self.post_id = 0
    
    def following(self, user: object):
        self.followings.add(user)
    
    def unfollowing(self, user: object):
        self.followings.remove(user)
    
    def display_followings(self):
        for person in self.followings:
            print(f"{person.id} {person.nickname}")
    
    def choose_following(self, name: str):
        for person in self.followings:
            if name == person.nickname:
                return person
            else:
                return None
    
    def add_post(self, message: str):
        self.post_id += 1
        post = Post(message, self.post_id, self)
        self.posts.insert(0, post)
    
    def substract_post(self, post: object):
        self.posts.remove(post)
    
    def display_last_ten_posts(self):
        for post in self.posts[:10]:
            print(post)
    
    def display_following_feed(self):
        following_last_post = []
        
        for person in self.followings:
            following_last_post.extend(person.posts)
        
        last_feed = sorted(following_last_post,
                        key=lambda post: post.creation_date,
                        reverse=True)[:10]
        
        for post in last_feed:
            print(post.__str__())

class Post:
    def __init__(self, message: str, id: int, user: object):
        self.message = message
        self.id = id
        self.user = user
        self.creation_date = datetime.datetime.now(datetime.UTC)
        self.likes = 0
        self.liked = set()
    
    def add_likes(self, user: object):
        if user not in self.liked:
            self.likes += 1
            self.liked.add(user)
            return True
        else:
            return False
    
    def substract_like(self, user: object):
        if user.nickname in self.liked:
            self.likes -= 1
            self.liked.remove(user)
    
    def display_post_id(self, array: list):
        for post in array:
            print(f"{post.id} - {post.message}")
    
    def __str__(self):
        return f"{self.user.id} {self.user.nickname}\n{self.message}\n{self.creation_date}   ❤️{self.likes}"

class SocialNetwork:
    def __init__(self):
        self.users = []
        self.id = 0
    
    def create_user(self, nickname: str, password: str):
        self.id += 1
        user = User(nickname, password, self.id)
        return user
    
    def add_user(self, user: object):
        self.users.append(user)
    
    def display_last_posts(self, user: object):
        for post in user.posts:
            return user.__str__(), post.__str__()
    
    def login(self, nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                return user
        print("Usuario o contraseña incorrectos")
        return 

def main():
    social_network = SocialNetwork()
    while True:
        print(f"{'#' * 5} MySocial NetWork {'#' * 5}")
        print("1. Login.\n"
            "2. Salir")
        start = int(input())
        match start:
            case 1:
                if social_network.users:
                    attempts = 3
                    while attempts > 0:
                        nickname = input("Usuario: ")
                        password = input("Contraseña: ")
                        user = social_network.login(nickname, password)
                        if not user:
                            attempts -= 1
                            print(f"Intentos restantes {attempts}")
                        else:
                            while True:
                                print("1. Escribir post.\n" 
                                    "2. Eliminar post.\n"
                                    "3. Seguir usuario.\n"
                                    "4. Dejar de seguir a usuario.\n"
                                    "5. Ver posts de usuarios seguidos.\n"
                                    "6. like a post.\n" 
                                    "7. Dislike post.\n"
                                    "8. Mostrar posts propios.\n"
                                    "10. Logout.")
                                options = int(input())
                                match options:
                                    case 1:
                                        while True:
                                            message = input("Escriba el post.")
                                            if len(message) < 200:
                                                user.add_post(message)
                                                break
                                    case 2:
                                        for post in user.posts:
                                            print(f"{post.id} - {post.message}")
                                        id_del = int(input("Indiqué el número de id: "))
                                        for post in user.posts:
                                            if post.id == id_del:
                                                user.substract_post(post)
                                                break
                                            print(f"El id {id_del}, no existe.")
                                    case 3:
                                        print(social_network.users)
                                        user_to_follow = input("Indique el usuario a seguir: ")
                                        for nickname in social_network.users:
                                            if nickname.nickname == user_to_follow:
                                                user.following(nickname)
                                    case 4:
                                        print(user.followings)
                                        user_to_unfollow = input("Indique el usuario a dejar de seguir: ")
                                        for nickname in user.followings:
                                            if nickname.nickname == user_to_unfollow:
                                                user.unfollowing(nickname)
                                    case 5:
                                        user.display_following_feed()
                                    case 6:
                                        user.display_followings()
                                        name = input("Indique el usuario: ")
                                        person = user.choose_following(name)
                                        post_id = int(input("Indique id del post a dear like: "))
                                        found = False
                                        for post in person.posts:
                                            if post.id == post_id:
                                                result = post.add_likes(user)
                                                found = True
                                                break
                                            
                                        if result == None:
                                            print("Ya le has dado like a este post.")
                                    case 7:
                                        user.display_followings()
                                        name = input("Indique el usuario: ")
                                        person = user.choose_following(name)
                                        post_id = int(input("Indique id del post a dear like: "))
                                        found = False
                                        for post in person.posts:
                                            if user.nickname in post.liked and post_id == post.id:
                                                post.substract_like(user)
                                                found = True
                                                break
                                        if not found:
                                            print(f"No diste like a nigún post con id {post_id}")
                                    case 8:
                                        user.display_last_ten_posts()
                                    case 9:
                                        print("Saliendo de la red social.")
                                        break
                                    case _:
                                        print("La opción no es valida.")
                    print("se ha suoerado el número de intentos")
                    break
                else:
                    print("Lista de usuarios vacía, crearemos nuevo usuario")
                    nickname = input("Nombre de usuario: ")
                    password = input("Crear contraseña: ")
                    user = social_network.create_user(nickname, password)
                    social_network.add_user(user)
                    print(f"Usuario {nickname} creado correctamente.")
            case 2:
                print("Cerrando red social.")
                break