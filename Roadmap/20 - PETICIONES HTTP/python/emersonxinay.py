"""
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */
"""

import requests


def main():
    url = "https://www.compilandocode.com"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la petición fue exitosa

        print("Contenido de la web:")
        print(response.text)  # Imprime el contenido de la respuesta

    except requests.exceptions.RequestException as e:
        print("Error al realizar la petición:", e)


if __name__ == "__main__":
    main()
