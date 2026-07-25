r"""
 EJERCICIO:
 La alternativa descentralizada a X, Bluesky, comienza a atraer
 a nuevos usuarios. ¿Cómo funciona una red de este estilo?
 
 Implementa un sistema que simule el comportamiento de estas
 redes sociales.
 
 Debes crear las siguientes operaciones:
 - Registrar un usuario por nombre e identificador único.
 - Un usuario puede seguir/dejar de seguir a otro.
 - Creación de post asociado a un usuario. Debe poseer
   texto (200 caracteres máximo), fecha de creación 
   e identificador único.   
 - Eliminación de un post.
 - Posibilidad de hacer like (y eliminarlo) en un post.
 - Visualización del feed de un usuario con sus 10 publicaciones
   más actuales ordenadas desde la más reciente.
 - Visualización del feed de un usuario con las 10 publicaciones
   más actuales de los usuarios que sigue ordenadas 
   desde la más reciente.
   
 Cuando se visualiza un post, debe mostrarse:
 ID de usuario, nombre de usuario, texto del post, 
 fecha de creación y número total de likes.
 
 Controla errores en duplicados o acciones no permitidas.
"""
from datetime import datetime as dt, timedelta as td
from random import randint as rndi
from time import sleep

users = [
    {"userid": 1, "username": "neslarra", "following": [1, 2, 3, 4]},
    {"userid": 2, "username": "toribio", "following": [2, 6]},
    {"userid": 3, "username": "pepapig", "following": [3, 1, 2, 4, 5]},
    {"userid": 4, "username": "sandmanteo", "following": [4, 3]},
    {"userid": 5, "username": "eltartufo", "following": [5, 3, 1, 2]},
    {"userid": 6, "username": "gorilin", "following": [6, 2, 4]}
]
posts = [
    {"postid": 1, "userid": 1, "post": "Hoy es un buen día para empezar de nuevo", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [3]},
    {"postid": 2, "userid": 1, "post": "La clave del éxito está en la persistencia.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [3, 5]},
    {"postid": 3, "userid": 2, "post": "Haz que cada momento cuente.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [1, 3, 5, 6]},
    {"postid": 4, "userid": 3, "post": "Menos perfección, más autenticidad.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 5, "userid": 3, "post": "El futuro es creado por lo que haces hoy", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 6, "userid": 2, "post": "La actitud positiva es la clave de todo.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 7, "userid": 3, "post": "A veces, los pequeños pasos nos llevan lejos.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [1, 5]},
    {"postid": 8, "userid": 4, "post": "La vida es un reflejo de tus pensamientos.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 9, "userid": 3, "post": "No se trata de esperar, se trata de crear.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 10, "userid": 4, "post": "Lo importante no es lo que haces, sino cómo lo haces.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 11, "userid": 5, "post": "El cambio comienza desde adentro.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 12, "userid": 6, "post": "Sueña en grande, actúa más grande.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 13, "userid": 5, "post": "Si no arriesgas, nunca sabrás lo que podrías lograr.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 14, "userid": 4, "post": "La vida no se mide en respiraciones, sino en momentos", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [6]},
    {"postid": 15, "userid": 5, "post": "Lo único imposible es lo que no intentas.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 16, "userid": 5, "post": "Hoy es un buen día para aprender algo nuevo.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [3]},
    {"postid": 17, "userid": 5, "post": "La felicidad es una elección, no un destino.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 18, "userid": 1, "post": "Cada error es una lección disfrazada.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 19, "userid": 1, "post": "Todo lo que necesitas está dentro de ti.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 20, "userid": 1, "post": "El éxito no es el final, es el camino.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": []},
    {"postid": 21, "userid": 6, "post": "Cambia tus pensamientos y cambiarás tu vida.", "time": dt.now() - td(days=rndi(1, 7), hours=rndi(1, 24), minutes=rndi(1, 60), seconds=rndi(1, 60)), "likedby": [2]}
]
current_user = ""


def login(username: str = "") -> bool:
    global current_user
    username = input("LOGIN: Ingrese nombre ed usuario: ").lower() if not username else username
    if not (username and username in [x["username"] for x in users]):
        return False
    current_user = username
    return True


def sign_up_user() -> bool:
    global users
    username = input("REGISTRACIÓN: Ingrese nombre ed usuario: ").lower()
    if not username or username in [x["username"] for x in users]:
        return False
    userid = users.__len__() + 1
    users.append({"userid": userid, "username": username, "following": [userid]})
    return True if login(username) else False


def add_post(post: str) -> None:
    global posts
    userid = [x["userid"] for x in users if x["username"] == current_user][0]
    posts.append({"postid": posts.__len__() + 1, "userid": userid, "post": post, "time": dt.now()})
    print("Nuevo post agregado")
    sleep(1)
    show_posts()


def show_posts() -> None:
    followed = [x["following"] for x in users if x["username"] == current_user][0]
    for followed_user in followed:
        available_posts = [x for x in posts if x["userid"] == followed_user]
        available_posts = sorted(available_posts, key=lambda x: x["time"], reverse=True)
        print(f"{'-' * 100}")
        for post in available_posts[0:10]:
            username = [x["username"] for x in users if x["userid"] == post["userid"]][0]
            my_id = [user["userid"] for user in users if user["username"] == current_user][0]
            liked = "TE GUSTÓ" if my_id in post['likedby'] else "(es tuyo)" if username == current_user else "¿Te gusta?"
            print(f"{post['time'].strftime('%d-%b-%Y %H:%M:%S')} {username}: {post['post']}")
            print(f"\tpostId: {post['postid']} likes: {post['likedby'].__len__()} => {liked}")


def remove_post():
    my_id = [user["userid"] for user in users if user["username"] == current_user][0]
    print("\nIndique el número de post a eliminar: ")
    while True:
        remove_postid = input("PostId (0 para cancelar): ")
        if remove_postid.isalnum():
            remove_postid = int(remove_postid)
            break
    if remove_postid > 0:
        post_index = -1
        for index, post in enumerate(posts):
            if post["postid"] == remove_postid and post["userid"] == my_id:
                post_index = index
                break
        if post_index > -1:
            post_ = posts.pop(post_index)
            print(f"Post {post_['postid']} eliminado.")
            sleep(1)
            show_posts()
        else:
            print(f"Post {remove_postid} NO Encontrado (SOLO podés eliminar tus propios posteos).")


def menu() -> int:
    print(f"\nBienvenido {current_user}")
    print("\n\t1- Cambiar de usuario")
    print("\t2- Hacer un posteo")
    print("\t3- Eliminar un posteo")
    print("\t4- ver posteos")
    print("\t5- Like/unLike un posteo")
    print("\t6- Segir/Dejar a otro usuario")
    print("\t0- Salir")
    while True:
        option = input("\n\t Ingresa opción => ")
        if option and option.isalnum() and 0 <= int(option) <= 6:
            break
    return int(option)


def follow():
    my_id = [user["userid"] for user in users if user["username"] == current_user][0]
    my_followings = [x["following"] for x in users if x["username"] == current_user][0]
    for user in users:
        followed = "LO SIGO" if user["userid"] in my_followings else "NO LO SIGO"
        if user["userid"] != my_id:
            print(f"{user['userid']} {user['username']} {followed}")
    print("\nIndicá el id de usuario a seguir (o dejar de seguir): ")
    while True:
        user_id = input("UserId (0 para cancelar): ")
        if user_id.isalnum():
            user_id = int(user_id)
            break
    if user_id > 0:
        user_index = -1
        for index, user in enumerate(users):
            if user["userid"] == user_id:
                user_index = index
                break
        if user_index > -1 and user_id != my_id:
            if users[user_index]["userid"] in my_followings:
                my_followings.remove(users[user_index]["userid"])
                new_state = f"Dejé de seguir a {users[user_index]["username"]}"
            else:
                my_followings.append(users[user_index]["userid"])
                new_state = f"Empecé de seguir a {users[user_index]["username"]}"
            print(f"{new_state}")
            sleep(1)
            show_posts()
        else:
            print(f"Usuario no encontrado (y no te podés seguir/dejar a vos mismo).")


def like():
    my_id = [user["userid"] for user in users if user["username"] == current_user][0]
    print("\nIndicá el número de post que te gusta (o dejó de gustar): ")
    while True:
        liked_postid = input("PostId (0 para cancelar): ")
        if liked_postid.isalnum():
            liked_postid = int(liked_postid)
            break
    if liked_postid > 0:
        post_index = -1
        for index, post in enumerate(posts):
            if post["postid"] == liked_postid and post["userid"] != my_id:
                post_index = index
                break
        if post_index > -1:
            if my_id in posts[post_index]["likedby"]:
                posts[post_index]["likedby"].remove(my_id)
                new_state = "DEJÓ DE GUSTARME"
            else:
                posts[post_index]["likedby"].append(my_id)
                new_state = "ME GUSTA"
            print(f"Post {liked_postid} {new_state}.")
            sleep(1)
            show_posts()
        else:
            print(f"Post {liked_postid} NO Encontrado (SOLO podés 'gustar' posts de tus seguidos).")


def main():
    global current_user
    while True:
        if not current_user:
            if not login():
                if not sign_up_user():
                    break
        option = menu()
        match int(option):
            case 0:
                quit()
            case 1:
                current_user = ""
                login()
            case 2:
                post = input("Ingrese el mensaje a postear: ")
                post = post if post.__len__() <= 200 else post[0:200]
                add_post(post)
            case 3:
                remove_post()
            case 4:
                show_posts()
            case 5:
                like()
            case 6:
                follow()


if __name__ == "__main__":
    main()
