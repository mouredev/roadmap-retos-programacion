// FUNCIONES BASICAS DE TYPESCRIPT

/* function name(parameter: typeof, parameter: type, ...): returnType{
  do something
} */

// 📌 Funcion Basica sin parametros y sin retorno
function saludar(): void {
  console.log("Hola mundo");
}
saludar();

// 📌 Funcion Basica con parametros y retorno
function suma(a: number, b: number): number {
  return a + b;
}
console.log(suma(3, 2));

// 📌 Funciones dentro de funciones 'CallBacks'

function telefono(llamadas: Function): string {
  llamadas();
  return `Telefono ocupado`;
}

function llamada1() {
  console.log("Estoy en una llamada");
  console.log("Llamada 1 finalizada");
  telefono(llamada2);
}

function llamada2() {
  console.log("Realizando llamada 2");
}
telefono(llamada1);

// 📌 Funciones ya creadas por el Lenguaje

// setTimeOut
setTimeout(() => {
  console.log("Esto es una funcion ya creada por el lengguaje");
  console.log("Se ejecuto despues de 3 segundos...");
}, 3000);

// setInterval
let i = 0;
let interval = setInterval(() => {
  console.log(++i);
}, 1000);

setTimeout(() => {
  clearInterval(interval);
}, 5000);

// Variable Local y globlal
let variableGloblal: string = "Variable Globlal"; // Esta disponible en todo el codigo
function scopeLocal() {
  let variableLocal = "Variable Local"; // Solamente esta disponible en este bloque de codigo {}
  variableGloblal = "Actualizacion de la Variable Global";
  console.log(variableGloblal);
  console.log(variableLocal);
}
// variaableLocal = "Actualizacion de la varibale Local"; //Error: No encuentra la variable
console.log(variableGloblal);
scopeLocal();

/* DIFICULTAD EXTRA (opcional):
 Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
   - La función retorna el número de veces que se ha impreso el número en lugar de los textos */
let count: number = 1;
let multiploNum = (cadena1: string, cadena2: string): number => {
  let contadorNumeros: number[] = [];
  while (count <= 100) {
    if (count % 3 === 0 && count % 5 === 0) {
      console.log(cadena1 + cadena2, count);
    } else if (count % 3 === 0) {
      console.log(cadena1, count);
    } else if (count % 5 === 0) {
      console.log(cadena2, count);
    } else {
      contadorNumeros.push(count);
    }
    count++;
  }
  return contadorNumeros.length;
};
console.log(multiploNum("Hola", "mundo"));
