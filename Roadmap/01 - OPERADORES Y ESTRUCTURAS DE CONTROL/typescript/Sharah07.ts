//Tipos de operadores en TypeScript

//OPERADORES ARITMÉTICOS
 
let n1:number = 4;
let n2:number = 6;

//Suma
console.log( n1 + "+" + n2 + "=" + (n1+n2)); // 4+6=10
//Resta
console.log( n1 + "-" + n2 + "=" + (n1-n2)); // 4-6=-2
//Multiplicación
console.log(n1 + "*" + n2 + "=" + (n1*n2)); // 4*6=24
//División
console.log(n1 + "/" + n2 + "=" + (n1/n2)); // 4/6=0.6666666666666666
//Módulo
console.log(n1 + "%" + n2 + "=" + (n1%n2)); // 4%6=4

//OPERADORES DE INCREMENTO Y DECREMENTO

//Incremento
console.log(n1++);
//Decremento
console.log(n1--);

//OPERADORES DE ASIGNACIÓN
/**
 * Asignación
 */                                        
n2 = 8;
console.log("Asignación: " + n2); // Asignación: 8
/** 
 * Asignación de suma
*/
let n3:number = 3;
n3 += n2;
console.log("Asignación de suma: " + n3); // Asignación de suma: 11
/** 
 * Asignación de resta
*/
n3 -= n1;
console.log("Asignación de resta: " + n3); // Asignación de resta: 7
/**
 * Asignación de multiplicación
 */
n3 *= n1;
console.log("Asignación de multiplicación" + n3); // Asignación de multiplicación: 28
/** 
 * Asignación de división
 */
n3 /= n2;
console.log("Asignación de división" + n3); // Asignación de división: 3.5


//OPERADORES DE COMPARACIÓN
/**
 * Igualdad
 */
console.log( n1 == n2 ); // false
/**
 * Igualdad estricta
 */
console.log(n1 === n2); // false
/**
 * Desigualdad
 */
console.log(n1 != n2); // true
/**
 * Desigualdad estricta
 */
console.log(n1 !== n2); // true
/**
 * Mayor que
 */
console.log(n1 > n2); // false
/**
 * Mayor o igual que
 */
console.log(n1 >= n2);  //false
/**
 * Menor que
 */
console.log(n1 < n2); // true
/**
 * Menor o igual que
 */
console.log(n1 <= n2); // true

//OPERADORES LÓGICOS
n1 = 2;
n2 = 3;
n3 = 3;
/**
 *   && - AND
 */
console.log(n1 == n2 && n2 ==n3); // false
/**
 *   || - OR
 */
console.log(n1 == n2 || n2 == n3); // true
/**
 *   ! - NOT
 */
console.log(!(n1 == n2)); //true

// OPERADORES BITS A BITS
/**
 *  AND - &
 */
console.log(n1 & n2); //2
/**
 * 
 *  OR - |
 */
console.log(n1 | n2); //3
/**
 * 
 *  XOR - ^
 */
console.log(n1 ^ n2); //1
/**
 * 
 * NOT - ~ 
 */
console.log(~(n1 & n2)); //-3
/**
 * 
 * Desplazamiento a la izquierda
 */
console.log(n1 << 1); //4
/**
 * 
 * Desplazamiento a la derecha
 */
console.log(n1 >> 1); //1



// ESTRUCTURAS DE CONTROL
n1 = 9;
n2 = 3;
n3 = 3;

//Estructuras de control condicionales
/**
 * if: ejecuta el código si la condición es true.
 */ 
if(n2 == n3){
    console.log("true: la condición es verdadera"); // true: la condición es verdadera
}
/**
 * if else: si la condición es true ejecuta el primer código,
 * de lo contrario ejecuta el segundo.
 */
if(n2 == n1){
    console.log("true: la condición es verdadera");
}else{
    console.log("false: la condición es falsa"); // false: la condición es falsa
}
/**
 * else if: evalúa varias condiciones y ejecuta el código de la
 * que sea true, si ninguna es verdadera ejecuta el bloque de código de else.
 */
const edad:number= 28;

if(edad < 18){
    console.log("Eres menor de edad.");
}else if(edad >= 18 && edad < 60){
    console.log("Eres mayor de edad"); // Eres mayor de edad
}else{
    console.log("Eres adulto mayor.");
}
/**
 * switch: compara la expresion con varios valores(casos) 
 * y ejecuta el código del caso con el que coincida.
 */
const nota:number= 4;

switch(nota){
    case 1:
        console.log("muy malo.");
        break;
    case 2:
        console.log("malo");
        break;
    case 3:
        console.log("regular");
        break;
    case 4:
        console.log("bien"); // bien
        break;
    case 5:
        console.log("excelente");
        break;
    default:
        console.log("Nota no valida");
}

// Estructuras de control re repetición (Bucles)
/**
 * for: repiten un bloque de código una cantidad específica de veces.
 */
for(let i = 0; i < 6; i++){
    console.log("vuelta #", i); //vuelta # 0, vuelta # 1, vuelta # 2, vuelta # 3, vuelta # 4, vuelta # 5
}
/**
 * for of: recorre los valores de una lista.
 */
const dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]; 
for(const dia of dias){
    console.log(dia); //lunes, martes, miercoles, jueves, viernes
}
/**
 * for in: recorre las claves o índices del objeto.
 */
const nombres = ["Seira", "Juan", "Stiven", "Luisa"];
for(const nombre in nombres){
    console.log(nombre); //0, 1, 2, 3
}
/**
 * while: ejecuta un bloque de código mientras la condición sea verdadera,
 * si la condición desde el inicio el falsa, no se ejecuta nada.
 */
let i= 1;
while(i < 6){
    console.log(i); //1, 2, 3, 4, 5
    i++;
} 
/**
 * do while: ejecuta el bloque de código al menos una vez, sin importar si la condición
 * es false o true, debido a que la condición se evalúa al final.
 */
let no = 8;
do{
    console.log(no); //8
    no++
}while(no < 5);

// Estructuras de control de manejo de errores
/**
 *  try catch
 */
function validarEdad(edad:number) {
    try{    
        if(edad < 0){
            throw new Error("Cómo vas a tener de edad un número negativo!?, Sopenco!!");
        }else if(edad == 0){
            throw new Error("No se puede 0");
        }
        return console.log("edad: ", edad);
    }catch (error){
        console.log("Error: ", error.message);
    }    
}

validarEdad(-6); //Error:  Cómo vas a tener de edad un número negativo!?, Sopenco!!
validarEdad(0); //Error:  No se puede 0
validarEdad(21); //edad:  21

//Estructuras de control especiales.
/**
 * break
 */
let numeros = [2, 6, 4, 9, 8, 10];

for(let numero of numeros){
    if(numero % 2 != 0){
        console.log("Primer número impar: ", numero); //Primer número impar: 9
        break; 
    }
}
/**
 * continue
 */

for(i=0; i < 10; i++){
    if(i % 2 != 0){
        continue;
    }
    console.log(i); //0, 2, 4, 6, 8
}
/**
 * return: devuelve un valor desde una función 
 * al punto donde se invoca y termina la función.
 */
function numero(a:number){
    if(a < 0){
        return console.log("Número negativo");
    }
    console.log("Número positivo");
} 

numero(8);
numero(-4);


// DIFICULTAD EXTRA

for(i= 10; i >= 10 && i <= 55; i++){
    if(i % 2 != 0 || i % 3 == 0 || i == 16){
        continue;
    }
    console.log(i); // 10, 14, 20, 22, 26, 28, 32, 34, 38, 40, 44, 46, 50, 52
}