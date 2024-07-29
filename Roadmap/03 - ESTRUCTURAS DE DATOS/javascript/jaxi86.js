/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */

console.log('OBJETOS');

let miObjeto = {
    nombre : 'jaxi',
    apellido :'jax',
    edad : 23,
}

console.log(miObjeto);

miObjeto.email='jaxijax86@gmail.com';//insercion.
console.log(miObjeto);

delete miObjeto.edad;//borrado.
console.log(miObjeto)

miObjeto.nombre='josue';//actualizacion.
console.log(miObjeto)

//no hay operacion de ordenacion para objetos

console.log('ARRAY');

let miArray = [2, 5, 4, 9];
let mi2Array = [55, 88, 11, 99];
console.log(miArray);

miArray[4] =1;//insercion en un indice que le indique.
miArray.push(3);//insercion siempre de ultimo indice del array.
miArray.unshift(10);//insercion siempre en el indice 0 del array empujando a los demas a lo indices siguientes
console.log(miArray);

delete miArray[1];//borrar el valor de un indice que le indiquemos.
miArray.pop();//borrar el valor del ultimo indice
miArray.shift();//borrar el valor del indice 0
miArray.splice(2,3)//borrar (el primer numero es el indice de donde se quiere empezar a borrar, el segundo es de CUANTOS indices a la derecha se quiere borrar contando el indice que se quiere borrar)
console.log(miArray);

miArray[0]=15;//actualizacion.
console.log(miArray);

mi2Array.sort();//ordenacion
console.log(mi2Array)

console.log('MAPS')


let miMapa = new Map();
console.log(miMapa)


miMapa.set('clave1', 1);// Inserción
miMapa.set('clave2', 'valor2');
console.log(miMapa)

miMapa.delete('clave1');//borrar
console.log(miMapa);

miMapa.set('clave2', 'nuevo valor')//actualizacion
console.log(miMapa)

//no hay operacion para ordenar un mapa

console.log('SET')

let miSet = new Set([1, 5, 8, 2]);
console.log(miSet);

miSet.add(4);//insercion.
console.log(miSet);

miSet.delete(1);
console.log(miSet);

//no tiene un opperador para actualizar

//no tiene un operador para ordenacion

console.log('DIFICULTAD EXTRA');

let lista = [];

function validarNumerotele (numero){
    return /^\d{11}$/.test(numero);
}


function buscarContactos (nombre){
    return lista.find(contacto => contacto.Nombre === nombre);
}

function panelPrincipal (){
    console.log('marca 1 para registrar un contacto, 2 para actualizar un  contacto, 3 para buscar contacto, 4 para eliminar contacto y 5 para salir de la funcion');
    let eleccion = prompt('ingresa un numero para elegir una accion: ');

    switch(eleccion){
        case '1':
            insertarContacto();
            break;
        case '2':
            actualizarContacto();
            break;
        case '3':
            buscarYMostrarContactos();
            break;
        case '4':
            borrarContacto();
            break;
        case '5':
            console.log('saliste del programa');
            break;
    }
}
panelPrincipal();

function insertarContacto(){//1
    console.log('maraca 1 para ingresar contacto, 2 para volver al panel principal');
    let eleccion = prompt ('marca una opcion')
    switch (eleccion){
        case '1':
            let nombre = prompt('escribe el nombre del contacto');
            let numero = prompt('escribe el numero del contacto');
        
            if (validarNumerotele(numero)){
                lista.push({Nombre: nombre, Numero: numero});
                console.log('contacto guardado');
            }else{ console.log('contacto no valido') }
        case '2':
            return panelPrincipal();
        default:
            console.log('accion no valida');
            return insertarContacto();
    }
    
}

function actualizarContacto (){//2
    console.log('buscar contacto para actualizar');
    let buscando = prompt('introduce el nombre del contacto que desea actualizar: ');    
    if(lista.find(contacto => contacto.Nombre === buscando)){
        lista.Nombre = prompt ('nuevo nombre del contacto');
        lista.Numero = prompt ('nuevo numero telefonico');
        console.log('contacto actualizado');
    }else{ console.log('contacto no encontrado')}
    return panelPrincipal();
}

function buscarYMostrarContactos(){//3
    console.log('marca 1 para ver un contacto indicado, 2 para ver todos los contactos, 3 para volver atras');
    let eleccion = prompt ('seleciona una opcion');

    switch(eleccion){
        case '1':
            let buscando = prompt('introduce el nombre del contacto que desea ver: ');
            let verContacto = buscarContactos(buscando)
            if(verContacto){
                for (idx of lista){
                    if (idx === verContacto){
                        console.log(idx);
                    }
                }
            }else{ console.log('contacto no encontrado')}
            break;
        case '2':
            console.log(lista);
            break;
        case '3':
            return panelPrincipal();
            break;
        default:
            console.log('accion no reconocida');
            
    }
    return panelPrincipal()
}

function borrarContacto(){//4
    console.log ('ingresa el nombre del contacto que desea borrar');
    let buscando = prompt('introduce el nombre del contacto que desea borrar: ');
    let contactoBorrar = buscarContactos(buscando)
    
    if(contactoBorrar){
        lista = lista.filter(contacto => contacto.Nombre !== contactoBorrar);
        console.log('contacto borrado')
    }else{ console.log('contacto no encontrado')}
    return panelPrincipal()
}

