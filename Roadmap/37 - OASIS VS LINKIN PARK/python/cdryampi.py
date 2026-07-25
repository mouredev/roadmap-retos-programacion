# /*
#  * EJERCICIO:
#  * ¡Dos de las bandas más grandes de la historia están de vuelta!
#  * Oasis y Linkin Park han anunciado nueva gira, pero, ¿quién es más popular?
#  * Desarrolla un programa que se conecte al API de Spotify y los compare.
#  * Requisitos:
#  * 1. Crea una cuenta de desarrollo en https://developer.spotify.com.
#  * 2. Conéctate al API utilizando tu lenguaje de programación.
#  * 3. Recupera datos de los endpoint que tú quieras.
#  * Acciones:
#  * 1. Accede a las estadísticas de las dos bandas.
#  *    Por ejemplo: número total de seguidores, escuchas mensuales,
#  *    canción con más reproducciones...
#  * 2. Compara los resultados de, por lo menos, 3 endpoint.
#  * 3. Muestra todos los resultados por consola para notificar al usuario.
#  * 4. Desarrolla un criterio para seleccionar qué banda es más popular.
#  */


import base64
import urllib.parse
import aiohttp
import asyncio

class ConnSpotify():

    __CLIENT_ID = ":)"
    __CLIENT_SECRET = ":("
    
    __ACCESS_TOKEN = None
    __HEADERS = None
    __URL_CONN_API = "https://api.spotify.com"
    __URL_CONN_TOKEN = "https://accounts.spotify.com/api/token"

    __ENDPOINTS = {
        "artist": "/v1/artists/",
        "top_tracks": "/v1/artists/{id}/top-tracks",
        "albums": "/v1/artists/{id}/albums"
    }

    __ARTIST = {
        "linkinpark": "6XyY86QOPPrYVGvF9ch6wz",
        "oasis": "2DaxqgrOhkeH0fpeiQq2f4"
    }

    async def __get_access_token(self, session):
        credentials = f"{self.__CLIENT_ID}:{self.__CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

        headers = {
            'Authorization': f'Basic {encoded_credentials}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = urllib.parse.urlencode({
            'grant_type': 'client_credentials'
        })

        async with session.post(self.__URL_CONN_TOKEN, data=body, headers=headers) as response:
            if response.status == 200:
                token_info = await response.json()
                self.__ACCESS_TOKEN = token_info["access_token"]
                self.__HEADERS = {
                    'Authorization': f'Bearer {self.__ACCESS_TOKEN}',
                    'Content-Type': 'application/json'
                }
            else:
                print(f'Error: {response.status}')

    async def get_headers(self, session):
        if self.__HEADERS is None:
            await self.__get_access_token(session)
        return self.__HEADERS

    async def api_call(self, session):
        raw_data = []
        headers = await self.get_headers(session)
        
        for artist_name, artist_id in self.__ARTIST.items():
            url = f"{self.__URL_CONN_API}{self.__ENDPOINTS['artist']}{artist_id}"
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    raw_data.append(data)
                else:
                    print(f'Error fetching {artist_name}: {response.status}')
        return raw_data
    
    async def get_top_track(self, session, artist_id):
        url = self.__URL_CONN_API+f"{self.__ENDPOINTS['top_tracks']}".format(id = artist_id)+"?market=US"
        headers = await self.get_headers(session)
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Ha habido un problema a la hora de recuperar los datos... {response.status}")
                return None
            
    async def get_albums(self, session, artist_id):
        url = self.__URL_CONN_API+f"{self.__ENDPOINTS['albums']}".format(id = artist_id)+"?market=US"
        headers = await self.get_headers(session)
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Ha habido un problema a la hora de recuperar los datos... {response.status}")
                return None

    async def comparar_bandas(self, session):
        bandas = await self.api_call(session)

        banda_1, banda_2 = bandas[:2]
        banda_1_point, banda_2_point = 0,0
        band_data = {
            "top_tracks": [],
            "albums": []
        }
        for banda in bandas:
            uri =  banda['uri'].split(":")[-1]

            band_data["top_tracks"].append(
                await self.get_top_track(session=session, artist_id= uri)
            )
            band_data["albums"].append(
                await self.get_top_track(session=session, artist_id= uri)
            )

        if "tracks" in band_data['top_tracks'][0] and "tracks" in band_data['top_tracks'][1]:
            banda_1_point += len(band_data['top_tracks'][0]["tracks"]) > len(band_data['top_tracks'][1]["tracks"])
            banda_2_point += len(band_data['top_tracks'][0]["tracks"]) < len(band_data['top_tracks'][1]["tracks"])

        
        pop_albums_1 = sum([album['popularity'] for album in band_data['albums'][0]["tracks"]])/ len(band_data['albums'][0]["tracks"])

        pop_albums_2 = sum([album['popularity'] for album in band_data['albums'][1]["tracks"]])/ len(band_data['albums'][1]["tracks"])

        if pop_albums_1 != pop_albums_2:

            banda_1_point += pop_albums_1 > pop_albums_2
            banda_2_point += pop_albums_1 < pop_albums_2
        
            

        banda_1_point += banda_1['popularity'] > banda_2['popularity']
        banda_2_point += banda_1['popularity'] < banda_2['popularity']


        banda_1_point += banda_1['followers']['total'] > banda_2['followers']['total']
        banda_2_point += banda_1['followers']['total'] < banda_2['followers']['total']
        
        if len(banda_1['genres']) != len(banda_2['genres']):
            banda_1_point += len(banda_1['genres']) > len(banda_2['genres'])
            banda_2_point += len(banda_1['genres']) < len(banda_2['genres'])

        if banda_1_point != banda_2_point:
            ganador = banda_1 if banda_1_point > banda_2_point else banda_2
            print(f"El ganador es: {ganador['name']}")
        else:
            print("Ha habido un empate técnico.")

async def main():
    api = ConnSpotify()

    async with aiohttp.ClientSession() as session:
        await api.comparar_bandas(session)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
