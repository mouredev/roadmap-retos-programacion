import requests

# Ejercicio

req = requests.get("https://mouredev.com/brais-moure/")
print(req.status_code)
if req.status_code == 200:
    print(req.text)
else:
    print(f'Error: {req.status_code}')


# Dificultad Extra

def info_pokemon(id=None, name=None):
    if id is not None:
        url = f'https://pokeapi.co/api/v2/pokemon/{id}'
    elif name is not None:
        url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    else:
        print("Debes proporcionar un ID o un nombre.")
        return

    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        print(f"Nombre: {pokemon['name']}")
        print(f"ID: {pokemon['id']}")
        print(f"Peso: {pokemon['weight']} hectogramos")
        print(f"Altura: {pokemon['height']} decímetros")
        print("Tipos:")
        for tipo in pokemon['types']:
            print(f"  - {tipo['type']['name']}")

        especies_url = pokemon['species']['url']
        especies_response = requests.get(especies_url)

        if especies_response.status_code == 200:
            especies = especies_response.json()
            evolucion_url = especies['evolution_chain']['url']
            evolucion_response = requests.get(evolucion_url)

            if evolucion_response.status_code == 200:
                evolucion = evolucion_response.json()
                cadena = evolucion['chain']
                print("Cadena de evolución:")
                while cadena:
                    print(f"  - {cadena['species']['name']}")
                    if cadena['evolves_to']:
                        cadena = cadena['evolves_to'][0]
                    else:
                        break
            else:
                print(f'Error al obtener la cadena de evolución: {
                      evolucion_response.status_code}')
        else:
            print(f'Error al obtener la especie del Pokémon: {
                  especies_response.status_code}')

        print("Aparece en los siguientes juegos:")
        for juego in pokemon['game_indices']:
            print(f"  - {juego['version']['name']}")
    else:
        print(f'Error: {response.status_code}')


# Ejemplo de uso
info_pokemon('muk')
