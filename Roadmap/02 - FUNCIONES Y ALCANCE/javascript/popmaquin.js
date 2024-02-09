/*........funciones basicas.......*/

//Sin parametro ni retornos.
function func(){
    console.log("Hola mundo, sin parametro ni retornos!");
}
    func();

    // Con retorno
    function con_retorno() {
        return ("La multiplicación de 5*5 es: "+(5*5)); 
    }
    con_retorno();

//Con uno parametro.
function saludar(name) {
    console.log("Bienvenido " + name);
}
    saludar("Elena"); // Salida: "Bienvenido Elena"

//Con dos argumentos
function sumar(num1, num2) {
    console.log("La suma de " + num1+"+"+ num2+ " es: "+ (num1+num2));
}

sumar(5,5); // 5+5 = 10

//funciones con argumentos y retorno.

let numero1= parseInt(prompt("ingrese un numero: "));          //las variables numero1 y numero2 guardan
let numero2= parseInt(prompt("ingrese el segundo numero: "));  //los valores ingresados por el usuario. Funcion parseInt convierte los valores a enteros.

const funcConArgumentos= function(numero1, numero2) {
    return (numero1+"+"+numero2+" es: "+(numero1+numero2));  
}
funcConArgumentos(numero1,numero2); // se invoca la funcion.


//funciones anonimas
const operacion_suma= function() { 
    return ("Funcion anonima para sumar 5+5 es: "+(5+5));   
}
operacion_suma();  // salida: 10 Se llama por la constante operacion_suma.

// funcion flecha. omite la palabra reservada function por la flecha.
const restar= () =>{ 
    return ("Funcion flecha para restar 5-2 es: "+ (5-2));   
}
restar();

/*.............funciones dentro de funciones.............*/ 

/*Primero se crea una funcion que recibe los datos al usuario.
* Segundo la funcion ingresarDatos... 
* dentro la funccion ingresarDatos se crea la tercera funcion que realiza la suma.
*/
function obtenerdatos(){
    let numero1= parseInt(prompt("ingrese un numero: "));
    let numero2= parseInt(prompt("ingrese el segundo numero: "));
    return [numero1,numero2];
}
function ingresarDatos() {
    let [num1, num2] = obtenerdatos();
    let total=0;
    function opsumar() {
        total= num1+num2;
        console.log("La suma de "+num1 + " + " + num2 + " es: " + total);
    }
    opsumar();
}
ingresarDatos(); // se manda llamar la funcion.

/*.............funciones propias del lenguaje.............*/ 

let cadena = "Hola mundo, Javascript";

console.log(cadena.split(",")); //divide la cadena en un array apartir de un caracter separador. 
                                //Salida: ["hola mundo","Javascript"]

console.log(cadena.substring(0,3)); //extrae la información a opartir de un indece A a B sin incluir.
                                //Salida: Hol

console.log(typeof("20")); //salida: 'string'  ---Indica el tipo de datos.
typeof(parseInt("20")); //salida: number, ---convierte a numero entero.

/*.............variable local y global.............*/

let variable_global= "variable golobal"

function holaMundo() {
    let variable_local= "Hola soy variable local. Ejecucion de la función holaMundo()"
    console.log(variable_local);
    console.log("Soy una variable global. Ejecucion dentro de la función holaMundo() " +variable_global);
    
}
holaMundo();
try {
    console.log( "Accediendo a la viarible local, afuera de la funcion holaMundo() "+ variable_local);
} catch (error) {
    console.log("Imposible acceder a una variable local, fuera de holaMundo()")
}

/*.............Dificultad Extra.............*/ 
/*Imprime numero de 1 hasta 100 pero si es multipo de 3 imprime primer texto, 
* si es multipo de 5 imprime segundo texto y si son ambos concatena textos.
* la variable contador indica la veces que se imprime los numeros.
*/
function generarNumero(txt1, txt2) {
    let contador=0;
      for (let index = 1; index <= 100; index++) {
          if (index%3==0 && index%5==0) {
                  console.log(txt1 + txt2);
          }else if(index%3==0){
              console.log(txt1);
          }else if(index%5==0){
              console.log(txt2);
          }else {
               console.log(index); 
              contador++;
          }
  
            }  
  return (console.log("Total numeros impresos: "+contador)); 
      }
  
  generarNumero("uno", "dos"); // los textos se puede cambiar.

