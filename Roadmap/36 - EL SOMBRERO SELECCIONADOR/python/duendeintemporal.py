#36 { Retos para Programadores } EL SOMBRERO SELECCIONADOR 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""  
 * EJERCICIO:
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
 *    pero indicándole al alumno que la decisión ha sido complicada).

"""

log = print

questions = [
    {
        "question": "What type of projects are you most interested in developing?",
        "answers": [
            {"option": "Native mobile applications for multiple platforms.", "house": "Mobile"},
            {"option": "Visually appealing and responsive interfaces.", "house": "Frontend"},
            {"option": "Processing and analyzing large volumes of data.", "house": "Data Analysis"},
            {"option": "Robust systems and server performance optimization.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "What aspect of development do you enjoy the most?",
        "answers": [
            {"option": "Creating efficient and functional mobile applications.", "house": "Mobile"},
            {"option": "Working on design and user experience.", "house": "Frontend"},
            {"option": "Analyzing data to make data-driven decisions.", "house": "Data Analysis"},
            {"option": "Solving complex logic and scalability problems.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "What tool do you prefer to use in your day-to-day work?",
        "answers": [
            {"option": "Kotlin or Swift for developing native mobile apps.", "house": "Mobile"},
            {"option": "Frameworks like React or Angular.", "house": "Frontend"},
            {"option": "Python or R for data analysis.", "house": "Data Analysis"},
            {"option": "Languages like Node.js or Python for server management.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "How do you see yourself in a development team?",
        "answers": [
            {"option": "Developing the interface and functionality of a mobile app.", "house": "Mobile"},
            {"option": "Designing interactions and visual components.", "house": "Frontend"},
            {"option": "Modeling data and building analysis dashboards.", "house": "Data Analysis"},
            {"option": "Responsible for server logic and APIs.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "What motivates you the most when working on a project?",
        "answers": [
            {"option": "Ensuring that a mobile application works perfectly on any device.", "house": "Mobile"},
            {"option": "Seeing the design come to life on the screen.", "house": "Frontend"},
            {"option": "Discovering insights from data analysis.", "house": "Data Analysis"},
            {"option": "Optimizing system performance and scalability.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "What is your approach to learning new technologies?",
        "answers": [
            {"option": "Trying out new platforms and tools for mobile development.", "house": "Mobile"},
            {"option": "Experimenting with new libraries and frameworks for user interfaces.", "house": "Frontend"},
            {"option": "Exploring advanced data analysis and machine learning techniques.", "house": "Data Analysis"},
            {"option": "Learning about new architectures and server languages.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "What type of challenges do you enjoy solving the most?",
        "answers": [
            {"option": "Creating smooth user experiences on mobile devices.", "house": "Mobile"},
            {"option": "Optimizing interfaces to look good on any device.", "house": "Frontend"},
            {"option": "Analyzing large volumes of data to detect hidden patterns.", "house": "Data Analysis"},
            {"option": "Solving concurrency and load issues on servers.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "How do you like to measure the success of your work?",
        "answers": [
            {"option": "By the smoothness and performance of the mobile app on different devices.", "house": "Mobile"},
            {"option": "By user satisfaction with the visual interface.", "house": "Frontend"},
            {"option": "By the accuracy and relevance of the results obtained from data analysis.", "house": "Data Analysis"},
            {"option": "By the stability and speed of the system under load.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "What do you find most interesting when working with emerging technologies?",
        "answers": [
            {"option": "Developing mobile apps that leverage new hardware capabilities.", "house": "Mobile"},
            {"option": "Trying out new tools and methodologies to improve design and UX.", "house": "Frontend"},
            {"option": "Working with big data or artificial intelligence technologies.", "house": "Data Analysis"},
            {"option": "Exploring new architectures to improve server performance.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    },
    {
        "question": "How do you approach a new problem in a project?",
        "answers": [
            {"option": "Exploring how to improve the user experience on mobile devices.", "house": "Mobile"},
            {"option": "Reassessing the visual and functional structure of the interface.", "house": "Frontend"},
            {"option": "Looking for patterns and solutions based on data analysis.", "house": "Data Analysis"},
            {"option": "Analyzing the data structure and backend logic.", "house": "Backend"},
            {"option": "All of the above", "house": "Fullstack"}
        ]
    }
]

def start(questions):
    log('\n')
    log('Welcome to the best roadmap for developers you have ever seen!')
    log('\n')
    log('Every September 1st, the Hogwarts Express departs for the Hogwarts School of Code for Wizards and Witches of programming.')
    log('\n')
    log('There, the famous Sorting Hat helps programmers find their path...')
    log('\n')
    log("Let's get started! Happy coding!")
    log('\n')

    answers = []
    count = 0

    def show_result(answer):
        result = []
        areas = ['Mobile', 'Frontend', 'Data Analysis', 'Backend', 'Fullstack']

        for i in range(1, 6):
            total = answer.count(i)
            result.append(total)

        max_value = max(result)
        max_indices = [index for index, value in enumerate(result) if value == max_value]

        log('You seem to be oriented to the next area/areas:')
        for r in max_indices:
            log(f"{areas[r]}")

    def make_question(count):
        if count < len(questions):
            log('Options:')
            for idx, opt in enumerate(questions[count]['answers']):
                log(f"{idx + 1}. {opt['option']}")
            log('Question:')
            user_input = input(f"{questions[count]['question']} Please choose a # from 1 to 5 according to the option: ")
            log('\n')
            try:
                result = int(user_input)
                if 1 <= result <= 5:
                    answers.append(result)
                    make_question(count + 1)
                else:
                    log('Invalid input. You must select a # between 1 and 5. Please try again.')
                    make_question(count)  # Repeat the last question
            except ValueError:
                log('Invalid input. Please enter a number.')
                make_question(count)  # Repeat the last question
        else:
            show_result(answers)

    make_question(count)

start(questions)

