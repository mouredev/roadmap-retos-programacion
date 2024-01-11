//Sin parametros ni return
function holaMundo(){
    console.log("Hola Mundo!");
}
holaMundo();

//Con parametros y return
function concatenaTexto(a, b){
    return a+b;
}
console.log(concatenaTexto("Hola! Soy ", "N1sek"));

//Funcion con varios parametros
function variosParametros(...args){
    for(let i = 0; i<args.length;i++){
        console.log(args[i])
    }
}
variosParametros(1, 2, 3, 4);

//Funciones anidadas
function funcionUno(){
    console.log("Hola desde funcionUno");

    function funcionDos(){
        console.log("Hola desde funcionDos")
    }

    funcionDos(); //Estamos llamando la funcion dos dentro de funcionUno por lo que si funciona
}
funcionUno();
//funcionDos(); No funcionaria porque solamente existe dentro de funcionUno

//Funcion 'Built-in'
let variableNumerica = 2
let variableTexto = "Hola"
console.log("variableNumerica: " + typeof(variableNumerica) + " variableTexto: " + typeof(variableTexto))

//Variable global
let global = "Soy una variable global"
function variableGlobal(){
    console.log(global)
}
variableGlobal();
console.log(global)

//Variable local
function variableLocal(){
    let local = "Soy una variable local"
    console.log(local)
}
variableLocal();
//console.log(local); // No funciona porque la variable solo existe dentro de la funcion

//Funcion flecha sin argumentos
const flechaSinArgumentos = () => console.log("Soy una funcion flecha sin argumentos")
flechaSinArgumentos();

//Funcion flecha con argumentos
const flechaConArgumentos = (str1, str2) => str1+str2; //Return implicito
console.log(flechaConArgumentos("Soy una funcion flecha", " con argumentos"))

//Funcion flecha con varios argumentos
const flechaConVariosArgumentos = (...args) => {
    for(let i = 0; i<args.length; i++){
        console.log(args[i])
    }
}
flechaConVariosArgumentos(1, "Hola", 2345);

//Funciones flecha anidadas
const flechaAnidada = (a) => (b) => a+b
console.log(flechaAnidada(2)(5))

//Funcion flecha variable global
const flechaGlobal = () => global
console.log(flechaGlobal())

//Funcion flecha variable local
const flechaLocal = () => {
    let local = "Hola desde funcion flecha local"
    return local
}
console.log(flechaLocal())

/* DIFICULTAD EXTRA */

function ejercicioExtra(arg1, arg2) {
    try{
        if(typeof(arg1) != "string" || typeof(arg2) != "string"){
            throw new Error("Error: uno de los parametros no es texto")
        }

        let contador = 0
        for(let i = 0; i<100; i++){
            if(i % 3 == 0 && i % 5 == 0){
                console.log(arg1,arg2)
            } else if(i % 3 == 0){
                console.log(arg1)  
            } else if(i % 5 == 0){
                console.log(arg2)
            } else{
                console.log(i)
                contador++
            }
        }
        return contador

    }catch(error){
        console.log(error.message)
    }
}

console.log("Se han imprito los numeros " + ejercicioExtra("Roadmap JavaScript", "2024 by MoureDev") + " veces")