"""
 EJERCICIO:
 ¡Los JJOO de París 2024 han comenzado!
 Crea un programa que simule la celebración de los juegos.
 El programa debe permitir al usuario registrar eventos y participantes,
 realizar la simulación de los eventos asignando posiciones de manera aleatoria
 y generar un informe final <=>> por terminal.
 Requisitos:
 1. Registrar eventos deportivos.
 2. Registrar participantes por nombre y país.
 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 5. Mostrar los ganadores por cada evento.
 6. Mostrar el ranking de países según el número de medallas.
 Acciones:
 1. Registro de eventos.
 2. Registro de participantes.
 3. Simulación de eventos.
 4. Creación de informes.
 5. Salir del programa.
"""


class Athlete:

    def __init__(self, name: str, country: str, game: str, participation: str):
        self.name = name
        self.country = country
        self.game = game
        self.participation = participation

    def get_name(self):
        return self.name

    def get_country(self):
        return self.country


class Game:

    def __init__(self, game: dict):
        self.name = game["name"]
        self.members = game["members"]
        self.competitors_team = dict()
        self.medals_team = {"gold": "", "silver": "", "bronze": ""}
        self.scores_team = dict()
        self.competitors_individual = dict()
        self.medals_individual = {"gold": "", "silver": "", "bronze": ""}
        self.scores_individual = dict()

    def add_competitor(self, athlete: Athlete):
        if athlete.participation == "Team":
            self.add_competitors_team(athlete)
        else:
            self.add_competitors_individual(athlete)

    def add_competitors_team(self, athlete: Athlete):
        if athlete.country in self.competitors_team.keys():
            self.competitors_team[athlete.country].append(athlete)
        else:
            self.competitors_team[athlete.country] = [athlete]

    def set_scores_team(self, country: str, score: float):
        self.scores_team[country] = score

    def set_medals_team(self):
        positions = list(sorted(self.scores_team.items(), key=lambda x: x[1], reverse=True))
        self.medals_team["gold"] = positions[0][0]
        self.medals_team["silver"] = positions[1][0]
        self.medals_team["bronze"] = positions[2][0]

    def add_competitors_individual(self, athlete: Athlete):
        if athlete.country in self.competitors_individual.keys():
            self.competitors_individual[athlete.country].append(athlete)
        else:
            self.competitors_individual[athlete.country] = [athlete]

    def set_scores_individual(self, athlete: str, score: float):
        self.scores_individual[athlete] = score

    def set_medals_individual(self):
        positions = list(sorted(self.scores_individual.items(), key=lambda x: x[1], reverse=True))
        self.medals_individual["gold"] = positions[0][0]
        self.medals_individual["silver"] = positions[1][0]
        self.medals_individual["bronze"] = positions[2][0]


def get_valid_name() -> str:
    import requests
    api_names_url = "https://randomuser.me/api/"
    lower_letters = list(map(chr, range(ord("a"), ord("z") + 1)))

    while True:
        req = requests.get(api_names_url)
        data = req.json()
        firstname = data["results"][0]["name"]["first"]
        lastname = data["results"][0]["name"]["last"]
        if all([c.lower() in lower_letters for c in firstname + lastname]):  # evitar otros alfabetos
            break
    return firstname + " " + lastname


def load_games(games: list, countries: list):
    x = 0
    print("Cargando 504 atletas...")
    for game in games:
        for country in countries:
            for participation_type in ("Individual", "Team"):
                if participation_type == "Individual":
                    members = 1
                else:
                    members = game.members
                for i in range(0, members):
                    if (x % 3) == 0:
                        print(f"\b\b\b\b---{x}>", end="")
                        if (x % 60) == 0:
                            print("")
                    x += 1
                    name = get_valid_name()
                    athlete = Athlete(name, country, game.name, participation_type)
                    game.add_competitor(athlete)


def competition(game: Game):
    from random import uniform
    get_scores = lambda x: list(map(lambda a: uniform(13, 16).__round__(3), range(0, x)))
    get_media = lambda x: sum(x) / x.__len__()

    for country in game.competitors_team.keys():
        scores = get_scores(game.members)
        media = get_media(scores)
        game.set_scores_team(country, media)

    for athlete in game.competitors_individual.values():
        scores = get_scores(1)
        media = get_media(scores)
        game.set_scores_individual(athlete[0], media)


def final_report(game: Game):
    print(f"\n{game.name}")
    print("\tIndividual")
    for medal, athlete in game.medals_individual.items():
        print(f"\t\t{medal} {athlete.get_name()} / {athlete.get_country()}")
    print("\tTeams")
    for medal, country in game.medals_team.items():
        print(f"\t\t{medal} {country}")


games = []
for game in [{"name": "Shoot", "members": 2}, {"name": "Archery", "members":  4}, {"name": "Swim", "members":  4}, {"name": "Gymnastic", "members":  6},
             {"name": "Tennis", "members":  2}, {"name": "Judo", "members":  4}, {"name": "Fencing", "members":  4}, {"name": "Table Tennis", "members":  2}]:
    games.append(Game(game))

countries = ['AIM', 'Argelia', 'Argentina', 'Brasil', 'Canada', 'China', 'Corea', 'EEUU', 'Egipto', 'España', 'Jamaica', 'Japón', 'México', 'Sudáfrica']

load_games(games, countries)

print("")
for game in games:
    competition(game)
    game.set_medals_individual()
    game.set_medals_team()
    final_report(game)
