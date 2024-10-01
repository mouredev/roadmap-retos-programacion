import os, platform, random

if (platform.platform().startswith("macOS") or platform.platform().startswith("Linux")):
    os.system('clear')
else:
    os.system('cls')


""" * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada)."""


houses_score = [0,0,0,0]
houses_dict = {"Frontend":0, "Backend":0, "Mobile":0 , "Data":0}

points_distribution =  [{1:[1,4,2,6],2:[1,6,2,4],3:[1,4,6,2],4:[6,1,4,2]},
                        {1:[2,4,6,1],2:[6,1,4,2],3:[1,4,2,6],4:[2,6,1,4]},
                        {1:[1,2,4,6],2:[6,1,4,2],3:[1,6,2,4],4:[1,2,6,4]},
                        {1:[1,4,6,2],2:[1,4,2,6],3:[1,6,4,2],4:[6,1,4,2]},
                        {1:[1,6,2,4],2:[2,1,6,4],3:[6,2,4,1],4:[2,1,4,6]},
                        {1:[1,6,2,4],2:[6,1,4,2],3:[1,4,2,6],4:[4,1,6,2]},
                        {1:[1,6,2,4],2:[6,2,4,1],3:[1,4,2,6],4:[4,1,6,2]},
                        {1:[1,6,4,2],2:[2,4,1,6],3:[4,2,6,1],4:[6,2,4,1]},
                        {1:[6,2,1,4],2:[4,2,1,6],3:[4,6,1,2],4:[1,4,6,2]},
                        {1:[6,1,4,2],2:[2,6,4,1],3:[4,2,6,1],4:[2,1,4,6]}]

questions = {"\nPregunta 1: ¿Cual de estas definiciones se ajusta más a tu personalidad?":
             ["1 - Analítico, me gusta tener todo perféctamente calculado",
             "2 - Introvertido, me gusta tener perfil bajo y trabajar en la sombra",
             "3 - Nómada digital, me gusta viajar pero estar siempre conectado",
             "4 - Creativo, me gusta enseñar mis obras y disfruto con el estilo"],

              "\nPregunta 2: ¿Cual de estas tecnologías te gusta más?":
              ["1 - Kotlin", "2 - CSS", "3 - MySQL", "4 - Python"],

              "\nPregunta 3: ¿Cual de estos dispositivos portátiles preferirías como regalo?":
              ["1 - Un Chromebook", "2 - Un iPad con apple pencil", "3 - Un laptop con Arch Linux", "4 - Un smartphone de gama alta"],

              "\nPregunta 4: ¿Cual de estas asignaturas te gusta o te gustó más estudiar?":
              ["1 - Telecomunicaciones", "2 - Matemáticas", "3 - Robótica", "4 - Dibujo artístico"],

              "\nPregunta 5: ¿Cual de 4 películas según tu personalidad crees que más se adapte a ti por temática?, (si no la has visto busca la sinopsis)":
              ["1 - El indomable will Hunting--back", "2 - Her--mobile", "3 - Ghost in the shell--front", "4 - Moneyball--data"],

              "\nPregunta 6: ¿Cual de estos coches crees que va mejor contigo?":["1 - Cualquier utilitario barato, funcional y discreto",
              "2 - Uno con estilo tipo Fiat 500 o Mini Cooper", "3 - El que mejor relación específica tenga entre CV/Cilindrada/Consumo",
              "4 - Un Tesla o similar, que sea eléctrico y con conectividad de todo tipo con mi smartphone a bordo y en remoto"],

              "\nPregunta 7: ¿Cual de estas carreras hubieses elegido de no haber sido la de informática?":["1 - Cualquier otra ingeniería",
              "2 - Bellas artes", "3 - Sin duda administración de empresas", "4 - Si existe, alguna que estudie nanotecnología"],

              "\nPregunta 8: Otra de tecnologías , ¿Cual de estas te gusta más?":["1 - Java", "2 - MongoDB", "3 - Swift", "4 - Tailwind"],

              "\nPregunta 9: ¿Qué programa/aplicación de estas te gusta o usas más?":["1 - Google Chrome", "2 - PowerBI", "3 - VScode", "4 - Android Studio"],

              "\nPregunta 10: ¿Cual de estas características de la marca Apple crees que es más importante en su éxito?":
                ["1 - Su interfaz visual , el diseño de sus dispositivos, su enfoque hacia el mundo creativo y visual y su framework gráfico SwiftUI",
                 "2 - Su lenguaje propio Swift y lo buenos y productivos que son sus ordenadores para trabajo con cualquier lenguaje de programación en general"
                 "3 - Sus dispositivos y los sistemas operativos iOS, IpadOS, watchOS, tvOS y sobre todo la joya de la corona, el iPhone",
                 "4 - Su capacidad de innovación y de mantenerse siempre en los ranking de ventas, 9 de cada 10 personas en el mundo conocen a Apple"]
              }


name = input("introduzca su nombre: ").title()

def points_management(answer:int, round:int):
    distribution_question:dict = points_distribution[round-1]
    distribution_answer:list = distribution_question[answer]
    for points in range (0,len(houses_score),1):
            
            houses_score[points] = houses_score[points] + distribution_answer[points]
            
def quest_printer(questions:dict):
    round = 0
    for question in list(questions.keys()):  
        print(question)
        for answers in questions[question]:
            print(answers)
        answer = input("Elija una de las 4 opciones--> ")
        while not answer.isdigit() or int(answer) < 1 or int(answer) > 4:
            print("Sólo se pueden introducir números del 1 al 4, pruebe de nuevo")
            answer = input("Elija una de las 4 opciones--> ")
            
        round += 1
        points_management(int(answer), round)

quest_printer(questions)

tie = False
for result in houses_score:
    while houses_score.count(result) > 1: 
        my_bool = random.randint(0, 1)
        bool(my_bool)  
        if bool:
            result -= 1
        tie = True
          
houses_dict["Frontend"] = houses_score[0]
houses_dict["Backend"] = houses_score[1]
houses_dict["Mobile"] = houses_score[2]
houses_dict["Data"] = houses_score[3]
win = max(houses_dict.items(), key=lambda x: x[1])[0]

print(f"Por las respuestas que has dado {name} parece que el sector de programación que más se adapta a ti es el de {win}")
if tie:
    print("Pero la decisión ha sido difícil")

