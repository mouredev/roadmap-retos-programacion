/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
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

const legendario = (frase2, callback) => {
  const frase = "Mi nombre es Caterina, Caterina " + frase2;
  diMiApellido(frase);
};

const diMiApellido = (frase) => {
  console.log(frase);
};

legendario("Rodríguez", diMiApellido);

console.log("--------------DIFICULTAD EXTRA---------------");

const pedir = (nombrePlato, confirmar, notificarListo, notificarEntregado) => {
  confirmar(nombrePlato);

  setTimeout(() => {
    notificarListo(nombrePlato);

    setTimeout(() => {
      notificarEntregado(nombrePlato);
    }, Math.floor(Math.random() * 10 + 1) * 1000);
  }, Math.floor(Math.random() * 10 + 1) * 1000);
};

const confirmar = (nombrePlato) => {
  console.log(`El pedido ${nombrePlato} se ha recibido correctamente ✅`);
};

const notificarListo = (nombrePlato) => {
  console.log(`El pedido ${nombrePlato} ya está listo! 😄`);
};

const notificarEntregado = (nombrePlato) => {
  console.log(`El pedido ${nombrePlato} ya se ha entregado 😲`);
};

pedir(
  "Padthai con doble de lima 🍋",
  confirmar,
  notificarListo,
  notificarEntregado
);
