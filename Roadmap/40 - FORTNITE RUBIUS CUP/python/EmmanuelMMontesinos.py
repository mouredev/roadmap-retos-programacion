"""
/*
 * EJERCICIO:
 * ¡Rubius tiene su propia skin en Fortnite!
 * Y va a organizar una competición para celebrarlo.
 * Esta es la lista de participantes:
 * https://x.com/Rubiu5/status/1840161450154692876
 *
 * Desarrolla un programa que obtenga el número de seguidores en
 * Twitch de cada participante, la fecha de creación de la cuenta 
 * y ordene los resultados en dos listados.
 * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
 *   (NO subas las credenciales de autenticación)
 * - Crea un ranking por número de seguidores y por antigüedad.
 * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
 */
"""
import requests
import datetime
import os

# NO subas las credenciales de autenticación
os.environ["TWITCH_CLIENT_ID"] = "tu-id-de-twitch"
os.environ["TWITCH_CLIENT_SECRET"] = "tu-key-secret-de-twitch"


id = os.environ.get("TWITCH_CLIENT_ID")
secret = os.environ.get("TWITCH_CLIENT_SECRET")

# Clase para el token de acceso
class Token:
    def __init__(self,id,secret) -> None:
        self.id = id
        self.secret = secret
        self.token = self.generate_token()
    def generate_token(self):
        url = "https://id.twitch.tv/oauth2/token"
        params = {
            "client_id": self.id,
            "client_secret": self.secret,
            "grant_type": "client_credentials"
        }

        response = requests.post(url,params=params)

        if response.status_code == 200:
            return response.json()["access_token"]
        
        else:
            response = response.json()
            print(f"Error: {response['status']}\n{response['message']}")
            return None


class Participante:
    lista_participantes = []
    mas_antiguo = []
    mas_seguido = []
    token = Token(id,secret)
    def __init__(self,nombre) -> None:
        self.nombre = nombre
        self.fecha_registro = None
        self.seguidores = 0
        self.tiempo_total = 0
        self.id = None

        Participante.lista_participantes.append(self)

    # Ordene los resultados en dos listados
    def ordenar_mas_antiguo(self):
        Participante.mas_antiguo = sorted(Participante.lista_participantes, key=lambda p: p.tiempo_total, reverse=True)

    def ordenar_mas_seguido(self):
        Participante.mas_seguido = sorted(Participante.lista_participantes, key=lambda p: p.seguidores, reverse=True)


    # Crea un ranking por número de seguidores y por antigüedad
    def mostrar_tabla_mas_antiguo(self):
        print("RANKING DE MAS ANTIGUOS")
        print("-"*50)
        for position, participante in enumerate(Participante.mas_antiguo):
            if participante.fecha_registro is None:
                print(f"{position+1}. {participante.nombre.upper()} no tiene cuenta de Twitch")
            else:
                print(f"{position+1}. {participante.nombre.upper()} creado el {participante.fecha_registro}")
            print("-"*30)
            print()
        print()
    def mostrar_tabla_mas_seguido(self):
        print("RANKING DE MAS SEGUIDOS")
        print("-"*50)
        for position, participante in enumerate(Participante.mas_seguido):
            if participante.seguidores == 0:
                print(f"{position+1}. {participante.nombre.upper()} no tiene seguidores o cuenta de Twitch")
            else:
                print(f"{position+1}. {participante.nombre.upper()} con {participante.seguidores} seguidores")
            print("-"*30)
            print()
        print()

    # Desarrolla un programa que obtenga el número de seguidores en
    # Twitch de cada participante, la fecha de creación de la cuenta
    def obtener_datos(self):
            # Usa el API de Twitch

            url = f"https://api.twitch.tv/helix/users?login={self.nombre}"
            headers = {
                'Client-ID': Participante.token.id,
                'Authorization': f'Bearer {Participante.token.token}',
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200 and len(response.json()["data"]) > 0:
                datos = response.json()
                self.id = datos["data"][0]["id"]
                # Obtenga la fecha de creación de la cuenta
                fecha_regisro = datos["data"][0]["created_at"][0:10]
                self.fecha_registro = datetime.datetime.strptime(fecha_regisro, "%Y-%m-%d").strftime("%d/%m/%Y")
                self.tiempo_total = datetime.datetime.now() - datetime.datetime.strptime(self.fecha_registro, "%d/%m/%Y")
                self.tiempo_total = self.tiempo_total.days

                print(f"Usuario {self.nombre.upper()} registrado")
            else:
                # Si algún participante no tiene usuario en Twitch, debe reflejarlo
                print(f"No se encontro el usuario {self.nombre.upper()}")
                self.tiempo_total = 0


    # Obtenga el número de seguidores
    def obtener_seguidores(self):
        if self.id is None:
            self.seguidores = 0
        else:
            url = f"https://api.twitch.tv/helix/channels/followers"
            
            params = {
                "broadcaster_id": self.id
                }
            headers = {
                'Client-ID': Participante.token.id,
                'Authorization': f'Bearer {Participante.token.token}',
            }

            response = requests.get(url, headers=headers,params=params)

            if response.status_code == 200:
                response = response.json()
                self.seguidores = response['total']

            else:
                print(f"Error: {response.status_code}\n{response.json()['message']}")
                self.seguidores = 0


    


# Pruebas

lista = [
    "littleragergirl","ache","AdriContreras4","agustin51","alexby11","ampeterby7",
    "tvandeR","arigameplays","arigeli_","auronplay","axozer","beniju03","bycalitos",
    "byviruzz","carreraaa","celopan","srcheeto","crystalmolly","darioemehache",
    "dheylo","djmariio","doble","elvisayomastercard","elyas360","folagorlives",
    "thegrefg","guanyar","hika","hiperop","ibai","ibelky_","illojuan","imantado",
    "irinaisasia","jesskiu","jopa","jordiwild","kenaisouza","keroro","kiddkeo",
    "kikorivera","knekro","kokorok","kronnozomber","leviathan","lolkilla","lola_lolita",
    "lolito","luzu","mangel","mayichi","meelo","missasofia","mixwell","mrjagger",
    "nategentile","nexxuz","nissaxter","ollie","orslok","outconsumer","papigavi",
    "paracetamor","patica","paulagonu","pausenpaii","perxita","plex","polispol",
    "quackity","recuerdop","reven","rivers","robertpg","roier","rojuu","rubius",
    "shadoune","silithur","spreen","spursito","staxx","suzyrox","vicens","vituber",
    "werlyb","xavi","xcrystal","xokas","zarcort","zeling","zorman"
]

for i in lista:
    p = Participante(i)
    p.obtener_datos()
    p.obtener_seguidores()

Participante.ordenar_mas_antiguo(Participante)
Participante.ordenar_mas_seguido(Participante)

Participante.mostrar_tabla_mas_seguido(Participante)
Participante.mostrar_tabla_mas_antiguo(Participante)
