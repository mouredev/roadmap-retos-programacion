/*
* EJERCICIO:
* Explora el concepto de callback en tu lenguaje creando un ejemplo
* simple (a tu elección) que muestre su funcionamiento.
*
* DIFICULTAD EXTRA (opcional):
* Crea un simulador de pedidos de un restaurante utilizando callbacks.
 Estará formado por una función que procesa pedidos.
* Debe aceptar el nombre del plato, una callback de confirmación, una
* de listo y otra de entrega.
* - Debe imprimir un confirmación cuando empiece el procesamiento.
* - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
*   procesos.
* - Debe invocar a cada callback siguiendo un orden de procesado.
* - Debe notificar que el plato está listo o ha sido entregado.
*/

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms));
}
  
async function main(){
    await task_callback(tarea(), callback)
}
  
async function task_callback(tarea, callback){
    await tarea,
    callback()
}
  
async function tarea(){
    console.log("Sumando numeros..")
    await sleep(2 * 1000)
    console.log("Tarea Finalizada")
}
  
function callback(){
    console.log("Funcion invocada luego de terminar task")
}
  
main()


////////////////////// ------------------------ EXTRA -------------------------------- ////////////////////////////

const menu = ["Hamburguesa", "Pizza", "Tacos", "Ensalada Cesar", "Pollo Frito"]

function sleep(ms){
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function order_process(plato, confirmarCallback, readyCallback, deliveryCallback){
  
  confirmarCallback(plato)
  
  const preparation_time = Math.floor(Math.random() * 10) + 1;
  console.log(`Preparando ${plato}...(espera ${preparation_time} segundos)`);
  await sleep(preparation_time * 1000);
  
  readyCallback(plato);
  
  const delivery_time = Math.floor(Math.random() * 10) + 1;
  console.log(`Entregando ${plato}...(espera ${delivery_time} segundos)`);
  await sleep(delivery_time * 1000);
  
  deliveryCallback(plato);
}

function confirmarPedido(plato){
  console.log(`Pedido confirmado: ${plato}`);
}

function pedidoListo(plato){
  console.log(`Pedido listo: ${plato}`);
}

function entregarPedido(plato){
  console.log(`Pedido entregado: ${plato}`);
}

function mostrarMenu_y_pedido(){
  console.log("Menu de platos disponible");
  menu.forEach((plato, id) =>{
    console.log(`${id + 1}. ${plato}`);
  });
  
  return new Promise((resolve) => {
    const readline = require('readline').createInterface({
      input: process.stdin,
      output: process.stdout
    });
    
    readline.question("\nIngrese el numero de plato que desea pedir: ", (numero) => {
      const election = parseInt(numero);
      if (election >= 1 && election <= menu.length) {
        readline.close();
        resolve(menu[election - 1]);
      }else{
        console.log("Numero invalido porfavor intente nuevamente.");
        readline.close();
        resolve(mostrarMenu_y_pedido());
      }
    });
  });
  
}

async function realizarPedidos(){
  console.log("Simulador de pedidos de un restaurante\n");
  
  const platoElegido = await mostrarMenu_y_pedido();
  
  await order_process(platoElegido, confirmarPedido, pedidoListo, entregarPedido);
}

realizarPedidos();

