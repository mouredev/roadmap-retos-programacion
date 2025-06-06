# /*
#  * EJERCICIO:
#  * La alternativa descentralizada a X, Bluesky, comienza a atraer
#  * a nuevos usuarios. ¿Cómo funciona una red de este estilo?
#  * 
#  * Implementa un sistema que simule el comportamiento de estas
#  * redes sociales.
#  * 
#  * Debes crear las siguientes operaciones:
#  * - Registrar un usuario por nombre e identificador único.
#  * - Un usuario puede seguir/dejar de seguir a otro.
#  * - Creación de post asociado a un usuario. Debe poseer
#  *   texto (200 caracteres máximo), fecha de creación 
#  *   e identificador único.   
#  * - Eliminación de un post.
#  * - Posibilidad de hacer like (y eliminarlo) en un post.
#  * - Visualización del feed de un usuario con sus 10 publicaciones
#  *   más actuales ordenadas desde la más reciente.
#  * - Visualización del feed de un usuario con las 10 publicaciones
#  *   más actuales de los usuarios que sigue ordenadas 
#  *   desde la más reciente.
#  *   
#  * Cuando se visualiza un post, debe mostrarse:
#  * ID de usuario, nombre de usuario, texto del post, 
#  * fecha de creación y número total de likes.
#  * 
#  * Controla errores en duplicados o acciones no permitidas.
#  */
import uuid
from datetime import datetime
import os

class User():

    def __init__(self, name: str) ->None:
        self.id = uuid.uuid4()
        self.name = name
        self.tweets = []
        self.followers = []
        self.likes = []
        self.dislikes = []
        self.following = []

    def follow_unfollow(self, user) -> None:
        """Función para seguir o dejar de seguir a un usuario."""
        if user.id == self.id:
            raise ValueError("No podemos seguirnos a nosotros mismos.")
        
        if user not in self.following:
            self.following.append(user)
            user.followers.append(self)
            print(f"Acabas de seguir al usuario '{user.name}'.")
        else:
            self.following.remove(user)
            user.followers.remove(self)
            print(f"Haz dejado de seguir al usuario '{user.name}'.")


    def add_tweet(self, tweet)-> None:

        local_tweet = next((t for t in self.tweets if t.id ==tweet.id), None)
        
        if local_tweet == None:
            self.tweets.append(tweet)
            print(f'Tweet anañadido por el usuario {self}')
        else:
            print(f'Ya has publicado el tweet {tweet.id}')

    def delete_tweet(self, tweet)-> None:

       local_tweet = next((u for u in self.tweets if u.id ==tweet.id), None)
       if local_tweet:
           self.tweets.remove(tweet)

    def like_dislike(self, tweet)-> None:
        if tweet not in self.likes:
            if tweet in self.dislikes:
                self.dislikes.remove(tweet)
            self.likes.append(tweet)
            print(f'Le acabas de dar like a {tweet.id}')
        else:
            if tweet in self.likes:
                if tweet in self.dislikes:
                    self.dislikes.append(tweet)
                self.likes.remove(tweet)
                print(f'Le acabas de dar dislike a {tweet.id}')
    

    def print_feed(self)->None:
        for tweet in self.ordered_tweets_list():
            print(tweet)
    
    def ordered_tweets_list(self)->list:
        return sorted(self.tweets, key=lambda d: d.data)

    def get_following(self)->list:
        return [f'{user.name}' for user in self.following]
    
    def user_feed(self)-> None:

        print(f"{self}:\n")
        print(f"Número de seguidores: {len(self.followers)}")
        print(f"Número de seguidos: {len(self.following)}")

        if len(self.tweets) > 0:
            print(f"Últimos post:")
            for tweet in self.ordered_tweets_list()[:10]:
                print()
                print(tweet)
                print()

        print(f"likes: {len(self.likes)}")
        print(f"Dislikes: {len(self.dislikes)}")


    def __str__(self)-> str:
        return f'{self.name}@{self.id}'
    
class Tweet():

    def __init__(self, user:User, msg:str, hora=datetime.now())-> None:
        self.id = uuid.uuid4()
        self.user= user
        if len(msg) >=200:
            raise("No puedes tener un Tweet tan largo")
        self.msg = msg
        self.data = hora

    def __str__(self):
        return f'{self.user}:\n{self.msg}\n{self.data.strftime("%d/%m/%Y %H:%M:%S")}'

class Twitter():
    def __init__(self):
        self.users = []
    
    def order_tweets(self)-> list:
        local_tweets= []
        if len(self.users) > 0:
            for user in self.users:
                list_tweets = user.ordered_tweets_list()
                if list_tweets:
                    local_tweets.extend(list_tweets)

        return sorted(local_tweets, key=lambda d: d.data, reverse=True)

    def add_user(self, user:User)-> None:
        local_user = next((u for u in self.users if u.id == user.id), None)
        if local_user == None:
            self.users.append(user)
        print(f'Usuario {user} Añadido a Twitter')

    def add_tweet(self, user:User, msg:Tweet)-> None:
        local_user = next((u for u in self.users if u.id == user.id),None)
        if local_user == None:
            self.add_user(user)
            local_user = next((u for u in self.users if u.id == user.id),None)
        local_user.add_tweet(msg)

    def user_exist(self, user_name:str)-> bool:
        local_user = next((u for u in self.users if u.name == user_name), None)
        return True if local_user is not None else False

    def print_last_tweets(self)->None:
        tweets = self.order_tweets()[:10]

        for tweet in tweets:
            print(tweet)

    def get_users(self)->list:
        return self.users

    def print_user_info(self, user_name:str)-> None:
        local_user = next((u for u in self.users if u.name == user_name), None)
        if local_user:
            local_user.user_feed()
        else:
            print(f"El usuario '{user_name}' no existe")

    def safe_execute_clear_from_cmd(self) -> None:
        """Limpia la consola dependiendo del sistema operativo"""
        try:
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        except Exception as e:
            print(f"Error al limpiar la consola: {e}")

def main():
    twitter = Twitter()

    for user in [User(f"User{i}") for i in range(10)]:
        twitter.add_user(user)

    for user in twitter.get_users():

        for i in range(10):
            tweet_date = datetime(2024, 11, 20, 21, (50 + i) % 24, (30 + i * 3) % 60)
            tweet = Tweet(user, f"Tweet {i + 1} from {user.name}", tweet_date)
            twitter.add_tweet(user, tweet)

    for i, user in enumerate(twitter.get_users()):
        if i + 1 < len(twitter.get_users()):
            user.follow_unfollow(twitter.get_users()[i + 1])

    for i, user in enumerate(twitter.users):
        if i + 1 < len(twitter.get_users()):
            next_user = twitter.get_users()[i + 1]
            if twitter.user_exist(next_user.name):
                for tweet in next_user.tweets[:5]:
                    user.like_dislike(tweet)

    twitter.safe_execute_clear_from_cmd()

    while True:
            print("\n--- Twitter Management ---")
            print("1. Crear usuario")
            print("2. Publicar un tweet")
            print("3. Seguir o dejar de seguir a un usuario")
            print("4. Dar like a un tweet o dislike")
            print("5. Mostrar últimos tweets")
            print("6. Mostrar todo el feed de un usuario")
            print("7. Mostrar nombres de los usuarios")
            print("8. Salir")
            choice = input("Elige una opción: ")
            match choice:
                case "1":
                    # Crear usuario
                    name = input("Introduce el nombre del usuario: ")
                    if twitter.user_exist(name):
                        print(f"El usuario {name} ya existe en Twitter")
                    else:
                        user = User(name)
                        twitter.add_user(user)

                case "2":
                    # Publicar un tweet
                    if not twitter.get_users():
                        print("Primero debes crear usuarios.")
                        continue
                    user_name = input("¿Quién publicará el tweet? Ingresa el nombre: ")
                    user = next((u for u in twitter.get_users() if u.name == user_name), None)
                    if user:
                        msg = input("Escribe tu tweet (máx 200 caracteres): ")
                        tweet = Tweet(user, msg)
                        twitter.add_tweet(user, tweet)
                    else:
                        print("Usuario no encontrado.")

                case "3":
                    # Seguir a un usuario
                    if len(twitter.get_users()) < 2:
                        print("Debes tener al menos dos usuarios para seguirse entre sí.")
                        continue
                    follower_name = input("¿Quién seguirá a otro usuario? Ingresa el nombre: ")
                    followee_name = input("¿A quién quieres seguir? Ingresa el nombre: ")
                    follower = next((u for u in twitter.get_users() if u.name == follower_name), None)
                    followee = next((u for u in twitter.get_users() if u.name == followee_name), None)
                    if follower and followee:
                        try:
                            follower.follow_unfollow(followee)
                        except ValueError as e:
                            print(e)
                    else:
                        print("Uno o ambos usuarios no existen.")

                case "4":
                    # Dar like a un tweet
                    if not twitter.get_users():
                        print("Primero debes crear usuarios.")
                        continue
                    liker_name = input("¿Quién dará like? Ingresa el nombre: ")
                    user = next((u for u in twitter.get_users() if u.name == liker_name), None)
                    if user:
                        tweet_owner_name = input("¿De quién es el tweet? Ingresa el nombre: ")
                        tweet_owner = next((u for u in twitter.get_users() if u.name == tweet_owner_name), None)
                        if tweet_owner and tweet_owner.tweets:
                            print("Tweets disponibles:")
                            for i, tweet in enumerate(tweet_owner.tweets, 1):
                                print(f"{i}. {tweet.msg}")
                            tweet_index = int(input("Selecciona el número del tweet: ")) - 1
                            if 0 <= tweet_index < len(tweet_owner.tweets):
                                tweet = tweet_owner.tweets[tweet_index]
                                user.like_dislike(tweet)
                            else:
                                print("Número de tweet inválido.")
                        else:
                            print("Usuario no encontrado o no tiene tweets.")
                    else:
                        print("Usuario no encontrado.")

                case "5":
                    # Mostrar últimos tweets
                    print("\nÚltimos tweets publicados:")
                    twitter.print_last_tweets()

                case "6":
                    # Mostrar feed
                    name = input("Introduce el nombre del usuario: ")
                    if twitter.user_exist(name):
                        twitter.print_user_info(name)
                    else:
                        print(f"El usuario {name} no existe.")

                case "7":
                    # Mostrar nombres de los usuarios
                    for user in twitter.get_users():
                        print(user.name)
                case "8":
                    # Salir
                    print("Saliendo del programa. ¡Hasta luego!")
                    break
                case _:
                    print("Opción no válida, por favor elige una opción del menú.")


if __name__ == '__main__':
    main()