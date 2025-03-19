/* Manejo de Excepciones */

try {
  let resultado = 10 / 0;
} catch (error) {
  console.error("Error:", error.message);
} finally {
  console.log("La ejecucion ha finalizado");
}

/* Forzando errores */

try {
  let lista = [1, 2, 3];
  console.log(lista[5]);
} catch (error) {
  console.error("Error:", error.message);
}
