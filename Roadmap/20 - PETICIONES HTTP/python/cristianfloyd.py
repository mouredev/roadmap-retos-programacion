# EJERCICIO:
# Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
# una petición a la web que tú quieras, verifica que dicha petición
# fue exitosa y muestra por consola el contenido de la web.

from typing import Any, Dict, Optional

import requests

def print_web_content(url: str) -> None:
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Error: {response.status_code}")


print_web_content("https://pokeapi.co/api/v2/pokemon/clefairy/")

#
# DIFICULTAD EXTRA (opcional):
# Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
# terminal al que le puedas solicitar información de un Pokémon concreto
# utilizando su nombre o número.
# - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
# - Muestra el nombre de su cadena de evoluciones
# - Muestra los juegos en los que aparece
# - Controla posibles errores


class PokemonInfo:
    BASE_URL = "https://pokeapi.co/api/v2/"

    def __init__(self, pokemon_id: str) -> None:
        self.pokemon_id = pokemon_id.lower().strip()
        self.pokemon_data: Optional[dict[str, Any]] = None
        self.especies_data: Optional[dict[str, Any]] = None
        self.cadena_evoluciones: Optional[dict[str, Any]] = None

    def get_pokemon_info(self) -> bool:
        """Obtiene los datos basicos del pokemon

        Retorns:
        - True si se obtuvieron los datos correctamente
        - False si no se obtuvieron los datos correctamente
        """

        try:
            response = requests.get(
                f"{self.BASE_URL}pokemon/{self.pokemon_id}", timeout=10
            )

            if response.status_code == 200:
                self.pokemon_data = response.json()
                return True
            else:
                print(f"Error: {response.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return False

    def get_datos_especie(self):
        """Obtiene los datos de la especie del pokemon

        Retorns:
        - True si se obtuvieron los datos correctamente
        - False si no se obtuvieron los datos correctamente
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}pokemon-species/{self.pokemon_id}", timeout=10
            )

            if response.status_code == 200:
                self.especies_data = response.json()
                return True
            else:
                print(
                    f"Error: {response.status_code} al obtener los datos de la especie"
                )
                return False
        except requests.exceptions.RequestException as e:
            print(f"Error: {e} al obtener los datos de la especie")
            return False

    def get_cadena_evoluciones(self) -> bool:
        """Obtiene la cadena de evoluciones del pokemon

        Retorns:
        - True si se obtuvieron los datos correctamente
        - False si no se obtuvieron los datos correctamente
        """
        try:
            if not self.especies_data:
                print("Error: no se han obtenido los datos de la especie")
                return False

            evolution_url = self.especies_data.get("evolution_chain", {}).get("url", "")

            if not evolution_url:
                print("Error: No se encontró la URL de la cadena de evoluciones")
                return False

            response = requests.get(evolution_url, timeout=10)

            if response.status_code == 200:
                self.cadena_evoluciones = response.json()
                return True
            else:
                print(
                    f"Error: {response.status_code} al obtener la cadena de evoluciones"
                )
                return False

        except requests.exceptions.RequestException as e:
            print(f"Error: {e} al obtener la cadena de evoluciones")
            return False

    def show_informacion_basica(self):
        """Muestra la informacion basica del pokemon"""

        if not self.pokemon_data:
            print("Error: No se han obtenido los datos del pokemon")
            return

        print("\n" + "=" * 50)
        print("INFORMACIÓN DEL POKÉMON")
        print("=" * 50)
        print(f"Nombre: {self.pokemon_data['name'].capitalize()}")
        print(f"ID: {self.pokemon_data['id']}")
        print(f"Peso: {self.pokemon_data['weight'] / 10:.1f} kg")
        print(f"Altura: {self.pokemon_data['height'] / 10:.1f} m")

        tipos = [tipo["type"]["name"] for tipo in self.pokemon_data.get("types", [])]
        print(f"Tipo(s): {', '.join(tipo.capitalize() for tipo in tipos)}")

    def show_games(self):
        """Muestra los juegos en los que aparece el pokemon"""

        if not self.pokemon_data:
            print("Error: No se han obtenido los datos del pokemon")
            return

        juegos = [
            juego["version"]["name"]
            for juego in self.pokemon_data.get("game_indices", [])
        ]

        if juegos:
            print("\n" + "=" * 50)
            print("JUEGOS EN LOS QUE APARECE")
            print("=" * 50)
            for juego in juegos:
                print(f" - {juego.replace('-', ' ').title()}")
        else:
            print("\nNo se han encontrado juegos en los que aparezca el pokemon")

    def show_cadena_evoluciones(self):
        """Muestra la cadena de evoluciones del pokemon"""
        if not self.cadena_evoluciones:
            print("Error: No hay datos en la cadena de evoluciones disponibles")
            return

        print("\n" + "=" * 50)
        print("CADENA DE EVOLUCIONES")
        print("=" * 50)

        def get_evoluciones(chain: Dict[str, Any], nivel: int = 0) -> None:
            """
            Funcion recursiva

            Args:
                chain: La cadena de evoluciones
                nivel: El nivel de indentacion
            """
            nombre = chain["species"]["name"]
            identacion = "  " * nivel
            print(f"{identacion}- {nombre.capitalize()}")

            if chain.get("evolves_to"):
                for evolucion in chain["evolves_to"]:
                    get_evoluciones(evolucion, nivel + 1)

        get_evoluciones(self.cadena_evoluciones["chain"])

    def show_toda_informacion(self) -> None:
        """Muestra toda la informacion del pokemon"""
        if not self.get_pokemon_info():
            return

        self.show_informacion_basica()
        self.show_games()

        if self.get_datos_especie():
            if self.get_cadena_evoluciones():
                self.show_cadena_evoluciones()

        print("\n" + "=" * 50)


def main():
    print("=" * 80)
    print("CONSULTA INFORMACION DE UN POKEMON")
    print("=" * 80)

    pokemon_id = input("\n Introduce el ID o nombre del pokemon: ")

    if not pokemon_id:
        print("Error: Debes introducir un ID o nombre de pokemon.")
        return

    pokemon = PokemonInfo(pokemon_id)
    pokemon.show_toda_informacion()


if __name__ == "__main__":
    main()
