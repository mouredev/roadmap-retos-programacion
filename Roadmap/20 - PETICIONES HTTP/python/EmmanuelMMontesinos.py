"""
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 */
"""

# Peticiones HTTP
import requests

respuesta = requests.get("https://retosdeprogramacion.com/")

if respuesta.status_code == 200:
    print(respuesta.text)

else:
    print(f"Hay un error: {respuesta.status_code}")

"""
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""

# Clase para la consulta
class PokeConsulta:
    
    URL = "https://pokeapi.co/api/v2/pokemon/"

    # Función para imprimir listas
    def anidado(self,campo,nombre=None,evoluciones=False):
        ciclo = 0
        # Si NO son evoluciones
        if not evoluciones:
            for n in campo:
                ciclo += 1
                print(f"{ciclo} - {n}")
        # Si son evoluciones
        else:
            marcador = "Pre-Evolución"
            for n in campo:
                ciclo += 1
                if nombre == n:
                    marcador = "Pokemon Actual"
                elif nombre != n and marcador == "Pokemon Actual":
                    marcador = "Evolución"
                print(f"{ciclo} - {n} ({marcador})")

        print()

    # Función para consultar a la Api
    def consultar(self,consulta):

        respuesta = requests.get(f"{PokeConsulta.URL+str(consulta)}")

        if respuesta.status_code == 200:
            # Asigna valores para despues imprimirlos
            pokemon = respuesta.json()
            nombre = pokemon["name"].title()
            id = pokemon["id"]
            peso = pokemon["weight"]
            altura = pokemon["height"]
            tipos = [t["type"]["name"].title() for t in pokemon["types"]]

            # Nueva request para obtener todas las evoluciones
            evoluciones = []
            respuesta_evo = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{id}")
            respuesta_evo = respuesta_evo.json()
            url_evo = respuesta_evo["evolution_chain"]["url"]
            respuesta_evo = requests.get(url_evo)
            respuesta_evo = respuesta_evo.json()

            check = False
            nido = respuesta_evo["chain"]
            baby = None
            if nido["is_baby"] == True:
                baby = nido["species"]["name"].title()
            while not check:
                evoluciones.append(nido["species"]["name"].title())
                if len(nido["evolves_to"]) == 0:
                    check = True
                else:
                    nido = nido["evolves_to"][0]
            # Obtener todos los juegos donde aparece
            juegos = [game["version"]["name"].title() for game in pokemon["game_indices"]]

            # Imprimir Info
            print(f"Nombre: {nombre}")
            print(f"ID: {id}")
            print(f"Peso: {peso}")
            print(f"Altura: {altura}")
            print()
            print("Evoluciones:")
            print(f"Bebe: {baby}")
            self.anidado(evoluciones,nombre=nombre,evoluciones=True)
            print("Tipos:")
            self.anidado(tipos)
            print("Ha salido en los siguientes Juegos:")
            self.anidado(juegos)
        else:
            print(f"{consulta} no aparece en la api, comprueba que sea un nombre/numero válido")

# Programa en terminal
def program_terminal():

    check = False
    consulta = PokeConsulta()
    while not check:

        solicitud = input("Ponga el numero o el nombre de un pokemon (escribir 'salir' para cerrar): ")

        if solicitud.lower() == "salir":
            check = True
        else:
            consulta.consultar(solicitud)

# Pruebas
if __name__ == "__main__":
    program_terminal()
