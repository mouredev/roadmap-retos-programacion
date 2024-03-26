

let pi = 3.14; // Variable global

// Ejemplo 1: Función sin parámetros ni retorno
function saludar() {
    console.log("Hola, ¿cómo estás?");
}

// Ejemplo 2: Función con parámetros
function suma(a, b) {
    return a+b;
}

// Ejemplo 3: Función con parámetros y retorno
function resta(a, b) {
    return a - b;
}

// Ejemplo 4: Función que retorna el área de un círculo utilizando la variable global pi
function areaCir(r) {
    return pi * (r ** 2);
}

// Ejemplo 5: Función que retorna el área de un círculo utilizando una variable local pi
function areaCir2(r) {
    let pi = 3.1415; // Variable local
    return pi * (r ** 2);
}

// Ejemplo 6: Función dentro de una función
function operaciones(a,b) {
    function multiplicar() {
        return a * b;
    }
    console.log(`${a} por ${b} es ${multiplicar()}`); // Llamada a la función interna

    function dividir() {
      return a / b;
    }
    console.log(`${a} dividido ${b} es ${dividir()}`); // Llamada a la función interna

  function restar() {
    return a - b;
  }
  console.log(`${a} menos ${b} es ${restar()}`); // Llamada a la función interna

  function potencia() {
    return a** b;
  }
  console.log(`${a} elevado a la ${b} es ${potencia()}`); // Llamada a la función interna
}


// Ejemplo de función ya creada en el lenguaje: Math.round()
function redondear(numero) {
    return Math.round(numero);
}

// Prueba de variables LOCAL y GLOBAL
console.log(pi); // Muestra la variable global pi
function probarScope() {
    let pi = 3.141592653589793; // Variable local
    console.log(pi); // Muestra la variable local pi
}

// Llamadas a las funciones
saludar();
console.log(`la suma de los parametros es ${suma(5, 8)}`);//devuelve 13
console.log(resta(8, 6));//devuelve 2
console.log(areaCir(2));
console.log(areaCir2(2));
let resultsuma = suma(5,8);//almacenamos e resultado de la suma en una variable
let resultresta = resta(8,6);//almaceamos el resultado de la resta en una variable
operaciones(6,3);
operaciones(resultsuma,resultresta);//usamos las variables que almacenamos en las operaciones
console.log(redondear(3.1415));
probarScope();
console.log(pi); // Muestra la variable global pi nuevamente