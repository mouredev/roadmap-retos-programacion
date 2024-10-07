# 40 FORTNITE RUBIUS CUP

import requests
import base64
from datetime import datetime
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env para obtener CLIENT_ID y CLIENT_SECRET
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Funciones


def obtener_token() -> str:
    url = "https://id.twitch.tv/oauth2/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception(f"Error obteniendo el token de Twitch: {
                        response.json()}.")

    return response.json()["access_token"]


def buscar_participante(token: str, login: str):
    url = f"https://api.twitch.tv/helix/users?login={login}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": CLIENT_ID
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {
            "login": login,
            "estado del usuario de twitch": "Inactivo"
        }
    resultados = response.json().get("data", [])
    if resultados:
        return {
            "id": resultados[0]["id"],
            "login": resultados[0]["login"],
            "usuario twitch": resultados[0]["display_name"],
            "creación de cuenta": (datetime.strptime(resultados[0]["created_at"], "%Y-%m-%dT%H:%M:%SZ")),
            "descripción": resultados[0]["description"],
            "estado del usuario de twitch": "activo"
        }
    return {}


def buscar_seguidores_participante(token: str, id: str):
    url = f"https://api.twitch.tv/helix/channels/followers?broadcaster_id={id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": CLIENT_ID
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {
            "total de seguidores": 0,
            "estado del usuario de twitch": "Inactivo",
            "seguido desde": "Sin informacion disponible"
        }

    resultados = response.json()
    total_seguidores = resultados.get("total", 0)

    if resultados.get("data"):
        resultados_canal = resultados["data"][0]
        return {
            "total de seguidores": total_seguidores,
            "broadcaster id": resultados_canal['user_id'],
            "login del usuario": resultados_canal['user_login'],
            "seguido desde": resultados_canal['followed_at']
        }
    return {
        "total de seguidores": total_seguidores,
        "estado del usuario de twitch": "Activo",
        "seguido desde": "Sin informacion disponible"
    }


def buscar_info_canal(token: str, broadcaster_id: str):
    url = f"https://api.twitch.tv/helix/channels?broadcaster_id={
        broadcaster_id}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Client-Id": CLIENT_ID
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {
            "juegos": "sin información",
            "tópicos del canal": "sin información",
        }
    resultados_canal = response.json().get("data", [])
    if resultados_canal:
        return {
            "juegos": resultados_canal[0]['game_name'],
            "tópicos del canal": resultados_canal[0]['content_classification_labels']
        }
    return {
        "juegos": "sin información",
        "tópicos del canal": "sin información",
    }

# Uso de codigo


token = obtener_token()

participantes_lista = [
    'littleragergirl', 'DJMARIIO', 'KikoRivera', 'NISSAXTER',
    'SHADOUNE666', 'ACHE', 'DOBLE', 'KNEKRO',
    'OllieGamerz', 'SILITHUR', 'AdriContreras4', 'ElvisaYomastercard',
    'KOKO', 'ORSLOK', 'spok_sponha', 'agustin51',
    'elyas360', 'KronnoZomberOficial', 'Outconsumer', 'SPREEN',
    'ElSpreen', 'FolagorLives', 'Leviathan', 'PapiGaviTV',
    'Spursito', 'Ampeterby7', 'TheGrefg', 'LITkillah',
    'paracetamor', 'bysTaXx', 'tvandeR', 'GUANYAR',
    'LOLALOLITA', 'patica1999', 'SUZYROXX', 'ARIGAMEPLAYS',
    'HIKA', 'LOLITOFDEZ', 'PAULAGONU', 'VICENS',
    'ARIGELI_', 'Hiperop', 'LUH', 'PAUSENPAII',
    'VITU', 'AURONPLAY', 'IBAI', 'LUZU',
    'PERXITAA', 'WERLYB', 'AXOZER', 'IBELKY_',
    'MANGEL', 'NoSoyPlex', 'XAVI', 'BENIJU03',
    'ILLOJUAN', 'MAYICHI', 'POLISPOL1', 'XCRY',
    'BYCALITOS', 'IMANTADO', 'MELO', 'QUACKITY',
    'elxokas', 'BYVIRUZZ', 'IRINA ISASIA', 'MISSASINFONIA',
    'Recuerd0p', 'THEZARCORT', 'CARRERAAA', 'JESSKIU',
    'MIXWELL', 'REVENXZ', 'ZELING', 'CELOPAN',
    'JOPA', 'JaggerPrincesa', 'rivers_gg', 'ZormanWorld',
    'srcheeto', 'JORDIWILD', 'NATEGENTILE7', 'ROBERTPG',
    'CRYSTALMOLLY', 'kenaivsouza', 'NEXXUZ', 'ROIER',
    'DARIOEMEHACHE', 'MrKeroro10', 'LakshartNia', 'ROJUU',
    'DHEYLO', 'TheKiddKeo95', 'nilojeda', 'RUBIUS'
]


informacion_participantes_seguidores = []
informacion_participantes_antiguedad = []


for nombre in participantes_lista:
    try:
        participante = buscar_participante(token, nombre)
        info = {"usuario twitch": nombre}

        if "id" in participante:
            info["id"] = participante["id"]
            info["estado del usuario de twitch"] = participante.get(
                "estado del usuario de twitch", "Inactivo")
            seguidores = buscar_seguidores_participante(
                token, participante["id"])
            info["total seguidores"] = int(
                seguidores.get("total de seguidores", 0))

            if "broadcaster id" in seguidores:
                canal = buscar_info_canal(token, seguidores["broadcaster id"])
                info["juegos"] = canal.get(
                    "juegos", "Informacion no disponible")
                info["tópicos del canal"] = canal.get()
        else:
            info["estado del usuario de twitch"] = "No tiene cuenta de twitch"
            info["total seguidores"] = 0

        informacion_participantes_seguidores.append(info)

    except Exception as e:
        print(f"Error al procesar {nombre}: {e}")

for nombre in participantes_lista:
    try:
        participante = buscar_participante(token, nombre)
        cuenta = {"usuario twitch": nombre}
        if "id" in participante:
            cuenta["id"] = participante["id"]
            cuenta["estado del usuario de twitch"] = participante.get(
                "estado del usuario de twitch", "Inactivo")
            cuenta["creación de cuenta"] = participante.get(
                "creación de cuenta", None)
            creacion = buscar_seguidores_participante(
                token, participante["id"])
            creacion["seguido desde"] = creacion. get("seguido desde", None)
        else:
            cuenta["estado del usuario de twitch"] = "No tiene cuenta de twitch"
            cuenta["creación de cuenta"] = None

        informacion_participantes_antiguedad.append(cuenta)

    except Exception as e:
        print(f"Error al procesar {nombre}: {e}")


informacion_participantes_seguidores = sorted(
    informacion_participantes_seguidores,
    key=lambda x: x.get("total seguidores", 0),
    reverse=True
)


informacion_participantes_antiguedad = sorted(
    informacion_participantes_antiguedad,
    key=lambda x: x.get("creación de cuenta") if x.get(
        "creación de cuenta") is not None else datetime.min,
    reverse=True
)
# Participantes del evento Rubius Cup
print("\nLista de los seguidores de los participantes del evento Rubius Cup en Twitch\n")
for participante_evento_fortnite in informacion_participantes_seguidores:
    print(f"Participante: {participante_evento_fortnite['usuario twitch']}, Estado: {
          participante_evento_fortnite['estado del usuario de twitch']}, Seguidores: {participante_evento_fortnite['total seguidores']}")

print("\nLista de antiguedad de las cuentas de los participantes del evento Rubius Cup en Twitch\n")

# Participantes del evento Rubius Cup
for participante_evento_fortnite in informacion_participantes_antiguedad:
    fecha_creacion = participante_evento_fortnite.get("creación de cuenta")

    if isinstance(fecha_creacion, datetime):
        fecha = fecha_creacion.strftime("%d-%m-%Y %H:%M:%S")
    elif isinstance(fecha_creacion, str):
        fecha = fecha_creacion
    else:
        fecha = "Información no disponible"

    print(f"Participante: {participante_evento_fortnite['usuario twitch']}, Estado: {
          participante_evento_fortnite['estado del usuario de twitch']}, Creación de cuenta: {fecha}")
