/*Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...*/

let a = 5; //Asignación
let b = 18;
let c = 5;
let d = 5.0;

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
console.log(!false)// negacion devuelve verdadero
console.log(!true)// negación devuelve falso
console.log(!!false)//doble negacion devuelve false

//comparacion
console.log("")
console.log("COMPARACIONES");
console.log(a>b);//devuelve falso porque a no es mayor que b
console.log(a<b);//devuelve verdadero 
console.log(a==b);//devuelve falso porque a y b tienen valores diferentes
console.log(a!=b);//devuelve verdadero porque a es distinto de b
console.log(a>=b);//devuelve falso porqueno es mayor o igual que b
console.log(a<=b);//devuelve verdadero porque a es menor o igual a b
console.log(a===b);//devuelve falso 
console.log(a===d);//devuelve verdadero porque son iguales y del mismo tipo
console.log(a!==b); //devuelve verdadero porque son distintos

//pertenencia
console.log("")
console.log("PERTENENCIA");
const lista = [10,20,30];
const string =  "Hola; javascript";
console.log(lista.includes (10));// devuelve true
console.log(lista.includes(40))//devuelve false
console.log (string.includes('o'));//devuelve true
console.log (string.includes('e'));//devuelve false
console.log(string.includes("hola")); //devuelve false porque distingue entre mayusculas y minusculas

//estructuras de control condicional if
console.log("")
puntaje=300;
puntajeNecesario=500;

if(puntaje >= puntajeNecesario){//calcula si el puntaje sacado  es mayor o igual al necesario para ganar
    console .log ("Ganaste el premio!");
}else{
   console.log("No ganaste el premio");  
}

clima = "nublado";
if (clima === "soleado"){
    console.log("Es un dia hermoso para salir.");
} else if (clima ==="lluvioso" || clima=="nublado") {
    console.log("Vamos a llevar un paraguas.")
} else {
    console.log("no tenemos datos exactos del clima.")
}

//estructura de control repetitiva
numero = 0;
while (numero <= 5){
    console.log(numero);
    numero= numero +1 ;
}

//estructura de control iterativa
for (i=0;i < string.length;i++){//recorre  cada letra de la cadena de texto e imprime cada caracter
    console.log(string[i]);
}

/*DIFICULTAD EXTRA (opcional):
Crea un programa que imprima por consola todos los números comprendidos
entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3 */

for (let i = 10; i<=55; i++) {
    if (i % 2===0 && i !== 16 && i %  3!==0) {
        console.log(i);
    }        
}