/**
 * ESTRUCTURAS DE DATOS
 */

// 1. Array
const myArray = [1, 2, 3, 4, 5];
console.log(myArray);

/* Acceder a los elementos de un Array */
console.log(myArray.length); //Tamaño de elementos de array
// -> 5
myArray[2]; //Acceder a una posición especifica del array
// -> 3
myArray[4] = 0; //Modificar un elemto del array
// -> [1, 2, 3, 4, 0]
const lastItem = myArray.length -1; //Código para acceder al último elemento cuando no se conoce el tamaño del array
console.log(myArray[lastItem]);
// -> 0
const myArrayNew = myArray.with(0, 0); //Crea una copia del array original garantizando la inmutabilidad de esta
// -> myArray = [1, 2, 3, 4, 0]
// -> myArrayNew = [0, 2, 3, 4, 0]

/* Añadir o eliminar elementos de un Array */
myArray.push(6); //Inserta el valor indicado al FINAL del array
// -> 6 == devuleve el tamaño del array ([1, 2, 3, 4, 0, 6])
myArray.unshift(0); //Inserta el valor indicado al INICIO del array
// -> 7 == devuleve el tamaño del array ([0, 1, 2, 3, 4, 0, 6])
myArray.pop(); //Extrae el ÚLTIMO valor del array
// -> 6 == devuleve el elemento extraido ([0, 1, 2, 3, 4, 0])
myArray.shift(); //Extrae el PRIMER valor del array
// -> 0 == devuleve el elemento extraido ([1, 2, 3, 4, 0])

/*  Buscar elementos en un Array */
const numbers = [5, 10, 15, 20, 25, 20, 15, 10, 5];
numbers.includes(15); //Comprueba si el elemento existe y devuleve un valor Boolean
// -> true
numbers.includes(30);
// -> false
numbers.includes(20,2); //El segundo parámetro indica la posición desde donde se empieza a buscar el elemento
// -> true
numbers.indexOf(20); //Devuleve la posición de un elemento dentro del array
// -> 4
numbers.indexOf(0);
// -> -1
numbers.indexOf(15,4) //El segundo parámetro permite encontrar elementos repetidos despues del indice indicado
// -> 6
numbers.lastIndexOf(10); //Devuelve la posición del elemento indicado, pero esta vez busca desde el último hasta el primer elementos del Array
// -> 7
numbers.lastIndexOf(50);
// -> -1
numbers.lastIndexOf(10,2);
// -> 1

/* Ordenación de un Array */
//.reverse() y .toReversed()
const elements = ['A', 'B', 'C', 'D', 'E', 'F'];
const reversedElements = elements.reverse();
// -> reversedElements = ['F', 'E', 'D', 'C', 'B', 'A']
// -> elements = ['F', 'E', 'D', 'C', 'B', 'A'] -> Array mutado

const newReversedElements = elements.toReversed();
// -> newReversedElements = ['F', 'E', 'D', 'C', 'B', 'A'];
// -> elements = ['A', 'B', 'C', 'D', 'E', 'F'] -> Array no mutado

//.sort() y .toSorted()
const names = ['Paula', 'Angela', 'Sofia', 'Karen', 'Valentina'];
const sortedName = names.sort();
// -> sortedName = ['Angela', 'Karen', 'Paula', 'Sofia', 'Valentina']
// -> names = ['Angela', 'Karen', 'Paula', 'Sofia', 'Valentina'] -> Array Mutado

const newSortedName = names.toSorted();
// -> newSortedName = ['Angela', 'Karen', 'Paula', 'Sofia', 'Valentina']
// -> names = ['Paula', 'Angela', 'Sofia', 'Karen', 'Valentina'] -> Array no mutado

//Ordenar números
const number = [1, 8, 2, 32, 9, 7, 4];

const naturalOrden = (a, b) => a - b;

const naturalNumbs = number.toSorted(naturalOrden);
// -> naturalNumbs = [1, 2, 4, 7, 8, 9, 32]


// 2. Obejto
const player = {
    name : 'Barbaros',
    life : 100,
    power : 82,
};

/* Acceder a las propiedades de un objeto */
console.log(player.name);  //Notación con punto
// -> Barbaros
console.log(player['life']);  //Notación con llaves
// -> 100

/* Añadir propiedades a un objeto*/
player.damage = 75;
player['velocity'] = 30;
console.log(player);
// -> {name: 'Barbaros', life: 100, power: 82, damage: 75, velocity: 30}

/* Ver las propiedades de un objeto */

// Método Object.keys()
const keys = Object.keys(player);
console.log(keys);
// -> ['name', 'life', 'power', 'damage', 'velocity']

// Método Object.values()
const values = Object.values(player);
console.log(values);
// -> ['Barbaros', 100, 82, 75, 30]

//Método Object.entries()
const properties = Object.entries(player);
console.log(properties);
// -> [['name', 'Barbaros'], ['life', 100], ['power', 82], ['damage', 75], ['velocity', 30]]

/* Eliminar propiedades de un objeto */
delete player.damage;
delete player['velocity'];
console.log(player);
// -> {name: 'Barbaros', life: 100, power: 82}

/* Modificar las porpiedades de un objeto */

// Modificar un valor
player.power = 90;
player['life'] = 100 + 5;
console.log(player);
// -> {name: 'Barbaros', life: 105, power: 90}

// Modificar una llave
player.avatar = player.name; // 1. asignamos el valor de la llave original a una nueva llave
delete player.name; // 2. borramos la llave original
console.log(player);
// -> {avatar: 'Barbaros', life: 105, power: 90}

/* Combinar objetos o propiedades */

// Método Object.assign
const habilidades = {vission : 50, audition : 75,};
Object.assign(player, habilidades);
console.log(player);
// -> {avatar: 'Barbaros', life: 105, power: 90, vission: 50, audition: 75}

// 3. Set
const mySet = new Set([1, 2, 2, 3, 4]);
// -> Set(4) {1, 2, 3, 4}

mySet.size; // Cantidad de elemntos de un Set
// -> 4
mySet.add(5).add('A').add('B').add(true); // Añadir elementos en un Set
// -> Set(8) {1, 2, 3, 4, 5, "A", "B", "C", true}
mySet.has(4); //Comprobar si existe un elemento en un Set
// -> true
mySet.has('a');
// -> false 'case sensitive'
mySet.delete('A'); // borrar un elemento de un Set
// -> true Set(7) {1, 2, 3, 4, 5, "B", "C", true}
mySet.clear(); //Borra todos lo elementos de un Set

console.log(mySet);
// -> Set(0) {size: 0}

// 4. Map
const myMap = new Map ([
    ['libro', 'Cien años de Soledad'],
    ['autor', 'Gabriel Garcia Marquez'],
    ['nacionalidad', 'Colombiano'],
    ['disponible', true],
]);
// -> Map(4) {'libro' => 'Cien años de Soledad', 'autor' => 'Gabriel Garcia Marquez', 'nacionalidad' => 'Colombiano', 'disponible' => true}}

myMap.size; // Cantidad de elemntos en un Map
// -> 4
myMap.set('cantidad', 0); // Se añade la clave si no existe en el Map
// -> Map(5) {'libro' => 'Cien años de Soledad', 'autor' => 'Gabriel Garcia Marquez', 'nacionalidad' => 'Colombiano', 'disponible' => true, 'cantidad' => 0}
myMap.set('disponible', false); // Se sorbreescribe el valor de la clave indicada
// -> Map(5) {'libro' => 'Cien años de Soledad', 'autor' => 'Gabriel Garcia Marquez', 'nacionalidad' => 'Colombiano', 'disponible' => false, 'cantidad' => 0}
myMap.has('autor'); // Comprueba si existe un elemento en un Map por medio de su clave
// -> true
myMap.has('Cien años de Soledad');
// -> false
myMap.delete('nacionalidad'); // borrar un elemento de un Map
// -> true
myMap.clear(); // Borrar todos lo elementos de un Map

console.log(myMap);
// -> Map(0) {size: 0}


/**
 * DIFICULTAD EXTRA
 */

// Importar el modulo 'readline' de Node.js
const { parse } = require('path');
const readline = require('readline');

// Declaración e inicialización de la interfaz
const rl = readline.createInterface({
    input: process.stdin,       // Recibe y alamcena la entreda de datos del usuario
    output: process.stdout,     // Imprime la información recibida
});

const agendaContactos = [];

const menuAgenda = () => {
    console.log(`
        MENÚ AGENDA TELEFÓNICA.
        1. Crear contacto
        2. Buscar contactos
        3. Editar contacto
        4. Ver contactos
        5. Eliminar contacto
        6. Salir de la agrenda
    `);

    rl.question('Seleccione una opción del 1 al 6: ', (opcion) => {
        switch(opcion){
            case '1':
                crearContacto();
                break;
            case '2':
                buscarContacto();
                break;
            case '3':
                editarContacto();
                break;
            case '4':
                verContacto();
                break;
            case '5':
                eliminarContacto();
                break;
            case '6':
                console.log('\nSaliendo de los contactos... ¡Adiós!');
                rl.close();
                break;
            default:
                console.log('Opción no disponible. Seleccione una opción del 1 al 6:');
                menuAgenda();
                break;
        }
    });
}

// Opcion 1: Crear contacto
const crearContacto = () => {
    rl.question('\nNombre y Apellido: ', (name) => {
        rl.question('Celular: ', (phone) => {
            if(validarLongitudCelular(phone)){
                //Guarda el Object dentro del Array agendaContactos[]
                agendaContactos.push({
                    Nombre: name, //{llave: valor}
                    Celular: phone,
                });

                console.log('\nContacto registrado.');
            } else{
                console.log('\nContacto no registrado: El celular debe tener máximo 10 números.');
            }
            menuAgenda();
        })
    })
    
}

// Opcion 2: Buscar contactos
const buscarContacto = () => {
    if(agendaContactos.length === 0){
        console.log('\nNo hay usuarios registrados.');
        return menuAgenda();
    }

    rl.question('\nIngrese el nombre del contacto: ', (name) => {
        const encontrarContacto = agendaContactos.find(contacto => contacto.Nombre.toLocaleLowerCase().includes(name.toLocaleLowerCase()));
        
        if(encontrarContacto){
            console.log(`
                Contacto encontrado.
                Nombre: ${encontrarContacto.Nombre}
                Celular: ${encontrarContacto.Celular}
            `);
        } else{
            console.log('El contacto no existe.');
            
        }

        menuAgenda();
    })
}

//Opcion 3: Editar contacto
const editarContacto = () => {
    rl.question('\nIngresa el nombre del contacto: ', (name) => {
        const indiceContacto = agendaContactos.findIndex(contacto => contacto.Nombre.toLocaleLowerCase() === name.toLocaleLowerCase()) ?? -1;

        if(indiceContacto === -1){
            console.log("El contacto no existe.");
            return menuAgenda();
        } else{
            const menuEditarContacto = () => {
                console.log(`
                    ¿Qué dato quieres actualizar:
                    1. Nombre y Apellido
                    2. Celular
                    3. Toda la información del contacto
                    4. Volver al menú principal
                `);
                rl.question(`Seleccione una opción del 1 al 3: `, (opcion) => {
                    switch(opcion){
                        case '1':
                            rl.question('\nEscriba el nuevo Nombre y Apellido: ', (newName) =>{
                                agendaContactos[indiceContacto].Nombre = newName;
                                console.log('Nombre y Apellido de contacto actualizado.');

                                menuAgenda();
                            });
                            break;

                        case '2':
                            rl.question('\nEscriba el nuevo número: ', (phone) => {
                                if(validarLongitudCelular(phone)){
                                    agendaContactos[indiceContacto].Celular = phone;
                                    console.log('Celular actualizado.');
                                    menuAgenda();
                                } else{
                                    console.log('Error: El celular debe tener máximo 10 números.');
                                    menuEditarContacto();
                                }
                            });
                            break;

                        case '3':
                            rl.question('\nEscriba el nuevo Nombre y Apellido: ', (newName) => {
                                rl.question('Escriba el nuevo número: ', (phone) => {
                                    if(validarLongitudCelular(phone)){
                                        agendaContactos[indiceContacto] = {Nombre: newName, Celular: phone};
                                        console.log('\nContacto actualizado.')
                                        menuAgenda();
                                    } else{
                                        console.log('\nNo se actualizó la información del contacto : El celular debe tener máximo 10 números.');
                                        menuEditarContacto();
                                    }
                                });
                            });
                            break;
                        
                        case '4':
                            menuAgenda();
                            break;

                        default:
                            console.log('Opción no disponible. Seleccione una opción del 1 al 3.');
                            menuEditarContacto();
                            break;
                        }
                });
            }
            menuEditarContacto();
        } 
    });
}

// Opcion 4: Ver contactos
const verContacto = () => {
    if(agendaContactos.length === 0){
        console.log('Aún no hay contactos registrados.');
    } else{
        for(const registros of agendaContactos){
            console.log(registros);
        }
    }

    rl.question('\n¿Quiere registrar un nuevo contacto? (Si/No) ', (registroNuevo) => {
        if(registroNuevo.toLocaleLowerCase() === 'si'){
            crearContacto()
        } else{
            menuAgenda();
        }
    });
}

// Opcion 5: Elimianr contacto
const eliminarContacto = () => {
    rl.question('\nIngrese el nombre del contacto: ', (name) => {
        const indiceContacto = agendaContactos.findIndex(contacto => contacto.Nombre.toLocaleLowerCase() === name.toLocaleLowerCase()) ?? -1;

        if(indiceContacto === -1){
            console.log("El contacto no existe.");
            return menuAgenda();
        } else{
            rl.question(`\n¿Esta seguro que quiere eliminar a ${name} de sus contactos? `, (confirmarBorrado) => {
                if(confirmarBorrado.toLocaleLowerCase() === 'si'){
                    agendaContactos.splice(indiceContacto, 1);
                    console.log('\nContacto eliminado');
                    menuAgenda();
                } else{
                    return menuAgenda();
                }
            });
        }
    });
}

//Valida condición del telefono
const validarLongitudCelular = function (telefono){
    if(!isNaN(telefono) && telefono.length === 10){ //Código para verificar que sea un dato Number y que tenga 10 digitos
        return true;
    } else{
        return false;
    }
}


menuAgenda();