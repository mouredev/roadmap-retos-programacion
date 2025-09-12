import os
import re
import json

CHALLENGE_PATTERN = r"^\d{2} - "
EXCLUDED = ["stats.py", "stats.json", "ejercicio.md",
            ".ds_store", "tempcoderunnerfile.py"]

path = os.path.dirname(__file__)

challenges = {}
current_challenge = ""
languages = {}
users = {}
files_total = 0

for dirpath, _, files in os.walk(path):

    challenge = os.path.basename(dirpath)
    if re.match(CHALLENGE_PATTERN, challenge):
        current_challenge = challenge

    language_files = 0

    for file in files:

        if file.lower() not in EXCLUDED:

            language = os.path.basename(dirpath).lower()
            languages[language] = languages.get(language, 0) + 1

            user = os.path.splitext(file)[0].lower()
            user_files = users.get(user, (0, []))[0] + 1
            user_languages = users.get(user, (0, []))[1]
            if language not in user_languages:
                user_languages.append(language)

            users[user] = (user_files, user_languages)

            language_files += 1
            files_total += 1

    if current_challenge != "":
        challenges[current_challenge] = challenges.get(
            current_challenge, 0) + language_files

sorted_challenges = sorted(
    challenges.items(), key=lambda challenge: challenge[1], reverse=True)

sorted_languages = sorted(
    languages.items(), key=lambda language: language[1], reverse=True)

sorted_users = sorted(
    users.items(), key=lambda user: (user[1][0], len(user[1][1])), reverse=True)

challenges_total = len(challenges)
languages_total = len(languages)
users_total = len(users)

challenges_ranking = []
languages_ranking = []
users_ranking = []

print("ESTADÍSTICAS:\n")

print(f"Retos: {challenges_total}")
print(f"Lenguajes de programación: {languages_total}")
print(f"Correcciones: {files_total}")
print(f"Usuarios: {users_total}")

print("\nRanking de retos:")
for index, challenge in enumerate(sorted_challenges):

    order = index + 1
    name = challenge[0]
    count = challenge[1]

    challenges_ranking.append({
        "order": order,
        "name": name,
        "count": count
    })

    print(f"#{order} {name} (Ejercicios: {count})")

print("\nRanking de lenguajes:")
for index, language in enumerate(sorted_languages):

    order = index + 1
    name = language[0]
    count = language[1]
    percentage = round((language[1] * 100) / files_total, 2)

    languages_ranking.append({
        "order": order,
        "name": name,
        "count": count,
        "percentage": percentage
    })

    print(f"#{order} {name} (Ejercicios: {count}) (Porcentaje: {percentage}%)")

print("\nRanking de usuarios:")
for index, user in enumerate(sorted_users):

    order = index + 1
    name = user[0]
    count = user[1][0]
    languages = len(user[1][1])

    users_ranking.append({
        "order": order,
        "name": name,
        "count": count,
        "languages": languages
    })

    print(
        f"#{order} {name} (Ejercicios: {count}) (Lenguajes: {languages})")

data = {
    "challenges_total": challenges_total,
    "languages_total": languages_total,
    "files_total": files_total,
    "users_total": users_total,
    "challenges_ranking": challenges_ranking,
    "languages_ranking": languages_ranking,
    "users_ranking": users_ranking
}

json_data = json.dumps(data, indent=4)
with open(os.path.join(path, "stats.json"), "w") as file:
    file.write(json_data)
