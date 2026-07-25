import requests # pip install requests

YT_URL = "https://www.youtube.com"

try:
    response = requests.get(YT_URL)
    if response.status_code == 200: # 200 -> OK
        print("Petición exitosa!")
        print(response.text[:128]) # Imprimir los primeros 128 caracteres de la pagina

except requests.exceptions.RequestException as e:
    print(e)
print("\n")

# ---- DIFICULTAD EXTRA ----

pokeAPI = "https://pokeapi.co/api/v2/pokemon/"

busqueda = input("Ingrese el nombre o id de un pokemon => ")

try:
    response = requests.get(pokeAPI + busqueda)
    response.raise_for_status()
    data = response.json()

except Exception as e:
    print(e)

else:
    print("Nombre: " + data["name"])
    print("ID: " + str(data["id"]))
    print("Peso: " + str(data["weight"]))
    print("Altura: " + str(data["height"]))
    print("Tipos: " + ", ".join([tipo["type"]["name"] for tipo in data["types"]]))

    print("\n")

    especies_data = requests.get(data["species"]["url"]).json()
    cadena_evolucion_data = requests.get(especies_data["evolution_chain"]["url"]).json()
    
    evoluciones = [cadena_evolucion_data["chain"]["species"]["name"]]
    ev = cadena_evolucion_data["chain"]["evolves_to"]
    is_evolve = ev != []

    while is_evolve:
        evoluciones.append(ev[0]["species"]["name"])
        ev = ev[0]["evolves_to"]
        is_evolve = ev != []
    
    print("Cadena de evolución: " + " -> ".join(evoluciones))
    print("Aparicion en juegos: " + ", ".join([i["version"]["name"] for i in data["game_indices"]]))