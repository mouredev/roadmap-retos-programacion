// Autor: Héctor Adán 
// GitHub: https://github.com/hectorio23
"use strict";

/*******************************************
*************** EJERCICO **************+****
*******************************************/

const print = message => console.log(`Mensaje impreso por callback: ${ message }`);

function doSomething(message, callback) {
    callback(message);
}

doSomething("¡Hola Mundo!", print);
console.log("\n**************** EJERCICIO EXTRA *******************+\n")


/*******************************************
************ EJERCICO EXTRA  **********+****
*******************************************/

// Función que confirma el pedido, por defecto es Falso
function confirmacion(nombre_plato, check) {
    console.log(`[Confirmacion] - ¿Usted desea confirmar el pedido llamado "${nombre_plato}"?: ${check ? 'Yes' : 'No'}`);

    return check;
}

// Función que imprime si el pedido está listo
async function listo(nombre_plato, confirmado) {
    await new Promise(resolve => setTimeout(resolve, Math.random() * 10000));
    console.log(`[Listo] - El pedido "${nombre_plato}" está listo para ser entregado`);
}

// Función que imprime si el pedido ya ha sido entregado
async function entrega(nombre_plato) {
    await new Promise(resolve => setTimeout(resolve, Math.random() * 10000));
    console.log(`[Entrega] - El pedido "${nombre_plato}" ha sido entregado`);
}

// Función que procesa las órdenes
async function make_order(nombre_plato, confirmacion, listo, entrega, check = false) {
    const confirmado = confirmacion(nombre_plato, check);
    if (!check) {
        console.log(`[Cancelled] - El pedido "${nombre_plato}" no se confirmó, por lo que se canceló el pedido`);
        return;
    }
    
    await listo(nombre_plato, confirmado);
    await entrega(nombre_plato);
}

// Función principal
async function main() {
    const orders = [
        make_order("Papas a la francesa", confirmacion, listo, entrega, true),
        make_order("Carne de Cocodrilo a la parrilla", confirmacion, listo, entrega, false),
        make_order("Tacos de Pastor", confirmacion, listo, entrega, true),
        make_order("Ensalada de Papas con albondigas", confirmacion, listo, entrega, true)
    ];
    await Promise.all(orders);
}

// Ejecución del ejercicio extra
main().catch(console.error);