// Tipos de operadores en JavaScript:

// Operadores de Asignacion:

// Operador de asignacion (=):
// Asignando un valor a una variable con =:
let miVariable = "Soy una variable";
console.log(miVariable);
// Operador Asignacion de adicion (+=):
let numeroASumar = 20;
numeroASumar += 1;
console.log(numeroASumar); // 21
// Operador Asignacion de resta (-=):
let numeroARestar = 70;
numeroARestar -= 10;
console.log(numeroARestar); // 60
// Operador Asignacion de multiplicacion (*=):
let numeroAMultiplicar = 60;
numeroAMultiplicar *= 5;
console.log(numeroAMultiplicar); // 300
// Operador Asignacion de division (/=):
let numeroADividir = 40;
numeroADividir /= 2;
console.log(numeroADividir); // 20
// Operador Asignacion de residuo (%=):
let numeroAModular = 30;
numeroAModular %= 3;
console.log(numeroAModular); // 0
// Operador Asignacion de exponenciacion (**=):
let numeroAExponenciar = 12;
numeroAExponenciar **= 5;
console.log(numeroAExponenciar);
// Operador Asignacion de desplazamiento a la izquierda (<<=):
let numeroABinario = 5; // En binario: 101
let vecesADesplazarIzquierda = 3;
numeroABinario <<= vecesADesplazarIzquierda; /* 101000 --> 40 // Los numeros del extremo derecho se pasan a la izquierda y el lugar en donde 
                                    estaban los numeros que se han desplazado se reemplazan por ceros */
console.log(numeroABinario);
// Operador Asignacion de desplazamiento a la derecha (>>=):
let numeroABinario1 = 8; // En binario: 1000
let vecesADesplazarDerecha = 2;
numeroABinario1 >>= vecesADesplazarDerecha; /* 0010  --> 2 // Los numeros del extremo izquierdo se pasan a la derecha y el lugar en donde
                                            estaban los numeros que se han desplazado se reemplazan por ceros*/
console.log(numeroABinario1)
// Operador Asignacion de desplazamiento a la derecha sin signo (>>>=):
let numeroABinarioNegativo = -8;
let vecesADesplazarDerechaSinSigno = 2;
numeroABinarioNegativo >>>= vecesADesplazarDerechaSinSigno; /* 0b00111111111111111111111111111110 --> 1073741822 // Realiza el desplazamiento
                                                            sin importar el signo */
console.log(numeroABinarioNegativo);
// Operador Asignacion AND bit a bit (&=):
let convertirABinarioAND = 8; // --> 0b1000
convertirABinarioAND &= 2; // --> 0b1000 & (AND) 0b0010 --> 00000 --> 0 // Si 0 AND 0 es 0, 1 AND 0 es 0 (Se compara cada bit con AND)
console.log(convertirABinarioAND);
// Operador Asignacion OR bit a bit (|=):
let convertirABinarioOR = 9; // --> 0b1001
convertirABinarioOR |= 3;  // --> 0b1001 | (OR) 0b0011 --> 1011 --> 11 // Si 0 OR 1 es 1, 1 OR 1 es 1 y 0 OR 0 es 0 (Se compara cada bit con OR)
console.log(convertirABinarioOR);
// Operador Asignacion XOR bit a bit (^=):
let convertirABinarioXOR = 11; // --> 0b1011
convertirABinarioXOR ^= 5; // --> 0b1011 ^ (XOR) 0b0101 --> 1110 --> 14 // Si son iguales es 0 y sin diferentes es 1 (Se compara cada bit con XOR)
console.log(convertirABinarioXOR);
// Operador Asignacion OR logico (||=):
let booleanoAAsignar = true;
booleanoAAsignar |= false; // true, Esta comparando con OR: true = true || false --> true
console.log(booleanoAAsignar);
// Operador Asignacion de anulacion logica (??=) // ESTE OPERADOR FUE INTRODUCIDO EN ECMAScript 11, si usas NodeJS tendrias que actualizar a la version MAS RECIENTE
// El operador ?? verifica si el primero operando se undefined o null, si lo es retorna el otro operando. De lo contrario retorna el primer operando
let variableUndefined = undefined;
variableUndefined ??= 4; // -> 4 // Esta comparando si el primer operando es undefined o null si lo es reasignalo con el otro operando que es 4
console.log(variableUndefined);

// Operadores Aritmeticos:

// Suma (+)
let operandoSuma1 = 20;
let operandoSuma2 = 10;
resultadoDeLaSuma = operandoSuma1 + operandoSuma2;
console.log(resultadoDeLaSuma);

// Resta (-)
let operandoResta1 = 30;
let operandoResta2 = 20;
resultadoDeLaResta = operandoResta1 - operandoResta2;
console.log(resultadoDeLaResta);

// Multiplicacion (*)
let operandoMultiplicacion1 = 20;
let operandoMultiplicacion2 = 3;
resultadoDeLaMultiplicacion = operandoMultiplicacion1 * operandoMultiplicacion2;
console.log(resultadoDeLaMultiplicacion);

// Division (/)
let operandoDivision1 = 40;
let operandoDivision2 = 5;
resultadoDeLaDivision = operandoDivision1 / operandoDivision2;
console.log(resultadoDeLaDivision);

// Residuo o Modulo (%):
let dividendo = 20;
let divisor = 4;
let residuo = dividendo % divisor;
console.log(residuo);

// Incremento (++):
let numeroAIncrementar = 20;
numeroAIncrementar++;
console.log(numeroAIncrementar); // 21

// Decremento (--):
let numeroADecrementar = 24;
numeroADecrementar--;
console.log(numeroADecrementar); // 23

// Negacion Unaria (-): // Niega su operando
let numeroANegar = 3;
let numeroNegado = -numeroANegar;
console.log(numeroNegado); // -3

// Positivo Unario (+): // Convierte el operando a Number, si el operando no se puede convertir a Number devolvera NaN
let stringANumero = "20";
let numeroPositivo = +stringANumero;
console.log(numeroPositivo); // 20

// Exponenciacion (**):
let numeroAExponenciar2 = 13;
resultadoDeLaExponenciacion = 13 ** 3;
console.log(resultadoDeLaExponenciacion); // 2197

// Operadores de comparacion: 

// Igual (==): // Este operador convierte los operandos a un tipo comun antes de realizar la comparacion
let valorBooleano = "3" == 3;
console.log(valorBooleano); // Por eso nos devuelve true, ya que convierte el String a Number

// Estrictamente Igual (===): // Este operador no convierte los operandos los compara con sus respectivos tipos de datos (mas recomendable)
let valorEstrictoBooleano = null === undefined;
console.log(valorEstrictoBooleano); // false

// No es igual (No estricto): // Este operador convierte los operandos a un tipo comun antes de comparar si no son iguales
let valorNoEstrictoAlComparar = 4 != "4"; // false, ya que si son iguales, recuerden no es una comparacion estricta
console.log(valorNoEstrictoAlComparar); // false

// Desigualdad Estricta: // Este no convierte a los operandos para hayar desigualdad
let valorEstrictoAlComparar = undefined !== null;
console.log(valorEstrictoAlComparar); // true

// Mayor que (>):
let mayorQue = 20 > 3;
console.log(mayorQue); // true

// Mayor o igual que (>=)
let mayorOIgualQue = 20 >= 20;
console.log(mayorOIgualQue); // true

// Menor que (<):
let menorQue = 10 < 20;
console.log(menorQue) // true

// Menor o igual que (<=):
let menorOIgualQue = 20 <= 10;
console.log(menorOIgualQue); // false

// Operadores bit a bit