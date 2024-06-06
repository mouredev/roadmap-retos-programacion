// 1º Ejemplos de asignación de variables por valor
let n1: number = 5;
let n2: number = n1;

console.log('Antes de la modificación: n1 = ' + n1 + ' n2 = ' + n2);

n1 = 10;

console.log('Después de la modificación: n1 = ' + n1 + ' n2 = ' + n2);

// 2º Ejemplos de asignación de variables por referencia
interface Persona {
    nombre : string;
    edad : number;
    trabajo : string;
}

let programador1 : Persona = { nombre: "Arrian", edad: 25 , trabajo : 'desarrolador'};
let programador2 : Persona = programador1;

programador2.nombre = 'Adrián';
console.log('Valor original: ' + programador1.nombre);
console.log('Valor cambiado: ' + programador2.nombre);

// 3º Funciones con parametros por valor
function gritar(cadena : string): string {
    return cadena.toUpperCase();
}

let cadenaOg : string = 'Igledev'
let cadenaMod : string = gritar(cadenaOg);

console.log('Valor original: ' + cadenaOg);
console.log('Valor cambiado: ' + cadenaMod);

// 4º Funciones con parametros por referencia
function incrementarEdad(persona: Persona): void {
    persona.edad++;
}

let programador3: Persona = { nombre: "Ana", edad: 22 , trabajo : 'Desarrolladora'};
console.log('Edad antes de la función: ' + programador3.edad);

incrementarEdad(programador3);

console.log('Edad después de la función: ' + programador3.edad);

// Ejercicio Extra
// Por valor
    function intercambiarValor(valor1 : number, valor2 : number): [number, number] {
        let temp: number = valor1;
        valor1 = valor2;
        valor2 = temp;
        return [valor1, valor2];
    }

    let valor1: number = 5;
    let valor2: number = 10;

    console.log('Antes de la modificación: valor1 = ' + valor1 + ' valor2 = ' + valor2);

    let [nuevoValor1, nuevoValor2] = intercambiarValor(valor1, valor2);

    console.log('Después de la modificación: valor1 = ' + valor1 + ' valor2 = ' + valor2);
    console.log('Valores intercambiados: valor1 = ' + nuevoValor1 + ' valor2 = ' + nuevoValor2);

// Por Referencia
    interface Datos {
        dato1: number;
        dato2: number;
    }

    function intercambiarReferencia(datos: Datos): Datos {
        let temp: number = datos.dato1;
        datos.dato1 = datos.dato2;
        datos.dato2 = temp;
        return datos;
    }

    let datosOriginales: Datos = { dato1: 5, dato2: 10 };

    console.log('Antes del intercambio: datosOriginales = ' + JSON.stringify(datosOriginales));

    let nuevosDatos = intercambiarReferencia({ ...datosOriginales });

    console.log('Después del intercambio: datosOriginales = ' + JSON.stringify(datosOriginales));
    console.log('Valores intercambiados: nuevosDatos = ' + JSON.stringify(nuevosDatos));