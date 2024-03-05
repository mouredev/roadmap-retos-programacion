/*function UserException(message) {
  this.message = message;
  this.name = "UserException";
}

UserException.prototype.toString = function () {
  return `${this.name}: "${this.message}"`
}

throw new UserException("Valor muy Alto");*/

try {
  console.lg("Hello World");
} catch (error) {
  console.log(error = 'Error de tipeado: console.lg("Hello World") no es una función.');
}

class Error_Personalizado extends Error {
  constructor(message) {
    super(message);
    this.name = "Este es un error personalizado";
  }
}

