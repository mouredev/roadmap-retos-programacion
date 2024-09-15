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
        question: '1- ¿Qué tipo de proyectos te entusiasma más desarrollar?',
        options: {
            a: { text: 'APIs y lógica de negocio en el servidor.', points: { Backend: 2 } },
            b: { text: 'Análisis de datos y modelos predictivos.', points: { Data: 2 } },
            c: { text: 'Aplicaciones móviles con experiencia de usuario fluida.', points: { Mobile: 2 } },
            d: { text: 'Aplicaciones web interactivas con diseño atractivo.', points: { Frontend: 2 } },
        },
    },
    {
        question: '2- ¿Cuál es tu entorno de trabajo favorito?',
        options: {
            a: { text: 'Terminales y scripts de automatización.', points: { Backend: 2 } },
            b: { text: 'Emuladores y entornos móviles.', points: { Mobile: 2 } },
            c: { text: 'Entornos visuales y herramientas de diseño.', points: { Frontend: 2 } },
            d: { text: 'Herramientas de análisis de datos y estadísticas.', points: { Data: 2 } },
        },
    },
    {
        question: '3- ¿Qué lenguaje de programación prefieres?',
        options: {
            a: { text: 'Python o R para análisis de datos.', points: { Data: 2 } },
            b: { text: 'JavaScript o TypeScript para desarrollo web.', points: { Frontend: 2 } },
            c: { text: 'Python o Java para desarrollo backend.', points: { Backend: 2 } },
            d: { text: 'Kotlin o Swift para desarrollo móvil.', points: { Mobile: 2 } },
        },
    },
    {
        question: '4- ¿Qué aspecto disfrutas más al resolver problemas?',
        options: {
            a: { text: 'Extraer y analizar patrones de grandes volúmenes de datos.', points: { Data: 2 } },
            b: { text: 'Crear interfaces intuitivas y responsivas.', points: { Frontend: 2 } },
            c: { text: 'Implementar funcionalidades en dispositivos móviles.', points: { Mobile: 2 } },
            d: { text: 'Optimizar la lógica y la arquitectura del servidor.', points: { Backend: 2 } },
        },
    },
    {
        question: '5- ¿Qué tecnología o framework te interesa aprender más?',
        options: {
            a: { text: 'Node.js, Django, o Spring.', points: { Backend: 2 } },
            b: { text: 'TensorFlow, Pandas, o Spark.', points: { Data: 2 } },
            c: { text: 'React, Angular, o Vue.', points: { Frontend: 2 } },
            d: { text: 'React Native, Flutter, o SwiftUI.', points: { Mobile: 2 } },
        },
    },
    {
        question: '6- ¿Cómo prefieres estructurar tu código?',
        options: {
            a: { text: 'Controladores de vistas y gestores de estado.', points: { Mobile: 2 } },
            b: { text: 'Scripts y pipelines de datos organizados.', points: { Data: 2 } },
            c: { text: 'Servicios y controladores bien definidos.', points: { Backend: 2 } },
            d: { text: 'Componentes modulares y reutilizables.', points: { Frontend: 2 } },
        },
    },
    {
        question: '7- ¿Qué herramienta te parece más útil en tu desarrollo diario?',
        options: {
            a: { text: 'Simuladores y herramientas de debugging móvil.', points: { Mobile: 2 } },
            b: { text: 'Inspectores de navegador y herramientas de diseño.', points: { Frontend: 2 } },
            c: { text: 'Postman y bases de datos.', points: { Backend: 2 } },
            d: { text: 'Jupyter Notebooks y herramientas de visualización de datos.', points: { Data: 2 } },
        },
    },
    {
        question: '8- ¿Qué te motiva más en tu carrera de desarrollo?',
        options: {
            a: { text: 'Llevar nuevas ideas al mercado rápidamente en dispositivos móviles.', points: { Mobile: 2 } },
            b: { text: 'Asegurar la estabilidad y seguridad del sistema.', points: { Backend: 2 } },
            c: { text: 'Descubrir conocimientos ocultos en los datos.', points: { Data: 2 } },
            d: { text: 'Crear interfaces que los usuarios amen usar.', points: { Frontend: 2 } },
        },
    },
    {
        question: '9- ¿Qué consideras más importante en un proyecto?',
        options: {
            a: { text: 'La portabilidad y rendimiento en diferentes dispositivos.', points: { Mobile: 2 } },
            b: { text: 'La eficiencia y escalabilidad del backend.', points: { Backend: 2 } },
            c: { text: 'La precisión y utilidad de los insights de datos.', points: { Data: 2 } },
            d: { text: 'La experiencia y estética del usuario.', points: { Frontend: 2 } },
        },
    },
    {
        question: '10- ¿En qué área te gustaría especializarte más?',
        options: {
            a: { text: 'Desarrollo de aplicaciones móviles innovadoras.', points: { Mobile: 2 } },
            b: { text: 'Ciencia de datos y aprendizaje automático.', points: { Data: 2 } },
            c: { text: 'Desarrollo de interfaces de usuario y experiencia.', points: { Frontend: 2 } },
            d: { text: 'Arquitectura de software y servicios web.', points: { Backend: 2 } },
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
                Object.keys(option.points).forEach((houseName) => {
                    house[houseName] += option.points[houseName];
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
console.log("\n¡Bienvenido a Hogwarts, la escuela de programación para magos y brujas del código!")
console.log("El sombrero seleccionador decidirá cuál es tu casa como programador.")
rl.question('\n¿Cuál es tu nombre? ', (name) => {
    studentName = name;
    askQuestion(); 
});