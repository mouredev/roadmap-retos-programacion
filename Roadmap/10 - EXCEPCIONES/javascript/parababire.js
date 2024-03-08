//Provocar error

/*La declaración try...catch detecta el error(forzado) lo registra e imprime el mensage creado*/
try {
  console.lg("Hello World");
} catch (error) {
  console.log(error = 'Error de tipeado: console.lg("Hello World") no es una función.');
}

class Error_Personalizado extends Error {
  constructor(message) {
    super(message);
    this.name = "NumberError";
  }
}

function evaluarNumero(num) {
  try {
    if (typeof num === "string") {
      throw new Error_Personalizado("No es un número");
    } else  if (typeof num === "number") {
      console.log(num + num);
    }
  } catch (err) {
    if (err instanceof Error_Personalizado) {
      console.log("Dato ingresado no es un número: " + err.message);
    } else {
      throw err;
    }
  }
}
evaluarNumero("3");