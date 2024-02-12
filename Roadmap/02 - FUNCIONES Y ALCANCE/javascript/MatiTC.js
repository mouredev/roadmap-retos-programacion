//#02 FUNCIONES Y ALCANCE
//Algunas de las funciones son las siguientes:

//1. Sin parámetros ni retorno
function saludar(){
    console.log("Hola mundo!"); // imprime: "Hola mundo!"
}
saludar();
console.log(`.........................................`);

//2. Con uno o varios parámetros:
function unaVariableSinRetorno(a){
    console.log("El resultado es: " + a) 
}
function dosVariablesSinRetorno(a, b){
    console.log("El resultado es: " + (a + b)); 
}
unaVariableSinRetorno(2) //imprime: El resultado es: 2
dosVariablesSinRetorno(2, 2) //imprime: El resultado es: 4
console.log(`.........................................`);

//3. Con retorno
function conRetorno(a , b){
    return (a * b);
}
let resultado = conRetorno(2, 3)
console.log("El resultado es: " + resultado); // imprime: El resultado es: 6
console.log(`.........................................`);

//4. Funciones con parámetros por defecto:
function saludarDefault(nombre = "usuario") {
    console.log(`¡Hola, ${nombre}!`);
}
saludarDefault("Matias")  // imprime: "¡Hola. Matias!"
console.log(`.........................................`);

//5. Función flecha con argumentos
let sumaFlecha = (a, b) => a + b;
let resultadoFlecha = sumaFlecha(10, 20);
console.log("El resultado es: " + resultadoFlecha) // imprime: El resultado es: 30
console.log(`.........................................`);

//6. Función que imprime un saludo
let saludarFlecha = () => {
    console.log("Soy una función flecha sin argumentos");
};
saludarFlecha(); // imprime: Soy una función flecha sin argumentos
console.log(`.........................................`);

//Función dentro de otra función
function funcionGrande(num){
    console.log("El numero es ", num) // imprime: El numero es: num
    unaVariableSinRetorno(num)// imprime: El resultado es: num
    console.log(`Multiplicaremos el numero ${num} por 3`); // imprime: Sumaremos en numero num con el 1;
    let multiplicacion = conRetorno(num, 3);
    function doble() {
        return multiplicacion * 2;
    }
    let resultadoDoble = doble();
    return(resultadoDoble);
}
let resultadoFuncionGrande = funcionGrande(7)
console.log(resultadoFuncionGrande);// imprime: 42
console.log(`.........................................`);

//Concepto de variable LOCAL y GLOBAL.
let variableGlobal = "Soy global";

function variables(){
    let variableLocal = "Soy local"
    console.log(variableGlobal); // Accede a la variable global desde fuera
    console.log(variableLocal); // Accede a la variable local desde la propia funcion

    variableGlobal = "Soy la variableGlobal que esta siendo modificada"
}
variables();
console.log(variableGlobal);
//console.log(variableLocal) <--error puesto que esta definida dentro de la funcion variables
console.log(`.........................................`);

//DIFICULTAD EXTRA (opcional):
function dificultadExtra(texto1, texto2) {
    let contador = 0;
    for (let i = 1; i <= 100; i++) {
      if (i % 3 === 0 && i % 5 === 0) {
        console.log(texto1 + texto2);
      } else if (i % 3 === 0) {
        console.log(texto1);
      } else if (i % 5 === 0) {
        console.log(texto2);
      } else {
        console.log(i);
      }
  
      contador++;
    }
    return contador;
  }
  
  // Ejemplo de uso
  const extra = dificultadExtra("Mizz ", "Frizz");
  console.log("Número de veces que se ha impreso: " + extra); //Imprime mucho xd
  