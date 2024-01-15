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
console.log('========================');
console.log('ASIGNACION BASICA variable 1 = variable 2');
let operator1; //-->no inicializado, undefined o indefinido.
let asingValue = 5;
console.log(operator1+" sin asignarle nada a la variable");
console.log(`asignamo valor a "variable = ${operator1=asingValue}": ${operator1=asingValue}`); 
console.log('========================');

//Asignacion suma: --> +=
console.log('========================');
console.log('ASIGNACION SUMA variable1 += variable2');
let operator2; //-->no inicializado, undefined o indefinido.
asingValue = 10;
console.log(operator2 +" SIN INICIALIZAR"); 
console.log(`${operator2} += ${asingValue} = ${operator2 += asingValue}`); //--> no se puede operar con valores undefined. 
operator2 = 2; //-->inicializar para que no devuelva NaN.
console.log(operator2 +" INICIALIZADA");
console.log(`${operator2} += ${asingValue} = ${operator2 += asingValue}`); //--> al valor inicializado suma el valor de asignaicon y reasigna valor sumado.
console.log(`Al valor inicializado suma el valor de asignaicon,
y reasigna valor sumado a la variable.`);
console.log('========================');

//Asignacion resta: --> -=
console.log('========================');
console.log('ASIGNACION RESTA variable 1 -= variable 2');
let operator3; //-->no inicializado, undefined o indefinido.
asingValue = 10;
console.log(operator3 +" SIN INICIALIZAR");
console.log(`${operator3} -= ${asingValue} = ${operator3 -= asingValue}`); //--> no se puede operar con valores undefined. 
operator3 = 2; //-->inicializar para que no devuelva NaN.
console.log(operator3 +" INICIALIZADA");
console.log(`${operator3} -= ${asingValue} = ${operator3 -= asingValue}`); //--> al valor inicializado resta el valor de asignaicon y reasigna valor restado.
console.log(`Al valor inicializado se resta el valor de asignaicon,
y reasigna valor restado.`);
console.log('========================');

//Asignacion de multiplicación: --> *=
console.log('========================');
console.log('ASIGNACION MULTIPLICACIÓN variable 1 *= variable 2');
let operator4 = 5; //Declaracion e Inicialización.
asingValue = 10;
console.log(`Al igual que con suma y resta,
la variable deve tener valor, 
para poder operar con ella.
${operator4} *= ${asingValue} = ${operator4 *= asingValue}`);//--> el valor inicializado se multiplica por el valor de asignaicon y reasigna valor multiplicado.
console.log(`El valor inicializado se multiplica por el valor de asignaicon,
y reasigna valor multiplicado.`);
console.log('========================');

//Asignacion de división: --> /=
console.log('========================');
console.log('ASIGNACION DIVISIÓN variable 1 /= variable 2');
let operator5 = 5; //Declaracion e Inicialización.
asingValue = 10;
console.log(`La variable deve tener valor, 
para poder operar con ella.
${operator5} /= ${asingValue} = ${operator5 /= asingValue}`);//--> el valor inicializado se divde por el valor de asignaicon y reasigna valor dividido.
console.log(`El valor inicializado se divde por el valor de asignaicon, 
y reasigna valor dividido.`);
console.log('========================');

//Asignacion de residuo o resto: --> %=
console.log('========================');
console.log('ASIGNACION RESTO variable 1 %= variable 2');
let operator6 = 10; //Declaracion e Inicialización.
asingValue = 7;
console.log(`La variable deve tener valor, 
para poder operar con ella.
${operator6} %= ${asingValue} = ${operator6 %= asingValue}`);//--> el valor inicializado se divde por el valor de asignaicon y reasigna valor del resto de la division.
console.log(`El valor inicializado se divde por el valor de asignaicon, 
y reasigna valor del resto de la division.`);
console.log('========================');

//Asignacion de exponenciación: --> **=
console.log('========================');
console.log('ASIGNACION POTENCIA variable 1 **= variable 2');
asingValue = 5;
console.log(`La variable deve tener valor, 
para poder operar con ella.
${operator6} **= ${asingValue} = ${operator6 **= asingValue}`);//--> el valor del operador6 se eleva al exponente de asignacion y reasigna valor del exponente.
console.log(`El valor actual de operator6 se eleva al valor de asignaicon, 
y reasigna valor de la potencia.`);
console.log('========================');

//Asignación de desplazamiento de bits a la izquierda: --> <<=
console.log('========================');
console.log('ASIGNACION DESPLAZAMEINTO BIT A BIT A LA IZQUIERDA variable 1 <<= variable 2');
asingValue = 3;
console.log(` ${operator4} (${operator4.toString(2).padStart(32,"0")}) 
<<= ${asingValue}
${operator4 <<= asingValue} (${operator4.toString(2).padStart(32,"0")})`);// al valor binario (ejm: 50 = 00000000000000000000000000110010) del operador agrega n (valor de asignacion) ceros a la izquierda, y reasigna valor binario resultante en decimal.
console.log(`El valor de la variable en formato binario de 32bits,
es desplazado a la izquierda tastas posiciones segun valor de asignaicon, 
y reasigna valor resultante de binario de 32bits a decimal,
las posiciones que se desplazan toman valor 0.`);
console.log('========================');

//Asignación de desplazamiento de bits a la derecha: --> >>= combierte en binarios de 32 bits
console.log('========================');
console.log('ASIGNACION DESPLAZAMEINTO BIT A BIT A LA DERECHA CON SIGNO variable 1 >>= variable 2');
operator4 = -243;
asingValue = 2;
console.log(`${operator4} (${(operator4>>>0).toString(2).padStart(32,"0")}) 
>>= ${asingValue}
 ${operator4 >>= asingValue} (${(operator4>>>0).toString(2).padStart(32,"0")})`);// Desplaza hacia la derecha los bits de una variable el número de bits especificados en el valor de la expresión, manteniendo el signo, y asigna el resultado a la variable.
console.log('========================');
operator4 = 243;
asingValue = 2;
console.log(`${operator4} (${(operator4>>>0).toString(2).padStart(32,"0")}) 
>>= ${asingValue}
 ${operator4 >>= asingValue} (${(operator4>>>0).toString(2).padStart(32,"0")})`);// Desplaza hacia la derecha los bits de una variable el número de bits especificados en el valor de la expresión, manteniendo el signo, y asigna el resultado a la variable.
console.log('========================');
console.log(`El valor de la variable en formato binario de 32bits,
es desplazado a la derecha tastas posiciones segun valor de asignaicon, 
y reasigna valor resultante de binario de 32bits a decimal, manteniendo el signo,
las posiciones que se desplazan toman valor 0 si es decimal pisitivo, 
y 1 si el decimal negativo.`)
 console.log('========================');

 //Asignación de desplazamiento a la derecha sin signo: --> >>>=
console.log('========================');
console.log('ASIGNACION DESPLAZAMEINTO BIT A BIT A LA DERECHA SIN SIGNO variable 1 >>>= variable 2');
operator4 = -243;
asingValue = 2;
console.log(`      ${operator4} (${(operator4>>>0).toString(2).padStart(32,"0")}) 
>>>= ${asingValue}
${operator4 >>>= asingValue} (${operator4.toString(2).padStart(32,"0")})`);// Desplaza hacia la derecha los bits de una variable el número de bits especificados en el valor de la expresión, sin mantener el signo, y asigna el resultado a la variable.
console.log('========================');
operator4 = 243;
asingValue = 2;
console.log(`${operator4} (${(operator4>>>0).toString(2).padStart(32,"0")}) 
>>= ${asingValue}
 ${operator4 >>= asingValue} (${(operator4>>>0).toString(2).padStart(32,"0")})`);// Desplaza hacia la derecha los bits de una variable el número de bits especificados en el valor de la expresión, manteniendo el signo, y asigna el resultado a la variable.
console.log('========================');
console.log(`El valor de la variable en formato binario de 32bits,
es desplazado a la derecha tastas posiciones segun valor de asignaicon, 
y reasigna valor resultante de binario de 32bits a decimal, sin mantener el signo,
las posiciones que se desplazan toman valor 0.`);
console.log('========================');
console.log('========================');
console.log(`En ambos desplacamientos a la dercha, 
los bit que quedna mas ala derecha de posision 0,
pierden el valor.`);
console.log('========================');

//Asignación AND bit a bit: --> &=
console.log('========================');
console.log('ASIGNACION AND BIT A BIT variable 1 &= variable 2');
let operatorbit1 = 3;
asingValue = 4;
console.log(operatorbit1); // ahora es 3
console.log(`${operatorbit1} (${(operatorbit1).toString(2).padStart(32,"0")}) AND, 
${asingValue} (${(asingValue).toString(2).padStart(32,"0")}) bit a bit es igual a, 
${operatorbit1&=asingValue} (${(operatorbit1).toString(2).padStart(32,"0")})`);
console.log(operatorbit1); // ahora es 0
console.log('========================');
console.log('========================');
operatorbit1 = 6;
asingValue = 4;
console.log(operatorbit1); // ahora es 6
console.log(`${operatorbit1} (${(operatorbit1).toString(2).padStart(32,"0")}) AND, 
4 (${(4).toString(2).padStart(32,"0")}) bit a bit es igual a, 
${operatorbit1&=4} (${(operatorbit1).toString(2).padStart(32,"0")})`);
console.log(operatorbit1); // ahora es 4
console.log('========================');
console.log(`AND, 
solo si los dos bit de los operadores es 1
el bit del resultado sera 1,
si uno o ambos bit son 0 sera 0.`);
console.log('========================');

//Asignación XOR bit a bit: --> ^= or exclusiva.
console.log('========================');
console.log('ASIGNACION XOR BIT A BIT variable 1 ^= variable 2');
let operatorbit2 = 6;
asingValue=55;
console.log(operatorbit2); // ahora es 6
console.log(` ${operatorbit2} (${(operatorbit2).toString(2).padStart(32,"0")}) XOR, 
${asingValue} (${(asingValue).toString(2).padStart(32,"0")}) bit a bit es igual a, 
${operatorbit2^=asingValue} (${(operatorbit2).toString(2).padStart(32,"0")})`);
console.log(operatorbit2); // ahora es 49
console.log('========================');
console.log('========================');
operatorbit2 = 4;
asingValue=10;
console.log(operatorbit2); // ahora es 4
console.log(` ${operatorbit2} (${(operatorbit2).toString(2).padStart(32,"0")}) XOR, 
${asingValue} (${(asingValue).toString(2).padStart(32,"0")}) bit a bit es igual a, 
${operatorbit2^=asingValue} (${(operatorbit2).toString(2).padStart(32,"0")})`);
console.log(operatorbit2); // ahora es 4
console.log('========================');
console.log(`XOR es or exlusiva, 
solo si uno de los dos bit de los operadores es 1,
el bit del resultado sera 1,
si ambos bit son 1 sera 0,
al igual que si ambos son 0.`);
console.log('========================');

//Asignación OR bit a bit: --> |= 
console.log('========================');
console.log('ASIGNACION OR BIT A BIT variable 1 |= variable 2');
let operatorbit3 = 5896;
asingValue = 4589; 
console.log(operatorbit3); // ahora es 5896
console.log(`${operatorbit3} (${(operatorbit3).toString(2).padStart(32,"0")}) OR, 
${asingValue} (${(asingValue).toString(2).padStart(32,"0")}) bit a bit es igual a, 
${operatorbit3|=asingValue} (${(operatorbit3).toString(2).padStart(32,"0")})`);
console.log(operatorbit3); // ahora es 6125
console.log('========================');
asingValue = 6126;
console.log(operatorbit3); // ahora es 6125
console.log(`${operatorbit3} (${(operatorbit3).toString(2).padStart(32,"0")}) OR, 
${asingValue} (${(asingValue).toString(2).padStart(32,"0")}) bit a bit es igual a, 
${operatorbit3|=asingValue} (${(operatorbit3).toString(2).padStart(32,"0")})`);
console.log(operatorbit3); // ahora es 6127
console.log('========================');
console.log(`OR, 
solo si uno o ambos bit de los operadores es 1,
el bit del resultado sera 1,
si ambos bit son 0 sera 0.`);
console.log('========================');

//Asignación AND lógico: --> &&=
console.log('========================');
console.log('ASIGNACION AND LOGICO variable 1 &&= variable 2');
let operatorLogic1 = true;
let operatorLogic2 = true;
console.log(`${operatorLogic1} AND ${operatorLogic2}`);
operatorLogic1 &&= operatorLogic2; //si ambos operadorres son true asigna al operador 1 true
console.log(`operador izda = ${operatorLogic1}`); 
operatorLogic2 = false;
console.log(`${operatorLogic1} AND ${operatorLogic2}`);
operatorLogic1 &&= operatorLogic2; // si alguno de los opreadores, o ambos son false asigna false 
console.log(`operador izda = ${operatorLogic1}`);
console.log('========================');
console.log(`AND logico, 
solo si los dos operadores es 1
el resultado sera 1 y se reasignara al operador de la izquierda,
si uno o ambos son 0 sera 0 y se reasignara al operador de la izquierda.`);
console.log('========================');

//Asignación OR lógico: --> ||=
console.log('========================');
console.log('ASIGNACION OR LOGICO variable 1 ||= variable 2');
let operatorLogic3 = true;
let operatorLogic4 = false;
console.log(`${operatorLogic3} OR ${operatorLogic4}`);
operatorLogic3 ||= operatorLogic4; //si uno o los dos operadorres son true asigna al operador 3 true
console.log(`operador izda = ${operatorLogic3}`); 
operatorLogic3 = false;
console.log(`${operatorLogic3} OR ${operatorLogic4}`);
operatorLogic3 ||= operatorLogic4; // si abmos opreadores son false, asigna false 
console.log(`operador izda = ${operatorLogic3}`);
console.log('========================');
console.log(`OR logico, 
solo si uno o ambos operadores es 1,
resultado sera 1 y se reasignara al operador de la izquierda,
si ambos son 0 sera 0 y se reasignara al operador de la izquierda.`);
console.log('========================');

//Asignación anulacion lógica: --> ??=
console.log('========================');
console.log('ASIGNACION ANULACION LOGICA variable 1 ??= variable 2');
let operatorLogic5;
let operatorLogic6 = false;
console.log(`${operatorLogic5} ANULACION ${operatorLogic6}`);
operatorLogic5 ??= operatorLogic6; // si el operador a la izquierda no esta definido, se arigna el valor de operador de la derecha.
console.log(`operador izda = ${operatorLogic5}`);
operatorLogic5 = true;
console.log(`${operatorLogic5} ANULACION ${operatorLogic6}`);
operatorLogic5 ??= operatorLogic6; // si el operador de la izquierda esta definido, se queda con el valor que tenia.
console.log(`operador izda = ${operatorLogic5}`);
console.log('========================');
console.log(`ANULACION logica, 
si el operador de la izquierda no esta inicializado,
se reasigna el valor del derecho,
pero si esta inicializado, se queda con su valor.`);
console.log('========================');

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
console.log('========================');
console.log('COMPARACION IGUALDAD resultado = (variable 1 == variable 2)');
let upshot;
upshot = (operator3 == operator2);
console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (upshot));
operator3 = 5; 
operator2 = 5;
upshot = (operator3 == operator2);
console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (upshot));
operator3 = "alberto"; 
operator2 = "alberto";
upshot = (operator3 == operator2);
console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (upshot));
operator3 = "alberto";
operator2 = "Alberto";
upshot = (operator3 == operator2);
console.log("es "+(operator3)+" igual a "+(operator2)+": "+ (upshot));
operator3 = 1.0; 
operator2 = 1;
upshot = (operator3 == operator2);
console.log(`es ${operator3} igual a ${operator2}: ${upshot}`);
operator3 = 50; 
operator2 = 50n;
upshot = (operator3 == operator2);
console.log(`es ${operator3} int igual a ${operator2} bigint: ${upshot}`);
upshot = (operatorLogic1 == operatorLogic2);
console.log(`es ${operatorLogic1} igual a ${operatorLogic2}: ${upshot}`);
operatorLogic1 = true;
upshot = (operatorLogic1 == operatorLogic3);
console.log(`es ${operatorLogic1} igual a ${operatorLogic3}: ${upshot}`);
operator1 = undefined;
operator2 = null;
upshot = (operator1 == operator2);
console.log(`es ${operator1} igual a ${operator2}: ${upshot}`);
upshot = (operator1 == 0);
console.log(`es ${operator1} igual a ${0}: ${upshot}`);
upshot = (operator2 == 0);
console.log(`es ${operator2} igual a ${0}: ${upshot}`);
upshot = (operatorLogic1 == 1);
console.log(`es ${1} igual a ${operatorLogic1}: ${upshot}`);
upshot = (operatorLogic2 == 0);
console.log(`es ${0} igual a ${operatorLogic2}: ${upshot}`);
upshot = (operatorLogic2 == operator1);
console.log(`es ${operator1} igual a ${operatorLogic2}: ${upshot}`);
upshot = (operatorLogic2 == operator2);
console.log(`es ${operator2} igual a ${operatorLogic2}: ${upshot}`);
console.log('========================');

//NO IGUAL: --> !=
console.log('========================');
console.log('COMPARACION DESIGUALDAD resultado = (variable 1 != variable 2)');
upshot = (operator1 != operator2);
console.log(`${operator1} no es igual a ${operator2}: ${upshot}`);
upshot = (operatorLogic1 != operatorLogic2);
console.log(`${operatorLogic1} no es igual a ${operatorLogic2}: ${upshot}`);
operator3 = "alberto";
operator2 = "Alberto";
upshot = (operator3 != operator2);
console.log((operator3)+" no es igual a "+(operator2)+": "+ (upshot));
console.log('========================');

//EXTRICTAMENTE IGUAL: --> ===
console.log('========================');
console.log('COMPARACION IGUALDAD EXTRICTA resultado = (variable 1 === variable 2)');
operator1 = undefined;
operator2 = null;
upshot = (operator1 === 0);
console.log(`es ${operator1} extrictamente igual a ${operator2}: ${upshot}`);
upshot = (operator1 === operator2);
console.log(`es ${operator1} extrictamente igual a ${0}: ${upshot}`);
upshot = (operator2 === 0);
console.log(`es ${operator2} extrictamente igual a ${0}: ${upshot}`);
upshot = (operatorLogic1 === 1);
console.log(`es ${1} extrictamente igual a ${operatorLogic1}: ${upshot}`);
upshot = (operatorLogic2 === 0);
console.log(`es ${0} extrictamente igual a ${operatorLogic2}: ${upshot}`);
console.log('========================');

//DESIGUALDAD EXTRICTA: --> !==
console.log('========================');
console.log('COMPARACION DESIGUALDAD EXTRICTA resultado = (variable 1 !== variable 2)');
upshot = (operator1 !== operator2);
console.log(`${operator1} no es igual a ${operator2} extricatemente: ${upshot}`);
upshot = (operatorLogic1 !== operatorLogic2);
console.log(`${operatorLogic1} no es igual a ${operatorLogic2} extrictamente: ${upshot}`);
operator3 = "alberto";
operator2 = "Alberto";
upshot = (operator3 !== operator2);
console.log((operator3)+" no es igual a "+(operator2)+" extrictamente: "+ (upshot));
console.log('========================');

//MAYOR QUE: --> >
console.log('========================');
console.log('COMPARACION MAYOR QUE resultado = (variable 1 > variable 2)');
operator1 = 1;
operator2 = 5;
upshot = (operator1 > operator2);
console.log(`es ${operator1} mayor que ${operator2}: ${upshot}`);
upshot = (operator2 > operator1);
console.log(`es ${operator2} mayor que ${operator1}: ${upshot}`);
operator3 = "alberto";
operator2 = "Alberto";
upshot = (operator3.length > operator2.length);
console.log(`es "${operator3}" mayor que "${operator2}": ${upshot}
en longiturd no.`);
upshot = (operator3 > operator2);
console.log(`es "${operator3}" mayor que "${operator2}": ${upshot}
como cadenas si porque el valor ASCII de las minusculas en mayor que el de las mayusculas.`);
console.log('========================');

//MAYOR O IGUAL: --> >=
console.log('========================');
console.log('COMPARACION MAYOR O IGUAL QUE resultado = (variable 1 >= variable 2)');
let value = 5;
let otherValue = 5;
upshot = (value >= otherValue);
console.log(`es ${value} mayor o igual que ${otherValue}: ${upshot}`);
value = 5;
otherValue = 3;
upshot = (value >= otherValue);
console.log(`es ${value} mayor o igual que ${otherValue}: ${upshot}`);
value = 5;
otherValue = 6;
upshot = (value >= otherValue);
console.log(`es ${value} mayor o igual que ${otherValue}: ${upshot}`);
let name1 = "alberto";
let name2 = "Alberto";
upshot = (name1.length>=name2.length);
console.log(`es ${name1} (${name1.length}) mayor o igual que ${name2} (${name2.length}): ${upshot}`);
name1="albertooo";
name2="Alberto   ";
upshot = (name1.length>=name2.length);
console.log(`es ${name1} (${name1.length}) mayor o igual que ${name2}(${name2.length}): ${upshot} por logitud`);
upshot = (name1>=name2);
console.log(`es ${name1} (${name1.length}) mayor o igual que ${name2}(${name2.length}): ${upshot} por cadena`);
console.log('========================');

//MENOR QUE: --> <
console.log('========================');
console.log('COMPARACION MENOR QUE resultado = (variable 1 < variable 2)');
value = 1;
otherValue = 5;
upshot = (value < otherValue)
console.log(`es ${value} menor que ${otherValue}: ${upshot}`);
value = 5;
otherValue = 1;
upshot = (value < otherValue)
console.log(`es ${value} menor que ${otherValue}: ${upshot}`);
value = 5;
otherValue = 5;
upshot = (value < otherValue)
console.log(`es ${value} menor que ${otherValue}: ${upshot}`);
console.log('========================');

//MENOR O IGUAL: --> <=
console.log('========================');
console.log('COMPARACION MENOR O IGUAL QUE resultado = (variable 1 <= variable 2)');
value = 5;
otherValue = 5;
upshot = (value <= otherValue)
console.log(`es ${value} menor o igual que ${otherValue}: ${upshot}`);
value = 5;
otherValue = 3;
upshot = (value <= otherValue)
console.log(`es ${value} menor o igual que ${otherValue}: ${upshot}`);
value = 5;
otherValue = 6;
upshot = (value <= otherValue)
console.log(`es ${value} menor o igual que ${otherValue}: ${upshot}`);
name1 = "alberto";
name2 = "Alberto";
console.log(`es ${name1}(${name1.length}) menor o igual que ${name2}(${name2.length}): ${name1.length<=name2.length}`);
name1="albertooo";
name2="alberto   ";
upshot = (name1.length<=name2.length)
console.log(`es ${name1}(${name1.length}) menor o igual que ${name2}(${name2.length}): ${upshot}`);
console.log('========================');

/* OPERADORES ARITMETICOS:
Un operador aritmético toma valores numéricos (ya sean literales o variables) como sus operandos y devuelve un solo valor numérico. 
Los operadores aritméticos estándar son suma (+), resta (-), multiplicación (*) y división (/). 
Estos operadores funcionan como lo hacen en la mayoría de los otros lenguajes de programación cuando se usan con números de punto flotante (en particular, ten en cuenta que la división entre cero produce Infinity).
*/

//RESIDUO O RESTO: --> % actua como en el de asignacion, pero no asigna valor al operador de la izquierda.
console.log('========================');
console.log('OPERADOR ARITMETICO RESIDUO O RESTO %');
let num1 = 5;
let num2 = 3;
console.log(`El resto de ${num1} entre ${num2} es = ${upshot=(num1%num2)}`);//2
num1 = 550;
num2 = 10;
console.log(`El resto de ${num1} entre ${num2} es = ${upshot=(num1%num2)}`);//0, 550 es multiplo de 10.
upshot = num1%num2
console.log('========================');
console.log(`Un operador aritmetico solo no asigna,
por lo que si queremos trabajar con el valor de la operacion
se deve almacenar en una variable 
{
let upshot; 
upshot=num1%num2;
}.`)
console.log('========================');

//INCREMENTO: --> ++
console.log('========================');
console.log('OPERADOR ARITMETICO INCREMENTO ++');
value = 100;
console.log(`Incremento de ++(${value}) = ${upshot=(++value)}`); //inclementa 1 al valor de value
console.log('========================');
console.log(`Incrementa en 1 el valor actual de la variable.
Un operador aritmetico solo no asigna,
por lo que si queremos trabajar con el valor de la operacion
se deve almacenar en una variable ejem: upshot = ${upshot}.`)
console.log('========================');

//DECREMENTO: --> --
console.log('========================');
console.log('OPERADOR ARITMETICO DECREMENTO --');
console.log(`Incremento de --(${value}) = ${upshot=(--value)}`); //decrementa 1 al valor de value
console.log('========================');
console.log(`Decrementa en 1 el valor actual de la variable.
Un operador aritmetico solo no asigna,
por lo que si queremos trabajar con el valor de la operacion
se deve almacenar en una variable ejem: upshot = ${upshot}.`)
console.log('========================');

//NEGACION UNARIA: --> - 
console.log('========================');
console.log('OPERADOR ARITMETICO NEGACION UNARIA -');
value = -59;
console.log(`Negacion unaria de -(${value}) = ${upshot=(-value)}`); //inclementa 1 al valor de value
console.log('========================');
console.log(`Decrementa en 1 el valor actual de la variable.
Un operador aritmetico solo no asigna,
por lo que si queremos trabajar con el valor de la operacion
se deve almacenar en una variable ejem: upshot = ${upshot}.`)
console.log('========================');


//POSITIVO UNARIO: --> +
console.log('========================');
console.log('OPERADOR ARITMETICO POSITIVO UNARIO +');
value = false;
console.log(`Inicialmente la variable es ${value}, de tipo ${typeof(value)},
pero con el operador, resultado = (+variable), este pasa a ser ${upshot=(+value)}, que es de tipo ${typeof(upshot)}.`);
value="2";
console.log(`Ahora la variable es ${value}, de tipo ${typeof(value)},
pero con el operador, resultado = (+variable), este pasa a ser ${upshot=(+value)}, que es de tipo ${typeof(upshot)}.`);
value="alberto";
console.log(`Ahora la variable es ${value}, de tipo ${typeof(value)},
pero con el operador, resultado = (+variable), este pasa a ser ${upshot=(+value)}, que es de tipo ${typeof(upshot)}.`);
console.log('========================');


//EXPONECIACION, EXPONENTE: --> **
console.log('========================');
console.log('OPERADOR ARITMETICO EXPONENCIACION resultado = (variable 1 ** variable 2)');
value = 5;
otherValue = 6;
upshot = (value ** otherValue);
console.log(`${value} elevado a ${otherValue} es = ${upshot}`);
value = 2;
otherValue = 8;
upshot = (value ** otherValue);
console.log(`${value} elevado a ${otherValue} es = ${upshot}`);
console.log('========================')

/* OPERADORES BIT A BIT:
Un operador bit a bit trata a sus operandos como un conjunto de 32 bits (ceros y unos), en lugar de números decimales, hexadecimales u octales. 
Por ejemplo, el número decimal nueve tiene una representación binaria de 1001. 
Los operadores bit a bit realizan sus operaciones en tales representaciones binarias, pero devuelven valores numéricos estándar de JavaScript.
*/

//AND bit a bit: --> & sin asignacion.
console.log('========================')
console.log(`OPERADOR BIT A BIT AND resultado = (variable 1 & variable 2)`)
operatorbit1 = -3;
let andValue = -5
upshot = (operatorbit1 & andValue);
console.log(`${operatorbit1} AND ${andValue} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1} 
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")},
${andValue} 
= 
${((andValue)>>>0).toString(2).padStart(32,"0")},
con and solo quedan a 1 los que coniciden en abmos por eso queda: 
${upshot} 
= 
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//XOR bit a bit: --> ^ or exclusiva.
console.log('========================')
console.log(`OPERADOR BIT A BIT AND resultado = (variable 1 & variable 2)`)
operatorbit1 = -559;
let xorValue=632;
upshot = (operatorbit1 ^ xorValue);
console.log(`${operatorbit1} XOR ${xorValue} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1} 
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")}, 
${xorValue} 
= 
${(xorValue>>>0).toString(2).padStart(32,"0")},
con xor solo quedan a 1 los que son 1 en uno u otro operador, pero no si coiciden en abmos por eso queda: 
${upshot} 
=
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//OR bit a bit: --> | 
console.log('========================')
console.log(`OPERADOR BIT A BIT OR resultado = (variable 1 | variable 2)`)
operatorbit1 = -559;
let orValue=632;
upshot = (operatorbit1 | orValue);
console.log(`${operatorbit1} XOR ${orValue} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1} 
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")}, 
${orValue} 
= 
${(orValue>>>0).toString(2).padStart(32,"0")},
con or quedan a 1 los que son 1 en uno u otro operador y si coiciden en abmos por eso queda: 
${upshot} 
=
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//NOT bit a bit: --> ~
console.log('========================')
console.log(`OPERADOR BIT A BIT NOT resultado = (~variable)`)
operatorbit1 = 598;
upshot = (~operatorbit1);
console.log(`not ${operatorbit1} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1} 
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")}, 
con not se invierten los valores de los bits: 
${upshot} 
=
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//IZQUIERDA bit a bit: --> <<
console.log('========================')
console.log(`OPERADOR BIT A BIT IZQUIERDA resultado = (variable 1 << variable 2)`)
operatorbit1 = -559;
let moveValue =3;
upshot = (operatorbit1 << moveValue);
console.log(`${operatorbit1} << ${moveValue} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1}
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")}, 
con desplazamiento a la izquierda, desplazamos tantos bits a la izquierda como valor entre 0 y 31
que asignemos la variable de movimiento. los bit desplazados son remplazados por 0: 
${upshot} 
=
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//DERECHA bit a bit CON SIGNO: --> >> 
console.log('========================')
console.log(`OPERADOR BIT A BIT DERECHA MANTENIENDO SIGNO resultado = (variable 1 >> variable 2)`)
operatorbit1 = -559;
moveValue =5;
upshot = (operatorbit1 >> moveValue);
console.log(`${operatorbit1} >> ${moveValue} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1} 
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")}, 
con desplazamiento a la derecha manteniendo el signo, desplazamos tantos bits a la derecha como valor entre 0 y 31
que asignemos la variable de movimiento. los bit desplazados son remplazados por 0 si la variable tienen un valor positivo,
y si la variable tiene un valor negativo se reemplazan con 1, para mantener el signo, lo valores mas a la derecha de posicion 0 se pierden.:  
${upshot} 
=
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//DERECHA bit a bit SIN SIGNO: --> >>>
console.log('========================')
console.log(`OPERADOR BIT A BIT DERECHA SIN MANTENER SIGNO resultado = (variable 1 >>> variable 2)`)
operatorbit1 = -559;
moveValue =0;
upshot = (operatorbit1 >>> moveValue);
console.log(`${operatorbit1} >>> ${moveValue} bit a bit es igual a ${upshot}`);
console.log(`${operatorbit1} 
= 
${(operatorbit1>>>0).toString(2).padStart(32,"0")}, 
con desplazamiento a la derecha sin mantener el signo, desplazamos tantos bits a la derecha como valor entre 0 y 31
que asignemos la variable de movimiento. los bit desplazados son remplazados por 0 , por lo que el signo se pierde.:  
${upshot} 
=
${((upshot)>>>0).toString(2).padStart(32,"0")}.`);
console.log('========================')

//OPERADOR TERNARIO
//expresión ? "si es true" : "si es false";
console.log('========================')
console.log(`OPERADOR TERNIARIO expresión ? "si es true" : "si es false"`)
let edad;
let acceso;
console.log(`${edad=32} ${acceso = edad >= 18 ? "Permitir acceso" : "Denegar acceso"}`);
console.log('========================')

//ESTRUCTURAS DE CONTROL:

//CONDICIONALES:

//if else:
console.log('========================')
console.log(`Estructura de control condicional: if...else`);
operator1 = 56;
operator2 = 54;
if (operator1 == operator2){
    console.log(`${operator1} es  igual a ${operator2}`);
}
else if (operator1 > operator2){
    console.log(`${operator1} mayor que ${operator2}`);
}
else {
    console.log(`${operator1} menor que ${operator2}`);
}
console.log('========================')

//switch
console.log('========================')
console.log(`Estructura de control switch:`);
let operacion ="**";
operator1 = 2;
operator2 = 256;
switch (operacion) {
    case "+":
        upshot = operator1 + operator2
        console.log(`${operator1} + ${operator2} = ${upshot}`);
        break;
    case "-":
        upshot = operator1 - operator2
        console.log(`${operator1} - ${operator2} = ${upshot}`);
        break;
    case "*":
        upshot = operator1 * operator2
        console.log(`${operator1} * ${operator2} = ${upshot}`);
        break;
    case "/":
        upshot = operator1 / operator2
        console.log(`${operator1} / ${operator2} = ${upshot}`);
        break;
    case "**":
        upshot = operator1 ** operator2
        console.log(`${operator1} ** ${operator2} = ${upshot}`);
        break;
    case "%":
        upshot = operator1 % operator2
        console.log(`${operator1} % ${operator2} = ${upshot}`);
        break;
    default:
        console.log(`Lo sentimos, la operacion ${operacion} no es valida.`);
}
console.log('========================')

//BUCLES E ITERACIONES:

//WHILE:
console.log('========================')
console.log(`Bucle while:`);
let whileCounter = 20;
while (whileCounter < 20) {
    console.log(`Iteración: ${whileCounter}`);
    whileCounter++;
}
console.log(`Se ejecuta mientras la condicion se cumple,
en este caso mientras contador < 20, como contador hemos establecido en 20,
no ejecuta nada, porque primero comprueba estado contador.`);
console.log('========================')


//DO WHILE
console.log('========================')
console.log(`Bucle do while:`);
let contadorDoWhile = 20;
do {
    console.log(`Iteración: ${contadorDoWhile}`);
    contadorDoWhile++;
} while (contadorDoWhile < 20);
console.log(`Se ejecuta hasta que la ocndicion deja de cumplirse,
en este caso hasta que contador < 20, como contador hemos establecido en 20,
ejecuta una vez y compreba estado.`);
console.log('========================')

//FOR
console.log('========================')
console.log(`Bucle for:`);
for (let i = 0; i <= 100; i++) {
    console.log(`Vuelta: ${i}`);
}
console.log('========================')
for (let i = 0; i <= 100; ++i) {
    console.log(`Vuelta: ${i}`);
}
console.log('========================')

//FOR OF
console.log('========================')
console.log(`Bucle for of:`);
let arrayForOf = [10, 20, 30, 40, 50];
for (let valor of arrayForOf) {
    console.log(`Valor elemento arrayForOf: ${valor}`);
}
console.log('========================')
//FOR IN
console.log('========================')
console.log(`Bucle for in:`);
let objetoForIn = { a: 1, b: 2, c: 3, d: 4, e: 5};

for (let propiedad in objetoForIn) {
    console.log(`Propiedad ${propiedad} = ${objetoForIn[propiedad]}`);
}
console.log('========================')

//FOR EACH
console.log('========================')
console.log(`Bucle for each:`);
let arrayForEach = [1, 2, 3, 4, 5, 6];

arrayForEach.forEach(function (elemento) {
    console.log(`Elemento: ${elemento}`);
});
console.log('========================')

//EXCEPCIONES
//Try catch:
console.log('========================')
console.log(`Try catch`);
value = "5";

try {
    if (value === 5) {
        throw new Error("El número es igual a 5")
    }
    console.log('Esto se imprime Si El número es distinto de 5')
} catch (error) {
    console.log(`Se ha producido un error poque ${error.message}`)
}
console.log('========================')
value = 5;

try {
    if (value === 5) {
        throw new Error("El número es igual a 5")
    }
    console.log('Esto se imprime si El número es distinto de 5')
} catch (error) {
    console.log(`Se ha producido un error poeque ${error.message}`)
}
console.log('========================')

//Try catch con bloque finally:
console.log('========================')
console.log('try-catch-finally')
value = "5";
try {
    if (value === 5) {
        throw new Error("El número es igual a 5")
    }
    console.log("El número es distinto de 5")
} catch (error) {
    console.log("Se ha producido un error porque "+error.message)
} finally {
    console.log("Bloque finally. Esto siempre se ejecuta haya o no excepción")
}
console.log('========================')
value = 5;
try {
    if (value === 5) {
        throw new Error("El número es igual a 5")
    }
    console.log("El número es distinto de 5")
} catch (error) {
    console.log("Se ha producido un error porque "+error.message)
} finally {
    console.log("Bloque finally. Esto siempre se ejecuta haya o no excepción")
}
console.log('========================')


//DIFICULTAD EXTRA:
/*
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/
console.log('========================')
console.log(`Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
for (let i = 10; i<=58; i++ ){
  if (i%2===0 && i !== 16 && i%3!==0){
    console.log(i)
  }
}`)
for (let i = 10; i<=55; i++ ){
  if (i%2===0 && i !== 16 && i%3!==0){
    console.log(i)
  }
}
console.log('========================')
