// Valor y Referencia

// Asignación por valor

let a = 10;
let b = a;

b = 30;

console.log({ a, b }); // No se modifica el valor de a


// Funcion que recibe un variable por valor

const cambiarValor = a => {
    a = 20;
    console.log({ a });
}

let c = 10;
cambiarValor(c);

console.log({ c }); // No se modifica el valor de c




// Asignación por referencia

let persona = { nombre: 'Fabian' };
let persona2 = persona;

persona2.nombre = 'Juan';

console.log({ persona, persona2 }); // Se modifica el valor de persona


// Funcion que recibe una variable por referencia

const cambiarValorObjeto = (objeto) => {
    objeto.nombre = 'Juan';
    console.log({ objeto });
}

let personaa = { nombre: 'Fabian' };
cambiarValorObjeto(personaa);

console.log({ personaa }); // Se modifica el valor de persona