const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function printQuiz() {
    const preguntas = [
        {
            pregunta: "¿Qué es lo que más disfrutas al programar?",
            opciones: [
                { respuesta: "Diseñar interfaces atractivas", casa: "Frontend" },
                { respuesta: "Optimizar el rendimiento del servidor", casa: "Backend" },
                { respuesta: "Crear aplicaciones móviles útiles", casa: "Mobile" },
                { respuesta: "Analizar grandes conjuntos de datos", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Qué tipo de proyecto te atrae más?",
            opciones: [
                { respuesta: "Aplicaciones web con mucho estilo", casa: "Frontend" },
                { respuesta: "Sistemas que manejen grandes volúmenes de datos", casa: "Backend" },
                { respuesta: "Aplicaciones para teléfonos inteligentes", casa: "Mobile" },
                { respuesta: "Dashboards para visualizar información", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Qué herramienta te resulta más interesante?",
            opciones: [
                { respuesta: "HTML, CSS y JavaScript", casa: "Frontend" },
                { respuesta: "Node.js o Python", casa: "Backend" },
                { respuesta: "React Native o Swift", casa: "Mobile" },
                { respuesta: "SQL o Python con Pandas", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Cuál es tu mayor fortaleza como programador?",
            opciones: [
                { respuesta: "Crear interfaces amigables", casa: "Frontend" },
                { respuesta: "Solucionar problemas complejos en el servidor", casa: "Backend" },
                { respuesta: "Desarrollar apps funcionales", casa: "Mobile" },
                { respuesta: "Encontrar patrones en los datos", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Qué prefieres en un equipo de desarrollo?",
            opciones: [
                { respuesta: "Ser quien diseña el look y feel", casa: "Frontend" },
                { respuesta: "Ser quien gestiona la arquitectura de la aplicación", casa: "Backend" },
                { respuesta: "Ser quien se encarga de la versión móvil", casa: "Mobile" },
                { respuesta: "Ser quien analiza el rendimiento del sistema", casa: "Data" }
            ]
        },
        {
            pregunta: "¿En qué te enfocas más cuando trabajas en un proyecto?",
            opciones: [
                { respuesta: "En el diseño visual y la experiencia de usuario", casa: "Frontend" },
                { respuesta: "En la estabilidad y escalabilidad del sistema", casa: "Backend" },
                { respuesta: "En hacer que la app funcione en dispositivos móviles", casa: "Mobile" },
                { respuesta: "En el análisis y visualización de los datos", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Cuál es tu mayor motivación como desarrollador?",
            opciones: [
                { respuesta: "Crear experiencias de usuario memorables", casa: "Frontend" },
                { respuesta: "Resolver problemas complejos con eficiencia", casa: "Backend" },
                { respuesta: "Desarrollar aplicaciones que la gente use todos los días", casa: "Mobile" },
                { respuesta: "Descubrir patrones ocultos en los datos", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Qué aspecto prefieres de un nuevo proyecto?",
            opciones: [
                { respuesta: "Hacer que se vea genial y sea fácil de usar", casa: "Frontend" },
                { respuesta: "Asegurarme de que el servidor funcione sin problemas", casa: "Backend" },
                { respuesta: "Hacer que funcione bien en dispositivos móviles", casa: "Mobile" },
                { respuesta: "Organizar y visualizar los datos de forma eficiente", casa: "Data" }
            ]
        },
        {
            pregunta: "¿Qué tecnología te emociona más aprender?",
            opciones: [
                { respuesta: "Frameworks de JavaScript como React o Angular", casa: "Frontend" },
                { respuesta: "Microservicios o arquitectura en la nube", casa: "Backend" },
                { respuesta: "Desarrollo de aplicaciones móviles", casa: "Mobile" },
                { respuesta: "Big Data o inteligencia artificial", casa: "Data" }
            ]
        },
        {
            pregunta: "Si pudieras elegir un área de especialización, ¿cuál sería?",
            opciones: [
                { respuesta: "Interfaz y experiencia de usuario", casa: "Frontend" },
                { respuesta: "Desarrollo y mantenimiento del servidor", casa: "Backend" },
                { respuesta: "Aplicaciones móviles", casa: "Mobile" },
                { respuesta: "Ciencia de datos y análisis", casa: "Data" }
            ]
        }
    ];

    const answers = [];

    const askQuestion = (index) => {
        if (index < preguntas.length) {
            console.log(preguntas[index].pregunta);
            preguntas[index].opciones.forEach((opcion, idx) => {
                console.log(`${String.fromCharCode(97 + idx)}: ${opcion.respuesta}`);
            });
            rl.question('Selecciona una opción: ', (answer) => {
                answers.push(answer);
                askQuestion(index + 1);
            });
        } else {
            rl.close();
            const house = selectHouse(answers);
            console.log(`La casa seleccionada es: ${house}`);
        }
    };

    askQuestion(0);
}

function selectHouse(answers) {
    const countFront = answers.filter((a) => a === 'a').length;
    const countBackend = answers.filter((a) => a === 'b').length;
    const countMobile = answers.filter((a) => a === 'c').length;
    const countData = answers.filter((a) => a === 'd').length;

    const casas = { Frontend: countFront, Backend: countBackend, Mobile: countMobile, Data: countData };
    const maxCount = Math.max(...Object.values(casas));

    const posiblesCasas = Object.keys(casas).filter(casa => casas[casa] === maxCount);

    if (posiblesCasas.length > 1) {
        console.log("¡Ha sido una decisión complicada!");
        return posiblesCasas[Math.floor(Math.random() * posiblesCasas.length)];
    }

    return posiblesCasas[0];
}

function main() {
    rl.question('Introduce tu nombre: ', (name) => {
        printQuiz();
    });
}

main();
