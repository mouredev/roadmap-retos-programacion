"""
/*
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
 */
"""
from datetime import datetime 

class SocialNetwork():

    def __init__(self, msg_test=False) -> None:
        self.postId = 0
        self.users = {}
        self.posts = {}
        self.msg_test = msg_test

    def __str__(self) -> str:
        text_output = ''.join([f"User ID: {id} - Name: {user['name']}\n" 
                        for id, user in self.users.items()])
        return text_output
    
    def register_user(self, name: str, id: int) -> None:
        if id in self.users:
            print(f"User ID:{id} already")
            return
        self.users[id] = {"name": name, 
                          "following": set(),
                          "followers": set(),
                          "post": []}
        
    def follow_user(self, id: int, id_to_follow: int) -> None:

        if id not in self.users and id_to_follow not in self.users:
            print(f"User ID:{id} or ID:{id_to_follow} not found")
            return
        
        self.users[id]["following"].add(id_to_follow)
        self.users[id_to_follow]["followers"].add(id)

        if self.msg_test:
            print(
                f"{self.users[id]['name']} ahora sigue a " +
                f"{self.users[id_to_follow]['name']}."
            )

    def unfollow_user(self, id: int, id_to_unfollow: int) -> None:
        
        if id not in self.users and id_to_unfollow not in self.users:
            print(f"User ID:{id} or ID:{id_to_unfollow} not found")
            return
        
        self.users[id]["following"].discard(id_to_unfollow)
        self.users[id_to_unfollow]["followers"].discard(id)

        if self.msg_test:
            print(
                f"{self.users[id]['name']} ahora dejó de seguir a " +
                f"{self.users[id_to_unfollow]['name']}."
            )

    def create_post(self, userId: int, text: str) -> None:
        if userId not in self.users:
            print(f"User ID:{userId} not found")
            return
        if len(text) > 200:
            print("Post text too long, maximum 200 characters")
            return

        self.postId += 1

        postId = self.postId
        
        self.users[userId]["post"].append(postId)
        # Create post
        self.posts[postId] = {
            "userId": userId,
            "text": text,
            "date": datetime.now(),
            "likes": set()
        }
        if self.msg_test:
            print(f"Post created with ID: {postId}")

    def delete_post(self, post_id: int) -> None:
        if post_id not in self.posts:
            print(f"Post ID:{post_id} not found")
            return
        
        userId = self.posts[post_id]["userId"]
        self.users[userId]["post"].remove(post_id)
        del self.posts[post_id]
        if self.msg_test:
            print(f"Post ID:{post_id} deleted")

    def like_post(self, userId: int, postId: int) -> None:
        if userId not in self.users:
            print(f"User ID:{userId} not found")
            return
        if postId not in self.posts:
            print(f"Post ID:{postId} not found")
            return
        
        self.posts[postId]["likes"].add(userId)
        if self.msg_test:
            print(f"New like in post ID:{postId}")

    def unlike_post(self, userId: int, postId: int) -> None:
        if userId not in self.users:
            print(f"User ID:{userId} not found")
            return
        if postId not in self.posts:
            print(f"Post ID:{postId} not found")
            return
        
        self.posts[postId]["likes"].discard(userId)
        if self.msg_test:
            print(f"Like removed in post ID:{postId}")
    
    def visualization_feed_user(self, userId: int):
        
        if userId not in self.users:
            print(f"User ID:{id} not found")
            return
        
        feed = sorted((self.posts[postId] 
                       for postId in self.users[userId]["post"]), 
                      key=lambda x: x["date"], reverse=True)
        
        for counter, postId in enumerate(feed):
            if counter == 10:
                break
            print(
                f"User ID: {userId} - {self.users[userId]['name']}\n" +
                f"Text: {postId['text']}\n\n" +
                f"Likes: {len(postId['likes'])} - Publication date: {postId['date']}\n"
            )

    def visualization_feed_follow(self, userId: int):
        
        if userId not in self.users:
            print(f"User ID:{id} not found")
            return
        

        postFollowId = []
        for followId in self.users[userId]["following"]:
            postFollowId.extend(self.users[followId]["post"])

        feed = sorted((self.posts[postId] 
                       for postId in postFollowId), 
                      key=lambda x: x["date"], reverse=True)

        for counter, postId in enumerate(feed):
            if counter == 10:
                break
            userPostId = postId["userId"]
            userPostName = self.users[userPostId]["name"]
            print(
                f"User ID: {userPostId} - {userPostName}\n" +
                f"Text: {postId['text']}\n\n" +
                f"Likes: {len(postId['likes'])} - Publication date: {postId['date']}\n"
            )

if __name__ == "__main__":
    
    TestSocialNetwork = SocialNetwork()
    TestSocialNetwork.register_user("Rigo", 1)
    TestSocialNetwork.register_user("Mary", 2)
    TestSocialNetwork.register_user("John", 3)

    TestSocialNetwork.follow_user(1, 2)
    TestSocialNetwork.follow_user(1, 3)
    TestSocialNetwork.follow_user(2, 1)

    TestSocialNetwork.follow_user(3, 1)
    TestSocialNetwork.follow_user(3, 2)
    TestSocialNetwork.follow_user(2, 3)
    TestSocialNetwork.unfollow_user(3, 2)

    TestSocialNetwork.create_post(1, "Hello World")

    TestSocialNetwork.create_post(2, "Hola a todos bienvenidos")
    TestSocialNetwork.create_post(2, "Hola a todos bienvenidos")
    TestSocialNetwork.create_post(3, "Hola a todos bienvenidos")
    TestSocialNetwork.delete_post(1)
    TestSocialNetwork.create_post(1, "Nuevo post")
    TestSocialNetwork.like_post(1, 4)
    TestSocialNetwork.like_post(2, 4)
    
    print("\n----------------------")
    print("Testing Social Network")
    print("----------------------\n")
    print(TestSocialNetwork)
    print("\nUser feed")
    TestSocialNetwork.visualization_feed_user(1)
    print("\nUser Following feed")
    TestSocialNetwork.visualization_feed_follow(1)