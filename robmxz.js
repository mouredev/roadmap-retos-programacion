// Reto #01 -> OPERADORES Y ESTRUCTURAS DE CONTROL

// Operadores

// 1. Aritméticos

// 1.1 Suma "+"
let suma = 1 + 2; // Suma los valores 1 y 2
console.log("Resultado de la suma:", suma);

// 1.2 Resta "-"
let resta = 24 - 20; // Resta los valores 24 y 20
console.log("Resultado de la resta:", resta);

// 1.3 Multiplicación "*"
let multiplicacion = 2 * 4; // Multiplica los valores 2 y 4
console.log("Resultado de la multiplicación:", multiplicacion);

// 1.4 División "/"
let division = 10 / 2; // Divide los valores 10 y 2
console.log("Resultado de la división:", division);

// 1.5 Módulo "%"
let modulo = 10 % 3; // Obtiene el residuo de la división de los valores 10 y 3
console.log("Resultado del módulo:", modulo);

// 1.6 Exponenciación "**"
let exponenciacion = 2 ** 3; // Eleva el valor 2 a la potencia 3
console.log("Resultado de la exponenciación:", exponenciacion);

// 2. Lógicos

// 2.1 AND "&&" -> compara si las 2 condiciones son verdaderas
let and = 2 > 1 && 24 < 20;
console.log("Resultado del operador &&:", and);

// 2.2 OR "||" -> compara si al menos una de las 2 condiciones es verdadera
let or = 2 > 1 || 24 < 20;
console.log("Resultado del operador ||:", or);

// 2.3 NOT "!" -> niega el valor de la condición
let not = !(24 < 20);
console.log("Resultado del operador !:", not);

// 3. Comparación

// 3.1 Igualdad "==" -> compara si los valores son iguales
let igualdad = 1 == 1;
console.log("Resultado del operador =:", igualdad);

// 3.2 Desigualdad "!=" -> compara si los valores son diferentes
let desigualdad = 24 != 20;
console.log("Resultado del operador !=:", desigualdad);

// 3.3 Estrictamente igual "===" -> compara si los valores y tipos de datos son iguales
let estrictamenteIgual = 20 === "20";
console.log("Resultado del operador ===", estrictamenteIgual);

// 3.4 Estrictamente desigual "!==" -> compara si los valores y tipos de datos son diferentes
let estrictamenteDesigual = "24" !== 24; 
console.log("Resultado del operador !==:",estrictamenteDesigual);

// 3.5 Mayor que ">" -> compara si el valor de la izquierda es mayor que el de la derecha
let mayorQue = 24 > 20;
console.log("Resultado del operador >:", mayorQue);

// 3.6 Menor que "<" -> compara si el valor de la izquierda es menor que el de la derecha
let menorQue = 20 < 24;
console.log("Resultado del operador <:", menorQue);

// 3.7 Mayor o igual que ">=" -> compara si el valor de la izquierda es mayor o igual que el de la derecha
let mayorIgual = 20 >= 20;
console.log("Resultado del operador >=:", mayorIgual);

// 3.8 Menor o igual que "<=" -> compara si el valor de la izquierda es menor o igual que el de la derecha
let menorIgual = 24 <= 24;
console.log("Resultado del operador <=:", menorIgual);

// 4. Asignación

// 4.1 Asignación básica "="
let asignacion = "Hola";
console.log("Valor de la variable:", asignacion);

// 4.2 Asignación de adición "+=" -> (a = a + b)
let asignacionAdicion = 3;
asignacionAdicion += 6;
console.log("Valor de la variable:", asignacionAdicion);

// 4.3 Asignación de sustracción "-=" -> (a = a - b)
let asignacionSustraccion = 3;
asignacionSustraccion -= 1;
console.log("Valor de la variable:",asignacionSustraccion);

// 4.4 Asignación de multiplicación "*=" -> (a = a * b)
let asignacionMultiplicacion = 3;
asignacionMultiplicacion *= 2;
console.log("Valor de la variable:",asignacionMultiplicacion);

// 4.5 Asignación de división "/=" -> (a = a / b)
let asignacionDivision = 8;
asignacionDivision /= 2; // Divide el valor 2 a la variable
console.log("Valor de la variable:", asignacionDivision);

// 5. Ternario "?"
let ternario = 24 > 20 ? "Verdadero" : "Falso"; // Si 24 es mayor que 20, asigna "Verdadero", de lo contrario asigna "Falso"
console.log("Resultado del operador ternario:", ternario);

// 6. Operadores de bits

// 6.1 AND "&" -> compara bit a bit si ambos son "1" retorna 1 de lo contario 0
let bitAnd = 0b1111 & 0b1001;
console.log("Resultado del operador &:", bitAnd.toString(2));

// 6.2 OR "|" -> compara si al menos uno de los bits son "1" retorna 1 de lo contrario 0
let bitOr = 0b1111 | 0b1001;
console.log("Resultado del operador |:", bitOr.toString(2));

// 6.3 XOR "^" -> retorna 1 si los bits son diferentes de lo contrario 0
let bitXor = 0b1111 ^ 0b1001;
console.log("Resultado del operador ^:", bitXor.toString(2));

// 6.4 NOT "~" -> cambia el valor de los bits a su opuesto 1 por 0 y 0 por 1
let bitNot = ~0b1111;
console.log("Resultado del operador ~:", bitNot.toString(2));

// 6.5 Desplazamiento a la izquierda "<<" -> desplaza los bits a la izquierda y los restantes se llenan con 0
let bitDesplazamientoIzquierda = 0b1111 << 2;
console.log("Resultado del operador <<:",bitDesplazamientoIzquierda.toString(2));

// 6.6 Desplazamiento a la derecha ">>" -> desplaza los bits a la derecha y los restantes se llenan con 0
let bitDesplazamientoDerecha = 0b1111 >> 2;
console.log("Resultado del operador >>:", bitDesplazamientoDerecha.toString(2));

// Estructuras de control

// 1. if
if (10 > 4) {
  console.log("Verdadero");
}

// 2. if else
if (4 > 10) {
  console.log("Verdadero");
} else {
  console.log("Falso");
}

// 3. switch
let opcion = 1;
switch (opcion) {
  case 1:
    console.log("Opción 1");
    break;
  case 2:
    console.log("Opción 2");
    break;
  default:
    console.log("Opción no válida");
    break;
}

// 4. for
for (let i = 1; i <= 10; i++) {
  console.log("Valor actual de i:", i);
}

// 5. while
let condicion = true;
while (condicion) {
  console.log("Ciclo while");
  condicion = false;
}

// 6. do while
let condicion2 = false;
do {
  console.log("Ciclo do while");
} while (condicion2);

// Dificultad extra :)

/*
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
*/

function extra(a,b){
    for(let i = a; i <= b; i++){
        if(i % 2 == 0 && i != 16 && i % 3 != 0){
        console.log("Número :",i);
        }
    }
}
extra(10,55);
