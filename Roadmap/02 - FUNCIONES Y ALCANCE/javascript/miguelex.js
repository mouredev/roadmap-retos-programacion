// Ejemplo de funcion sin variables ni retorno

function saludo() {
    console.log("Hola");
}

// Ejemplo de funcion con paso de variable y sin retorno

function saludo2(nombre) {
    console.log("Hola " + nombre);
}

saludo2("Migue");

// Ejemplo de funcion con paso de variable y retorno

function saludo3(nombre) {
    return "Hola " + nombre;
}

let msj = saludo3("Migue");
console.log(msj);

// Ejemplo de funcion flecha de funcion sumar

const sumar = (a, b) => {
    return a + b;
}

let suma = sumar(2, 3);

// Ejemplo de funcion creada dentro de otra funcion

function saludoYSuma(a, b) {
    console.log("Hola, vamos a hacer una suma");
    function sumar(a, b) {
        return a + b;
    }
    console.log(sumar(a, b));
}

saludoYSuma(2, 3);

// Ambito global y local de las variables

let variableGlobal = "Soy global";

function mostrarVariableGlobal() {
    console.log(variableGlobal);
}

mostrarVariableGlobal();

function mostrarVariableLocal() {
    let variableLocal = "Soy local";
    console.log(variableLocal);
}

// Ejemplo de funciones del sistema

console.log(parseInt("20"));

// Ejemplo de funcion anonima

let anonima = function() {
    console.log("Soy anonima");
}
anonima();

// Extra

function ejercicioExtra(param1, param2) {
    let numVeces = 0;
    for (let i = 1; i <= 100; i++) {
      if (i % 15 === 0) {
        console.log(param1 + param2);
      } else if (i % 3 === 0) {
        console.log(param1);
      } else if (i % 5 === 0) {
        console.log(param2);
      } else {
        console.log(i);
        numVeces++;
      }
    }
    return numVeces;
  }
  
  const extra = ejercicioExtra("Fizz ", "Buzz");
  console.log("Cantidad de numeros imprimidos =  " + extra)


