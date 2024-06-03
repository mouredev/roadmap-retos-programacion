// Una función de callback es una función que se pasa a otra función como un argumento, que luego se invoca dentro de la función externa para completar algún tipo de rutina o acción.

// function saludar (nombre) {
//     console.log('hola ' + nombre)
// }

// function antesDecallback (funcionCallback) {
// const name = 'david'
// funcionCallback(name)
// }

// antesDecallback(saludar)

// DIFICULTAD EXTRA (opcional):
//  * Crea un simulador de pedidos de un restaurante utilizando callbacks.
//  * Estará formado por una función que procesa pedidos.
//  * Debe aceptar el nombre del plato, una callback de confirmación, una
//  * de listo y otra de entrega.
//  * - Debe imprimir un confirmación cuando empiece el procesamiento.
//  * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
//  *   procesos.
//  * - Debe invocar a cada callback siguiendo un orden de procesado.
//  * - Debe notificar que el plato está listo o ha sido entregado.



function  pedidos (platillo, confirmado, listo, entregado ) {
  
    confirmado(platillo)
    const numberRandom = () => {
        return Math.floor(Math.random() * 10) * 1000
    }
    setTimeout(() => {
        listo(platillo)
        
    }, numberRandom());
    setTimeout(() => {
        entregado(platillo)
    }, numberRandom());
}

function confirmado (platillo ) {


    console.log('platillo confirmado : ' + platillo) //son callbacks
    
}
function listo (platillo ) {


    console.log('platillo listo : ' + platillo)
    //son callbacks
    
}
function entregado (platillo ) {


    console.log('platillo entregado : ' + platillo)//son callbacks
    
}

pedidos('caldo de pollo',confirmado, listo , entregado)
pedidos('filete de res',confirmado, listo , entregado)
