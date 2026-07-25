import uuid
from datetime import datetime

# Almacenamos los usuarios y posts globalmente
users = {}
posts = {}

# Límite de caracteres para los posts
POST_TEXT_LIMIT = 200


# Función para registrar un usuario
def register_user(name):
    if name in [user["name"] for user in users.values()]:
        raise ValueError(f"El nombre de usuario '{name}' ya existe.")
    user_id = str(uuid.uuid4())  # Genera un identificador único
    users[user_id] = {
        "id": user_id,
        "name": name,
        "following": set(),  # Usuarios que sigue
    }
    return user_id


# Función para seguir a otro usuario
def follow_user(follower_id, followee_id):
    if follower_id not in users or followee_id not in users:
        raise ValueError("Uno o ambos IDs de usuario no existen.")
    if follower_id == followee_id:
        raise ValueError("Un usuario no puede seguirse a sí mismo.")
    users[follower_id]["following"].add(followee_id)


# Función para dejar de seguir a otro usuario
def unfollow_user(follower_id, followee_id):
    if follower_id not in users or followee_id not in users:
        raise ValueError("Uno o ambos IDs de usuario no existen.")
    users[follower_id]["following"].discard(followee_id)  # No arroja error si no lo sigue


# Función para crear un post
def create_post(user_id, text):
    if user_id not in users:
        raise ValueError("El usuario no existe.")
    if len(text) > POST_TEXT_LIMIT:
        raise ValueError(f"El texto del post no puede superar los {POST_TEXT_LIMIT} caracteres.")
    post_id = str(uuid.uuid4())  # Genera un identificador único
    posts[post_id] = {
        "id": post_id,
        "author_id": user_id,
        "text": text,
        "created_at": datetime.now(),
        "likes": set(),  # IDs de usuarios que dieron like
    }
    return post_id


# Función para eliminar un post
def delete_post(post_id):
    if post_id not in posts:
        raise ValueError("El post no existe.")
    del posts[post_id]


# Función para dar like a un post
def like_post(user_id, post_id):
    if user_id not in users:
        raise ValueError("El usuario no existe.")
    if post_id not in posts:
        raise ValueError("El post no existe.")
    posts[post_id]["likes"].add(user_id)


# Función para quitar un like de un post
def unlike_post(user_id, post_id):
    if user_id not in users:
        raise ValueError("El usuario no existe.")
    if post_id not in posts:
        raise ValueError("El post no existe.")
    posts[post_id]["likes"].discard(user_id)


# Función para visualizar el feed de un usuario
def view_feed(user_id, include_following=False):
    if user_id not in users:
        raise ValueError("El usuario no existe.")
    # Filtrar los posts relevantes
    if include_following:
        relevant_posts = [
            post for post in posts.values()
            if post["author_id"] == user_id or post["author_id"] in users[user_id]["following"]
        ]
    else:
        relevant_posts = [
            post for post in posts.values() if post["author_id"] == user_id
        ]
    # Ordenar por fecha de creación (más recientes primero)
    relevant_posts.sort(key=lambda x: x["created_at"], reverse=True)
    # Limitar a los 10 más recientes
    relevant_posts = relevant_posts[:10]
    # Mostrar los posts
    for post in relevant_posts:
        author = users[post["author_id"]]
        print(f"[{post['created_at']}] {author['name']} (ID: {author['id']}):")
        print(f"    {post['text']}")
        print(f"    Likes: {len(post['likes'])}")
        print()


# Pruebas iniciales
if __name__ == "__main__":
    # Crear usuarios
    user1 = register_user("Alice")
    user2 = register_user("Bob")
    user3 = register_user("Charlie")

    # Seguir usuarios
    follow_user(user1, user2)
    follow_user(user1, user3)

    # Crear posts
    post1 = create_post(user1, "Hola, este es mi primer post.")
    post2 = create_post(user2, "¡Hola a todos! Este es Bob.")
    post3 = create_post(user3, "Charlie en la casa.")

    # Likes
    like_post(user1, post2)
    like_post(user3, post2)
    like_post(user2, post3)

    # Ver feeds
    print("\n--- Feed de Alice (siguiendo a Bob y Charlie) ---")
    view_feed(user1, include_following=True)

    print("\n--- Feed propio de Bob ---")
    view_feed(user2, include_following=False)

    # Eliminar un post
    delete_post(post1)

    print("\n--- Feed de Alice después de eliminar un post ---")
    view_feed(user1, include_following=True)
