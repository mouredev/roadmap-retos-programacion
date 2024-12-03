let clientes:string[]=["Roberto", "Sara"];

function addCliente(nombre:string){
    if(nombre.length>0){
        clientes.push(nombre);
    }
    console.log(`\nel cliente ${nombre} agregado:`)
    console.log(clientes)
}
function removePila(){
    clientes.pop();
    console.log("\nRemoviendo último cliente:")
    console.log(clientes)
}

function removeToCola(){
    clientes.shift();
    console.log("\nRemoviendo el primer cliente:")
    console.log(clientes)
}

addCliente("Carlos");
removePila(); 
addCliente("Rodrigo");
removeToCola();


//EXTRA PILAS***************************************
var prompt = require("prompt-sync")();
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let paginasWeb:string[]=["google.com"];

console.log("*****Navegando entre páginas*****")
console.log(`\nintroduzca la palabra "atras" o "adelante" para navegar entre las páginas.
            cualquier otra palabra introducida servirá para agregar una página nueva a la pila de páginas.
            escriba "salir" para terminar el programa.`)
console.log("\npáginas actuales:")
console.log(paginasWeb);

let currentPage:number=0;
let accion:string="";

function iniciarPila(){
    accion=prompt("Introduzca una palabra: ");
    if(accion.trim().length<=0){
        console.log("La palabra no puede estar vacía, inténtalo de nuevo")
    }
    if(accion.trim().toLowerCase()=="atras"){
       volverAtras();
       iniciarPila();
    } else if(accion.trim().toLowerCase()=="adelante"){
       irAdelante();
       iniciarPila();
    } else if(accion.trim().toLowerCase()=="salir"){
        rl.close();
    } else {
        agregarPagina();
        iniciarPila();
    }
}

function volverAtras(){
    if(currentPage<=0){
        return console.log(paginasWeb[0]);
    }
    else{
        currentPage--;
        return console.log(paginasWeb[currentPage]);
    }
}

function irAdelante(){
    if(currentPage>=paginasWeb.length-1){
        return console.log(paginasWeb[paginasWeb.length-1]);
    } else{
        currentPage++;
        return console.log(paginasWeb[currentPage]);
    }
}

function agregarPagina(){
    paginasWeb.push(accion);
    console.log(`Nueva página ${accion} agregada:`)
    console.log(paginasWeb);
}

//EXTRA COLAS***************************************
let colaImpresion:string[]=["Hoja1"];
console.log("\n******************Impresión de documentos******************")
console.log(`Documentos en cola actualmente: ${colaImpresion}`);
console.log(`Si desea agregar una hoja a la cola de impresión escriba el nombre del documento, 
        si desea imprimir la última hoja en la cola escriba "imprimir",
        si desea salir de la aplicación escriba "salir".\n`)

function iniciarCola(){
    let respuesta=prompt(`Introduzca la acción deseada: `)
    if(validarRespuesta(respuesta)){
        switch (respuesta.trim().toLowerCase()) {
            case "imprimir":
                imprimir();
                iniciarCola();
                break;
            case "salir":
                rl.close();
                break;
            default:
                agregarAlaCola(respuesta);
                iniciarCola();
                break;
        }
    }
}
function validarRespuesta(res:string):boolean{
    if(res.trim().length<=0){
        console.log("\nLa respuesta no puede ser vacía, inténtalo de nuevo.")
        return false;
    } else {
        return true;
    }
}

function imprimir(){
    if(colaImpresion.length<0){
        console.log("\nNo hay documentos en cola para imprimir.");
    } else {
        console.log(`\nDocumento impreso: ${colaImpresion.shift()}`);
        console.log(colaImpresion);
    }
}

function agregarAlaCola(doc:string){
    colaImpresion.push(doc);
    console.log(`\nEl documento ${doc} fue agregado a la cola de impresión:`);
    console.log(colaImpresion);
}



iniciarPila();
console.log("\n")
iniciarCola();

