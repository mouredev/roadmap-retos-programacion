from random import randint

# Array de Preguntas del Sombrero

preguntas = [
    "¿Te sientes cómodo manejando servidores?",
    "¿Eres bueno con Javascript y CSS?",
    "¿Manejas bases de datos?",
    "¿Programas en Python, Ruby, C, u otro lenguaje de Backend?",
    "¿Te gusta tomar café?",
    "¿Haz hecho algun proyecto de páginas web?",
    "¿Conoces tecnologías de manejo de datos?",
    "¿Te gusta programar programas de escritorio?",
    "¿Usas PHP?",
    "¿Usas Kotlin y/o Java?"
]

# Variables de respuestas

n = "no"
s = "si"
l = "lo manejo"
m = "no mucho"

# Posibles variaciones de respuestas
# N de Array = N de Preguntas

responses = {
    "Frontend": [n, s, n, n, m, l, n, m, m, m],
    "Backend":  [l, m, l, s, s, s, l, l, l, l],
    "Mobile":   [m, l, m, m, l, n, m, n, n, s],
    "Data":     [s, n, s, l, n, m, s, s, s, n]
    }

houses_points = {
    "Frontend": 0,
    "Backend":  0,
    "Mobile":   0,
    "Data":     0
    }

def main():
    name = input("Ingrese el nombre del alumno: ")
    print("Bienvenido al Hogwarts Express, %s!" % (name))
    print("Este es tu sombrero seleccionador, encuentra tu camino hacia la escuela de programación de Hogwarts.")
    print("Empezamos las preguntas.")
    for pregunta in range(len(preguntas)):
        bad_answer = True
        while bad_answer:
            respuesta = input(preguntas[pregunta] + " (Si/No/No mucho/Lo manejo): ").lower()
            if respuesta in ["si", "no", "lo manejo", "no mucho"]:
                for i in responses.keys():
                    if responses[i][pregunta] == respuesta:
                        houses_points[i] += 1
                bad_answer = False
            else:
                print("Respuesta incorrecta, intenta nuevamente.")
    
    casas_mas_probables = []

    for i in houses_points.keys():
        casas_mas_probables.append((houses_points[i], i))
    casas_mas_probables.sort(reverse=True)
    
    casa_mas_probable = 0
    
    if casas_mas_probables[0][0] == casas_mas_probables[1][0]:
        print("La decision ha sido dificil...")
        casa_mas_probable = randint(0,1)
    
    return name, casas_mas_probables[casa_mas_probable][1]

if __name__ == "__main__":
    nombre_alumno, estancia = main()
    print("¡%s, te ha tocado %s!" % (nombre_alumno, estancia))
