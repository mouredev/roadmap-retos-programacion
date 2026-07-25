// Autor: Héctor Adán
// GitHub: https://github.com/hectorio23

const readline = require('readline-sync');
// npm install readline-sync

// Casas
const houses = ["Frontend", "Backend", "Mobile", "Data"];

// Preguntas y asignación de puntos
const questions = [
    { question: "¿Prefieres trabajar en interfaces visuales?", scores: [3, 1, 2, 0] },
    { question: "¿Te gusta optimizar el rendimiento del servidor?", scores: [0, 3, 1, 1] },
    { question: "¿Te interesa crear aplicaciones móviles?", scores: [1, 0, 3, 1] },
    { question: "¿Te apasiona analizar grandes conjuntos de datos?", scores: [0, 1, 0, 3] },
    // 6 preguntas más...
];

function askQuestions() {
    let scores = [0, 0, 0, 0];  // Puntos de cada casa
    for (const q of questions) {
        console.log(q.question);
        const answer = readline.questionInt("Responde 1, 2, 3 o 4: ") - 1;
        scores = scores.map((score, i) => score + q.scores[answer]);
    }
    return scores;
}

function sortingHat() {
    const name = readline.question("¿Cuál es tu nombre? ");
    const scores = askQuestions();
    const maxScore = Math.max(...scores);
    
    const candidates = houses.filter((_, i) => scores[i] === maxScore);
    
    // Si hay empate, selecciona aleatoriamente
    if (candidates.length > 1) {
        console.log(`${name}, la decisión ha sido complicada...`);
        const assignedHouse = candidates[Math.floor(Math.random() * candidates.length)];
        console.log(`${name}, has sido asignado a ${assignedHouse}.`);
    } else {
        console.log(`${name}, has sido asignado a ${candidates[0]}.`);
    }
}

// Ejecutar el sombrero seleccionador
sortingHat();
