/*Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...*/

let a = 5; //Asignación
let b = 18;

suma = a + b; //Operador aritmético de suma
console.log("el resultado de sumar " + a, "+ " + b, "es: " + suma);
resta = a - b; // Operador aritmetico resta
console.log("El resultado de restar",a, "-", b," es :" + resta);
multiplicacion = a * b; //Operador aritmetico multiplicación
console.log("El resultado de", a, "x", b, "es : " + multiplicacion);
division = a / b; //Operador  aritmetico de la division
console.log("El resultado de", a, "/", b, "es: " + division);
modulo = a % b; //Operador aritmetico modulo
console.log("El residuo es:" + modulo);
potencia = a ** b; //Operador aritmetico potenciaciado
console.log(a, "elevado a la potencia",b ,"es: " + potencia);

//logicos
verdadero = true;
falso = false;

//and devuelve verdadero solo si las dos condiciones son verdadderas de lo contrario es falso
console.log("")
console.log("Tabla verdad AND");
console.log(verdadero && verdadero);//verdadero
console.log(verdadero && falso);//falso
console.log(falso && verdadero);//falso
console.log(falso && falso);//falso

//or devuelve verdadero si al menos una de las condiciones es verdadera
console.log("")
console.log("Tabla verdad OR");
console.log(verdadero || verdadero);//verdadero
console.log(verdadero || falso);//verdadero
console.log(falso || verdadero);//verdadero
console.log(falso || falso);//falso
