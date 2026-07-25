/*
 * EJERCICIO:
 * Papá Noel tiene que comenzar a repartir los regalos...
 * ¡Pero ha olvidado el código secreto de apertura del almacén!
 *
 * Crea un programa donde introducir códigos y obtener pistas.
 * 
 * Código:
 * - El código es una combinación de letras y números aleatorios
 *   de longitud 4. (Letras: de la A a la C, Números: del 1 al 3)
 * - No hay repetidos.
 * - Se genera de manera aleatoria al iniciar el programa.
 * 
 * Usuario:
 * - Dispone de 10 intentos para acertarlo.
 * - En cada turno deberá escribir un código de 4 caracteres, y 
 *   el programa le indicará para cada uno lo siguiente:
 *   - Correcto: Si el caracter está en la posición correcta.
 *   - Presente: Si el caracter existe, pero esa no es su posición.
 *   - Incorrecto: Si el caracter no existe en el código secreto.
 * - Deben controlarse errores de longitud y caracteres soportados.
 * 
 * Finalización:
 * - Papa Noel gana si descrifra el código antes de 10 intentos.
 * - Pierde si no lo logra, ya que no podría entregar los regalos.
*/

let enterCode;
let codeCounter = 1;
let alphanumerics = ["A", "B", "C", 1, 2, 3];
let secretCode = "";

const generateCode = (array) => {
  for (let index = array.length - 1; index > 0; index--) {
    const randomIndex = Math.floor(Math.random() * (index + 1));

    [array[index], array[randomIndex]] = [array[randomIndex], array[index]];
  }

  for (let index = 0; index < 4; index++) {
    secretCode += alphanumerics[index];
  }
};

generateCode(alphanumerics);

alert("Santa, introduce el código secreto para abrir el almacen.\nEl código está conformado por alguno de los siguientes caracteres: A - C, 1 - 3:");

for (let index = 1; index <= 10; index++) {
  enterCode = prompt(`Intento #${index}:`);

  if (enterCode === secretCode) {
    alert("Código correcto. Acceso autorizado al almacen.");

    break;
  } else {
    let errorMessage = `Código ingresado: ${enterCode}\n\n`;

    for (let index = 0; index < secretCode.length; index++) {
      let position = index + 1;

      if (secretCode[index] === enterCode[index]) {
        errorMessage += `· El caracter de la posición ${position} es correcto.\n`;
      }

      if (secretCode[index] !== enterCode[index] && secretCode.indexOf(enterCode[index]) > -1) {
        errorMessage += `· El caracter de la posición ${position} es incorrecto, pero existe en el código.\n`;
      }

      if (secretCode[index] !== enterCode[index] && secretCode.indexOf(enterCode[index]) === -1) {
        errorMessage += `· El caracter de la posición ${position} no existe.\n`;
      }
    }

    if (enterCode.length !== 4) {
      errorMessage += "· La longitud debe ser de cuatro caracteres.\n";
    }

    alert(errorMessage);

    if (index === 10) {
      alert("No decifraste el código y los regalos no podrán entregarse a tiempo.");
    }
  }
}
