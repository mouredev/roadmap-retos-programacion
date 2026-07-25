/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

// Operadores

    // Aritméticos
    console.log ("*** OPERADORES ARITMÉTICOS ***")
    console.log (`Suma 10 + 3 = ${10+3}`);
    console.log (`Resta 10 - 3 = ${10-3}`);
    console.log (`Multiplicación 10 * 3 = ${10*3}`);
    console.log (`División 10 / 3 = ${10/3}`);
    console.log (`Módulo ó resto 10 // 3 = ${10%3}`);
    console.log (`Potencia 10 ^ 3 = ${10**3}`);
    console.log ("");

    // Asignación
    console.log ("*** OPERADORES DE ASIGNACIÓN ***")
    let a = 10;
    console.log (`Se asigna a la variable a un valor = ${a}`);
    a += 3;
    console.log (`Con += se incrementa la variable a en el valor que se indique: a+=3 es ${a}`);
    a -= 3;
    console.log (`Con -= se disminuye la variable a en el valor que se indique: a-=3 es ${a}`);
    a *= 3;
    console.log (`Con *= se multiplica la variable a por el valor que se indique: a*=3 es ${a}`);
    a /= 3;
    console.log (`Con /= se divide la variable a por el valor que se indique: a/=3 es ${a}`);
    a **= 3;
    console.log (`Con **= se eleva la variable a el número de veces que el valor nos indique: a**=3 es ${a}`);
    console.log ("");

    // Comparación
    console.log ("*** OPERADORES DE COMPARACIÓN ***")
    console.log (`Con == se comprueba si hay igualdad solo de valor, no de tipo. Por ejemplo, para comparar si 5 (número) y 5 (string) es lo mismo en cuanto a valor sería ${5 == "5"}`); // true (compara solo el valor)
    console.log (`Con === se comprueba si hay igualdad tanto de valor como de tipo. Por ejemplo, para comparar si 5 (número) y 5 (string) es lo mismo en cuanto a valor y tipo sería ${5 === "5"}`); // false (compara valor y tipo)
    console.log (`Con != se comprueba si hay diferencia solo de valor, no de tipo. Por ejemplo, para comparar si 5 (número) y 5 (string) es diferente solo en cuanto a valor ${5 != "5"}`); // false (compara solo el valor)
    console.log (`Con !== se comprueba si hay diferencia tanto de valor como de tipo. Por ejemplo, para comparar si 5 (número) y 5 (string) es diferente en cuanto a valor y tipo sería ${5 !== "5"}`); // true (compara valor y tipo)
    console.log (`Con > se comprueba si el valor de la izquierda es mayor que el de la derecha. Por ejemplo en 10 > 5 nos da ${10 > 5}`); // true
    console.log (`Con < se comprueba si el valor de la izquierda es menor que el de la derecha. Por ejemplo en 10 < 5 nos da ${10 < 5}`); // false
    console.log (`Con >= se comprueba si el valor de la izquierda es mayor o igual que el de la derecha. Por ejemplo en 10 >= 5 nos da ${10 >= 5}`); // true
    console.log (`Con <= se comprueba si el valor de la izquierda es menor o igual que el de la derecha. Por ejemplo en 10 <= 5 nos da ${10 <= 5}`); // false
    console.log ("");

    // Lógicos
    console.log ("*** OPERADORES LÓGICOS ***")
    let x = true, y = false;
    console.log (`Con el operador && indicamos que si las dos condiciones que pongamos deben ser verdaderas. En este caso x = ${x} e y = ${y}, por lo tanto si las comparamos con && nos debe dar ${x && y}`); // false
    console.log (`Con el operador || indicamos que una de las dos condiciones que pongamos debe ser verdadera. En este caso x = ${x} e y = ${y}, por lo tanto si las comparamos con || nos debe dar ${x || y}`); // true
    console.log (`Con el operador ! antes de una variable hacemos que la nos devuelva el valor contrario de la variable. En este caso x = ${x}, por lo tanto hacer !x nos dará ${!x}`); // false
    console.log ("");

    // Incremento y decremento
    console.log ("*** OPERADORES DE INCREMENTO Y DECREMENTO ***")
    let z = 5;
    console.log (`El valor de la variable z ahora es de: ${z}`);
    console.log (`Si a la variable le añadimos detrás ++ le indicamos que incremente su valor después de usarla. Si lo hacemos ahora mostrará su valor y luego se incrementará: ${z++}`); // Muestra 5 (pero x ahora es 6)
    console.log (`Ahora se incrementa su valor y la variable z vale: ${z}`);
    console.log (`Si a la variable le añadimos delante ++ le indicamos que incremente su valor antes de usarla. Si lo hacemos ahora incrementará su valor antes de empezar a trabajar con ella: ${++z}`); // Muestra 7 (x se incrementa antes de mostrar)
    console.log ("");

    // Tipo
    console.log ("*** OPERADORES DE TIPO ***")
    console.log (`Con typeof comprobamos el tipo de dato que le indicamos justo después: typeof "Hola" nos debe dar string. Lo comprobamos: ${typeof "Hola"}`); // "string"
    console.log (`En el caso de typeof 10 nos debe dar number. Veamos: ${typeof 10}`); // "number"
    console.log (`Con instanceof comprobamos si un objeto es de un tipo de dato específico. En este ejemplo creamos un objeto con new Date () de tipo dato y luego preguntamos si ese objeto es instanceof Date. Veamos: escribimos console.log (new Date () instanceof Date): ${new Date() instanceof Date}`);
    console.log ("");

// Estructuras de control

    // Condicionales
    console.log ("*** OPERADORES CONDICIONALES ***")
        // if, else if, else
        console.log ("*** if, else if, else ***")
        let miEdad = 52;
        if (miEdad >= 14 && miEdad <16) {
            console.log (`Puedes conducir ciclomotores.`);
        } else if (miEdad >= 16 && miEdad < 18) {
            console.log (`Próximamente podrá tener el permiso A1.`);
        } else {
            console.log (`Puedes sacarte el carnet de conducir con A2.`);
        }
        console.log ("");

        // switch
        console.log ("*** switch ***")
        let nombre = `Juan`
        switch (nombre) {
            case `Pepe`:
                console.log (`Hola Pepe.`);
                break;
            case `Antonio`:
                console.log (`Hola Antonio.`);
                break;
            case `Ana`:
                console.log (`Hola Ana`);
                break;
            default:
                console.log (`Hola ${nombre}.`)
        }
        console.log ("");
        
        // Ternarios
        console.log ("*** OPERADORES TERNARIOS ***")
        console.log (`Los operadores ternarios son ? y : y se usan para expresar condiciones. Se comprueba si se cumple una condición o no. Si se cumple se ejecuta lo que haya despues de la ? y antes de : y si no se cumple la condición se ejecuta solo lo que hay detrás de :`)
        let edad = 18;
        let mensaje = (edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad";
        console.log (mensaje);
        console.log ("");

    // Iterativas (bucles)
        // for
        console.log ("*** for ***");
        console.log ("Con `for` hacemos que se repita algo un número controlado de veces.");
        console.log ("Vamos a escribir los números pares que hay del 1 al 50.");
        for (let i = 1; i <= 50; i++) {
            if (i % 2 === 0) {
                console.log (i);
            }
        }
        console.log ("");

        // while
        console.log ("*** while ***");
        console.log ("Con `while` hacemos que se repita algo un número indeterminado de veces, hasta que se cumpla alguna condición.");
        console.log ("Vamos a escribir un programa que pida un número y no pare hasta que le demos el número correcto (será el 1234).");
        let clave = 1234;
        let contraseña;
        while (contraseña !== clave) {
            contraseña = parseInt (prompt ("Escriba un número de 4 cifras: "));
        }
        console.log ("ENHORABUENA. Has dado con la contraseña.");
        console.log ("");

        // do... while
        console.log ("*** do... while ***");
        console.log ("Con `do... while` hacemos que primero se ejecute alguna acción y luego se repita algo un número indeterminado de veces, hasta que se cumpla alguna condición.");
        console.log ("Hagamos el mismo programa de antes pero usando el `do... while`.")
        let key = 1234;
        let password;
        do {
            password = parseInt (prompt ("Escriba un número de 4 cifras: "));
        }
        while (password !== key);
        console.log ("ENHORABUENA. Has dado con la contraseña.");
        console.log ("");

console.log ("Ejemplo de programa: números pares, no divisibles por 3 ni igual a 16")
for (let number = 10; number <= 55; number++) {
    if (number % 2 === 0 && number !== 16 && number % 3 !== 0) {
        console.log (number);
    }
}