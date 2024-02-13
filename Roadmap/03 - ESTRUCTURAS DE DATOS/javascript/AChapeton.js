// **** TIPOS DE ESTRUCTURAS ****
// ** ARRAYS **
// Tiene dos formas distintas de tiparlo pero ambas dan el mismo resultado
// Se pueden combinar los tipos de datos que se permiten almacenar o incluso personalizarlos, a estos elementos se les llama Tuplas
var numbers = [2, 4, 6, 8];
var letters = ['p', 'b', 'd', 'q'];
var combined = ['abc', true, 'def', false]; //No se permite otro tipo de dato que no sea String o Boolean
var users = [
    {
        id: 1,
        name: 'Andres',
        subscribed: true
    },
    {
        id: 2,
        name: 'Brais',
        subscribed: false
    },
    {
        id: 3,
        name: 'Chape',
        subscribed: false
    },
    {
        id: 4,
        name: 'Jesus',
        subscribed: true
    },
    {
        id: 5,
        name: 'Midudev',
        subscribed: true
    },
    {
        id: 6,
        name: 'Teffcode',
        subscribed: false
    }
];
console.log('users', users);


// Operaciones en Arrays

//Push - Agregar elementos al final
var pushUser = {
    id: 11,
    name: 'Moure',
    subscribed: true
};
users.push(pushUser);
console.log('push', users);

//Unshift - Agregar elementos al inicio
var unshiftUser = {
    id: 0,
    name: 'Mouredev',
    subscribed: false
};
users.unshift(unshiftUser);
console.log('unshift', users);

//Splice - Agregar elementos en cualquier posicion
//El primer parametro es para indicar en que posicion agregarlo
//El segundo parametro es para indicar cuantos elementos se reemplazarian (0 es ningun elemento)
//El tercer parametro es el elemento a agregar
var spliceUser = {
    id: 12,
    name: 'Chape',
    subscribed: false
};
users.splice(2, 0, spliceUser);
console.log('splice', users);

//Pop - Eliminar el ultimo elemento
users.pop();
console.log('pop', users);

//Shift - Eliminar el primer elemento
users.shift();
console.log('shift', users);

//Splice - Eliminar un elemento en cualquier posicion
//El primer parametro es la posicion del elemento
//El segundo parametro es la cantidad de elementos a eliminar desde la posiocion indicada
users.splice(2, 1);
console.log('splice', users);

//Filter - Crea un nuevo array con los elementos que cumplan el criterio
var fiteredUsers = users.filter(function (user) { return user.id < 10; });
console.log('filter', fiteredUsers);

//Sort - Metodo para ordenar datos
var unorderedArray = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
// Ordenar el array
unorderedArray.sort(function (a, b) { return a - b; });
console.log('sort', unorderedArray);


// ** SETS **
var mySet = new Set();
//Add - Agregar un valor
mySet.add(1);
mySet.add(2);
mySet.add(3);
// mySet.add('string') - No se permite porque el Set fue tipado de solo numeros
console.log('add', mySet);

//Has - Verificar si un valor existe dentro del Set
mySet.has(1); //true
mySet.has(3); //false
//Delete - Elimina un valor
mySet.delete(1);
console.log('delete', mySet);

//Size - Devuelve el tama;o del set
console.log('size', mySet.size);

//Clear - Eliminar todos los elementos
mySet.clear();
console.log('clear', mySet);

var contacts = [];
var agregarContacto = function () {
    var newName = null;
    var newPhone = null;
    do {
        newName = prompt('Nombre: ');
        if (!newName) {
            console.log('Por favor, ingresa un nombre válido.');
        }
    } while (!newName);
    do {
        newPhone = prompt('Telefono: ');
        if (!newPhone) {
            console.log('Por favor, ingresa un número de teléfono válido.');
        }
    } while (!newPhone);
    var newContact = {
        nombre: newName,
        telefono: parseInt(newPhone)
    };
    contacts.push(newContact);
};
var buscarContacto = function () {
    var searchedName = null;
    do {
        searchedName = prompt('Buscar por nombre: ');
    } while (!searchedName);
    var searchedResult = contacts.find(function (contact) { return contact.nombre.toLowerCase() === searchedName.toLowerCase(); });
    if (searchedResult === undefined) {
        alert(searchedName + ' no existe');
    }
    else {
        alert(JSON.stringify(searchedResult, null, 2));
    }
};
var actualizarContacto = function () {
    var _a, _b;
    var searchedName = null;
    do {
        searchedName = prompt('Buscar por nombre: ');
    } while (!searchedName);
    var searchedResult = contacts.findIndex(function (contact) { return contact.nombre.toLowerCase() === searchedName.toLowerCase(); });
    if (searchedResult === undefined) {
        alert(searchedName + ' no existe');
    }
    else {
        var newName = null;
        var newPhone = null;
        do {
            newName = prompt('Nuevo nombre', ((_a = contacts[searchedResult]) === null || _a === void 0 ? void 0 : _a.nombre) || '');
            contacts[searchedResult].nombre = newName;
        } while (newName === null);
        do {
            newPhone = prompt('Nuevo telefono', ((_b = contacts[searchedResult]) === null || _b === void 0 ? void 0 : _b.telefono.toString()) || '');
            contacts[searchedResult].telefono = parseInt(newPhone);
        } while (newPhone === null);
        alert(searchedName + ' fue actualizado a ' + newName);
    }
};
var eliminarContacto = function () {
    var searchedName = null;
    do {
        searchedName = prompt('Nombre de contacto a eliminar: ');
    } while (!searchedName);
    var searchedResult = contacts.findIndex(function (contact) { return contact.nombre.toLowerCase() === searchedName.toLowerCase(); });
    if (searchedResult === undefined) {
        alert(searchedName + ' no existe');
    }
    else {
        if (searchedResult >= 0 && searchedResult < contacts.length) {
            contacts.splice(searchedResult, 1);
            alert(searchedName + ' fue eliminado');
        }
        else {
            console.log('Índice inválido');
        }
    }
};
var listarContactos = function () {
    var contactsString = JSON.stringify(contacts, null, 2);
    alert(contactsString);
};
var agendaApp = function () {
    var option = '';
    var menu = 'MENU: \n 1. Agregar nuevo contacto \n 2. Buscar contacto \n 3. Actualizar contact \n 4. Eliminar un contacto \n 5. Listar todos los contactos \n 6. Salir';
    while (option !== '6') {
        option = prompt(menu);
        switch (option) {
            case '1':
                agregarContacto();
                break;
            case '2':
                buscarContacto();
                break;
            case '3':
                actualizarContacto();
                break;
            case '4':
                eliminarContacto();
                break;
            case '5':
                listarContactos();
                break;
            case '6':
                break;
            default:
                console.log('Opcion no valida. Intentar de nuevo.');
                break;
        }
    }
};
agendaApp();
