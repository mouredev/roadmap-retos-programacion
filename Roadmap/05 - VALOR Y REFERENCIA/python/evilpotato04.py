
#/*
# * EJERCICIO:
# * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
# *   su tipo de dato.
# * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
# *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
# * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
# *

# asignación por valor
games = ["Genshin Impact", "Sky", "Pokémon"]
ano_de_publicacion = [2020, 2019, 1996]

print(games)
print(ano_de_publicacion)

# asignación por referencia
games_ref = games
ano_de_publicacion_ref = ano_de_publicacion

print("-"*10)
print(games_ref)
print(ano_de_publicacion_ref)

games_ref.append("The Legend of Zelda")
ano_de_publicacion_ref.append(1986)

print("-"*10)
print(games)
print(ano_de_publicacion)
print(games_ref)
print(ano_de_publicacion_ref)

# funciones por valor
def agregar_nuevo_game(games: list, anos: list, nuevo_game: str, nuevo_ano: int):
    print("-"*10)
    games_actualizados = []
    for game in games:
        games_actualizados.append(game)
    games_actualizados.append(nuevo_game)

    anos_actualizados = []
    for ano in anos:
        anos_actualizados.append(ano)
    anos_actualizados.append(nuevo_ano)

    print(games)
    print(anos)
    print(games_actualizados)
    print(anos_actualizados)

agregar_nuevo_game(games, ano_de_publicacion, "Honkai Star Rail", 2023)

print(games)
print(ano_de_publicacion)

# funciones por referencia
def combinar_listas_de_games(games1: list, games2: list):
    print(games1)
    games1.extend(games2)
    print(games1)

combinar_listas_de_games(games, ["Palia", "Life Makeover", "Candy Crush"])
print(games)

# * DIFICULTAD EXTRA (opcional):
# * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
# * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
# *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
# *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
# *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
# *   Comprueba también que se ha conservado el valor original en las primeras.
# */

print("="*10)

player_1 = "Mario"
player_2 = "Luigi"

def cambiar_players(player_1: str, player_2: str):
    players = [player_1, player_2]
    player_1 = players[1]
    player_2 = players[0]
    print(player_1, "and", player_2)

    return player_1, player_2

print(player_1, "and", player_2)
player_1, player_2 = cambiar_players(player_1, player_2)
print(player_1, "and", player_2)

print("="*10)

def cambiar_players_ref(player_1: str, player_2: str):
    player_1, player_2 = player_2, player_1
    print(player_1, "and", player_2)

print(player_1, "and", player_2)
cambiar_players_ref(player_1, player_2)
print(player_1, "and", player_2)
