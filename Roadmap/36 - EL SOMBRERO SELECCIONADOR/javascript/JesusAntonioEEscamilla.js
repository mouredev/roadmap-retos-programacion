/** #36 - JavaScript -> Jesus Antonio Escamilla */

/**
 * EL SOMBRERO SELECCIONADOR.
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

// Casas y sus puntos iniciales
const house = {
    Frontend: 0,
    Backend: 0,
    Mobile: 0,
    Data: 0
}

// Preguntas y sus opciones con puntos asignados a cada casa
const questions = [
    {
        question: '1-¿Que te apasiona más al programador?',
        options: {
            a: {text: 'Crear interfaces de usuario', points: { Frontend: 2 }},
            b: {text: 'Desarrollador lógica de negocio', points: { Backend: 2 }},
            c: {text: 'Aplicaciones móviles', points: { Mobile: 2 }},
            d: {text: 'Trabajar con datos y descubrir patrones para mejorar decisiones', points: { Data: 2 }},
        },
    },
    {
        question: '2-¿Cuál es tu herramienta favorita?',
        options: {
            a: { text: 'React o Angular', points: { Frontend: 2 } },
            b: { text: 'Node.js', points: { Backend: 2 } },
            c: { text: 'Swift o Kotlin', points: { Mobile: 2 } },
            d: { text: 'Python y Pandas', points: { Data: 2 } },
        },
    },
    {
        question: '3-¿Cuál de estas tareas te resulta más satisfactoria?',
        options: {
            a: { text: 'Diseñar y estilizar componentes visuales', points: { Frontend: 2 } },
            b: { text: 'Crear APIs y gestionar bases de datos', points: { Backend: 2 } },
            c: { text: 'Optimizar aplicaciones para diferentes dispositivos móviles', points: { Mobile: 2 } },
            d: { text: 'Trabajar con grandes volúmenes de datos y modelos analíticos', points: { Data: 2 } },
        },
    },
    {
        question: '4-¿Con cuál de estas tecnologías te sientes más cómodo trabajando?',
        options: {
            a: { text: 'HTML, CSS, JavaScript', points: { Frontend: 2 } },
            b: { text: 'Python, Java, SQL', points: { Backend: 2 } },
            c: { text: 'Flutter, React Native', points: { Mobile: 2 } },
            d: { text: 'R, SQL, Hadoop', points: { Data: 2 } },
        },
    },
    {
        question: '5-¿Qué herramienta o lenguaje prefieres usar para resolver problemas?',
        options: {
            a: { text: 'Herramientas y frameworks para diseño de interfaces (e.g., Figma, React)', points: { Frontend: 2 } },
            b: { text: 'Lenguajes y frameworks para backend (e.g., Node.js, Django, Spring Boot)', points: { Backend: 2 } },
            c: { text: 'Herramientas de desarrollo móvil (e.g., Xcode, Android Studio)', points: { Mobile: 2 } },
            d: { text: 'Herramientas de análisis de dato (e.g., Jupyter, Tableau, Power BI)', points: { Data: 2 } },
        },
    },
    {
        question: '6-¿Cuál de estas actividades disfrutas más?',
        options: {
            a: { text: 'Crear experiencias de usuario interactivas y responsivas', points: { Frontend: 2 } },
            b: { text: 'Resolver problemas complejos de lógica y optimización de procesos', points: { Backend: 2 } },
            c: { text: 'Construir y probar aplicaciones que funcionen en múltiples dispositivos móviles', points: { Mobile: 2 } },
            d: { text: 'Analizar y visualizar datos para extraer información relevante', points: { Data: 2 } },
        },
    },
    {
        question: '7-¿Qué prefieres en un proyecto?',
        options: {
            a: { text: 'Trabajar en el diseño y la interacción con los usuarios', points: { Frontend: 2 } },
            b: { text: 'Enfocarte en la lógica de negocio y la eficiencia del sistema', points: { Backend: 2 } },
            c: { text: 'Desarrollar para plataformas móviles y trabajar con sus características únicas', points: { Mobile: 2 } },
            d: { text: 'Investigar y analizar datos para proporcionar insights', points: { Data: 2 } },
        },
    },
    {
        question: '8-¿Cuál es tu tipo de proyecto ideal?',
        options: {
            a: { text: 'Un sitio web interactivo y visualmente atractivo', points: { Frontend: 2 } },
            b: { text: 'Un sistema robusto que gestione datos y lógica de negocio', points: { Backend: 2 } },
            c: { text: 'Una aplicación móvil con una experiencia de usuario fluida', points: { Mobile: 2 } },
            d: { text: 'Un dashboard o modelo predictivo que ofrezca información clave', points: { Data: 2 } },
        },
    },
    {
        question: '9-¿Qué te da más satisfacción al finalizar un proyecto?',
        options: {
            a: { text: 'Ver a los usuarios interactuar de manera positiva con tu interfaz', points: { Frontend: 2 } },
            b: { text: 'Saber que tu código maneja de manera eficiente grandes volúmenes de datos', points: { Backend: 2 } },
            c: { text: 'Ver tu aplicación móvil en funcionamiento en diferentes dispositivos', points: { Mobile: 2 } },
            d: { text: 'Proveer información valiosa basada en datos a la empresa', points: { Data: 2 } },
        },
    },
    {
        question: '10-¿Qué consideras un reto divertido en el desarrollo?',
        options: {
            a: { text: 'Mejorar la usabilidad y la estética de una aplicación', points: { Frontend: 2 } },
            b: { text: 'Optimizar la seguridad y el rendimiento de un backend', points: { Backend: 2 } },
            c: { text: 'Resolver problemas de compatibilidad entre diferentes plataformas móviles', points: { Mobile: 2 } },
            d: { text: 'Desarrollar modelos predictivos y manejar bases de datos complejas', points: { Data: 2 } },
        },
    },
];

let currentQuestion = 0;
let studentName = '';

// Función para hacer preguntas
function askQuestion() {
    if (currentQuestion < questions.length) {
        const q = questions[currentQuestion];
        console.log(`\n${q.question}`);
        console.log(`a) ${q.options.a.text}`);
        console.log(`b) ${q.options.b.text}`);
        console.log(`c) ${q.options.c.text}`);
        console.log(`d) ${q.options.d.text}`);

        rl.question('Selección una opción (a, b, c, d): ', (answer) => {
            const option = q.options[answer.toLowerCase()];

            if (option) {
                Object.keys(option.points).forEach((house) => {
                    house[house] += option.points[house];
                });

                currentQuestion++;
                askQuestion();
            } else {
                console.log('Opción no válida. Intenta de nuevo.');
                askQuestion();
            }
        });
    } else {
        sortStudent();
    }
}

// Función para determinar la casa del estudiante
function sortStudent() {
    const sortedHouses  = Object.entries(house).sort(([, a], [, b]) => b - a);
    const topHouse = sortedHouses[0];
    const tiedHouse = sortedHouses.filter(([, points]) => points === topHouse[1]);

    if (tiedHouse.length > 1) {
        const chosenHouse = tiedHouse[Math.floor(Math.random() * tiedHouse.length)];
        console.log(`\n¡Vaya, ${studentName}! Fue una decisión complicada, pero te he colocado en ${chosenHouse[0]}!`);
    } else {
        console.log(`\n${studentName}, te he colocado en ${topHouse[0]}!`);
    }

    rl.close();
}

// Inicio del programa
rl.question('¿Cuál es tu nombre? ', (name) => {
    studentName = name;
    askQuestion(); 
});