#46 { Retos para Programadores } X VS BLUESKY 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

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

log = print

import uuid
from datetime import datetime
import time

class Post:
    def __init__(self, user, text):
        if len(text) > 200:
            raise ValueError("Post text cannot exceed 200 characters.")
        self.id = str(uuid.uuid4())
        self.user = user
        self.text = text
        self.created_at = datetime.now()
        self.likes = set()

    def like(self, user):
        self.likes.add(user)

    def unlike(self, user):
        self.likes.discard(user)

    def get_total_likes(self):
        return len(self.likes)

    def __str__(self):
        return f"Post by {self.user.name}: {self.text} (Likes: {self.get_total_likes()})"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.following = set()
        self.posts = []

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.discard(user)

    def create_post(self, text):
        post = Post(self, text)
        self.posts.append(post)
        return post

    def delete_post(self, post):
        if post not in self.posts:
            raise ValueError("Post not found.")
        self.posts.remove(post)

    def get_feed(self):
        feed = sorted(self.posts, key=lambda p: p.created_at, reverse=True)[:10]
        return feed

    def get_following_feed(self):
        feed = []
        for user in self.following:
            feed.extend(sorted(user.posts, key=lambda p: p.created_at, reverse=True)[:10])
        return sorted(feed, key=lambda p: p.created_at, reverse=True)[:10]

# Simulating the behavior of the JavaScript code
def main():
    log("Retosparaprogramadores #46.")

    user1 = User("Niko Zen", 1)
    user2 = User("Bob Marley", 2)
    user3 = User("Psicotrogato", 3)

    user1.follow(user2)
    user1.follow(user3)

    post1 = user1.create_post("I'm almost finishing this roadmap for developers.")
    post1_1 = user1.create_post("I'm thinking in the possibility of start some of the developer course in mouredev, to get more possibilities to find a remote job.")
    post1_2 = user1.create_post("I start to feel comfortable with Javascript and its ecosystem, right now I'm studying Next.js.")
    post2 = user2.create_post("But Jamming!")
    post2_1 = user2.create_post("I'm not going to wait in vain for your love!")
    post2_2 = user2.create_post("I shot the sheriff, but I didn't shoot the deputy!")
    post3 = user3.create_post("In a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society.")
    post3_1 = user3.create_post("My life is perfect because I accept it as it is.")

    post1.like(user2)
    post1.like(user3)

    # log the feeds with meaningful output
    log([str(post) for post in user1.get_feed()])
    log([str(post) for post in user1.get_following_feed()])
    log([str(post) for post in user2.get_feed()])
    log([str(post) for post in user2.get_following_feed()])
    log([str(post) for post in user3.get_feed()])
    log([str(post) for post in user3.get_following_feed()])

if __name__ == "__main__":
    main()

# Output:
"""   
Retosparaprogramadores #46.
["Post by Niko Zen: I'm almost finishing this roadmap for developers. (Likes: 2)", "Post by Niko Zen: I'm thinking in the possibility of start some of the developer course in mouredev, to get more possibilities to find a remote job. (Likes: 0)", "Post by Niko Zen: I start to feel comfortable with Javascript and its ecosystem, right now I'm studying Next.js. (Likes: 0)"]
["Post by Bob Marley: I'm not going to wait in vain for your love! (Likes: 0)", "Post by Bob Marley: I shot the sheriff, but I didn't shoot the deputy! (Likes: 0)", 'Post by Psicotrogato: In a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society. (Likes: 0)', 'Post by Psicotrogato: My life is perfect because I accept it as it is. (Likes: 0)', 'Post by Bob Marley: But Jamming! (Likes: 0)']
["Post by Bob Marley: I'm not going to wait in vain for your love! (Likes: 0)", "Post by Bob Marley: I shot the sheriff, but I didn't shoot the deputy! (Likes: 0)", 'Post by Bob Marley: But Jamming! (Likes: 0)']
[]
['Post by Psicotrogato: In a society that has abolished every kind of adventure, the only adventure that remains is abolishing the society. (Likes: 0)', 'Post by Psicotrogato: My life is perfect because I accept it as it is. (Likes: 0)']

"""