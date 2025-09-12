//Provocar error

/*La declaración try...catch detecta el error(forzado) lo registra e imprime el mensage creado*/
try {
  console.lg("Hello World");
} catch (error) {
  console.log(error = 'Error de tipeado: console.lg("Hello World") no es una función.');
} finally {
  console.log("La ejecución ha finalizado");
}

//Error personalizado

class Error_Personalizado extends Error {
  constructor(message) {
    super(message);
    this.name = "NumberError";
  }
}

function evaluarNumero(num) {
  try {
    if (typeof num === "string") {
      throw new Error_Personalizado("Debe ingresar un número.");
    } else  if (typeof num === "number") {
      if (num <= 0) {
        throw new TypeError(": Solo números positivos son permitidos.");
      } else if (!Number.isInteger(num)) {
        throw "Solo números enteros son permitidos."
      }
      console.log(num + num);
      console.log("Ningún error encontrado");
    }
  } catch (err) {
    if (err instanceof Error_Personalizado) {
      console.log("Dato ingresado de tipo string: " + err.message);
    } else if (err instanceof TypeError) {
      console.log(err.name + err.message);
    } else {
      console.log(err);
    }
  } finally {
    console.log("La ejecución ha finalizado");
  }
}
evaluarNumero("Hola");
evaluarNumero("3");
evaluarNumero(-3.3);
evaluarNumero(3.3);
evaluarNumero(33);