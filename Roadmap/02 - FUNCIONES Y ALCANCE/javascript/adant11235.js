//FUNCIONES BASICAS   
//Definidas por el usuario


//simple

function saludar() {
  console.log("Hola Javascript");
}
saludar();


//con retorno

let hola = "Hola Adant"

function returnSaludo() {
  console.log(hola);
  return hola;
}
saludar();
returnSaludo();

console.log("<br>");

function retSaludo()  {
  return "Hola Adant"
}
console.log(retSaludo());


//con argumento

function argSaludo(name) {
  console.log(`Hola ${name}`)
}
argSaludo("Brais");


//con un argumento predetermindao

function defSaludo(lenguaje ="Java") {
  console.log(`Hola ${lenguaje}`)
}
defSaludo();
defSaludo("Javascript");

console.log("<br>");


//con numero variable de argumentos

function varArgSaludo(...nombres) {
  for(nombre of nombres) {
    console.log(`Hola ${nombre} !`)
  }
}
varArgSaludo("Adant", "Javascript", "Brais");

console.log("<br>");


//funcines asignadas a constantes

const constSaludo = function (name) {
  console.log(`Holaaa ${name}`)
}
constSaludo("Adant");


//arrows

const flechaSaludo = (name) => {
  console.log(`Hola ${name}`)
}
flechaSaludo("Adanta");


let flecha2Saludo = (name) => console.log(`Hola holita ${name}`);

flecha2Saludo("Javascript");


console.log("<br>");


//FUNCIÖN DENTRO DE OTRA FUNCIÖN

function outerFunc() {
  function innerFunc() {
    console.log("Hola función interna");
  }innerFunc();
}
outerFunc();

console.log("<br>");


//EJEMPLOS DEFUNCIONES PROPRIA DEL LENGUAJE  (BUILT-IN)   METODOS

console.log("Hola");

console.log(typeof("23"));
console.log(parseFloat("23"));

console.log(parseInt("32"));
console.log(typeof(32));

console.log(isNaN("32"));
console.log(isNaN(32));
console.log(isNaN("Hola"));

console.log(Math.max(2, 3, 10));

console.log(Math.round(1,19));

console.log(Math.PI);

console.log(Date());


console.log("<br>");


//Ambito (scope)

//var GLOBAL = fuera de una función

let globVar = "Javascript";   //global
console.log(globVar);

function hiJava() {
  console.log(`Hola ${globVar}`);
}
hiJava();

//var LOCAL = dentro de la función

function hiLocalJava() {
  locVar = "Hola";    //local
  console.log(`${locVar} ${globVar}`);
}
hiLocalJava();

console.log(locVar);
//En Javascript se puede llamar una var interna desde fuera de la func

console.log("<br>");


//Dificultad EXTRA


function contNum(a = "a", b = "b") {
  let counter = 0
  for(let num = 1; num <= 100; num++) {
    
  if(num % 3 === 0 && num % 5 === 0) {
    console.log(a + b);
  } else if(num % 5 === 0) {
      console.log(b);
  } else if(num % 3 === 0) {
      console.log(a);
  } else{
      console.log(num);
      counter++
    }
  } console.log(`Se han contado numeros ${counter} veces`);
}
contNum();


