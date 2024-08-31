/********************************
**** OPERADORES ARITMETRICOS ****
*********************************/

// Suma 
console.log(`La suma de 4 + 4 es igual a: ${4+4}`);
// Resta 
console.log(`La resta de 10 - 7 es igual a: ${10-7}`);
// Multiplicacion 
console.log(`La multiplicacion de 3 * 9 es igual a: ${3 * 9}`);
// Division 
console.log(`La division de 25 / 5 es igual a: ${25 / 5}`);
// Resto 
console.log(`El resto de la division de 36 / 4 es igual a: ${36 % 4}`);
// Incremento 
let num = 4;
console.log(`El incremento de 4 es: ${++num}`);
// Decremento
let numII = 8;
console.log(`El decremento de 8 es: ${--numII}`);

/**********************************
**** OPERADORES de comparación ****
***********************************/

// Igualdad 
console.log(`El numero 25 es igual a 15 ? ${25==15}`);
// Desigualdad 
console.log(`El numero 25 no es igual a 15 ? ${25!=15}`);
// Mayor que  
console.log(`El numero 25 es mayor que 15 ? ${25>15}`);
// Mayor o Igual que  
console.log(`El numero 25 es mayor o Igual que 15 ? ${25>=15}`);
// Menor que  
console.log(`El numero 25 es menor que 25 ? ${25<15}`);
// Menor o Igual que  
console.log(`El numero 25 es menor o igual que 15 ? ${25<=15}`);

/*******************************
****** OPERADORES LOGICOS ******
********************************/

// AND 
console.log(`true && false : ${true && false}`);
console.log(`true && true : ${true && true}`),
console.log(`false && true : ${false && true}`);
console.log(`false && false : ${false && false}`);
// OR 
console.log(`true || false : ${true || false}`);
console.log(`true || true : ${true || true}`);
console.log(`false || true : ${false || true}`);
console.log(`false || false : ${false || false}`);
// NOT 
console.log(`!false : ${!false}`);
console.log(`!true : ${!true}`);

/*************************************
****** OPERADORES de ASIGNACION ******
**************************************/

let numIII = 10;

// Asignacion de sumna
console.log(`Le sumo 1 a mi numIII: ${numIII += 1}`);
// Asignacion de resto
console.log(`Ahora le resto 2 a mi numIII: ${numIII -= 2}`);
// Asignacion de multiplicacion
console.log(`Seguido lo multiplico * 4 a mi numIII: ${numIII *= 4}`);
// Asignacion de division
console.log(`Tambien lo divido por 2 a mi numIII: ${numIII /= 2}`);
// Asignacion de resto
console.log(`Por ultimo busco el resto de mi numIII por 4: ${numIII %= 4}`);

/*************************************
****** OPERADORES de IDENTIDAD *******
**************************************/

let a = "4";
let b = 4;

console.log(`La varibale a es igual a la variable b: ${a===b}`);
console.log(`La variable a es distinta a la variable b: ${a !==b}`);

/***************************************
****** OPERADORES de PERTENENCIA *******
****************************************/

console.log(`El numero 8 esta en [0,1,2,3,4,5,6,7,8,9] : ${8 in [0,1,2,3,4,5,6,7,8,9]}`);
console.log(`El numero 10 esta en [0,1,2,3,4,5,6,7,8,9] : ${10 in [0,1,2,3,4,5,6,7,8,9]}`);

/*******************************
****** OPERADORES de BIT *******
********************************/

let c = 8;
let d = 12;

console.log(`AND : 8 & 12 = ${8 & 12}`)
console.log(`OR : 8 | 12 = ${8 | 12}`)
console.log(`XOR : 8 ^ 12 = ${8 ^ 12}`)
console.log(`NOT : ~8 = ${~8}`)
console.log(`Desplazamiento a la derecha  : 8 >> 12 = ${8 >> 12}`)
console.log(`Desplazamineto a la izquierda : 8 << 12 = ${8 << 12}`)

/***********************************
****** ESTRUCTURA DE CONTROL *******
***********************************/

/*---------------------------------
--------------- IF ----------------
----------------------------------*/

let clima = "lluvia";

if (clima == "sol"){
    console.log("El clima de hoy es soleado")
} else if (clima == "lluvia"){
    console.log("El clima para hoy es de lluvia")
}


/*-------------------------------------
--------------- SWITCH ----------------
-------------------------------------*/

let estacion = "primavera";

switch(estacion){
    case "otoño": 
        console.log("Estamos en Otoño todo parece mas marron");
        break;
    case "invierno":
        console.log("Llego el invierno el azul nos predomina");
        break;
    case "primavera" :
        console.log("Momento de floreces con el color amarillo");
        break;
    case "verano":
        console.log("El verano esta aqui y con él el naranja se apodera del cielo");
        break;
    default:
        console.log("No conozco esa estacion, creo que esta un poco gris");
        break;
}

/*-------------------------------------
--------------- FOR -------------------
-------------------------------------*/

let array = [0,1,2,3,4,5,6,7,8,9];

for (let index = 0; index < array.length; index++) {
    const element = array[index];
    console.log (`Elemento = ${element}`);
};


/*-------------------------------------
--------------- WHILE -----------------
-------------------------------------*/

let cant = 0;

while (cant < 3) {
    console.log("La cantidad es", cant)
    cant++;
}


/*-------------------------------------
--------------- DO WHILE --------------
-------------------------------------*/

let cont = 0

do {
    console.log("La cantidad es", cont)
    cont++;
} while (cont < 3);

/*-------------------------------------
--------------- TRY CATCH -------------
-------------------------------------*/

try {
    let resultado = 10 / 0;
    console.log("El resultado es", resultado);
} catch (error) {
    console.log("Ocurrió un error:", error.message);
} finally {
    console.log("Esto se ejecuta siempre, haya o no error");
}

// ------------- EJERCICIO EXTRA ---------------- //

for (let i = 10; i <= 55; i++) {
    if ((i % 2 == 0) && (i !== 16) &&(i % 3 !== 0)) {
        console.log(i)
    }
}