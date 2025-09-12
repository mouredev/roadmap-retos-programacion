# /*
#  * EJERCICIO:
#  * ¡Rubius tiene su propia skin en Fortnite!
#  * Y va a organizar una competición para celebrarlo.
#  * Esta es la lista de participantes:
#  * https://x.com/Rubiu5/status/1840161450154692876
#  *
#  * Desarrolla un programa que obtenga el número de seguidores en
#  * Twitch de cada participante, la fecha de creación de la cuenta 
#  * y ordene los resultados en dos listados.
#  * - Usa el API de Twitch: https://dev.twitch.tv/docs/api/reference
#  *   (NO subas las credenciales de autenticación)
#  * - Crea un ranking por número de seguidores y por antigüedad.
#  * - Si algún participante no tiene usuario en Twitch, debe reflejarlo.
#  */


import urllib.parse
import aiohttp
import asyncio
from datetime import datetime


class ApiTwitch():
    """"""
    __CLIENT_ID = ':('
    __CLIENT_SECRET = ':)'

    __ACCESS_TOKEN = None
    __HEADERS = None
    __URL_CONN_API = 'https://api.twitch.tv/'
    __URL_CONN_TOKEN = 'https://id.twitch.tv/oauth2/token'
    __ENDPOINTS = {
        "followers": "helix/channels/followers?broadcaster_id={streamer}",
        "channels": "helix/users?login={streamer}",
        "id": "helix/users?login={streamer}"
    }
    __STREAMERS = {
        'ABBY': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ACHE': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'adricontreras4': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'agustin51': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ALEXBY11': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ampeterby7': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ANDER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ARIGAMPLAYS': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ARIGELI': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'AURONPLAY': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'AXOZER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'BENIJU': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'BYCALITOS': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'BYVIRUZZ': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'CARRERA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'CELOPAN': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'CHEETO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'CRYSTALMOLLY': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'DARIOEMEHACHE': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'DHEYLO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'DJMARIO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'DOBLE': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ELVISA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ELYAS360': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'FOLAGOR': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'GREFG': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'GUNYAR': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'HIKA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'HIPER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'IBAI': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'IBELKY': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ILLOJUAN': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'IMANTADO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'IRINAISASIA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'JESSKIU': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'JOPA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'JORDIWILD': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KENAISOUZA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KERORO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KIDDKEO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KIKORIVERA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KNEKRO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KOKO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'KRONNZOMBER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'LEVIATHAN': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'LITKILLAH': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'LOLALOLITA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'LOLITO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'LUH': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'LUZO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'MANGEL': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'MAYICHI': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'MELO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'MISSASINFONIA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'MIXWELL': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'jaggerprincesa': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'NATEGENTILE': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'NEXXUZ': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'lakshartnia': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'NILOJEDA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'NISSAXTER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'OLLIE': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ORSLOK': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'OUTCONSUMER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'PAPIGAVI': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'PARACETAMOR': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'PATICA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'PAULAGONU': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'PERXITAA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'nosoyplex': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'polispol1': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'QUACKITY': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'RECUERDOP': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'REVEN': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'RIVERS': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ROBERTPG': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ROIER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ROJUU': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'RUBIUS': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'SHADOUNE': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'SLITHUR': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'SPOKSPONHA': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'SPREEN': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'SPURSITO': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'STAXX': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'SUZYROXX': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'VICENS': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'VITUBER': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'WERLYB': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'XAVI': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'XCRY': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'XOKAS': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ZARCORT': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ZELING': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        },
        'ZORMAN': {
            'id': '',
            'followers': 0,
            'antiguedad': ''
        }
    }



    async def __get_access_token(self, session):


        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        body = urllib.parse.urlencode({
            'grant_type': 'client_credentials',
            'client_id': self.__CLIENT_ID,
            'client_secret': self.__CLIENT_SECRET
        })

        async with session.post(self.__URL_CONN_TOKEN, data= body, headers= headers) as response:
            if response.status == 200:
                token_info = await response.json()
                self.__ACCESS_TOKEN = token_info["access_token"]
                self.__HEADERS = {
                    'Authorization': f'Bearer {self.__ACCESS_TOKEN}',
                    'Client-Id': self.__CLIENT_ID
                }
            else:
                print(f'Error {response}')

    async def get_headers(self, session):
        if self.__HEADERS is None:
            await self.__get_access_token(session)
        return self.__HEADERS
    
    async def get_channel_id_and_created_at(self, session):
        headers = await self.get_headers(session)

        tasks = []
        for streamer in list(self.__STREAMERS.items()):
            url = f'{self.__URL_CONN_API}{self.__ENDPOINTS["id"]}'.format(streamer=streamer[0].lower())
            tasks.append(self.fetch_channel_data(session, headers, streamer[0], url))
        
        await asyncio.gather(*tasks)
        await self.get_followers(session=session)

    async def fetch_channel_data(self, session, headers, streamer_name, url):
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                if data["data"]:
                    self.__STREAMERS[streamer_name]["id"] = data['data'][0]["id"]
                    self.__STREAMERS[streamer_name]["antiguedad"] = data['data'][0]["created_at"]
                else:
                    print(f"Usuario {streamer_name} no tiene canal por lo tanto sale del concurso.")
                    self.__STREAMERS.pop(streamer_name, None)
            else:
                print(f"Error al llamar a {streamer_name}: {response.status}")
                self.__STREAMERS.pop(streamer_name, None)

    async def get_followers(self, session):
            headers = await self.get_headers(session)
            
            tasks = []
            for streamer in list(self.__STREAMERS.items()):
                url = f'{self.__URL_CONN_API}{self.__ENDPOINTS["followers"]}'.format(streamer=streamer[1]["id"])
                tasks.append(self.fetch_follower_data(session, headers, streamer[0], url))
            
            await asyncio.gather(*tasks)

    async def fetch_follower_data(self, session, headers, streamer_name, url):
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                if data["total"]:
                    self.__STREAMERS[streamer_name]["followers"] = int(data["total"])
                    if self.__STREAMERS[streamer_name]["followers"] == 0:
                        print(f"Usuario {streamer_name} tiene 0 seguidores, lo sacamos del concurso.")
                        self.__STREAMERS.pop(streamer_name, None)
                else:
                    print(f"Usuario {streamer_name} tiene 0 seguidores, lo sacamos del concurso.")
                    self.__STREAMERS.pop(streamer_name, None)
            else:
                print(f"Error al obtener seguidores de {streamer_name}: {response.status}")

    def ranking_followers(self):

        sorted_by_followers = dict(sorted(self.__STREAMERS.items(), key= lambda streamer: streamer[1]["followers"], reverse=True))

        for ranking, streamer in enumerate(sorted_by_followers.items(), start=1):
            print(f'{ranking}. {streamer[0]} -> {streamer[1]["followers"]} followers.')

    def ranking_by_created_at(self):
        format_data = "%Y-%m-%dT%H:%M:%SZ"
        sorted_by_created_at = dict(
            sorted(
                self.__STREAMERS.items(),
                key= lambda streamer: datetime.strptime(
                    streamer[1]['antiguedad'],
                    format_data)
                    if streamer[1]['antiguedad'] else datetime.max
                )
        )

        for ranking, streamer in enumerate(sorted_by_created_at.items(), start=1):
            print(f'{ranking}. {streamer[0]} -> {datetime.strptime(streamer[1]["antiguedad"], format_data).date()}.')



async def main():
    api = ApiTwitch()

    async with aiohttp.ClientSession() as session:
        await api.get_channel_id_and_created_at(session)
        print("Ranking de participantes por seguidores en Twitch:")
        print("\n")
        api.ranking_followers()
        print("\n")
        print("\n")
        print("Ranking de participantes por seguidores en Twitch:")
        print("\n")
        api.ranking_by_created_at()
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())