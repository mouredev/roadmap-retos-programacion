// tipos de funciones 

// Declaracion de funciones
function saludar (nombre){
  return `Hola, ${nombre}!`;
}
console.log (saludar("javascript"));

//Expreciones de función 

const sumar = function (a, b) {
return a + b ; 

};

console.log(sumar(3, 4));

// funciones flecha (Arrow Functiions)

const multiplicar = (a, b)=> a* b; 
console.log(multiplicar (5, 6));

// Parametros y valores por defecto

function saludarConEdad(nombre = "Invalido", edad=0){
return `Hola ${nombre},tienes ${edad} años.`;
}
console.log(saludarConEdad());

// Funciones con argumentos (Callbacks)

function procesarUsuario(nombre, callback){
 console.log(`Procesado usuario:${nombre}`)
  callback();
  
}

procesarUsuario("Farid", () => {
   console.log("Usuario procesado corectamete.");

});

//Funcion anidadas y alcance (Scope)

function externa(){
let mensaje = "Hola desde externa";

  function interna (){
    console.log(mensaje);
//Puede acceder a variables de externa 

  }
   interna();
}
externa();


// Formas de uso en funsiones 

// Declaracion de Funcion
function saludar(nombre){
   return `Hola, ${nombre}!`;

}
console.log(saludar("jesús"));

//Exprecion de funcion 
const despedir= function (nombre){
   return `Adios, ${nombre}!`;
};

console.log(despedir("Luis"));

//Arrow
const sumart = (a, b)=> a + b;
console.log(sumart(10, 7));

// Callbacks

function procesarUsuario(nombre, callback){
  console.log(`Procesando usuario: ${nombre}`);
  callback();
}

procesarUsuario("Marco",() =>
  console.log("Proceso completo!"));

//Metodos 

const persona= { 
  nombre : "benito", 
                saludar(){
                  console.log(`Hola, soy ${this.nombre}`);
}
               };
persona.saludar();

//IIFE
 (function (){
   console.log("Función autoejecutada");
 
 })();
 //Async/Awaitobter
async function obtenerDatos(){
return "Datos obtenidos";
  
}

obtenerDatos().then(console.log);


//Ejercisio extra 

var pardet = function (FirstText, SecondText){
  var count = 0
for (var i = 1; i <= 100; i++) {
if (i % 3 === 0 && i % 5 === 0){
console.log(FirstText + SecondText);
}
else if (i % 3 === 0){
console.log(FirstText);
}
  else if (i % 5 === 0){
console.log(SecondText);
  }
  else{
    count++;
    console.log(i);
}
  }
console.log('Numeros impresos: ', count);
  return count;
};
pardet ('Par', 'Det');
