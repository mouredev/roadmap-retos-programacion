/*
# #21 CALLBACKS
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 */

const numeros = [1, 2, 3, 4, 5, 6, 8, 9, 10];

//Esta funcion dejará los elementos según la función que se pase como callback
function filtrarArray(unArray, callback) {
  const resultado = [];
  for (const x of unArray) {
    if (callback(x))
      resultado.push(x);
  }
  return resultado;
}

function esPar(num) {
  return (num % 2 === 0) 
}

function esImpar(num) {
  return (num % 2 > 0) 
}

 console.log('Array original: ', numeros);
 
 const quitarPares = filtrarArray(numeros, esPar);
 console.log('Filtrar los pares: ', quitarPares);

 const quitarImpares = filtrarArray(numeros, esImpar);
 console.log('Filtrar los impares: ', quitarImpares);


 /*
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */
console.log('\n\nDIFICULTAD EXTRA: Simulador de Pedidos');

async function confirmarPedido(plato) {        
    return new Promise(resolve => {
      setTimeout(() => {
        console.log( `${Date.now()} 1. Pedido Confirmado: ${plato}`);
        resolve(true)
      }, 2000)
    })  
}

async function pedidoListo(plato) {
    return new Promise(resolve => {
      setTimeout(() => {
        console.log( `${Date.now()} 2. Pedido Listo: ${plato}`);
        resolve(true)
      }, 8000)
    })
}

async function entregarPedido(plato) {
    return new Promise(resolve => {
      setTimeout(() => {
        console.log( `${Date.now()} 3. Pedido Entregado: ${plato}`);  
        resolve(true)
      }, 8000)
    })
}

async function procesarPedido (plato, callbackConfirmacion, callbackListo, callbackOtraEntrega) {
  if (!plato) {
    throw new Error('No se ha indicado un plato');
  }
  console.log(`${Date.now()} Iniciar Pedido. Plato: ${plato}`)
  const mensaje1 = await confirmarPedido(plato);
  const mensaje2 = await pedidoListo(plato);
  const mensaje3 = await entregarPedido(plato);    
}
//Ejecucion
procesarPedido('papas fritas', confirmarPedido, pedidoListo, entregarPedido);
