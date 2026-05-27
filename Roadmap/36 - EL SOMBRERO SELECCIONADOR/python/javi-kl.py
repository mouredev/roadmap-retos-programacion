import random

l_preguntas = [
    "1. Horas al día programando?",
    "2. Edad?",
    "3. Hobby?",
    "4. Serie favorita?",
    "5. Lenguaje favorito?",
    "6. Profesor favorito?,",
    "7. Nivel de convicción?",
    "8. Que IA utilizas?",
    "9. Proyecto actual?",
    "10. Como te ves en 3 años?",
]

valid_answers = ["a", "b", "c", "d"]


def pedir_nombre():
    print("bienvenido a Hogwarts escuela de programación")
    nombre = input("Dime tu nombre\n-> ")
    return nombre


def asignar_puntos(l_preguntas):
    c_hogwarts = {"frontend": 0, "backend": 0, "mobile": 0, "data": 0}
    for p in l_preguntas:
        print(p)
        while True:
            respuesta = input("Opciones:\na\nb\nc\nd\n-> ").lower()
            if respuesta not in valid_answers:
                print("Presta atención!!!\nIntroduce una opción válida")
            else:
                break

        match respuesta:
            case "a":
                c_hogwarts["frontend"] += 1
            case "b":
                c_hogwarts["backend"] += 1
            case "c":
                c_hogwarts["mobile"] += 1
            case "d":
                c_hogwarts["data"] += 1

    return c_hogwarts


def asignar_alumno(c_hogwarts):
    casas = []
    n_max = max(c_hogwarts.values())
    for casa, puntos in c_hogwarts.items():
        if puntos == n_max:
            casas.append(casa)

    if len(casas) > 1:
        print(
            f"Ha habido un empate entre {', '.join(casas)}\nSe elegirá de forma aleatoria"
        )
        ganador = random.choice(casas)
        return ganador
    else:
        return casas[0]


def retornar_decisión(c_final, n_alumno):
    return f"El alumno {n_alumno} ha sido elegido para entrar en: {c_final}"


if __name__ == "__main__":  # Sirve para que no se pueda ejecutar como un modulo
    # (requiere lanzar este archivo directamente)
    n_alumno = pedir_nombre()
    c_hogwarts = asignar_puntos(l_preguntas)
    c_final = asignar_alumno(c_hogwarts)
    print(retornar_decisión(c_final, n_alumno))
