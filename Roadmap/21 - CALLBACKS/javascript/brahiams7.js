// * EJERCICIO:
//  * Explora el concepto de callback en tu lenguaje creando un ejemplo
//  * simple (a tu elección) que muestre su funcionamiento.

function saludar(nombre, callback){
    console.log(`Hola ${nombre}`);
    callback();
}
function despedir(){
    console.log("!Adios");
}

saludar("Saory",despedir)

// * DIFICULTAD EXTRA (opcional):
// * Crea un simulador de pedidos de un restaurante utilizando callbacks.
// * Estará formado por una función que procesa pedidos.
// * Debe aceptar el nombre del plato, una callback de confirmación, una
// * de listo y otra de entrega.
// * - Debe imprimir un confirmación cuando empiece el procesamiento.
// * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
// *   procesos.
// * - Debe invocar a cada callback siguiendo un orden de procesado.
// * - Debe notificar que el plato está listo o ha sido entregado.
function pedidos(nombrePlato,cbConfirmar,cbListo,cbEntregar){
    setTimeout(() => {
        cbConfirmar(nombrePlato);
        setTimeout(() => {
            cbListo(nombrePlato);
            setTimeout(() => {
               cbEntregar(nombrePlato); 
            }, Math.floor((Math.random() * (10 - 1 + 1)) + 1) * 1000);
        }, Math.floor((Math.random() * (10 - 1 + 1)) + 1) * 1000);
    }, Math.floor((Math.random() * (10 - 1 + 1)) + 1) * 1000);
}

const confirmar=(nombrePlato)=>{
    console.log(`Pedido de ${nombrePlato} confirmado.`);  
}
const listo=(nombrePlato)=>{
    console.log(`Pedido de ${nombrePlato} listo.`);  
}
const entregar=(nombrePlato)=>{
    console.log(`Pedido de ${nombrePlato} entregado.`);  
}

pedidos('salchipicada',confirmar,listo,entregar)