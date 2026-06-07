// -------tipos de operadores-------

// Operadores de asignación

let n1 = 32; //asigna el valor de su operando derecho a su operando izquierdo
let n2 = 35;//asigna el valor de su operando derecho a su operando izquierdo


console.log(`Asignación de adición: n1 += 5 ${n1 += 5}`); // n1 = n1 + 5
console.log(`Asignación de resta: n1 -= 5 = ${n1 -= 5}`);// n1 = n1 - 5
console.log(`Asignación de multiplicación: n1 *= 5 = ${n1 *= 5}`);// n1 = n1 * 5
console.log(`Asignación de división: n1 /= 5 = ${n1 /= 5}`);// n1 = n1 / 5
console.log(`Asignación de residuo: n1 %= 5 = ${n1 %= 5}`);// n1 = n1 % 5
console.log(`Asignación de exponenciación: n1 **= 5 = ${n1 **= 5}`);// n1 = n1 ** 5


// Operadores aritméticos

console.log(`Adición con signo + : n1 + n2: ${n1 + n2}`)
console.log(`Resta con signo - : n1 - n2: ${n1 - n2}`)
console.log(`Multiplicación con signo * : n1 * n2: ${n1 * n2}`)
console.log(`División con signo / : n1 / n2: ${n1 / n2}`)
console.log(`Residuo con signo % : n1 % n2: ${n1 % n2}`)
console.log(`Exponenciación con signo ** : n1 ** n2: ${n1 ** n2}`)
console.log(`Incremento con signo ++ : n1++${n1++}`);
console.log(`Decremento con signo -- : n1--${n1--}`);

//Operadores de comparación

// Suponiendo n1 = 32 y n2 = 35
console.log(`Igualdad débil: ${n1 == "32"}: true`);        //ignora tipo
console.log(`Igualdad estricta: ${n1 === "32"}: false`);   //importa el tipo
console.log(`Desigualdad débil: ${n1 != "32"}: false`);    //NO son distintos
console.log(`Desigualdad estricta: ${n1 !== "32"}: true`); //SÍ son distintos
console.log(`Mayor que: ${n1 > n2} : false `);
console.log(`Menor que: ${n1 < n2} : true `);
console.log(`Mayor o igual que: ${n1 >= n2} : false `);
console.log(`Menor o igual que: ${n1 <= n2} : true `);

// Operadores lógicos

let logeado = true;

console.log(`n1 y n2 : AND , signo && ${n1 && n2}`);
console.log(`n1 ó n2 : OR , signo || ${n1 || n2}`);
console.log(`invertir valor: NOT, signo ! ${!logeado}: logeado = false`)


//Operadores de cadena

console.log("cristian " + "orellana") //el espacio debe introducirse dentro de las cadenas

//Operador condicional

// Operador condicional ternario

let edad = 15;
let status = edad >= 18 ? "Adulto" : "Menor";

// Operadores relacionales
let colores = ['verde', 'amarillo', 'rojo'];
console.log(0 in colores) //true
console.log(1 in colores) //true
console.log('amarillo' in colores) //false, se debe especificar el número de índice.

//en objeto
let deportes = {
    disciplina: 'Judo',
    nacionalidad: 'Japón'
}

console.log('disciplina' in deportes) // devuelve true

//-------Estructuras de control-------

//-------condicionales

let edadPersona = 70;

//if-else

if (edadPersona >= 18) {
    console.log('Acceso permitido')
} else {
    console.log('Acceso denegado')
}


//else if

if (edadPersona < 18) {
    console.log('Eres menor de edad');
} else if (edadPersona >= 18 && edadPersona < 65) {
    console.log('Eres un adulto joven')
} else if (edadPersona >= 65 && edadPersona < 85) {
    console.log('Eres un adulto mayor')
} else {
    console.log('Eres leyenda')
}

//switch

let juegoElegido = prompt(`
    Elije un juego presionando los siguientes números:
    1.- Mario Bross.
    2.- CTR.
    3.- Spiderman.

    `)

switch (juegoElegido) {
    case "1":
        console.log('Elegiste el juego Mario Bross')
        break;

    case "2":
        console.log('Elegiste el juego Crash team racing')
        break;

    case "3":
        console.log('Elegiste el juego Spider-man')
        break;

    default:
        console.log('Elige un número correcto.')
        break;
}

//-------iterativas

//for -> hasta que una condición específica se evalúa como falsa.

for (let i = 0; i < 10; i++) {
    console.log(i);
}

//forEach -> para arrays

let array = [1, 2, 3, 4, 5, 6]

array.forEach(element => {
    console.log(element)
});

//while -> ejecuta sus instrucciones mientras una condición específica
//se evalúe como verdadera "true"

let x = 0;
let y = 0;

while (x < 4) {
    x++
    y += x;
    console.log(`x: ${x} , y: ${y}`)
}

// do...while -> se repite hasta que una condición específica se evalúe
//como false.

let i = 0;

do {
    i++;
    console.log(i);

} while (i < 5);


//-------excepciones -> error en tiempo de ejecución que interrumpe la ejecución normal del programa.
//-------suele ocurrir con -> variable no difinida, llamada incorrecta a una función, entrada no válida,
//-------una operación falla inesperadamente.
// puedes lanzar excepciones usando la instrucción throw y manejarlas
//usando las declaraciones try...catch

try {
    const json = JSON.parse('{"ok": "true"}');
    console.log(json.ok)
} finally {
    console.log('Acción terminada')
};

try {
    JSON.parse("{esto va a dar un error}");

} catch (error) {
    console.log("Error de parseado:", error.message)
}

//throw -> fallos intencionalmente
// Falta el campo obligatorio.    |	throw new Error("Email is required")
//Tipo de datos incorrecto	      |  throw new TypeError("Email must be a string")
//Formato no válido               |	throw new TypeError("Email must contain '@'")
//Valor fuera del rango permitido |	throw new RangeError("Password must be at least 8 characters long")

function validarEdad(anios) {
    if (typeof anios !== "number") {
        throw new TypeError("Se espera un número para ingresar");
    }
    return anios;
}


//opcional

for (let i = 10; i <= 55; i++) {
    if (i % 2 === 0 && i !== 16 && i % 3 !== 0) {
        console.log(i);
    }
};