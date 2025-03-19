import requests as re


def check_connection():
    try:
        r = re.get("https://retosdeprogramacion.com")
        print("La petición fue existosa")
    except Exception as e:
        print(f"Error: {e}")


def get_pokemon(identifier: str):
    try:
        r = re.get(f"https://pokeapi.co/api/v2/pokemon/{identifier}")
        r_json = r.json()

        types = r_json['types']

        print(f"\nID: {r_json['id']}")
        print(f"Nombre: {r_json['name']}")
        print(f"Peso: {r_json['weight']} libras")
        print(f"Altura: {r_json['height']} pies")
        print(f"Tipos:")
        for type in types:
            print(f"    - {get_type(type['type']['url'])}")

    except Exception as e:
        print("El Pokemon o ID no son válidos")


def get_type(url: str):
    r = re.get(url)
    r_json = r.json()
    return r_json['name']


def main():
    finish = False

    while not finish:

        print("\nSelecciona una opción:\n"
              "1 - Introducir nombre o ID del Pokemon\n"
              "2 - Salir")
        option = int(input("> "))

        match option:
            case 1:
                print("\nEscribe el nombre o identificador del Pokemon")
                identifier = input("> ")
                get_pokemon(identifier)
            case 2:
                finish = True
                print("Hasta pronto 👋")
            case _:
                print("⚠️ Opción seleccionada no válida")


if __name__ == '__main__':
    main()
