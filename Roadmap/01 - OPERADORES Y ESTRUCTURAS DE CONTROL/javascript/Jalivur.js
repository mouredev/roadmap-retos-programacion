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
    -Operadores de ASIGNACIÓN:
    Un operador de asignación asigna un valor a su operando izquierdo basándose en el valor de su operando derecho. 
    El operador de asignación simple es igual (=), que asigna el valor de su operando derecho a su operando izquierdo. Es decir, x = y asigna el valor de y a x.
    También hay operadores de asignación compuestos que son una abreviatura de las operaciones siguientes.
    */
        //Asignacion Basica: --> =
        let operator1 = 5; //-->asigna valor a la variable.
        console.log(operator1); // --> 5 en consola.

        //Asignacion suma: --> +=
        let operator2; //-->no inicializado, undefined o indefinido.
        operator2 += 10; //--> no se puede operar con valores undefined.
        console.log(operator2); // --> NaN en consola.
        operator2 = 2; //-->inicializar para que no devuelva NaN.
        operator2 += 10; //--> al valor inicializado suma el valor de asignaicon y reasigna valor sumado.
        console.log(operator2); // --> 12 en consola.

        //Asignacion resta: --> -=
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
        let operatorLogic2 = true;
        operatorLogic1 &&= operatorLogic2; //si ambos operadorres son true asigna al operador 1 true
        console.log(operatorLogic1); 
        operatorlogic2 = false;
        operatorLogic1 &&= operatorlogic2;
        console.log(operatorLogic1); // si alguno de los opreadores, o ambos son false asigna false 
        //Asignación OR lógico: --> ||=
        let operatorLogic3 = true;
        let operatorLogic4 = false;
        operatorLogic3 ||= operatorLogic4; //si uno o los dos operadorres son true asigna al operador 3 true
        console.log(operatorLogic3); 
        operatorLogic3 = false;
        operatorLogic3 ||= operatorLogic4; // si abmos opreadores son false, asigna false 
        console.log(operatorLogic3); 
        //Asignación anulacion lógica: --> ??=
        let operatorLogic5;
        let operatorLogic6 = false;
        operatorLogic5 ??= operatorLogic6; // si el poperador a la izquierda no esta definido, se arigna el valor de operador de la derecha.
        console.log(operatorLogic5); 
        operatorLogic5 = true;
        operatorLogic5 ??= operatorLogic6; // si el operador de la izquierda esta definido, se queda con el valor que tenia.
        console.log(operatorLogic5); 

    /*
    -Operadores de COMPARACION:
    Un operador de comparación compara sus operandos y devuelve un valor lógico en función de si la comparación es verdadera (true) o falsa (false). 
    Los operandos pueden ser valores numéricos, de cadena, lógicos u objetos. 
    Las cadenas se comparan según el orden lexicográfico estándar, utilizando valores Unicode.
    En la mayoría de los casos, si los dos operandos no son del mismo tipo, JavaScript intenta convertirlos a un tipo apropiado para la comparación. 
    Este comportamiento generalmente resulta en comparar los operandos numéricamente. 
    Las únicas excepciones a la conversión de tipos dentro de las comparaciones involucran a los operadores === y !==, que realizan comparaciones estrictas de igualdad y desigualdad. 
    Estos operadores no intentan convertir los operandos a tipos compatibles antes de verificar la igualdad.
    */
        //IGUAL: --> ==
        console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (operator3 == operator2));
        operator3 = 5; 
        operator2 = 5;
        console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (operator3 == operator2));
        operator3 = "alberto"; 
        operator2 = "alberto";
        console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (operator3 == operator2));
        operator3 = "alberto";
        operator2 = "Alberto";
        console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (operator3 == operator2));
        operator3 = 1.0; 
        operator2 = 1;
        console.log(`es ${operator3} igual a ${operator2}: ${operator3 == operator2}`);
        operator3 = 50; 
        operator2 = 50n;
        console.log(`es ${operator3} int igual a ${operator2} bigint: ${operator3 == operator2}`);
        console.log(`es ${operatorLogic1} igual a ${operatorLogic2}: ${operatorLogic1 == operatorLogic2}`);
        console.log(`es ${operatorLogic1} igual a ${operatorLogic3}: ${operatorLogic1 == operatorLogic3}`);
        operator1 = undefined;
        operator2 = null;
        console.log(`es ${operator1} igual a ${operator2}: ${operator1 == operator2}`);
        console.log(`es ${operator1} igual a ${0}: ${operator1 == 0}`);
        console.log(`es ${operator2} igual a ${0}: ${operator1 == 0}`);
        console.log(`es ${1} igual a ${operatorLogic2}: ${1 == operatorLogic2}`);
        console.log(`es ${0} igual a ${operatorLogic1}: ${0 == operatorLogic1}`);
        console.log(`es ${operator1} igual a ${operatorLogic1}: ${operator1 == operatorLogic1}`);
        console.log(`es ${operator2} igual a ${operatorLogic1}: ${operator2 == operatorLogic1}`);
        //NO IGUAL: --> !=
        console.log(`${operator1} no es igual a ${operator2}: ${operator1 != operator2}`);
        console.log(`${operatorLogic1} no es igual a ${operatorLogic2}: ${operatorLogic1 != operatorLogic2}`);
        operator3 = "alberto";
        operator2 = "Alberto";
        console.log((operator3)+" no es igual a "+(operator2)+": "+ (operator3 != operator2));
        //EXTRICTAMENTE IGUAL: --> ===
        operator1 = undefined;
        operator2 = null;
        console.log(`es ${operator1} extrictamente igual a ${operator2}: ${operator1 === operator2}`);
        console.log(`es ${operator1} extrictamente igual a ${0}: ${operator1 === 0}`);
        console.log(`es ${operator2} extrictamente igual a ${0}: ${operator1 === 0}`);
        console.log(`es ${1} extrictamente igual a ${operatorLogic2}: ${1 === operatorLogic2}`);
        console.log(`es ${0} extrictamente igual a ${operatorLogic1}: ${0 === operatorLogic1}`);
        //DESIGUALDAD EXTRICTA: --> !==
        console.log(`${operator1} no es igual a ${operator2} extricatemente: ${operator1 !== operator2}`);
        console.log(`${operatorLogic1} no es igual a ${operatorLogic2} extrictamente: ${operatorLogic1 !== operatorLogic2}`);
        operator3 = "alberto ";
        operator2 = "Alberto";
        console.log((operator3)+" no es igual a "+(operator2)+" extrictamente: "+ (operator3 !== operator2));
        //MAYOR QUE: --> >
        console.log(`es 1 mayor que 5: ${1>5}`);
        console.log(`es 5 mayor que 1: ${5>1}`);
        console.log(`es "alberto " mayor que "Alberto": ${operator3.length>operator2.length}`);
        //MAYOR O IGUAL: --> >=
        console.log(`es 5 mayor o igual que 5: ${5>=5}`)
        console.log(`es 5 mayor o igual que 3: ${5>=3}`)
        console.log(`es 5 mayor o igual que 6: ${5>=6}`)
        let name1 = "alberto";
        let name2 = "Alberto";
        console.log(`es ${name1}(${name1.length}) mayor o igual que ${name2}(${name2.length}): ${name1.length>=name2.length}`)
        name1="albertooo"
        name2="alberto   "
        console.log(`es ${name1}(${name1.length}) mayor o igual que ${name2}(${name2.length}): ${name1.length>=name2.length}`)
        //MENOR QUE: --> <
        console.log(`es 1 menor que 5: ${1<5}`);
        console.log(`es 5 menor que 1: ${5<1}`);
        console.log(`es "alberto " menor que "Alberto": ${operator3.length<operator2.length}`);
        //MENOR O IGUAL: --> <=
        console.log(`es 5 menor o igual que 5: ${5<=5}`)
        console.log(`es 5 menor o igual que 3: ${5<=3}`)
        console.log(`es 5 menor o igual que 6: ${5<=6}`)
        name1 = "alberto";
        name2 = "Alberto";
        console.log(`es ${name1}(${name1.length}) menor o igual que ${name2}(${name2.length}): ${name1.length<=name2.length}`)
        name1="albertooo"
        name2="alberto   "
        console.log(`es ${name1}(${name1.length}) menor o igual que ${name2}(${name2.length}): ${name1.length<=name2.length}`) 
    /* OPERADORES ARITMETICOS:
    Un operador aritmético toma valores numéricos (ya sean literales o variables) como sus operandos y devuelve un solo valor numérico. 
    Los operadores aritméticos estándar son suma (+), resta (-), multiplicación (*) y división (/). 
    Estos operadores funcionan como lo hacen en la mayoría de los otros lenguajes de programación cuando se usan con números de punto flotante (en particular, ten en cuenta que la división entre cero produce Infinity).
    */
        //RESIDUO O RESTO: --> % actua como en el de asignacion, pero no asigna valor al operador de la izquierda.
        console.log(`El resto de 5 entre 3 es = ${5%3}`)//2
        console.log(`El resto de 550 entre 10 es = ${550%10}`)//0, 550 es multiplo de 10.
        //INCREMENTO: --> ++
        let value = 1;
        console.log(++value); //inclementa 1 al valor de value
        //DECREMENTO: --> --
        console.log(--value); //decrementa 1 al valor de value
        //NEGACION UNARIA: --> - 
        console.log(-value); //devuelve la negacion del value
        //POSITIVO UNARIO: --> +
        value = false;
        console.log(typeof(value))
        console.log(+value); //combierte en numero si todavia no lo es
        console.log(typeof(+value))
        value="2"
        console.log(value)
        console.log(typeof(value))//value es de tipo estrin pero contiene un 2
        console.log(+value)
        console.log(typeof(+value))//value se convierte en un 2 number
        value="alberto"
        console.log(value)
        console.log(typeof(value))//value es una cadena de caracteres
        console.log(+value)//lo combierte en un NaN (not asigned number)
        console.log(typeof(+value))//value se convierte en un 2 number
        //EXPONECIACION, EXPONENTE: --> **
        console.log(`5 elevado a 6 es = ${5**6}`);
        console.log(`2 elevado a 8 es = ${2**8}`);
    /* OPERADORES BIT A BIT:
        Un operador bit a bit trata a sus operandos como un conjunto de 32 bits (ceros y unos), en lugar de números decimales, hexadecimales u octales. 
        Por ejemplo, el número decimal nueve tiene una representación binaria de 1001. 
        Los operadores bit a bit realizan sus operaciones en tales representaciones binarias, pero devuelven valores numéricos estándar de JavaScript.
    */
        //AND bit a bit: --> &
        operatorbit1 = 3;
        console.log(`${operatorbit1} AND 5 bit a bit es igual a ${operatorbit1&5}, ${(operatorbit1&5).toString(2).padStart(32,"0")}`);
        console.log(`${operatorbit1} = ${operatorbit1.toString(2).padStart(32,"0")}, y 5 = ${(5).toString(2).padStart(32,"0")},
con and solo quedan a 1 los que coniciden en abmos por eso queda 1 = ${(operatorbit1&5).toString(2).padStart(32,"0")}`);
        //XOR bit a bit: --> ^= or exclusiva.
        operatorbit1 = 5;
        console.log(`${operatorbit1} AND 5 bit a bit es igual a ${operatorbit1^5}, ${(operatorbit1^5).toString(2).padStart(32,"0")}`);
        console.log(`${operatorbit1} = ${operatorbit1.toString(2).padStart(32,"0")}, y 5 = ${(5).toString(2).padStart(32,"0")},
con xor solo quedan a 1 los que son 1 en uno u otro operador, pero nocoiciden en abmos por eso queda 0 = ${(operatorbit1&5).toString(2).padStart(32,"0")}`);
        //Asignación OR bit a bit: --> |= 
        operatorbit3 = 5896; //     00000000000000000001011100001000
            operatorbit3 |= 4589; //        00000000000000000001000111101101
            console.log(operatorbit3); //   00000000000000000001011111101101, 6125 en decimal, compara bit a bit y si uno o los dos coinciden en 1 asigna 1 en el resultado.
            operatorbit3 |= 6126; //        00000000000000000001011111101110
            console.log(operatorbit3); //   00000000000000000001011111101111, 6127 en decimal, compara bit a bit y si uno o los dos coinciden en 1 asigna 1 en el resultado.

  
