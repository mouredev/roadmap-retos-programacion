/** #22 - JavaScript ->Jesus Antonio Escamilla */

/**
 * Hemos visto cómo crear funciones que toman cadenas y números como argumentos.
 * A veces, necesitaremos crear funciones que tomen otras funciones como argumentos o las utilicen como valores de retorno.
 * Éstas se denominan funciones de orden superior.
 * Una función de orden mayor (HOF -> Higher-Order Function) se denomina a (1) cualquier función que reciba una función como parámetro o (2) cualquier función que retorne otra función.
 * 
*/

//---EJERCIÓ---
// Aquí se puede ver como funciona una HOFs en un mensaje donde retorna el mensaje
const higherOrderFunction = (callback) => {
    const string = '¡Las HOFs son realmente geniales!'
    callback(string);
}

// Aquí se muestra el ejemplo
higherOrderFunction(console.log);


// Creo un array de nombres para poder usarlo con los HOFs
const characters = [
    {
        firstName: 'Tulio',
        lastName: 'Triviño',
    },
    {
        firstName: 'Policarpo',
        lastName: 'Avendaño',
    },
    {
        firstName: 'Nicasio',
        lastName: 'Fallido',
    }
];

// Se creo la HOF usando MAP para encontrarlo
const names = characters.map(function(character) {
    return character.firstName + " " + character.lastName;
});

// Aquí se muestra el ejemplo
console.log(names);


// Creo un array de números para poder usarlo con los HOFs
const numbers = [1, 2, 3, 4];

// Creo la HOF se usa FILTER para hacer un filtro para encontrarlo
const even = numbers.filter(num => num % 2 === 0);

// Aquí se muestra el ejemplo
console.log(even);


// Creo la HOF REDUCE para hacer un 
const sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum);

// Retorna una función de HOF
function createMultiplier(multiplicar) {
    return function(num) {
        return num * multiplicar;
    };
}

// Las constantes para usar
const doble = createMultiplier(2);

// Los ejemplos de retorno de función
console.log(doble(4));
console.log(createMultiplier(3)(4));



/**-----DIFICULTAD EXTRA-----*/

//  Listado de Estudiantes
const students = [
    {"name": "Jesus", "birthDate": "22-12-1999", "grades": [7, 8.5, 8, 10]},
    {"name": "Fatima", "birthDate": "02-04-2001", "grades": [8, 7.2, 6, 9]},
    {"name": "Antonio", "birthDate": "15-11-1990", "grades": [5, 9.8, 10, 5]},
    {"name": "Lizette", "birthDate": "28-07-2002", "grades": [9.1, 9.6, 8.3, 10]},
];


//  Promedio de los Estudiantes en forma de lista
const promedios = students.map(estudiantes => {
    let sumar = estudiantes.grades.reduce((a, b) => a + b, 0);
    let promedio = sumar / estudiantes.grades.length;
    return {name: estudiantes.name, promedio: promedio};
});
//  Se muestra el Promedio
console.log('Los Promedio de los estudiantes', promedios);


//  Los Mejores Estudiantes en forma de lista
const mejoresEstudiantes = promedios.filter(estudiantes => estudiantes.promedio >= 9).map(estudiantes => estudiantes.name);
//  Se muestra los Mejores Estudiantes
console.log('Los Mejores Estudiantes',mejoresEstudiantes);


//  El Estudiante mas Joven en forma lista
const estudiantesOrdenados = students.slice().sort((a, b) => {
    const [dayA, monthA, yearA] = a.birthDate.split('-').map(Number);
    const [dayB, monthB, yearB] = b.birthDate.split('-').map(Number);
return new Date(yearB, monthB - 1, dayB) - new Date(yearA, monthA - 1, dayA);
});
//  Se muestra los Estudiantes en orden del mas Joven Primero
console.log('Los ordenados por fecha de Nacimiento (Por el mas Joven primero)',estudiantesOrdenados);


//  La Mayor Calificación de todos los Estudiantes
const todasCali = students.flatMap(estudiantes => estudiantes.grades);
const masAltaGrade = Math.max(...todasCali);
//  Se muestra la Calificación más alta
console.log(masAltaGrade);


/**-----DIFICULTAD EXTRA-----*/