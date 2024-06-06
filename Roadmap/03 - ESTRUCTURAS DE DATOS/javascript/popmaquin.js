/*__Estructura de datos__*/


/*.............colecciones indexadas.............*/


//--Array (matriz)-- => datos ordenados por indice numerico
// Formas de crear una matriz
matriz1 = new Array(" elemento1"," elemento2"," elemento3");
matriz2 = Array("elemento1","elemento2","elementoN");
matriz3 = ["elemento1","elemento2","elementoN"];


//Métodos para manipular matriz.
console.log(matriz1); //salida: ['elemento1', 'elemento2', 'elemento3']


//-Insercion- Agrega elementos al final y devuelve la longitud.
console.log("ahora tiene: "+matriz1.push("elemento10")+" elemento"); //4
console.log(matriz1); // ['elemento1', 'elemento2', 'elemento3', 'elemento10']


//-Elimina- 'elemento10' el último elemento y devuelve.
console.log("Eliminado: "+ matriz1.pop());


//-Actualiza- el valor del indece 1 por 'elemento4'
console.log("Actualizacion de valor indice 1 ")
console.log(matriz1[1] = " elemento4");
console.log(matriz1); // ['elemento1', 'elemento4', 'elemento3']


//-Ordena- los elemento y devuelve la matriz ordenada.
console.log("Ordenado ");
console.log(matriz1.sort());// ['elemento1', 'elemento3', 'elemento4']




/*.............colecciones con clave.............*/


//map
let mimap = new Map();
console.log(mimap.size);


//Métodos para manipular Map.
//Ingresar datos
mimap.set('nombre', 'Julio');
mimap.set('apellido', 'Maquin');
mimap.set('edad', '25');


console.log(mimap.size); //3

//-Eliminar-
mimap.delete('nombre')
console.log(mimap.get('nombre')); // undefined
console.log(mimap.get('apellido')); //Maquin
console.log(mimap.has('apellido')); //true


// Actualizacion
console.log(mimap.set('edad','32')); //['edad', '32']


console.log("Antes de ordenar");
console.log(mimap);// Ordenacion

//Elementos Map Ordenado por valores.
console.log("Map ordenado por valores");
let mapOrdenado= [...mimap.values()].sort();
console.log(mapOrdenado);
/*----------------------------*/


//WeakMap
let wekMap = new WeakMap();


// Objeto1 clave y valor
let clave1 = {
    id: 1
}
let obj1 = {
    marca: 'Toyota',
    modelo: 'Civic'
}
// Objeto2 clave y valor
let clave2 = {
    id: 2
}
let obj2 = {
    marca: 'Honda',
    modelo: 'Civic'
}
// Objeto2 clave y valor
let clave3 = {
    id: 3
}
let obj3 = {
    marca: 'Mazda',
    modelo: 'Sedan'
}
// Objeto4
let obj4 = {
    marca: 'Mazda',
    modelo: 'CX-3'
}


//Ingresar datos
//weakMap.set(clave, valor)
wekMap.set(clave1, obj1 );
wekMap.set(clave2, obj2 );
wekMap.set(clave3, obj3 );


//Mostrar los elementos.
console.log("Mostrar datos ingresados. ");
console.log(wekMap);


//Eliminar
//weakMap.delete(clave)
console.log("se ha eliminado exitosamente.");
console.log(wekMap.delete(clave3)); //true


//weakMap.has(clave)
console.log("comprobamos si existe objeto clave3.");
console.log(wekMap.has(clave3)); // false


//Actualizar
console.log("Objeto clave1 se actualiza valor con obj4. ");
console.log(wekMap.set(clave1, obj4 ));


//weakMap.get(clave)
console.log("Obtener dato objeto: clave2 ");
console.log(wekMap.get(clave2)); //{marca: 'Honda', modelo: 'Civic'}


//Ordenar
console.log("No es posible ordenar los elementos de WeakMap.");


/*----------------------------*/


//Set() con datos
let miset = new Set(['uno', 'dos'])


//Ingresar datos
miset.add('tres');
miset.add('cinco');


//Mostrar los elementos.
console.log("Mostrar datos ingresados. ");
console.log(miset);//{'uno', 'dos', 'tres', 'cinco'}


//Eliminar
console.log(" 'true' eliminado exitosamente si no, 'false' no existe");
console.log(miset.delete('tres')); //true o false


//miset.has('tres')
console.log("comprobamos si existe 'tres'.");
console.log(miset.has('tres')); // false o true


//miset.values()
console.log(miset.values());


//Actualizar
console.log("Set no proporciona un metodo para actualizar.");
//Ordenar
console.log("No proporciona un metodo para ordenar, Pero es posible convertirlo en array");




/*----------------------------*/


//WeakSet() /Solo admite objetos
let miwkset = new WeakSet();


// objetos
let objeto1 = {nombre: "objeto1"};
let objeto2 = {nombre: "objeto2"};
let objeto3 = {nombre: "objeto3"};

console.log(miwkset);

//Ingresar datos - add(value)
miwkset.add(objeto1);
miwkset.add(objeto2);
miwkset.add(objeto3);

//Eliminar - delete(value)
console.log("Se elimino objeto3:");
console.log(miwkset.delete(objeto3));

//-- has(value)
//Comprobar si un objeto está en el WeakSet
console.log("Objeto3 existe en weakset: ");
console.log(miwkset.has(objeto3));

//Actualizar
console.log("Set no proporciona un metodo para actualizar.");
//Ordenar
console.log("Set no proporciona un metodo para ordenar.");


/*.............Dificultad Extra.............*/ 

//Funcionalidad
/*
* Inserccion
* Busqueda
* actualizacion
* eliminación
*/

console.log("               Dificultad Extra  ")

function crearAgenda(){

    let agenda = new Map();
    let opcion;
    let condicion = true;
    let nombre = "";
    let numero = "";

    while (condicion) {
        console.log(" ");
        console.log(" 1. Crear contacto");
        console.log(" 2. Buscar contacto");
        console.log(" 3. Actualizar contacto");
        console.log(" 4. Eliminar contacto");
        console.log(" 5. Salir ");
    
        opcion = parseInt(prompt("Elige una opcion: "));

        switch (opcion) {
                case 1:
                
                nombre = prompt("Ingrese nombre: ");
                numero = prompt("Ingrese numero celular: ");

                if (numero.length>0 && numero.length<=8) {
                    agenda.set(nombre, numero);
                    console.log("Contacto guardado ");
                }else {
                    console.log(" El numero celular solo admite 8 digitos ");
                }
                    break;
                
                case 2:  
                    nombre = prompt("Ingrese nombre: ");
                    if ((agenda.has(nombre)) == true) {
                        console.log(nombre); 
                        console.log(agenda.get(nombre)); // muestra el numero de contacto
                    } else {
                        console.log("No existe el contacto.")
                    }
                    
                    break;

                case 3:
                    nombre = prompt("Ingrese nombre: ");
                    if ((agenda.has(nombre)) == true) {
                        numero = prompt("Ingrese el numero para actualizar: "); 
                        console.log(agenda.set(nombre, numero));
                        console.log("Se actualizo el contacto.");
                    } else {
                        console.log("No existe el contacto.");
                    }
                    break;

                case 4:
                    nombre = prompt("Ingrese nombre para eliminar: ");
                    if ((agenda.has(nombre)) == true) {
                        agenda.delete(nombre);
                        console.log("Contacto eliminado ");
                    } else {
                        console.log("No existe el contacto.");
                    }
                    break;

                case 5:
                    condicion =false;
                    console.log("Gracias por utilizar el programa")
                    break;

                default:
                console.log("Digite una opcion desde 1 a 5 ")
                    break;
        }
    }
}

crearAgenda();