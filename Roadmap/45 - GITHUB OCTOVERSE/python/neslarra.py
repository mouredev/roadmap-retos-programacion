r"""
 EJERCICIO:
 GitHub ha publicado el Octoverse 2024, el informe
 anual del estado de la plataforma:
 https://octoverse.github.com

 Utilizando el API de GitHub, crea un informe asociado
 a un usuario concreto.
 
 - Se debe poder definir el nombre del usuario
   sobre el que se va a generar el informe.
   
 - Crea un informe de usuario basándote en las 5 métricas
   que tú quieras, utilizando la informración que te
   proporciona GitHub. Por ejemplo:
   - Lenguaje más utilizado
   - Cantidad de repositorios
   - Seguidores/Seguidos
   - Stars/forks
   - Contribuciones
   (lo que se te ocurra)
"""
import requests


URL_BASE = "https://api.github.com/users/"


def get_github_data(url: str) -> dict:
    response = requests.request("GET", url)
    if response.status_code != 200:
        return {}
    return response.json()


def menu(options: list) -> str:
    while True:
        print("\nSeleccionar métrica:\n")
        for ind, opt in enumerate(options):
            print(f"\t{ind + 1} - {opt}")
        print("\t0 - Salir\n")
        option = input(f"\tOpción# [0-{metrics.__len__()}] => ")
        if option.isnumeric() and 0 <= int(option) < metrics.__len__():
            return "" if option == "0" else metrics[int(option) - 1]


username = input("Usuario: ")
data = get_github_data(URL_BASE + username)
metrics = []
if data:
    for k, v in data.items():
        if v:
            metrics.append(k)
    while True:
        metric = menu(metrics)
        if not metric:
            quit()
        if data[metric].__class__.__name__ == "str" and data[metric].startswith("http"):
            try:
                new_data = get_github_data(data[metric])
            except requests.exceptions.JSONDecodeError:
                new_data = {}
            if new_data:
                print(f"{metric}:")
                print(f"\t{new_data}")
            else:
                print(f"{metric}: acceda manualmente a {data[metric]}")
        else:
            print(f"{metric}: {data[metric]}")
        _ = input("\nPresiones ENTER para continuar...")
print(f"No se obtuvieron datos para {username}")
