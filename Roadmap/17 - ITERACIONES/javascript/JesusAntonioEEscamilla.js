/** #17 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Las iteraciones en JavaScript son acciones encargadas de extraer datos permanentemente que son solicitados a la base de datos para ser mostrados en el lado del cliente.
 * Una de las principales ventajas de la programación es la posibilidad de crear bucles y repeticiones para tareas específicas, y que no tengamos que realizar el mismo código varias veces de forma manual.
 * Los bucles ofrecen una forma rápida y sencilla de hacer algo repetidamente.
*/

//---EJERCIÓ---

// Utilizaremos el bucle FOR
for (let i = 1; i <= 10; i++) {     //for(inicializar; condición; incrementó)
    console.log(i);     //Aquí se imprime del 1 - 10
}

// Otro forma se usar bucle WHILE
let i = 1;  //Aquí se declara una variable para usar como condición
while (i <= 10) {   //Se pone el incrementó
    console.log(`El valor es:`,i);  //Aquí imprimimos la siempre la variable
    i = i + 1;      //Se va incrementando hasta que la condición diga
}

// Y la última forma de usar bucle es FOR-EACH
const números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];    //Hacemos un array de los números
números.forEach(number => {     //Y el Método forEach va iterando todos los elementos
    console.log(`Los números son ${number}`);   //Aquí se imprime los números
});



/**-----DIFICULTAD EXTRA-----*/

//Otra Forma de hacer Iteraciones:
//  DO...WHILE
let k = 1;  // Variable nueva
do {
    console.log(`Se imprimen ${k}`);
    k++
} while (k <= 10);

//  FOR...OF
const iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (const item of iterable) {
    console.log(`El numero es : ${item}`);
}

//  FUNCIÓN RECESIVA
function contar(i) {
    if (i <= 10) {
        console.log(`Se cuenta a ${i}`);
        contar(i + 1);
    }
}
contar(1);

//  FOR...IN
const number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for (const key in number) {
    console.log(`Se muestra el indice: ${number[key]}`);
}

/**-----DIFICULTAD EXTRA-----*/