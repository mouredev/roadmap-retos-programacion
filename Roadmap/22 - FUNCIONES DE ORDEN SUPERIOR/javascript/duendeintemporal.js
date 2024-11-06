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