// <------ Objetos --------->

let objetoLiteral = {}; // Objeto literal vacio

let user = {
    email: 'yesid@gmail.com',
    name: 'Yesid',
    dirección: {
        calle: 'Queen st',
        número: 13,
    },
    activo: true,
    recuperarClave: function () {
        console.log('Recuperando clave');
    }
}

/** No podemos cambiar las propiedades, pero si podemos agregarlo o quitarle propiedades a los objetos y arrays */

const user1 = {id:1};

user1.name = 'Yesid'; // Agraga la propiedad name
user1.guardar = function () { //Agrega la propiedad guardar
    console.log('Guardando', user1.name);
}

user1.guardar();

delete user.name; // Elimina la propiedad name
delete user1.guardar; // Elimina la propiedad guardar
console.log(user1);


const user2 = Object.freeze({id:1}); // Este método hace que no se pueda modificar

const user3 = Object.seal({id:1}); // ESte método permite cambiarle los valores a las propiedades eistentes, pero no permite quitarle ni agregarle propiedades.


// Factory function

//===> Nos permite crear objetos de una manera sencila y no repetitiva

function crearUsuario (name,email) {
    return {
        email,
        name,
        activo: true,
        recuperarClave: function() {
            console.log('Recuperando clave...');
        }
    }
}

let user4 = crearUsuario('Nicolas', 'nico@gmail.com');
let user5 = crearUsuario('felipe', 'felipe@gmail.com');
console.log(user4, user5);

//<--------- array ---------->

const letras = ['a', 'b'];

// Es posible modificar el contenido de un array, hay 3 métodos.

//Para agregar elementos

letras.push('c'); //Permite agregar elementos al final de un array.

letras.unshift('y', 'y'); // Permite agregar elementos al inicio de un array.

letras.splice(3,0,1,2); // Permite agregar elementos en una posición especifica. El primer dato corresponde al indice donde vamos a comenzar, el segundo a cuantos elementos queremos eliminar, los ultimos dos datos corresponden a los elementos que queremos agregar.

// Para eleminar elementos

const letras1 = ['a', 'b','c','d'];

//Para eliminar el ultimo elemento
const final = letras1.pop();
console.log(final,letras1);

//Para eliminar el primer elemento
const comienzo = letras1.shift(); // Nos devuelve el elemento que estamos eliminando.
console.log(comienzo,letras1);

// Para eliminar los elementos entre medio
const entremedio = letras1.splice(1,1); // El primer elemento hace referencia a el indice desde el cual se empezará a borrar, y el segundo, cuantos elementos se van a borrar.
console.log(entremedio,letras1);

// Para ordenar

let numeros = [15, 10. -3];

numeros.sort(); // Ordena los array de menor a mayor
numeros.reverse(); //Lo que hace es revertir el orden del arreglo.

console.log(numeros);

let letras2 = ['z', 'a','d'];
letras2.sort();
console.log(letras);

let conMayusculas = ['Z', 'a','d'];
letras.sort((a,b) => {
    /**
     * a antes b => -1
     * b antes a => 1
     * si son iguales => 0
     */
    let alower = a.toLocaleLowerCase();
    let blower = b.toLocaleLowerCase();

    if (alower < blower) {
        return -1;
    }

    if (alower > blower) {
        return 1;
    }
    return 0;
});
console.log(letras2);

// Map
const usuarios = [
    {edad:17, nombre: 'Nico'},
    {edad:13, nombre: 'Chanchito'},
    {edad:25, nombre: 'Feliz'},
    {edad:32, nombre: 'Fernanda'},
];

const lista = usuarios.map(usuarios => `<li>${usuarios.nombre}<li>`);
const html = `<ol>${lista.join('')}<ol>`;

console.log(html);

const mapped = usuarios.map(usuarios => {
    return {
        ...usuarios,
        mayor: usuarios.edad > 17,
    }
})

console.log(mapped);