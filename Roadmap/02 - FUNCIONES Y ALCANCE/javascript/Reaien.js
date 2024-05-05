//funcion declarada vacia
function vacio() {}
console.log(vacio);
//funcion declarada que retorna un valor
function saludo() {
  return console.log("soy una funcion");
}
//ejecucion de función declarada que retorna un valor
saludo();

//funcion tipo expresión con parametros
let varSumar = function sum2(num1, num2) {
  return num1 + num2;
};
console.log(varSumar(1, 2));

/* 
Función dentro de función
funcionCeption recibe un parámetro y ejecuta la 2da función la cual setea su parámetro
predefinido y junta ambas palabras y los retorna por consola, vuelve a la funcionCeption1 y esta ejecuta la funcionCeption2
*/
let funcionception = (palabra) => {
  let funcionCeption2 = (palabra2) => {
    palabra2 = "mundo";
    console.log(palabra + " " + palabra2);
  };
  return funcionCeption2();
};
//ejecución
funcionception("hola");

//función ya creada en JS charAt
let palabra = "hola mundo";
let charAt = palabra.charAt(1);
console.log(charAt);

//ejercicio dificultad extra
//arrow function
let funcionExtra = (palabra1, palabra2) => {
  for (let i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(`${palabra1 + " " + palabra2 + " " + i}`);
    } else if (i % 3 == 0) {
      console.log(palabra1 + " " + i);
    } else if (i % 5 == 0) {
      console.log(palabra2 + " " + i);
    }
  }
};
/*ejecución de arrow function 
retorna las 2 palabras si ambas condiciones se cumplen
retorna la primera palabra si i es múltiplo de 3
retorna la primera palabra si i es múltiplo de 5
*/
//ejecución de la función
funcionExtra("Hola", "Mundo");
