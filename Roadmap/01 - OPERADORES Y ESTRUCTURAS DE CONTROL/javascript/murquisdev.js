// https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_operators

/* 
    JS tiene tres tipos de operadores, unarios, binarios y condicional (ternario)
    Unario requiere un solo operando: operador operando (u operando operador) --> x++ "o" ++x
    Binario requerie dos operandos: operando1 operador operando2 --> 3 + 4, 5 * 3
    
*/

// Los principales operadores que tiene JS son los de comparación, aritméticos, lógicos, asignación y de cadenas, aunque también
// tiene de bit a bit.

// ASIGNACIÓN
// Le da el valor del operando derecho al operando izquierdo
/*
    ASIGNACIÓN ( = )
    x = 3
    y = 5
    x = y // x tiene el valor 5

    Se puede añadir una operación matemática antes de asignar el valor
    x += y // 8
    x *= y // 15
*/

// COMPARACIÓN --> Devuelve TRUE o FALSE
let var1 = 3
let var2 = 4
/*
    JS tiene dos operadores diferentes para comparar la igualdad (y la desigualdad) con unas características particulares de
    este lenguaje.

    IGUAL ( == ): Devuelve TRUE si los operandos son iguales
    Con el comparador igual JS intenta convertir el tipo de dato primitivo si no son iguales para hacer la comparación.

    3 == var1 // TRUE var1 tiene el valor NUMÉRICO 3 y lo compara con el número 3
    "3" == var1 // TRUE var1 tiene el valor NUMÉRICO 3 y la cadena de texto la convierte al número 3
    3 == '3' // TRUE compara el número 3 con la cadena de texto '3' que la convierte para la comparación

    IGUAL ESTRICTO ( === ): Devuelve TRUE si los operandos son iguales y del mismo tipo.

    3 === var1 // TRUE var1 tiene el valor NUMÉRICO 3 y se está comparando con el NÚMERO 3
    "3" === var1 // FALSE var1 es de tipo númerico y "3" es un STRING, no se pueden comparar.
    
    DESIGUAL ( != ): Devuelve TRUE cuando los operandos no son iguales.

    5 != var1 // TRUE
    var2 != "3" // TRUE

    DESIGUAL ESTRICTO ( !== ): Devuelve TRUE sin los operandos son de diferente tipo y si son del mismo tipo, sino no son iguales.
    
    var2 !== 5 // TRUE
    var2 !== 4 // FALSE
    var2 !=="5" //TRUE

    Mayor que ( > ), menor que ( < ), mayor o igual que ( >= ) y menor o igual que ( <= ): Devuelve TRUE cuando se cumple la condición
    "5" > var2 // TRUE 5 es mayor que 4
    4 >= var2 // TRUE 4 es igual a 4
    3 > var2 // FALSE
    3 < var2 // TRUE
 */

// ARITMÉTICOS (operaciones matemáticas) 
// Como característica de JS, la división entre cero produce infinito.
/*
    + suma // 3 + 5
    - resta // 5 - 3
    * multiplicación // 5 * 10
    / división // 10 / 2
    % módulo (devuelve el resto de una división) // 10 % 2 --> 0
    ** potencia o exponente // 3**2 --> 9
    ++ incremento // 4++ --> 5
    -- decremento // 4-- --> 3
*/

// LÓGICOS
// Son los operadores que se utilizan con valores booleanos (TRUE o FALSE), y devuelven el resultado de la comparación lógica, aunque
// si se utilizan sin valores boleanos pueden devolver valores no booleanos.

/*
    Y lógico ( && ): Devuelve TRUE si ambos operandos son TRUE

    (3 < 4) && ( 5 > 4) --> TRUE
    (4 < 4) && (4 > 3) --> FALSE

    O lógico ( || ) --> Devuelve FALSE cuando los dos operandos son FALSE, sino devuelve TRUE.

    (3 < 4) || ( 5 > 4) --> TRUE
    (4 < 4) || (4 > 3) --> TRUE (se cumple 4 > 3)
    (4 < 4) || (7 < 3) --> FALSE (no se cumple ninguna comparación)

    NO lógico ( ! ): Invierte el valor de una expresión.

    !(3 < 4) && ( 5 > 4) --> FALSE, invierto la primera expresión: (3 < 4) es TRUE, aplico la negación (!TRUE), es FALSE, y se hace la comparación
                             FALSE && TRUE --> FALSE 
    
    !(4 < 4) && (4 > 3) --> TRUE
*/

// CADENA (CONCATENACIÓN)
// Se utiliza para unir cadenas de texto (Strings)
/*
    CONCATENACIÓN ( + )

    "La cadena " + " está separada" // "La cadena está separada"
    
    let cadena = "Vamos a unir una cadena usando un "
    cadena += " operador de asignación" // "Vamos a unir una cadena usando un operador de asignación"
*/

// CONDICIONAL (ternario)
// Este operador se utiliza para obtener un valor de dos posibles ante una condición.
/*
    condition ? val1 : val2
    Si condición es TRUE se obtiene el val1, sino val2

    let age = 22
    let tipo = age >= 18 ? "adulto" : "menor" // tipo = adulto
    
    Si la variable age es mayor o igual a 18 tomo el valor adulto, sino menor

*/

// TYPEOF
// Operador unario que sirve para identificar el tipo de dato.
// Se utiliza mucho para saber el tipo de dato con el que está trabajando una variable.

/*
    let x = 1
    typeof x // number
    let x = "1"
    typeof(x) // string (se puede poner entre paréntesis o no)
    let x = TRUE
    typeof x // boolean
*/

// NOTA
/* Indicar que las expresiones se pueden anidar unas dentro de otras y modificar el orden en el que se quieren que se hagan comparaciones con ().

    No es lo mismo 5 + 3 * 5 // 20
    que (5 + 3) * 5 // 40

    Tampoco es lo mismo (3 > 4) || (4 > 3) && (4 === 4) --> TRUE (se lee de izquierda a derecha)
    que  (3 > 4) || ( (4 < 3)  && (4 === 4) ) --> FALSE: (4 < 3) --> FALSE al comparar con el operador Y --> FALSE y (3 > 4) FALSE en el operador O
*/

// Los operadores de tipo bits los puedes revisar en https://developer.mozilla.org/es/docs/Web/JavaScript/Guide/Expressions_and_operators#bit_a_bit
// Se utilizan para hacer modificaciones bit a bit en expresiones binarias.

// EXPRESIONES
/*  Una expresión es cualquier unidad de código que resuelve un valor, hay 2 tipos, las que asignan un valor y las que resuelven un valor.
    x = 7 asigna un valor, 3 + 4 resuelve el valor 3 + 4 (7)  
*/

// ESTRUCTURAS DE CONTROL

// CONDICIONALES --> https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/conditionals

/* 
    Las estructuras condicionales se utilizan para decir que camino debe seguir el programa 
    según el resultado de los operadores que le indiquemos

    Hay dos estructuras para esto:
    Estructura IF (else y else if)
    Estructura SWITCH

*/

// IF
let x = 25
if(x > 25){
    console.log("La variable X es mayor de 25")
}else if( x < 25 ){
    console.log("La variable X es menor de 25")   
}else{
    console.log("La variable X es igual a 25")
}

// Este código de arriba se podría leer así:
// Si es mayor de 25 muestro un mensaje, sino, si es menor de 25, muestro otro mensaje diferente, sino muestro otro mensaje.

// Se pueden meter IF dentro de otros (u otras estructuras), aunque hay que evitarlo en la medida de lo posible
if(x === 25){
    if((x % 5) === 0){ // Se pueden realizar operaciones, comparaciones lógicas...
        console.log("X es múltiplo de 5")
    }else{
        console.log ("X no es múltiplo de 5")
    } 
}

// Una mejor forma de escribir el código anterior sería introducción las condiciones en el mismo IF utilizando los operadores
// lógicos
if(x === 25 && ((x % 5) === 0)){ // Si X es estrictamente igual a 25 Y al dividir entre 5 obtengo un resto de 0
    console.log("X es múltiplo de 5")
}else{
    console.log ("X no es múltiplo de 5")
}

// La condición puede ser tan larga como se necesite
if(x == 5 || x == 7 || x == 1 || x == 2 || x == 3){
    console.log("X es un número primo")
}

// SWITCH
/*
    switch (expresion){
    case opcion1:
        ejecuta este código
        break;

    case opcion2:
        ejecuta este código
        break;

    // Se pueden incluir todos los casos que quieras

    default:
        Si no se cumple ningún caso
        ejecuta este código
    }
    ES NECESARIO UTILIZAR LA PALABRA RESERVADA BREAK, sino no sale del SWITCH cuando ejecuta el caso y sigue buscando ejecutar más código
*/

let dia = 4
switch(dia){
    case 1:
        console.log("Lunes")
        break;
    case 2:
            console.log("Martes")
            break;
    case 3:
        console.log("Miércoles")
        break;
    case 4:
            console.log("Jueves")
            break;
    case 5:
            console.log("Vienres")
            break;
    case 6:
        console.log("Sábado")
        break;
    case 7:
            console.log("Domingo")
            break;
    default:
        console.log("El número no se corresponde con un día de la semana")
        // En la última opción no es necesario el break
}

let tiempo = "soleado"
switch(tiempo){
    case "nublado":
        console.log("Está nublado")
        break;
    case "soleado":
        console.log("Está soleado")
        break;
    case "lluvioso":
        console.log("Está lluvioso")
}

// ITERACIONES (BUCLES) --> https://developer.mozilla.org/es/docs/Learn/JavaScript/Building_blocks/Looping_code

/* 
    La estructuras iterativas (o bucles) se utilizan para repetir código una cantidad determinada de veces.
    El número de repeticiones va a venir determinado por una condición, que va indicar el fin. Es necesario
    tener mucho cuidado con esto, porque si nunca se cumple esa condición se crea un bucle infinito y nunca
    se sale de él, creando un fallo en el programa.
*/

// FOR
/*
    // Se suele utilizar cuando sabemos la canitdad de veces que es necesario repetir el bucle
    for (inicializador; condición; operación){
        código a ejecutar
    }

*/
for(let x = 5; x < 9; x++){ // Para x = 5; mientras x menor que 9; sumar uno a X
    console.log(x) // 5,6,7,8
}

// WHILE
/*
    // Se suele utilizar cuando hay una condición de salida, por ejemplo en una búsqueda al encontrar el elemento.
    inicializador
    while(condición) {
        // código a ejecutar

        operación
    }
*/
let encontrado = false // Inicializador
let numero = 1
while(!encontrado){ // condición
    if(numero === 10){
        encontrado = true // operación
        console.log(numero)
    }else{
        numero++ 
    }
}

// DO WHILE
/*
    // Igual que WHILE, con la diferencia que al menos se ejecuta siempre una vez
    inicializador
    do {
        // código a ejecutar

        operación
    } while (condición)
*/
do{
    if(numero === 10){
        encontrado = true // operación
        console.log(numero)
    }else{
        numero++
    }
}while(!encontrado) // condición

// EJERCICIO PROPUESTO
/*
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
    -------------------------------------------------------------------------
    Analizamos el problema
        - Utilizamos el bucle FOR, sabemos cuantas repeticiones va a tener, empezamos en 10
          y terminamos en 55
        - Hay 3 condiciones para imprimir
            - Numeros pares ( usando el módulo de 2 = 0 sabemos si es par)
            - El número 16 no se debe de imprimir
            - Los multiplos de 3 no se deben imprimir ( usando el módulo 3 ! 0 sé que no es múltiplo)
*/

for(let cont = 10; cont <= 55;cont++){
    if((cont%2===0) && (cont!==16) && (cont%3!==0)){ // Si cont es par Y NO es 16 Y NO es múltiplo de 3
        console.log(cont)
    }
}
