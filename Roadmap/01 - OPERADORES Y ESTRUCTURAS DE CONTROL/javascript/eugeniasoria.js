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

//Ejemplos utilizando todos los tipos de operadores del lenguaje
// Assignment operators
let variable = 5;
console.log(">>>Operadores de Asignación");
console.log("Assignment 'variable = 5' =>", variable);
console.log("Addition Assignment 'variable += 3' =>", (variable += 3));
console.log("Subtraction Assignment 'variable -= 1' =>", (variable -= 1));
console.log("Multiplication Assignment 'variable *= 2' =>", (variable *= 2));
console.log("Division Assignment 'variable /= 2' =>", (variable /= 2));
console.log("Remainder Assignment 'variable %= 4' =>", (variable %= 4));
console.log("Exponentiation Assignment 'variable **= 3' =>", (variable **= 3));
console.log("Left Shift Assignment 'variable <<= 2' =>", (variable <<= 2));
console.log("Right Shift Assignment 'variable >>= 2' =>", (variable >>= 2));
console.log("Unsigned Right Shift Assignment 'variable >>>= 2' =>", (variable >>>= 2));
console.log("Bitwise AND assignment 'variable &= 3' =>", (variable &= 3));
console.log("Bitwise XOR assignment 'variable ^= 5' =>", (variable ^= 5));
console.log("Logical AND assignment  'variable &&= 1' =>", (variable &&= 1));
console.log("Logical OR assignment  'variable ||= 0' =>", (variable ||= 0));
console.log("Nullish coalescing assignment  'variable ??= 0' =>", (variable ??= 15));
console.log("\n")
console.log(">>>Operadores de Comparación");
console.log("Equal '1 == 2' => ", 1 == 2);
console.log("Not equal '1 != 2' => ", 1 != 2);
console.log(`Strict equal '1 === \"2\"' => `, 1 === "2");
console.log(`Strict not equal '1 !== \"2\"' => `, 1 === "2");
console.log("Greater than '1 > 2' => ", 1 > 2);
console.log("Less than '1 < 2' => ", 1 < 2);
console.log("Greater than or equal '1 >= 2' => ", 1 >= 2);
console.log("Less than or equal '1 <= 2' => ", 1 <= 2);

let x=10;
console.log("\n")
console.log(">>>Operadores Aritméticos");
console.log("Remainder 'x=10; x % 3' =>", (x % 3));
x=10; x++;
console.log("Increment 'x=10; x++' =>", (x));
x=10; x--;
console.log("Decrement 'x=10; x--' =>", (x));
x=10;
console.log("Unary negation 'x=10; -x' =>", (-x));
x="10"
console.log("Unary plus 'x=\"10\"; +x' =>", (+x));
console.log("Exponentiation operator 'x=10; x**2' =>", (x**2));

console.log("\n")
console.log(">>>Operadores Bitwise");
let a = 5;
let b = 3; 
console.log("a = 5 => 00000000000000000000000000000101");
console.log("b = 3 => 00000000000000000000000000000011");
console.log("Bitwise AND 'a & b' => 00000000000000000000000000000001 =>", a & b);
console.log("Bitwise OR 'a | b' => 00000000000000000000000000000111 =>", a | b);
console.log("Bitwise XOR 'a ^ b' => 00000000000000000000000000000110 =>", a ^ b);
console.log("Left shift 'a << b' => 00000000000000000000000000101000 =>", a << b);
b = 2;
let c = -5;
console.log("a = 5 => 00000000000000000000000000000101");
console.log("b = 2 => 00000000000000000000000000000010");
console.log("c = -5 => 11111111111111111111111111111011");
console.log("Right shift 'a >> b' => 00000000000000000000000000000001 =>", a >> b);
console.log("Right shift 'c >> b' => 00000000000000000000000000000000 =>", c >> b);
console.log("Unsigned Right shift 'a >> b' => 00000000000000000000000000000001 =>", a >>> b);
console.log("Unsigned Right shift 'c >> b' => 00111111111111111111111111111110 =>", c >>> b);

console.log("\n")
console.log(">>>Operadores Bitwise Lógicos");
a = 15;
b = 9;
console.log("a = 15 => 00000000000000000000000000001111");
console.log("b = 9 => 00000000000000000000000000001001");
console.log("a & b => 1001", a & b);
console.log("a | b => 1111", a | b);
console.log("a ^ b => 0110", a ^ b);
console.log("~a => 11111111111111111111111111110000", ~a);
console.log("~b => 11111111111111111111111111110110", ~b);

console.log("\n")
console.log(">>>Operadores Lógicos");
const exprTrue = true;
const exprFalse = false;
console.log("Logical AND");
console.log("exprTrue && exprTrue => ", exprTrue && exprTrue);
console.log("exprTrue && exprFalse => ", exprTrue && exprFalse);
console.log("exprFalse && exprFalse => ", exprFalse && exprFalse);
console.log("Logical OR");
console.log("exprTrue || exprTrue => ", exprTrue || exprTrue);
console.log("exprTrue || exprFalse => ", exprTrue || exprFalse);
console.log("exprFalse || exprFalse => ", exprFalse || exprFalse);
console.log("Logical NOT");
console.log("!exprTrue => ", !exprTrue);
console.log("!exprFalse => ", !exprFalse);

console.log("\n")
console.log(">>>Operadores BigInt");
console.log("Son los mismos que para Number, pero no se puede mezclar números de distinto tipo. Ambos deben ser BigInt")
const aBigInt = BigInt(123654789321456);
const bBigInt = 999999999999999n;
console.log("Operador + (por citar un ejemplo)");
console.log("aBigInt = BigInt(123654789321456)");
console.log("bBigInt = 999999999999999n"); 
console.log("aBigInt + bBigInt => ", aBigInt + bBigInt );

console.log("\n")
console.log(">>>Operadores String");
const aString = 'Carpe';
const bString = 'Diem';
console.log("aString = 'Carpe';")
console.log("bString = 'Diem'")
console.log("Operador +");
console.log("'aString + bString' =>", aString + bString);

console.log("\n")
console.log(">>>Operadores Condicional Ternario");
const edad = 100;
console.log("condicion ? val1 : val2");
console.log("edad = 100 => ", edad > 100 ? 'en serio?' : 'todavia joven :)');

console.log("\n")
console.log(">>>Operador Coma");
console.log("for (let a = 0, b =5; a <= 5; a++, b--) { "+
            "\n    console.log(a, b); '"+
            "\n}")

for (let a = 0, b =5; a <= 5; a++, b--) { 
  console.log(a, b); 
}

console.log("\n");
console.log(">>>Operadores Unarios");
console.log("Operador delete")
const developer = {
  name: 'Luna',
  apellido: 'Margarita'
};
console.log("const developer = { name: 'Luna', apellido: 'Margarita' }; => ", developer);
delete developer.name;
console.log("delete developer.name => ", developer);


console.log('\nOperador typeof')
const unaFuncion = new Function(2 + 5);
const unaString = "palabra";
const unNumero = 159;
const unArray = [4, 8, 15, 16, 23, 42, 108];
const unaFecha = new Date();

console.log("const unaFuncion = new Function(2 + 5);");
console.log('const unaString = "palabra";');
console.log("const unNumero = 159;");
console.log("const unArray = [4, 8, 15, 16, 23, 42, 108];");
console.log("const unaFecha = new Date();");

console.log("typeof unaFuncion => ", typeof unaFuncion);
console.log("typeof unaString => ", typeof(unaString));
console.log("typeof unNumero => ", typeof(unNumero));
console.log("typeof unArray => ", typeof(unArray));
console.log("typeof unaFecha => ", typeof(unaFecha));

console.log("\nOperador void")
console.log("void (4 ===\"4\") => ", void (4 ==="4"));

console.log("\n");
console.log(">>>Operadores Relacionales");
console.log('\nOperador in');
const perritos = ['Ash', 'Luna', 'Alma', 'Dana', 'Sami', 'Camila', 'Priscila'];
console.log('perritos = ', perritos);
console.log("'Firulais' in perritos => ", 'Firulais' in perritos);
console.log("'Ash' in perritos => ", 'Ash' in perritos);
console.log("4 in perritos => ", 4 in perritos);

console.log('\nOperador instanceof')
const dia = new Date();
console.log("dia = new Date();");
console.log("dia instanceof Date => ", dia instanceof Date);
console.log("dia instanceof BigInt => ", dia instanceof BigInt);


console.log("\n-----------------------------------------------")
console.log(">>>Estructuras de Control");

console.log('Loops and Iteration');
console.log("\nfor statement");
console.log('for (let i=5; i>0; i--){'+
'\n    console.log(\"Cuenta regresiva: \", i);'+
'\n}');
for (let i=5; i>0; i--){
  console.log("Cuenta regresiva: ", i);
}

console.log("\ndo...while statement");
console.log('let i = 0;'+
'\nlet valorMaximo = 10;'+
'\ndo {'+
'\n    console.log(`Valor de i: ${i});'+
'\n    i++;'+
'\n} while (i <= valorMaximo);');
let i = 0;
let valorMaximo = 10;
do {
  console.log(`Valor de i: ${i}, <= ${valorMaximo}`);
  i++;
} while (i <= valorMaximo);

console.log("\nwhile statement");
console.log('i = 0;' + 
'\nwhile (i <= valorMaximo) {' +
'\n  console.log(`Valor de i: ${i}, <= ${valorMaximo}`);' +
'\n  i++;' +
'\n}');
i = 0;
while (i <= valorMaximo) {
  console.log(`Valor de i: ${i}, <= ${valorMaximo}`);
  i++;
}

console.log("\nlabeled statement");

console.log('let sum = 0, a = 1;' + 
'\n// Label for outer loop' +
'\nouterloop: while (true) {' + 
'\n    a = 1;' + 
'\n ' + 
'\n    // Label for inner loop' + 
'\n    innerloop: while (a < 3) {' + 
'\n        sum += a;' + 
'\n        if (sum > 12) {' + 
'\n ' + 
'\n            // Break outer loop from inner loop' + 
'\n            break outerloop;' + 
'\n        }' + 
'\n        console.log("sum = " + sum);' + 
'\n        a++;' + 
'\n    }' + 
'\n}');
let sum = 0, aLabel = 1;
// Label for outer loop
outerloop: while (true) {
  aLabel = 1;
 
    // Label for inner loop
    innerloop: while (aLabel < 3) {
        sum += aLabel;
        if (sum > 12) {
 
            // Break outer loop from inner loop
            break outerloop;
        }
        console.log("sum = " + sum);
        aLabel++;
    }
}

console.log("\nbreak statement");
console.log('for (let i = 0; i < 10; i++) {'+
'\n    console.log("foor loop de 1 a 10, valor: ", i);'+
'\nif (i === 3) {'+
'\n    console.log("break");'+
'\n    break;'+
'\n}');
for (let i = 0; i < 10; i++) {
  console.log("foor loop de 1 a 10, valor: ", i);
  if (i === 3) {
    console.log("break");
    break;
  }
}

console.log("\ncontinue statement");
console.log('i = 0; valorMaximo = 10' +
'\nwhile (i <= valorMaximo) {  ' + 
'\n  i++;' + 
'\n  if (i > 3) {' + 
'\n    console.log("continue");' + 
'\n    continue;' + 
'\n  }  ' + 
'\n  console.log(`while loop de 1 a 10, valor ${i}`);' + 
'\n}');
i = 0;
while (i <= valorMaximo) {  
  i++;
  if (i > 3) {
    console.log("continue");
    continue;
  }  
  console.log(`while loop de 1 a 10, valor ${i}`);
}

console.log("\nfor...in statement");
console.log('const gato = { color: \'blanco\', nombre: \'Ele\', descripcion: \'hermosa\'};' + 
'\nfor (const g in gato)' + 
'\n    console.log(`${g}: ${gato[g]}`);' + 
'\n');
const gato = { color: 'blanco', nombre: 'Ele', descripcion: 'hermosa'};
for (const g in gato)
  console.log(`${g}: ${gato[g]}`);


console.log("\nfor...of statement");
console.log("const arr = [a', 'b', 'c', 'd'];" + 
'\nfor (const letra of arr) ' + 
'\n    console.log(letra)');
const arr = ['a', 'b', 'c', 'd'];
for (const letra of arr) 
  console.log(letra)


console.log("\n-----------------------------------------------")
console.log(">>>Estructuras Condicionales");

console.log("\nif...else statement");
console.log("let color = 'blanco';" +
"\nif (color === 'blanco') " + 
'\n{' + 
"\n   console.log('Esto es blanco');" + 
'\n} else {' + 
"\n   console.log('Esto es negro');" + 
'\n}');
console.log('OUTPUT: ');
let color = 'blanco';
if (color === 'blanco') 
{
  console.log('Esto es blanco');
} else {
  console.log('Esto es negro');
}


console.log("\nswitch statement");
console.log("let eleccion = 2;" + 
"\nlet respuesta = '';" + 
"\nswitch(eleccion) {" + 
"\n  case 1: " + 
"\n    respuesta = 'uno'" + 
"\n    break;" + 
"\n  case 2: " + 
"\n    respuesta = 'dos'" + 
"\n    break;" + 
"\n  case 3: " + 
"\n    respuesta = 'tres'" + 
"\n    break;" + 
"\n  default:" + 
"\n    console.log('No conozco ese valor');" + 
"\n}");
console.log('OUTPUT: ');
let eleccion = 2;
let respuesta = '';
switch(eleccion) {
  case 1: 
    respuesta = 'uno'
    break;
  case 2: 
    respuesta = 'dos'
    break;
  case 3: 
    respuesta = 'tres'
    break;
  default:
    console.log('No conozco ese valor');
}
console.log(`Tu elección ${eleccion} es ${respuesta}`);


console.log("\n-----------------------------------------------")
console.log(">>>Manejo de Excepciones");

console.log("\nthrow");
console.log('Solo muestro código porque si arrojo la excepción, la ejecución se detiene');
console.log('throw "Error2"; // String type' + 
'\nthrow 42; // Number type' + 
'\nthrow true; // Boolean type' + 
'\nthrow {' + 
'\n  toString() {' + 
'\n    return "Soy un objeto";' + 
'\n  },' + 
'\n};')

console.log('\ntry...catch statement');
console.log('let valor1=0, valor2=0;' + 
'\nlet resultado =0;' + 
'\ntry {' + 
"\n  if (valor2 === 0) throw 'Division por cero'" + 
'\n  resultado = valor1/valor2;' + 
'\n  console.log(resultado);' + 
'\n} catch (error) {' + 
'\n  console.log(error);' + 
'\n}');
console.log('OUTPUT: ');
let valor1=0, valor2=0;
let resultado =0;
try {
  if (valor2 === 0) throw 'Division por cero'
  resultado = valor1/valor2;
  console.log(resultado);
} catch (error) {
  console.log(error);
}

console.log('\nfinally block');
console.log('let valor1=0, valor2=0;' + 
'\nlet resultado =0;' + 
'\ntry {' + 
"\n  if (valor2 === 0) throw 'Division por cero'" + 
'\n  resultado = valor1/valor2;' + 
'\n  console.log(resultado);' + 
'\n} catch (error) {' + 
'\n  console.log(error);' + 
'\n} finally {' +
"\n  console.log('Este bloque se ejecuta haya o no error');" +
'\n}');
console.log('OUTPUT: ');
try {
  if (valor2 === 0) throw 'Division por cero'
  resultado = valor1/valor2;
  console.log(resultado);
} catch (error) {
  console.log(error);
} finally {
  console.log('Este bloque se ejecuta haya o no error');
}


console.log("\n-----------------------------------------------")
console.log(">>>DIFICULTAD EXTRA");

let numero = 10;
while (numero >= 10 && numero <=55) {

  if (numero % 2 === 0) {
    if (numero %3 != 0) {
      if (numero !=16) {        
        console.log(numero);
      }
    }
  }
  numero++;
}