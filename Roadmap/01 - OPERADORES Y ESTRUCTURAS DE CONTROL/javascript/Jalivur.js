/*
EJERCICIO:
- Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
- Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
- Debes hacer print por consola del resultado de todos los ejemplos.

DIFICULTAD EXTRA (opcional):
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

    Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */

//OPERADORES:
    /*
    -Operadores de asignación:
    */
        //Asignacion Basica: --> =
        let operator1 = 5; //-->asigna valor a la variable.
        console.log(operator1); // --> 5 en consola.

        //Asignacion de adición: --> +=
        let operator2; //-->no inicializado, undefined o indefinido.
        operator2 += 10; //--> no se puede operar con valores undefined.
        console.log(operator2); // --> NaN en consola.
        operator2 = 2; //-->inicializar para que no devuelva NaN.
        operator2 += 10; //--> al valor inicializado suma el valor de asignaicon y reasigna valor sumado.
        console.log(operator2); // --> 12 en consola.

        //Asignacion de resta: --> -=
        let operator3; //-->no inicializado, undefined o indefinido.
        operator3 -= 10; //--> no se puede operar con valores undefined.
        console.log(operator3); // --> NaN en consola.
        operator3 = 2; //-->inicializar para que no devuelva NaN.
        operator3 -= 10; //--> al valor inicializado resta el valor de asignaicon y reasigna valor restado.
        console.log(operator3); // --> -8 en consola.

        //Asignacion de multiplicación: --> *=
        let operator4 = 5; //Declaracion e Inicialización.
        operator4 *= 10; //--> al valor inicializado multiplica el valor de asignaicon y reasigna valor multiplicado.
        console.log(operator4); // --> 50 en consola.

        //Asignacion de división: --> /=
        let operator5 = 5; //Declaracion e Inicialización.
        operator5 /= 10; //--> al valor inicializado se divde por el valor de asignaicon y reasigna valor dividido.
        console.log(operator5); // --> 0.5 en consola.

        //Asignacion de residuo o resto: --> %=
        let operator6 = 10; //Declaracion e Inicialización.
        operator6 %= 7; //--> al valor inicializado se divde por el valor de asignaicon y reasigna valor del resto o residuo.
        console.log(operator6); // --> 3 en consola.

        //Asignacion de exponenciación: --> **=
        operator6 **= 5; //--> al valor del operador6 se eleva al exponente de asignacion y reasigna valor del exponente.
        console.log(operator6); // --> 243 en consola.

        //Asignación de desplazamiento de bits a la izquierda: --> <<=
        operator4 <<= 3; // al valor binario (ejm: 50 = 00000000000000000000000000110010) del operador agrega n (valor de asignacion) ceros a la izquierda, y reasigna valor binario resultante en decimal.
        console.log(operator4); // --> (en este caso: 00000000000000000000000110010000 = 400)400 en consola.

        //Asignación de desplazamiento de bits a la derecha: --> >>= combierte en binarios de 32 bits
        operator4 = -243; // Reasignamos valor de ejemplo. si es negativo se vombierte en 32 bits complemento a 2 (11111111111111111111111100001101 = -243)
        operator4 >>= 2; // Desplaza hacia la derecha los bits de una variable el número de bits especificados en el valor de la expresión, manteniendo el signo, y asigna el resultado a la variable.
        console.log(operator4); // --> (11111111111111111111111111000011 = -61) -61 en consola.

        //Asignación de desplazamiento a la derecha sin signo: --> >>>=
        operator6 = -243; //(11111111111111111111111100001101 = -243)
        operator6 >>>= 2; // Desplaza hacia la derecha los bits de una variable el número de bits especificados en el valor de la expresión sin signo, y asigna el resultado a la variable.
        console.log(operator6); // --> (00111111111111111111111111000011 = 1073741763 ) 1073741763 en consola.

       //Asignación AND bit a bit: --> &=
        let operatorbit1 = 3; //        00000000000000000000000000000011
        operatorbit1 &= 3; //           00000000000000000000000000000011
        console.log(operatorbit1); //   00000000000000000000000000000011, 3 en decimal, compara bit a bit, y si coninciden en 1 lo asigna como 1 al resultado.
        operatorbit1 &= 5; //           00000000000000000000000000000101
        console.log(operatorbit1); //   00000000000000000000000000000001, 1 en decimla, compara bit a bit, y si coninciden en 1 lo asigna como 1 al resultado.
        operatorbit1 = 5; //            00000000000000000000000000000101
        operatorbit1 &= 5; //           00000000000000000000000000000101
        console.log(operatorbit1); //   00000000000000000000000000000101, 5 en decimal, compara bit a bit, y si coninciden en 1 lo asigna como 1 al resultado.
       //Asignación XOR bit a bit: --> ^= or exclusiva.
        let operatorbit2 = 12; //       00000000000000000000000000001100
        operatorbit2 ^= 10; //          00000000000000000000000000001010
        console.log(operatorbit2); //   00000000000000000000000000000110, 6 en decimal, compara bit a bit y si uno o el otro es 1, pero no los dos, asigna 1 al resultado.
        operatorbit2 ^= 55; //          00000000000000000000000000110111
        console.log(operatorbit2); //   00000000000000000000000000110001, 49 en decimal, compara bit a bit y si uno o el otro es 1, pero no los dos, asigna 1 al resultado. 
        operatorbit2 = 12863; //        00000000000000000011001000111111
        operatorbit2 ^= 15896; //       00000000000000000011111000011000
        console.log(operatorbit2); //   00000000000000000000110000100111, 3111 en decimal,compara bit a bit y si uno o el otro es 1, pero no los dos, asigna 1 al resultado.
       //Asignación OR bit a bit: --> |= 
        let operatorbit3 = 5896; //     00000000000000000001011100001000
        operatorbit3 |= 4589; //        00000000000000000001000111101101
        console.log(operatorbit3); //   00000000000000000001011111101101, 6125 en decimal, compara bit a bit y si uno o los dos coinciden en 1 asigna 1 en el resultado.
        operatorbit3 |= 6126; //        00000000000000000001011111101110
        console.log(operatorbit3); //   00000000000000000001011111101111, 6127 en decimal, compara bit a bit y si uno o los dos coinciden en 1 asigna 1 en el resultado.

        //Asignación AND lógico: --> &&=
        let operatorLogic1 = true;
        operatorLogic1 &&= true;
        console.log(operatorLogic1);
        operatorLogic1 &&= false;
        console.log(operatorLogic1);
        //
        /* 
        Asignación AND lógico	x &&= y	x && (x = y)
        Asignación OR lógico	x ||= y	x || (x = y)
        Asignación de anulación lógica	x ??= y	x ?? (x = y)
        */



