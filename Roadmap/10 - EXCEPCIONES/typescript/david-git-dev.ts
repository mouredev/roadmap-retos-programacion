/*
  EJERCICIO:
  Explora el concepto de manejo de excepciones según tu lenguaje.
  Fuerza un error en tu código, captura el error, imprime dicho error
  y evita que el programa se detenga de manera inesperada.
  Prueba a dividir "10/0" o acceder a un índice no existente
  de un listado para intentar provocar un error.
 */
  function isNumeric(x:any) {
    return ["number", "bigint"].includes(typeof x);
  }

  function sum(...values:any[]) {
    if (!values.every(isNumeric)) {
      throw new TypeError("Can only add numbers");
    }
    return values.reduce((a, b) => a + b);
  }

  console.log(sum(1, 2, 3)); // 6
  try {
    sum("1", "2");
  } catch (e) {
    if(e instanceof Error)
    console.error(e); // TypeError: Can only add numbers
  }
  /*
  DIFICULTAD EXTRA (opcional):
  Crea una función que sea capaz de procesar parámetros, pero que también
  pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
  corresponderse con un tipo de excepción creada por nosotros de manera
  personalizada, y debe ser lanzada de manera manual) en caso de error.
  - Captura todas las excepciones desde el lugar donde llamas a la función.
  - Imprime el tipo de error.
  - Imprime si no se ha producido ningún error.
  - Imprime que la ejecución ha finalizado.
 */
class IHateNineNumberError extends Error {
  constructor(mensaje: string) {
    super(mensaje);
    this.name = "IHateNineNumberError"; // Establece el nombre del error
  }
}
function threeErrorTypes(...args:any[]) {
  try {
    //const divByZero = 1n / 0n; error by zero RangeError
    if (args.some((num) => num === 9))
      throw new IHateNineNumberError("dont use 9! number!!!");
    //const res = args[1].content.json; ReferenceError
    //args[5] error index of bounce RangeError
  } catch (e) {
   if(e instanceof Error){
    switch (e.name) {
      case "Error":
        console.error("Error general");
        break;
      case "RangeError":
        console.error("Error de rango");
        break;
      case "ReferenceError":
        console.error("Error de referencia");
        break;
      default:
        console.error("Vaya esto es nuevo...", e);
        break;
    }
   }
  } finally {
    console.log("Operacion terminada");
  }
}
threeErrorTypes(1, 9, "response", true);