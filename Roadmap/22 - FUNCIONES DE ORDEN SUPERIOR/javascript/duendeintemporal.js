//#22 - FUNCIONES DE ORDER SUPERIOR 
/* 
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales). 
 * */

//Reference Bibliografy:
//Eloquent Javascript A Modern Introduction to Programming by Marijn Haverbeke (z-lib.org)
//GPT


window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #22.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #22. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #22'); 
});



/* Functions that operate on other functions, either by taking them as arguments
or by returning them, are called higher-order functions. 
The term comes from mathematics, where the distinction between functions and other values is taken more seriously.
Higher-order functions allow us to abstract over actions, not just values. */


let log = console.log;

//For example, we can have functions that create new functions.

const powder = (n) => {
    return (m) => {
        if (n === 0) return 1; 
        return m * powder(n - 1)(m);
    };
}; 

let powder2 = powder(2);
log(powder2(10)) // 100

//And we can have functions that change other functions.

const applyToArray = (func)=>{
    return (...arr)=>  func(...arr);
}

const totalAmount = (...arg)=>{
    return arg.reduce((total, n)=> total + n, 0);
}

let sales = [123, 45, 67, 865, 76, 54, 3254, 23];

log(applyToArray(totalAmount)(...sales)); // 4507

//We can even write functions that provide new types of control flow.

function unless(test, then) {
    if (!test) then();
}

const isOddNum = (n)=> n % 2 !== 0; 

const addOddNums = (n)=> {
    let total = 0;
    do{
        unless(!isOddNum(n), ()=> total += n);
        n--;
    }while(n > 0)  
    return total;
}

log(addOddNums(100)); // 2500

//There are some built-in array methods, forEach, map, reduce, some... that provide something like a for/of loop as a higher-order function.

//EXTRA DIFICULTY EXERCISE

// Student class definition
class Student {
    constructor(name, birthday, calification) {
        this.name = name;
        this.birthday = new Date(birthday); 
        this.calification = calification; 
    }

    getName() {
        return this.name; 
    }

    getBirthday() {
        return this.birthday; 
    }

    getCalification() {
        return this.calification;
    }

    setName(name) {
        this.name = name; 
    }

    setBirthday(birthday) {
        this.birthday = new Date(birthday);
    }

    setCalification(calification) {
        this.calification = calification; 
    }
}

// List of students
let students = [
    new Student('Juan Rulfo', '1986-06-07', 7),
    new Student('Moure Dev', '1982-03-08', 8.5),
    new Student('Calvin Maker', '2000-04-02', 9.8),
    new Student('Adela Jimenez', '1976-01-09', 7.9),
    new Student('Crist Renegate', '2001-07-09', 5),
    new Student('Gautama Buda', '0623-05-23', 9),
    new Student('Niko Zen', '1983-08-08', 10)
];

// Function to get a list of students with their average grades
const studentsAverageList = (arr) => {
    return arr.map(student => ({
        name: student.getName(), 
        average: student.getCalification() 
    })).sort((a, b) => b.average - a.average);
};

// Function to get a list of students with grades of 9 or higher
const higherThan9Students = (arr) => {
    return arr.filter(student => student.getCalification() >= 9) 
              .map(student => student.getName()); 
};

// Function to sort students by their birth date
const sortStudentsByBirthday = (arr) => {
    return arr.slice().sort((a, b) => a.getBirthday() - b.getBirthday()) 
              .map(student => student.getName()); 
};

// Function to find the highest grade among all students
const highestCalification = (arr) => {
    return Math.max(...arr.map(student => student.getCalification())); 
};

// Execute the functions and store the results
let averageList = studentsAverageList(students); 
let bestStudents = higherThan9Students(students);
let sortedStudents = sortStudentsByBirthday(students); 
let highestGrade = highestCalification(students); 

// Display the results in the console
log("Average grades:", averageList); /*
Average grades:
Array(7) [ {…}, {…}, {…}, {…}, {…}, {…}, {…} ]
0: Object { name: "Niko Zen", average: 10 }
1: Object { name: "Calvin Maker", average: 9.8 }
2: Object { name: "Gautama Buda", average: 9 }
3: Object { name: "Moure Dev", average: 8.5 }
4: Object { name: "Adela Jimenez", average: 7.9 }
5: Object { name: "Juan Rulfo", average: 7 }
6: Object { name: "Crist Renegate", average: 5 }
 */
log("Best students (9 or higher):", bestStudents); // Best students (9 or higher): ['Calvin Maker', 'Gautama Buda', 'Niko Zen']
log("Students sorted by birth date:", sortedStudents); // Students sorted by birth date: (7) ['Gautama Buda', 'Adela Jimenez', 'Moure Dev', 'Niko Zen', 'Juan Rulfo', 'Calvin Maker', 'Crist Renegate']
log("Highest grade:", highestGrade); // Highest grade: 10
