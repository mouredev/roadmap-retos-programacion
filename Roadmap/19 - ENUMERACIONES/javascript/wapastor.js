// ENUMS en JavaScript
/*
Los enums en JavaScript son una forma de crear un conjunto de constantes que pueden ser utilizadas en cualquier parte de nuestro código.
los enumeradores (enums) no existen como una característica nativa del lenguaje, pero podemos simularlos utilizando objetos o técnicas específicas.
*/

// Definimos un objeto con las constantes que necesitamos
const diasDeLaSemana = {
    LUNES: 1,
    MARTES: 2,
    MIERCOLES: 3,
    JUEVES: 4,
    VIERNES: 5,
    SABADO: 6,
    DOMINGO: 7
};

// Utilizamos las constantes en nuestro código, por ejemplo:

let dia = diasDeLaSemana.LUNES;
console.log(dia); // 1

// Podemos utilizar un switch para hacer algo diferente dependiendo del valor de la constante:
switch (dia) {
    case diasDeLaSemana.LUNES:
        console.log('Hoy es Lunes');
        break;
    case diasDeLaSemana.MARTES:
        console.log('Hoy es Martes');
        break;
    case diasDeLaSemana.MIERCOLES:
        console.log('Hoy es Miércoles');
        break;
    case diasDeLaSemana.JUEVES:
        console.log('Hoy es Jueves');
        break;
    case diasDeLaSemana.VIERNES:
        console.log('Hoy es Viernes');
        break;
    case diasDeLaSemana.SABADO:
        console.log('Hoy es Sábado');
        break;
    case diasDeLaSemana.DOMINGO:
        console.log('Hoy es Domingo');
        break;
    default:
        console.log('Día no válido');
}

// Podemos hacer un bucle para recorrer todas las constantes:
for (let dia in diasDeLaSemana) {
    console.log(diasDeLaSemana[dia]);
}

// Podemos obtener el nombre de la constante a partir de su valor:
function getDia(dia) {
    for (let d in diasDeLaSemana) {
        if (diasDeLaSemana[d] === dia) {
            return d;
        }
    }
    return null;
}

console.log(getDia(1)); // LUNES

function obtenerNombreDelDia(valor){
    const clave = Object.keys(diasDeLaSemana).find(key => diasDeLaSemana[key] === valor);
    
    return clave || 'No existe';
}

console.log(obtenerNombreDelDia(1)); // LUNES
console.log(obtenerNombreDelDia(8)); // No existe
