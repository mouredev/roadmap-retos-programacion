from __future__ import annotations
import os, platform
from datetime import datetime as dt
from typing import Dict, Set, TypedDict


if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')

"""
 * EJERCICIO:
 * La alternativa descentralizada a X, Bluesky, comienza a atraer
 * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 * 
 * Implementa un sistema que simule el comportamiento de estas
 * redes sociales.
 * 
 * Debes crear las siguientes operaciones:
 * - Registrar un usuario por nombre e identificador único. 
 * - Un usuario puede seguir/dejar de seguir a otro. 
 * - Creación de post asociado a un usuario. Debe poseer
 *   texto (200 caracteres máximo), fecha de creación 
 *   e identificador único.                            
 * - Eliminación de un post.                           
 * - Posibilidad de hacer like (y eliminarlo) en un post. 
 * - Visualización del feed de un usuario con sus 10 publicaciones
 *   más actuales ordenadas desde la más reciente.                 
 * - Visualización del feed de un usuario con las 10 publicaciones
 *   más actuales de los usuarios que sigue ordenadas 
 *   desde la más reciente.
 *   
 * Cuando se visualiza un post, debe mostrarse:
 * ID de usuario, nombre de usuario, texto del post, 
 * fecha de creación y número total de likes.
 * 
 * Controla errores en duplicados o acciones no permitidas.
"""
class Post(TypedDict):
    message: str
    date: dt
    likes: Set[User]

class User:
    auto_increment_user_id:int = 0
    
    def __init__(self, name:str) -> None:
        self.name: str = name  
        User.auto_increment_user_id += 1
        self.id = User.auto_increment_user_id
        self.user_posts: Dict[int, Post] = {}
        self.index_message: int = 0
        self.following: Set[User] = set()
        self.followers: Set[User] = set()

    def create_post(self, message: str) -> None:
        if (len(message) > 200):
            print("No se puede crear un post de más de 200 caracteres")
        else:
            self.index_message +=1
            self.user_posts[self.index_message] = {
    "message": message,
    "date": dt.now(),
    "likes": set()
}

    def follow_users(self, *users: User) -> None:
        for user in users:
            if user.name == self.name:
                continue
            self.following.add(user)
            user.followers.add(self)
    
    
    def unfollow(self, user: User) -> None:  
        if user in self.following:
            self.following.remove(user) 
            user.followers.remove(self)
            print(f"{self.name} ha dejado de seguir a {user.name}")
        else:
            print(f"{self.name} no puede dejar de seguir a {user.name} porque no lo estaba siguiendo anteriormente")


    def show_posts(self) -> None:    
        if len(self.user_posts) == 0:
                print(f"{self.name} no tiene nigún mensaje")
                return
        print(f"\nMensajes de {self.name}:\n")
        for key, value in reversed(self.user_posts.items()):
            likes_counter = len(value["likes"])
            date = value["date"]
            print(f"- {value["message"]},  creado el " 
                  f"{date.strftime('%d/%m/%Y %H:%M:%S')},"
                  f" message id: {self.id}-{key}, número de likes: {likes_counter}"
                  )
        

    def show_user_profile(self) -> None:
        print(
        f"\nINFORMACIÓN DE USUARIO\n -------------------\n"
        f"Nombre: {self.name}, ID: {self.id}\n"
        f"\nLe {'siguen' if len(self.followers) != 1 else 'sigue'} {len(self.followers)} "
        f"{'usuarios' if len(self.followers) != 1 else 'usuario'}:\n"
        )
        for follower in self.followers:
            print("-", follower.name)
        print(
            f"\nSiguiendo a {len(self.following)}"
            f" {'usuario:' if len(self.following) == 1 else ('usuarios' if len(self.following) == 0 else 'usuarios:')}\n"
            )
        for follower in self.following:
            print("-", follower.name)
        self.show_posts()
        self.show_following_feed()   
        print()
        
    def show_following_feed(self) -> None:  
        if len(self.following) == 0:
            return
        posts = []
        for user in self.following:
            for post_id, post in user.user_posts.items():
                posts.append((user, post_id, post))

        posts.sort(key=lambda x: x[2]["date"], reverse=True)
        
        print(f"\nFeed de {self.name} con publicaciones de usuarios seguidos:\n")
        for user, post_id, post in posts[:10]:
            likes_counter = len(post["likes"])
            date = post["date"]
            print(f"- {user.name}: {post['message']} "
                f"(ID {user.id}-{post_id}, {date.strftime('%d/%m/%Y %H:%M:%S')} "
                f"{likes_counter} {'like' if likes_counter == 1 else 'likes'})")
        
    def delete_post(self, messageID:int) -> None:
        if type(messageID) != int:
            print("Sólo se admite un dato numérico")
            return
        if messageID not in self.user_posts:
            print(f"{self.name} no puede borrar el mensaje con id {self.id}-{messageID} porque no existe")
        else:
            print(f"{self.name} ha borrado su mensaje con id {self.id}-{messageID}")
            del(self.user_posts[messageID])
    

    def like_post(self, user:User, postId:int) -> None:
        print("---------------------------\n")

        if postId not in user.user_posts:
            print(f"{user.name} no tiene ningún mensaje con id {user.id}-{postId}\n")
            return

        message = user.user_posts[postId]["message"]

        if self in user.user_posts[postId]["likes"]: 
            print(f"{self.name} no puede dar like al mensaje '{message}' porque ya le dio like antes\n")
            return

        user.user_posts[postId]["likes"].add(self)
        likes_counter = len(user.user_posts[postId]["likes"]) 
       
        print(f"{self.name} ha dado like al mensaje con id:{user.id}-{postId} de {user.name}"
            f", el mensaje de {user.name} '{message}' acumula {likes_counter} {'like' if likes_counter == 1 else 'likes'}\n")


    def unlike_post(self, user:User, postId:int):
        print("---------------------------\n") 
        if postId not in user.user_posts:
            print(f"el usuario {user.name} no tiene ningún mensaje con id {postId}\n")
            return
        
        message = user.user_posts[postId]["message"]

        if self not in user.user_posts[postId]["likes"]:
            print(f"{self.name} no puede quitar el like del mensaje con id {postId} de {user.name}",
                  "porque no le había dado like antes\n")
            return
        
        user.user_posts[postId]["likes"].discard(self)
        likes_counter = len(user.user_posts[postId]["likes"]) 

        print(f"{self.name} ha quitado el like al mensaje con id:{postId} de {user.name}"
        f", el mensaje de {user.name} '{message}' acumula {likes_counter} {'like' if likes_counter == 1 else 'likes'}\n")
        return
        
#LISTA DE USUARIOS
users_list = ["Jesus", "Sara", "Luis", "Ana", "Kevin", "Sandra", "Pedro", "Megan", "Victor", "Paula",
               "Miguel", "Silvia", "Pablo", "Rocío", "Joseph", "Isabel", "Tony", "Cristina", "Marco", "Elena"]

#CREACIÓN DE INSTANCIAS DE CLASE
users = [User(name) for name in users_list]
jesus, sara, luis, ana, kevin, sandra, pedro, megan, victor, paula, \
miguel, silvia, pablo, rocio, joseph, isabel, tony, cristina, marco, elena = users

#CREACIÓN DE MENSAJES
jesus.create_post(f"Este es el primer mensaje de {jesus.name}")
jesus.create_post(f"Este es el segundo mensaje de {jesus.name}")
sara.create_post(f"Este es el primer mensaje de {sara.name}")
pedro.create_post(f"Este es el primer mensaje de {pedro.name}")
kevin.create_post(f"Este es el primer mensaje de {kevin.name}")
sara.create_post(f"Este es el segundo mensaje de {sara.name}")
elena.create_post(f"Este es el primer mensaje de {elena.name}")
victor.create_post(f"Este es el primer mensaje de {victor.name}")
miguel.create_post(f"Este es el primer mensaje de {miguel.name}")
jesus.create_post(f"Este es el tercer mensaje de {jesus.name}")
paula.create_post(f"Este es el primer mensaje de {paula.name}")
marco.create_post(f"Este es el primer mensaje de {marco.name}")
joseph.create_post(f"Este es el primer mensaje de {joseph.name}")
paula.create_post(f"Este es el segundo mensaje de {paula.name}")
cristina.create_post(f"Este es el primer mensaje de {cristina.name}")
isabel.create_post(f"Este es el primer mensaje de {isabel.name}")
jesus.create_post(f"Este es el cuarto mensaje de {jesus.name}")
kevin.create_post(f"Este es el segundo mensaje de {kevin.name}")
miguel.create_post(f"Este es el primer mensaje de {miguel.name}")
megan.create_post(f"Este es el primer mensaje de {megan.name}")
kevin.create_post(f"Este es el tercer mensaje de {kevin.name}")
luis.create_post(f"Este es el primer mensaje de {luis.name}")
silvia.create_post(f"Este es el primer mensaje de {silvia.name}")


#CREACIÓN DE USUARIOS SEGUIDOS
jesus.follow_users(luis, ana, rocio, paula, sara, joseph, megan)
sara.follow_users(pedro)
cristina.follow_users(victor, jesus, paula, joseph, luis)
ana.follow_users(pedro, elena, joseph)
victor.follow_users(jesus, paula, tony, pablo)
rocio.follow_users(megan, pedro, paula)
isabel.follow_users(kevin, marco, victor, cristina, paula, megan, jesus, cristina)
elena.follow_users(paula, isabel, kevin, joseph, victor, miguel, rocio, luis)
megan.follow_users(pedro, joseph, tony, cristina, megan)
kevin.follow_users(marco, miguel, elena, pablo, jesus, sandra)
sandra.follow_users(megan, paula, cristina, sara, silvia)

#EL USUARIO marco INTENTA SEGUIRSE A SÍ MISMO, EL SISTEMA LO OBVIA Y NO LO REGISTRA
marco.follow_users(cristina, elena, megan, jesus, rocio, marco) 

#EL USUARIO miguel ABRE LA FUNCIÓN PARA SEGUIR A OTROS PERO NO NOMBRA A NADIE, EL SISTEMA LO OBVIA Y NO LO REGISTRA
miguel.follow_users()

#EL USUARIO jesus INTENTA BORRAR UNA PUBLICACIÓN INEXISTENTE CON ID 4
jesus.show_user_profile()
jesus.delete_post(8)

#EL USUARIO jesus BORRA SU SEGUNDA PUBLICACIÓN CON ID 2
jesus.delete_post(2)
jesus.show_user_profile()

#LA USUARIA ISABEL INTENTA DEJAR DE SEGUIR A jesus AL QUE NO SEGUÍA ANTERIORMENTE
isabel.unfollow(jesus)

#LA USUARIA ISABEL DEJA DE SEGUIR A VICTOR
victor.show_user_profile()
isabel.unfollow(victor)
isabel.show_user_profile()
victor.show_user_profile()              

#CREACIÓN DE VARIOS LIKES A MENSAJES CONCRETOS POR SU ID
cristina.like_post(jesus, 1)
elena.like_post(jesus, 1)
isabel.like_post(victor, 1)
kevin.like_post(jesus, 1)
megan.like_post(jesus, 3)
cristina.like_post(jesus, 1)
jesus.like_post(kevin, 2)
sara.like_post(luis, 1)
megan.like_post(jesus, 4)
jesus.like_post(silvia, 1)
#jesus INTENTA DAR LIKE A UN MENSAJE DE JOSEPH QUE NO EXISTE
jesus.like_post(joseph, 2)

#LA USUARIA cristina QUITA EL LIKE AL MENSAJE CON ID1 DE jesus
cristina.unlike_post(jesus, 1)

#LA USUARIA cristina INTENTA QUITAR UN LIKE A UN MENSAJE QUE NO HABÍA DADO LIKE ANTES
cristina.unlike_post(joseph, 1)

#MUESTRA DE PERFIL COMPLETO DE VARIOS USUARIOS
jesus.show_user_profile()
sara.show_user_profile()
megan.show_user_profile()
pedro.show_user_profile() 
kevin.show_user_profile()
marco.show_user_profile()
victor.show_user_profile()
elena.show_user_profile()
cristina.show_user_profile()
isabel.show_user_profile()
miguel.show_user_profile()




