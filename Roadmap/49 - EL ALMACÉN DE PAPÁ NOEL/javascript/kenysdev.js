/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#49 EL ALMACÉN DE PAPÁ NOEL
-------------------------------------------------------
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
// ________________________________________________________
const readlineSync = require('readline-sync');

function verifyAllowedChar(codeEntry) {
    for (let ch of codeEntry) {
        if (!'abc123'.includes(ch)) {
            console.log("Uno de los caracteres no está entre los permitidos.\n");
            return false;
        }
    }
    return true;
}

function getEntry() {
    while (true) {
        const codeEntry = readlineSync.question("Código: ");

        if (codeEntry.length !== 4) {
            console.log("El código debe ser de 4 dígitos.\n");
            continue;
        }

        if (verifyAllowedChar(codeEntry)) {
            return codeEntry;
        }
    }
}

function isOpen(code) {
    const codeEntry = getEntry();
    if (codeEntry === code) {
        return true;
    }
    console.log("Código inválido.\n");

    for (let i = 0; i < codeEntry.length; i++) {
        if (codeEntry[i] === code[i]) {
            console.log(`'${codeEntry[i]}' está en la posición correcta.`);
        } else if (code.includes(codeEntry[i])) {
            console.log(`'${codeEntry[i]}' está en el código, pero en otra posición.`);
        } else {
            console.log(`'${codeEntry[i]}' no está presente en el código.`);
        }
    }

    return false;
}

// ____________________________________________________________________________
console.log(`
* Papá Noel tiene que comenzar a repartir los regalos...
* ¡Pero ha olvidado el código secreto de apertura del almacén!

- Tienes 10 intentos para adivinar el código que abre el almacén.
- Código de 4 caracteres. Permitidos: a, b, c, 1, 2, 3.
- Nota: No hay dígitos repetidos.`);

const code = shuffle("abc123").slice(0, 4);

for (let attempts = 0; attempts < 10; attempts++) {
    console.log(`\n___________\nIntento #${attempts + 1}`);

    if (isOpen(code)) {
        console.log("Código correcto, almacén abierto.");
        console.log("Papá Noel ahora podrá entregar los regalos.");
        break;
    }

    if (attempts === 9) {
        console.log("\n___________\nHas perdido.");
        console.log("Papá Noel ya no podrá entregar los regalos.");
    }
}

function shuffle(str) {
    const arr = str.split('');
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr.join('');
}
