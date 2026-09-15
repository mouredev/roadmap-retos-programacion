#  EJERCICIO:
#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.
import requests
get_response  = requests.get("https://httpbin.org/get")

print("Código de estado HTTP:", get_response.status_code)
get_info = get_response.json()
print(get_info)




# DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores
while True:
    code = input("Ingresa el nombre o id del pokemon (s para salir): ").lower()
    url =  "https://pokeapi.co/api/v2/pokemon/"
    if code == "s":
        print("Has salido de la pokedex")
        break
    else: 
        try:
            response = requests.get(
                f"{url}{code}"
            )

            response.raise_for_status()
            datos = response.json()
            print("Conexion correcta a la pokedex")
            print("\nDatos Principales de tu pokemon: ")
            print(f"Nombre: {datos['name']}")
            print(f"Id: {datos['id']}")
            print(f"Altura: {datos['height']/10} m")
            print(f"Peso: {datos['weight']/10} kg")
            print("\nTipo de pokemon: ")

            for tipo in datos["types"]:
                print(f"Tipo/s: {tipo['type']['name']}")
            print("\nJuegos en lo que ha aparecido: ")
            for games in datos["game_indices"]:
                print(f"Juegos: {games['version']['name']}")

            resp_especies = requests.get(datos["species"]["url"])
            datos_especies = resp_especies.json()
            url_evolucion = datos_especies["evolution_chain"]["url"]
            res_evo = requests.get(url_evolucion)
            datos_evo = res_evo.json()
            print("\nEvoluciones: ")

            print(f" {datos_evo['chain']['species']['name']}")
            for evo in datos_evo['chain']['evolves_to']:
                print(f"  {evo['species']['name']}")
                for evo2 in evo['evolves_to']:
                    print(f"   {evo2['species']['name']}")
            
        except requests.exceptions.HTTPError as httperr:
            print(f"Ocurrio un problema: error {httperr}")
        except requests.exceptions.ConnectionError as connerr:
            print(f"Ocurrio algo con la conexion: error {connerr}")
        except Exception as err:
            print(f"Ha ocurrido otro error desconicodo: error{err}")