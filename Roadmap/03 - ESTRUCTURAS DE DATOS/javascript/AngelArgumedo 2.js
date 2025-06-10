/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */

const { Console } = require('console');
const { get } = require('http');

// estructura de datos
//Areglos
console.log("Areglos");
let array = [1, 2, 3, 4];
console.log(array[0]);
array.push(5);
console.log(array.length);

//Objetos\
console.log("Objetos");
let objeto = {
    nombre: "Carl",
    edad: 25,
    esEstudiante: true,
};
console.log(objeto.nombre);
objeto.edad = 31; // modificar propiedad

// Sets (conjuntos)
console.log("Sets");
let set = new Set([1, 2, 3, 4]);
set.add(5);
set.delete(3);
console.log(set.size);
console.log(set.has(3));//false

// maps
console.log("Mapas");
let map = new Map();
map.set("nombre", "Carl");
map.set("edad", 25);
console.log(map);
console.log(map.get("nombre"));
map.delete("edad");
console.log(map.size);

// WeakSets (conjuntos debiles)
/* son como los set, pero solo almacenan objetos*/
console.log("WeakSets");
let weakSet = new WeakSet();
let obj = {};
weakSet.add(obj);
console.log(weakSet.has(obj));

// WeakMaps (mapas debiles)
let weakMap = new WeakMap();
let obj2 = {};
weakMap.set(obj, "valor");
console.log(weakMap.get(obj));

// Typed Arrays (arreglos tipados)
// son como los arreglos normales, pero manejan datos binarios y datos especificos
console.log("Typed Arrays");
let buffer = new ArrayBuffer(8);//crea buffer de 8 bytes
let int32view = new Int32Array(buffer);//crea arreglo de 32 bits
int32view[0] = 42;
console.log(int32view[0]);

// Stacks (pilas)
console.log("Stacks");
class Stack {
    constructor() {
        this.items = [];
    };
    push(element) {
        this.items.push(element);
    };
    pop() {
        if (this.items.length === 0) return "Underflow";
        return this.items.pop();
    };
    peek() {
        return this.items[this.items.length - 1];
    };
};
let stack = new Stack();
stack.push(1);
stack.push(2);
console.log(stack.peek());

// Queues (colas)
console.log("Queues");
class Queue{
    constructor() { 
        this.items = [];
    }
    enqueue(element) {
        this.items.push(element);
    }
    dequeue() {
        if (this.items.length === 0) return "Underflow";
        return this.items.shift();
    }
    front() {
        return this.items[0];
    } 
}
let queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
console.log(queue.front());
queue.dequeue();
console.log(queue.front());


// Ejercicio
const readline = require('readline');
const contactos = new Map();

class PedirDatos {
        constructor(input) {
            this.input = input;
        }
        getRespuesta() {
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });

            return new Promise((resolve) => {
                rl.question(this.input, (output) => {
                    rl.close();
                    resolve(output);
                })
            });
            
        }
};

class GetData extends PedirDatos {
        constructor(prompt) {
            super(prompt);
        }
        obtenerDatos() {
            return this.getRespuesta();
        }
};
    
const verContactos = async () => {
    if (contactos.size === 0) {
        console.log("No hay contactos");
    } else {
        const verConcatos = console.log(contactos);
        return verConcatos;
    }
};
    
const AgregarContacto = async () => {
    let persona = {
            id: contactos.size + 1,
            nombre: '',
            edad: 0,
            sexo: '',
            telefono: '',
            direccion: '',
            email: '',
            pronombre: ''
    };

    const datos = [
        { prompt: "Escribe el nombre: ", key: "nombre" },
        { prompt: "Escribe su edad: ", key: "edad" },
        { prompt: "Escribe su sexo: ", key: "sexo" },
        { prompt: "Escribe el numero de celular: ", key: "telefono" },
        { prompt: "Escribe su direccion: ", key: "direccion" },
        { prompt: "Escribe su email: ", key: "email" },
        { prompt: "con que nombre te gustaria guardar tu contacto?: ", key: "pronombre" },
    ];
    const getLength = (number) => number.toString().length;

    for (let dato of datos) {
        let getData = new GetData(dato.prompt);
        let inputData = await getData.obtenerDatos();

        // Validaciones
        if (dato.key === 'telefono') {
            if (!inputData) {
                console.log("Teléfono no válido");
                return;
            } else if (isNaN(inputData)) {
                console.log("El número de teléfono debe ser numérico");
                return;
            }else if ( getLength(inputData) !== 11) {
                console.log("Teléfono debe tener 11 dígitos");
                return;
            } 
        }

        if (dato.key === 'nombre' && !inputData) {
            console.log("No puedes dejar el nombre en blanco");
            return;
        }

        persona[dato.key] = inputData;
    }

    contactos.set(persona.pronombre, persona);
    console.log("concato agregado");

};

const EliminarContacto = async () => {
    let getData = new GetData("Escriba el nombre del contacto que desea eliminar: ");
    let nombre = await getData.obtenerDatos();
    if (contactos.has(nombre)) {
        contactos.delete(nombre);
        console.log("Contacto eliminado");
    } else {
        console.log("No existe el contacto que desea eliminar");
    }
};

const BuscarContacto = async () => {
    let getData = new GetData("Escriba el nombre del contacto que desea buscar: ");
    let nombre = await getData.obtenerDatos();
    if (contactos.has(nombre)) {
        console.log(contactos.get(nombre));
    } else {
        console.log("No existe el contacto que desea buscar");
    }
};

const ModificarContacto = async () => {
    let getData = new GetData("Escriba el nombre del contacto que desea modificar: ");
    let nombre = await getData.obtenerDatos();
    if (contactos.has(nombre)) {
        let contacto = contactos.get(nombre);
        let nuevoNombre = await new GetData("Escriba el nuevo nombre: ").obtenerDatos();
        let nuevaEdad = await new GetData("Escriba la nueva edad: ").obtenerDatos();
        let nuevoSexo = await new GetData("Escriba el nuevo sexo: ").obtenerDatos();
        let nuevoTelefono = await new GetData("Escriba el nuevo numero de celular: ").obtenerDatos();
        let nuevaDireccion = await new GetData("Escriba la nueva direccion: ").obtenerDatos();
        let nuevoEmail = await new GetData("Escriba el nuevo email: ").obtenerDatos();
        let nuevoPronombre = await new GetData("Con qué nombre te gustaría guardar tu contacto?: ").obtenerDatos();

        contacto.nombre = nuevoNombre || contacto.nombre;
        contacto.edad = nuevaEdad || contacto.edad;
        contacto.sexo = nuevoSexo || contacto.sexo;
        contacto.telefono = nuevoTelefono || contacto.telefono;
        contacto.direccion = nuevaDireccion || contacto.direccion;
        contacto.email = nuevoEmail || contacto.email;
        contacto.pronombre = nuevoPronombre || contacto.pronombre;

        contactos.set(nuevoPronombre, contacto);
        if (nombre !== nuevoPronombre) {
            contactos.delete(nombre);
        }

        console.log("Contacto modificado");
    } else {
        console.log("No existe el contacto que desea modificar");
    }
};

const interfaces = async () => {
    
    const recibirOpcion = async(text) => {
        return await new Promise((resolve) => {
            const rl = readline.createInterface({
                input: process.stdin,
                output: process.stdout
            });
            rl.question(text, (opcion) => {
                rl.close();
                resolve(opcion);
            })
        });
    };

    const printHome = async() => {
        let home = (`
 *******AGENDA DE CONTACTOS*******
        1.  ver contactos
        2.  Agregar contacto 
        3.  Eliminar contacto 
        4.  Buscar contacto
        5.  Modificar contacto
        6.  Finalizar programa

        escriba su opcion: `);
        const opcionHome = await recibirOpcion(home);
        return opcionHome;
    }



    let opcion = '';
    while (opcion !== '6') {
        opcion = await printHome();
        switch (opcion) {
            case '1':
                await verContactos();
                break;
            case '2':
                await AgregarContacto();
                break;
            case '3':
                await EliminarContacto();
                break;
            case '4':
                await BuscarContacto();
                break;
            case '5':
                await ModificarContacto();
                break;
            case '6':
                console.log('Finalizando programa.');
                break;
            default:
                console.log('Opción no válida, intente de nuevo.');
        }
    }
    
};



async function main() {
    await interfaces();
}

main();
