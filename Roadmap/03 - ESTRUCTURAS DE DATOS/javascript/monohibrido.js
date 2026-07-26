//___________________________________________________________________________
//__________________________Estructura de datos__________________________
//___________________________________________________________________________

//========================1.- arrays========================

/*
- proporciona métodos para efectuar operaciones de recorrido y mutación.
- la longitud como el tipo de elementos son variables.
- los datos se pueden almacenar en ubicaciones no contiguas.
*/

//Crear un array
let frutas = ["manzana", "frutilla", "sandía", "plátano"];

//cantidad de elementos en el array
console.log(`Cantidad de elementos en el array:  ${frutas.length}`);

//Acceder a un elemento del array mediante su índice
//el índice del primer elemento de un array es [0]
//el último es igual al valor de la propiedad length - 1
console.log(`Acceder a un elemento mediante su índice: ${frutas[3]}`);
console.log(`Acceder al último elemento: ${frutas.length - 1}`);

//Recorrer de un array
frutas.forEach(fruta => {
    console.log(fruta);
});

//Añadir un elemento al final de un array
frutas.push("naranja");
console.log(frutas); //["manzana", "frutilla", "sandía", "plátano", "naranja"]

//Eliminar el último elemento de un array
frutas.pop();
console.log(frutas) //["manzana", "frutilla", "sandía", "plátano"]

//Añadir un elemento al principio de un array
frutas.unshift("cereza");
console.log(frutas) // ["cereza", "manzana", "frutilla", "sandía", "plátano"]

//Eliminar el primer elemento de un array
frutas.shift();
console.log(frutas); //[ "manzana", "frutilla", "sandía", "plátano"]

//Encontrar el índice de un elemento del array, en base al length del array
console.log(frutas.indexOf("frutilla")); // 1

//Eliminar un único elemento mediante su posición
let posicionAEliminar = frutas.indexOf("frutilla"); // creamos una variable del índice a eliminar y lo buscamos con indexOf
frutas.splice(posicionAEliminar, 1); // índice donde empezar a eliminar, cuántos elementos eliminar.
console.log(frutas); //[ "manzana", "sandía", "plátano"]

//Eliminar varios elementos a partir de una posición
let vegetales = ["repollo", "lechuga", "betarraga", "zanahoria", "pepino"]

let posicion = 1,
    numElementos = 2;

vegetales.splice(posicion, numElementos);
console.log(vegetales); // ["repollo", "zanahoria", "pepino"]

//los elementos eliminados se pueden convertir en un nuevo array
let arrayElementosEliminados = vegetales.splice(posicion, numElementos);
console.log(arrayElementosEliminados); // ["lechuga", "betarraga"]

//copiar un array, en base al length del array
let arrayCopiado = vegetales.slice();
console.log(arrayCopiado);

// une todos los elementos de una matriz en una cadena y devuelve esta cadena
console.log(arrayCopiado.join()); //"lechuga, betarraga"
console.log(arrayCopiado.join(" - ")); //"lechuga - betarraga"
console.log(arrayCopiado.join("")); //"lechugabetarraga"

//crea un nuevo array con los resultados de la llamada a la función indicada aplicados a cada uno de sus elementos
let numbers = [1, 5, 10, 15];
let doubles = numbers.map(function (x) {
    return x * 2;
});

console.log(numbers); //[1,5,10,15]
console.log(doubles); //[2,10,20,30]

// otro ejemplo de map + Math.
let numbers2 = [1, 4, 6, 17, 43];
let raices = numbers2.map(function (num) {
    return Math.sqrt(num);
})
console.log(numbers2);
console.log(raices);

//invertir orden de los elementos en el array
let array1 = ["one", "two", "three", "four"];
console.log(`Array 1: ${array1}`);

let reversed = array1.reverse();
console.log(`Array reversed: ${reversed}`);

console.log(`Array1 fue modificado: ${array1}`); //Be careful!
//"Array1 fue modificado: ["three", "two", "one"]


//ordenar elementos de un array localmente y devuelve el arreglo ordenado.
//el modo de ordenación por defecto responde a la posición del valor string de acuerdo a su valor Unicode.
const numeros = [1, 15, 4, 13, 10, 12, 7, 2];

//orden números de forma ascendente
numeros.sort((a, b) => a - b);
console.log(numeros); // [1,2,4,7,10,12,13,15]

//orden npumeros de forma descendente
numeros.sort((a, b) => b - a);
console.log(numeros); // [15,13,12,10,7,4,2,1]

//orden de elementos string de forma alfabética 
const palabras = ["enchufe", "cargador", "cama", "alfombra", "mesa", "silla"];

palabras.sort();
console.log(palabras); // ["alfombra", "cama", "cargador", "enchufe", "mesa", "silla"]

const puntos = [1, 10, 2, 21];
puntos.sort(); // [1, 10, 2, 21]
// Tenga en cuenta que 10 viene antes que 2
// porque '10' viene antes que '2' según la posición del valor Unicode.

const cosas = ["word", "Word", "1 Word", "2 Words"];
cosas.sort(); // ['1 Word', '2 Words', 'Word', 'word']
// En Unicode, los números vienen antes que las letras mayúsculas
// y estas vienen antes que las letras minúsculas.


//ordenando caracteres no ASCII
let items = ["réservé", "premier", "cliché", "communiqué", "café", "adieu"];
items.sort(function (a, b) {
    return a.localeCompare(b);
});
console.log(items)//items is ['adieu', 'café', 'cliché', 'communiqué', 'premier', 'réservé']

//editar un elemento del array accediendo por índice, modifica el array original
let consolas = ["Play-Station", "X-box", "Game-cube", "Poly-Station"];

consolas[1] = "Nintendo-Switch";
console.log(consolas); // ["Play-Station", "Nintendo-Switch", "Game-cube", "Poly-Station"];

//========================2.- objetos========================

/**
- colección de propiedades clave:valor. Puede contener cualquier tipo de dato, incluso funciones.
- es usado para guardar una colección de datos definidos y entidades más complejas.

 */

//creación objeto literal el más común.
let persona = {
    nombre: "Cristian",
    edad: 32,
    saludar() {
        console.log(`Hola, soy ${this.nombre}`);
    }
};

console.log(persona.nombre); // Cristian
persona.saludar(); // ` Hola, soy Cristian`;

//agregar propiedad al objeto persona
persona.profesion = "Programador";
persona.hobby = "Deportes";

console.log(persona);

// actualizar valor de una propiedad en un objeto

persona.edad = 33;
console.log(persona) // edad: 33

//eliminar propiedad de un objeto
delete persona.edad;

console.log(`Después de eliminar la edad: ${persona}`)

// eliminar contenido completo del objeto
delete persona; // return true

//organizar objeto bajo criterios. 
// Primero se transforma a objeto array y luego lo transformamos nuevamente a objeto Object
let habilidades = {
    fuerza: 80,
    resistencia: 90,
    flexibilidad: 70
};

let objetoOrdenado = Object.fromEntries(Object.entries(habilidades).sort());
console.log(objetoOrdenado); // se ordenó el objeto por orden alfabético de las propiedades

// ordenar por valor numérico
//Ascendente
console.log(Object.fromEntries(Object.entries(habilidades).sort((a, b) => a[1] - b[1])));

//Descendente
console.log(Object.fromEntries(Object.entries(habilidades).sort((a, b) => b[1] - a[1])));





//creación de un objeto a partir de otro, Desestructuración de objetos.
// a partir de la <referencia> de otro
let user = {
    name: "Margarita",
    role: "Manager",
    life: 73
}

//solo superficial
let SurviveModeUser = {
    ...user,
    resistance: 75,
    role: "cook"
}

//para que no sobreescriba los valores en el objeto principal ocupamos structuredClone(objeto)
//clonado moderno, el clonado soporta diferentes niveles de profundidad.
let SurviveModeUser2 = {
    ...structuredClone(user),
    resistance: 85,
    role: "fisher"
}

console.log(user);
console.log(SurviveModeUser);
console.log(SurviveModeUser2);

// creación de objeto, si copia las propiedades pero no es una referencia directa
let copy = {};
Object.assign(copy, user);
copy.name = "otro nombre"; //Esto NO modifica user
console.log(user.name)
console.log(copy.name);



//creación de un objeto vacío con new Object(), ya no se usa mucho
let objetillo = new Object();
console.log(objetillo);  //{}

//agregando una propiedad al objeto
objetillo.name = 'cristian';
objetillo.city = 'Santiago de Chile';
console.log(objetillo); //{name: 'cristian', city: 'Santiago de Chile'};

//actualizar valor de una propiedad 
objetillo.name = 'Cristiancillo';
console.log(`El name del objeto se actualizó a: ${objetillo.name}`); // La propiedad name del objeto se actualizó a: Cristiancillo


//eliminar un elemento del objeto
delete objetillo.city;
console.log(`Tras borrado: ${objetillo}`);


// Object.create() crea un objeto nuevo, utilizando un objeto existente como el prototipo
//del nuevo objeto creado.
const miembro = {
    esHumano: false,
    saludin: function () {
        console.log(`Hola, mi nombre es ${this.nombre}. Soy un humano?: ${this.esHumano}`);
    },
};

const brother = Object.create(miembro);

brother.nombre = "Roberto"; // "nombre" es una propiedad seteable en "brother", pero no en "miembro"
brother.esHumano = true; //Inherited properties can be overwritten

brother.saludin(); // Hola, mi nombre es Roberto. Soy un humano?: true


//objeto con función constructora -> útil cuando se necesita crear muchos objetos con la misma estructura
function Deporte(nombre, nacionalidad) {
    this.nombre = nombre;
    this.nacionalidad = nacionalidad;
}

let judo = new Deporte("Judo", "Japón");
let boxeo = new Deporte("Boxeo", "Gran Bretaña");

console.log(judo.nombre); // Judo
console.log(boxeo.nombre); //Boxeo

//Objeto con class
class Pelicula {
    constructor(nombre, estreno) {
        this.nombre = nombre;
        this.estreno = estreno;
    }

    presentacion() {
        console.log(`${this.nombre}, es una película estrenada el ${this.estreno}`);
    }
}

let jurassic_park = new Pelicula("Jurassic Park", "17/06/1993");
jurassic_park.presentacion(); // -> Jurassic Park, es una película estrenada el 17/06/1993


//class heredada
class Vehiculo {
    constructor(tipo, marca, velocidadMax, pasajeros) {
        this.tipo = tipo
        this.marca = marca;
        this.velocidadMax = velocidadMax;
        this.pasajeros = pasajeros;
    }

    descripcion() {
        console.log(`El ${this.tipo} es un vehículo, marca ${this.marca} con una cap. máx. de ${this.pasajeros}pasajeros`);
    }
}

class Avion extends Vehiculo {
    constructor(tipo, marca, velocidadMax, pasajeros, altitudMax, cantAlas) {
        super(tipo, marca, velocidadMax, pasajeros);
        this.altitudMax = altitudMax;
        this.cantAlas = cantAlas;
    }
    descripcion() {
        console.log(`El ${this.tipo} es un vehículo, tiene ${this.cantAlas} alas y vuela a una altura de ${this.altitudMax}`);
    }
}

let Boeing_c17 = new Avion("Avion", "Boeing y Lockheed Martin", "950 km/h", 100, "13.716 mts", 2);

Boeing_c17.descripcion();



//======================== 3.- Set ========================

/*
-representan conjuntos de datos.
- colección de valores
-Los datos insertados NO se pueden repetir
-Puede incluir cualquier tipo de elemento

*/

let setVacio = new Set(); // Set({})
let setSinRepeticiones = new Set([5, 6, 7, 8, 9]); // Set({5,6,7,8,9}) conjunto de 5 elementos
let setConRepeticiones = new Set([4, 5, 5, 6, 7]); // Set({4,5,6,7}) conjunto de 4 elementos


console.log(setSinRepeticiones.size) // devuelve el número de valores en el objeto Set

//Añadir un valor al objeto Set
setSinRepeticiones.add(10);
console.log(setSinRepeticiones); // {5,6,7,8,9,10}

//Eliminar un valor al objeto Set
setSinRepeticiones.delete(6);
console.log(setSinRepeticiones); //{5,7,8,9,10}

//Saber si un valor está presente en el objeto Set, devuelve un boolean
console.log(setSinRepeticiones.has(6)); //false

//Eliminar todos elementos del objeto Set
setSinRepeticiones.clear();
console.log(setSinRepeticiones); // {}

//agregando denuevo elementos al objeto Set
setSinRepeticiones.add(14);
setSinRepeticiones.add("texto");

let otroObjeto = { a: 1, b: 2 };
setSinRepeticiones.add(otroObjeto);


//Iteración de elementos de acuerdo al ingreso de ellos en el objeto Set
for (let item of setSinRepeticiones) console.log(item);

//Ordenación, primero debe ser pasado a un array
//object Set() no tiene una ordenación nativa
// la clave es el misma que el valor

let numerosSet = new Set([1, 4, 7, 14, 8]);
console.log([...numerosSet].sort((a, b) => a - b)); //ordenados ascendentemente.



//======================== 4.- Map ========================

/*
- Retiene tuplas de llave-valor y mantiene el orden de inserción de las llaves.
- Admite cualquier valor (ambos objetos y valores primitivos) puede ser usado como llave o valor.
- Las llaves de un objeto Map pueden ser cualquier valor, incluyendo funciones, objetos, o cualquier primitivo


*/

// Creación de un objeto Map vacío
let objetoMap = new Map();

// Agregar elementos
objetoMap.set("c", 3);
objetoMap.set("a", 1);
objetoMap.set("b", 2);


//Buscar el valor de llave dentro del objeto Map
console.log(objetoMap.get("a")); // 1

//Modificar el valor de una llave dentro del objeto Map
objetoMap.set("a", 1994);
console.log(objetoMap.get("a")); // 1994

//Cantidad de elementos en el objeto Map
console.log(objetoMap.size); // 3

//Eliminar llave-valor de un objeto Map
objetoMap.delete("a");
console.log(objetoMap.size); // 2

//ordenamiento
let mapa = new Map();
mapa.set("kiwi", 1);
mapa.set("banana", 4);
mapa.set("naranja", 3);
mapa.set("chirimoya", 2);

//Ordenar por clave (alfabético)
let porClave = new Map([...mapa.entries()].sort((a, b) => a[0].localeCompare(b[0])));
console.log(porClave); // {"banana" => 4, "chirimoya" => 2, "kiwi" => 1, "naranja" => 3}

//Ordenar por valor (numérico)
let porValor = new Map([...mapa.entries()].sort((a, b) => a[1] - b[1]));
console.log(porValor); //{"kiwi" => 1, "chirimoya" => 2, "naranja" => 3, "banana" => 4}

//iterar elementos del objeto Map
mapa.forEach((valor, llave) => {
    console.log(`${llave}: ${valor}`);
});


//======================== DESAFÍO EXTRA ========================


const readline = require("readline");


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

const agenda = new Map();

function menu() {
    console.log(`
        ================================
                AGENDA CONTACTOS
        ================================
        1. Buscar contacto
        2. Insertar contacto
        3. Actualizar contacto
        4. Eliminar contacto
        5. Mostrar contactos
        0. Salir
        
        `);

    rl.question("Elige una opción: ", (opcion) => {
        switch (opcion) {
            case "1": buscarContacto(); break;
            case "2": insertarContacto(); break;
            case "3": actualizarContacto(); break;
            case "4": eliminarContacto(); break;
            case "5": mostrarContacto(); break;
            case "0": salir(); break;
            default:
                console.log("Opción inválida, elige un número dentro del menú.")
        }
    });
}

function buscarContacto() {
    console.log(`
    ======= Buscando Contacto =======
    `)
    rl.question("Nombre a buscar: ", (nombre) => {
        const telefono = agenda.get(nombre.trim());
        if (telefono) {
            console.log(`[Nombre: ${nombre} - Teléfono: ${telefono}]`);
        } else {
            console.log("Contacto no encontrado.");
        }
        menu();
    })
};

function insertarContacto() {
    console.log(`
    ======= Insertando Contacto =======
    `)
    rl.question("Nombre: ", (nombre) => {
        if (agenda.has(nombre.trim())) {
            console.log("El contacto ya existe.");
            menu();
        } else {
            rl.question("Teléfono: ", (telefono) => {
                if (!/^\d{1,12}$/.test(telefono.trim())) {
                    console.log("Teléfono inválido. Solo números, máximo 12 dígitos.");
                    menu();
                } else {
                    agenda.set(nombre.trim(), telefono.trim());
                    console.log("Contacto agregado exitosamente.");
                    menu();
                }
            });
        }
    });
};

function actualizarContacto() {
    console.log(`
    ======= Actualizando Contacto =======
    `)
    rl.question("Nombre a buscar: ", (nombre) => {
        const telefono = agenda.get(nombre.trim());
        if (telefono) {
            agenda.delete(nombre.trim());
            rl.question("Nuevo nombre: ", (nombreNuevo) => {
                rl.question("Nuevo teléfono: ", (telefonoNuevo) => {
                    agenda.set(nombreNuevo.trim(), telefonoNuevo.trim());
                    console.log("___Contacto actualizado correctamente.___");
                    menu();
                });
            });
        } else {
            console.log("Contacto no encontrado.");
            menu();
        }
    });
};

function eliminarContacto() {
    console.log(`
    ======= Eliminando Contacto =======
    `)
    rl.question("Contacto a eliminar: ", (nombre) => {
        const telefono = agenda.get(nombre.trim());
        if (telefono) {
            agenda.delete(nombre.trim());
            console.log("___Contacto eliminado correctamente.___");
            menu();
        } else {
            console.log("Contacto no encontrado.");
            menu();
        }
    })
};

function mostrarContacto() {
    console.log(`
    ======= Lista de Contactos =======
    `)
    if (agenda.size === 0) {
        console.log("No existen contactos.");
    } else {
        let mostrandoAgendaContactos = new Map([...agenda.entries()].sort((a, b) => a[0].localeCompare(b[0])));
        mostrandoAgendaContactos.forEach((telefono, nombre) => {
            console.log(`[Nombre: ${nombre} - Teléfono: ${telefono}]`);
        });
    };
    menu();
};

function salir() {
    console.log(`
    ======= Hasta luego =======
    `)
    rl.close();
};

menu();