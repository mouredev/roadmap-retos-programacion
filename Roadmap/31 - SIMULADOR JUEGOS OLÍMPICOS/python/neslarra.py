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
                    x += 1
                    if x % 3 == 0:
                        print(f"\b\b\b\b---{x}>", end="")
                    if x % 60 == 0:
                        print("")
                    name = get_valid_name()
                    athlete = Athlete(name, country, game.name, participation_type)
                    game.add_competitor(athlete)
    print(f"\b\b\b\b---{x}>")


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


def game_report(game: Game):
    print(f"\n{game.name}")
    print("\tIndividual")
    for medal, athlete in game.medals_individual.items():
        print(f"\t\t{medal} {athlete.get_name()} / {athlete.get_country()}")
    print("\tTeams")
    for medal, country in game.medals_team.items():
        print(f"\t\t{medal} {country}")


def final_report(games: list):
    countries_score = {}
    t = 0
    g = 0
    s = 0
    b = 0
    for game in games:
        for medal, athlete in game.medals_individual.items():
            if athlete.get_country() not in countries_score.keys():
                countries_score[athlete.get_country()] = {"total": 0, "gold": 0, "silver": 0, "bronze": 0}
            countries_score[athlete.get_country()]["total"] += 1
            if medal == "gold":
                countries_score[athlete.get_country()]["gold"] += 1
            elif medal == "silver":
                countries_score[athlete.get_country()]["silver"] += 1
            else:
                countries_score[athlete.get_country()]["bronze"] += 1
        for medal, country in game.medals_team.items():
            if country not in countries_score.keys():
                countries_score[country] = {"total": 0, "gold": 0, "silver": 0, "bronze": 0}
            countries_score[country]["total"] += 1
            if medal == "gold":
                countries_score[country]["gold"] += 1
            elif medal == "silver":
                countries_score[country]["silver"] += 1
            else:
                countries_score[country]["bronze"] += 1
    lista_paises = []
    for y in countries_score.items():
        lista_paises.append({"country": y[0], "gold": y[1]["gold"], "silver": y[1]["silver"], "bronze": y[1]["bronze"], "total": y[1]["total"]})
    lista_paises = sorted(lista_paises, key=lambda k: (-k["gold"], -k["silver"], -k["bronze"], -k["total"], k["country"]))

    for c in lista_paises:
        print(f"{c['country']}: Gold {c['gold']} / Plata {c['silver']} / Bronze {c['bronze']} <=> TOTAL {c['total']}")


games = []
for game in [{"name": "Shoot", "members": 2}, {"name": "Archery", "members":  4}, {"name": "Swim", "members":  4}, {"name": "Gymnastic", "members":  6},
             {"name": "Tennis", "members":  2}, {"name": "Judo", "members":  4}, {"name": "Fencing", "members":  4}, {"name": "Table Tennis", "members":  2}]:
    games.append(Game(game))

countries = ['AIM', 'Argelia', 'Argentina', 'Brasil', 'Canada', 'China', 'Corea', 'EEUU', 'Egipto', 'España', 'Jamaica', 'Japón', 'México', 'Sudáfrica']

load_games(games, countries)

for game in games:
    competition(game)
    game.set_medals_individual()
    game.set_medals_team()
    game_report(game)
print("\n Ranking Final\n")
final_report(games)

r"""
La salida es algo así:

Cargando 504 atletas...
--------------------------------------60>
-----------------------------------------------120>
------------------------------------------------------------180>
------------------------------------------------------------240>
------------------------------------------------------------300>
------------------------------------------------------------360>
------------------------------------------------------------420>
------------------------------------------------------------480>
---------------------------504>

Shoot
	Individual
		gold Farah Fossmo / España
		silver Stefania Nikolaus / Argelia
		bronze Joachim Hubert / Japón
	Teams
		gold EEUU
		silver España
		bronze Canada

Archery
	Individual
		gold Flurin Chevalier / Japón
		silver Waldtraut Wedekind / México
		bronze Amelia Matthews / Argelia
	Teams
		gold Argentina
		silver Egipto
		bronze EEUU

Swim
	Individual
		gold Sabrin Paulsrud / Egipto
		silver Archie Thomas / Jamaica
		bronze Franco Broeren / Argentina
	Teams
		gold Argelia
		silver Jamaica
		bronze Sudáfrica

Gymnastic
	Individual
		gold Patsy Fisher / China
		silver Calvin Peters / AIM
		bronze Freya Molnes / España
	Teams
		gold México
		silver AIM
		bronze Jamaica

Tennis
	Individual
		gold Signe Hansen / AIM
		silver Taliana Castro / Brasil
		bronze Aaron Blanc / Jamaica
	Teams
		gold EEUU
		silver Jamaica
		bronze Egipto

Judo
	Individual
		gold Storm Johansen / AIM
		silver Maelya Colin / China
		bronze Valerij Hartwich / Argentina
	Teams
		gold Japón
		silver Argelia
		bronze Sudáfrica

Fencing
	Individual
		gold Clayton Nelson / Brasil
		silver Prathiksha Manjunath / Egipto
		bronze Juho Halko / Argelia
	Teams
		gold Canada
		silver Egipto
		bronze Argentina

Table Tennis
	Individual
		gold Ajinkya Manjunath / Argentina
		silver Jagat Adiga / AIM
		bronze Aapo Kuusisto / Brasil
	Teams
		gold Japón
		silver España
		bronze Argelia

Ranking Final:

Japón: Gold 3 / Plata 0 / Bronze 1 <=> TOTAL 4
AIM: Gold 2 / Plata 3 / Bronze 0 <=> TOTAL 5
Argentina: Gold 2 / Plata 0 / Bronze 3 <=> TOTAL 5
EEUU: Gold 2 / Plata 0 / Bronze 1 <=> TOTAL 3
Egipto: Gold 1 / Plata 3 / Bronze 1 <=> TOTAL 5
Argelia: Gold 1 / Plata 2 / Bronze 3 <=> TOTAL 6
España: Gold 1 / Plata 2 / Bronze 1 <=> TOTAL 4
Brasil: Gold 1 / Plata 1 / Bronze 1 <=> TOTAL 3
China: Gold 1 / Plata 1 / Bronze 0 <=> TOTAL 2
México: Gold 1 / Plata 1 / Bronze 0 <=> TOTAL 2
Canada: Gold 1 / Plata 0 / Bronze 1 <=> TOTAL 2
Jamaica: Gold 0 / Plata 3 / Bronze 2 <=> TOTAL 5
Sudáfrica: Gold 0 / Plata 0 / Bronze 2 <=> TOTAL 2
"""
