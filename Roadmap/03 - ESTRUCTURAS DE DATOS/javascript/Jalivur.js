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

//ESTRUCTURAS DE DATOS:
//ARRAY
console.log(`===============`);
console.log(`ARRAYS: se pueden definir 
de 3 formas:`);
let arr1 = new Array(1, 1.1, "hola", true);
console.log(`let arr1 = new Array (1, 1.1, "hola", true)  
${arr1}`);
console.log(`===============`);
let arr2 = Array(1, 1.1, "hola", true);
console.log(`let arr2 = Array (1, 1.1, "hola", true)
${arr2}`);
console.log(`===============`);
let arr3 = [1, 1.1, "hola", true];
console.log(`let arr3 = [1, 1.1, "hola", true]
${arr3}`);
console.log(`===============`);
console.log(`Tambien se pueden asignar 
como propiedade de un objeto:
let obj1 = {}
obj1.prop = arr3`);
let obj1 = {};
obj1.prop = arr3;
console.log(obj1);
console.log(`===============`);
let arrayEmpty = Array(42);
console.log(`Tambien se pueden crear
sin elementos:
let arryEmpty = Array(${arrayEmpty.length})
${arrayEmpty}
en este caso con longitud ${arrayEmpty.length}.
Siempre y cuando el valor sea un numero entero.`);
console.log(`===============`);
let arrayEmpty2 = new Array(15);
console.log(`Tambien se puede:
let arryEmpty = new Array(${arrayEmpty2.length})
${arrayEmpty2}
en este caso con longitud ${arrayEmpty2.length}.
Si el valor no es numero enter, dara error de rango.`);
console.log(`===============`);
let arrayOneElement = [58];
console.log(`Sin ebargo con la declaracion literal:
let arryOneElement = [${arrayOneElement}]
en este caso es un array de un elemento: ${arrayOneElement}
culla longitud es ${arrayOneElement.length}.`);
console.log(`===============`);
let arrayOneElement2 = Array.of(10.5);
console.log(`Desde ES2015 se puede utilizar el metodo estatico Array.of:
let arryOneElement2 = Array.of(${arrayOneElement2})
en este caso es un array de un elemento: ${arrayOneElement2}
culla longitud es ${arrayOneElement2.length}.`);
console.log(`===============`);

//Manejo de arrays:
console.log(`===============`);
console.log(`Operaciones Con Arrays`);
console.log(`===============`);
let arrayEmpty3 =[];
console.log(`Un array se puede declarar vacio, let arrayEmpty3 = [${arrayEmpty3}];`);
console.log(`===============`);
arrayEmpty3.push("Alberto","Estella");
console.log(`Con el metodo arraEmpy3.push("${arrayEmpty3[0]}","${arrayEmpty3[1]}"), añadimos contenido [${arrayEmpty3}]`);
console.log(`===============`);
console.log(`===============`);
let array1=arrayEmpty3;
let array2=new Array("Jalivur","Pamplona");
console.log(`Teniendo dos array, array1=[${array1}] y array2=[${array2}],
Con el metodo array1.concat(array2), concatenamos el contenido [${array1=array1.concat(array2)}]`);
console.log(`===============`);
console.log(`===============`);
array1[4]=true;
console.log(`Tambien podemos añadir, o modificar los valores de un array haciendo referencia al index a añadir o modificar,
array1[4]=${array1[4]}, de esta manera ahora array1=[${array1}].`);
array1[3]="Falces"
console.log(`Si hacemos referencia a un index vacio, lo ocupamos, mientras que si hacemos referencia a un index ocupado, actualizamos su valor.
array1[3]="${array1[3]}", ahora el array queda array1=[${array1}]`);
array1[20]="hola"
console.log(`Si hacemos referencia a un index vacio lejano de los ocupados,
array1[20]="${array1[20]}", ahora el array queda array1=[${array1}]`);
console.log(`===============`);
console.log(`===============`);
let allValues=array1.join('-');
console.log(`Con el metodo join(delimiter=('-')) podemos unir todos los elementos en un string separados por el caracter del delimitador,
let allValues=array1.join('-')= ${allValues}.`);
console.log(`===============`);
console.log(`===============`);
let popValue = array1.pop();
console.log(`Con el metodo pop() extrae el ultimo valor del array,
let popValue = array1.pop()= ${array1}.
podemos usar par ir eliminando los valores desde el ultimo, o podemos almacenar esos valores en variables.
popValue = ${popValue}`);
console.log(`===============`);
console.log(`===============`);
let shiftValue = array1.shift();
console.log(`Con el metodo shift() extrae el primer valor del array,
let shiftValue = array1.shift()= ${array1}.
podemos usar par ir eliminando los valores desde el primero, o podemos almacenar esos valores en variables.
shiftValue = ${shiftValue}`);
console.log(`===============`);
console.log(`===============`);
let unshiftValue1 = ("Alberto");
let unshiftValue2 = (2);
array1.unshift(unshiftValue1,unshiftValue2)
console.log(`Con el metodo unshift() añadir valores al principio del array,
array1.unshift(${unshiftValue1},${unshiftValue2})= ${array1}.`);
console.log(`===============`);
console.log(`===============`);
let startIndex=0;
let upToIndex=4;
let sliceArray = array1.slice(startIndex,upToIndex)
console.log(`Con el metodo slice() añadir valores al principio del array,
array1.slice(${startIndex},${upToIndex})= [${sliceArray}}].`);
console.log(`===============`);
console.log(`===============`);
let index=5;
let countToRemove=20;
let addElement1="Tecnico De Mantenimento";
let addElement2="Volkswagen Navarra";
array1.splice(index, countToRemove, addElement1, addElement2)
console.log(`Con el metodo splice() eliminar valores, indicando el primer index a eliminar, y el numero de valores a eliminar,
y opcionalmente se pueden añadir valores.
array1.splice(${index},${countToRemove},${addElement1},${addElement2})= [${array1}].`);
console.log(`===============`);
console.log(`===============`);
console.log(`array1=[${array1}]`)
array1.reverse()
console.log(`Con el metodo revese() invertimos el orden del array.
array1.reverse()= [${array1}].`);
console.log(`===============`);
console.log(`===============`);
console.log(`array1=[${array1}]`)
array1.sort()
console.log(`Con el metodosort() ordenamos el array.
array1.sort()= [${array1}].`);
console.log(`===============`);

//Map:
console.log(`===============`);
console.log(`Objeto Mapa, Map(), son objetos clave,valor:
Se puede definir,
let matrimonios = new Map()`);
let matrimonios = new Map();
let setKey1 = "Alberto";
let setValue1 = "Sandra";
let setKey2 = "Cesar";
let setValue2 = "Nadie";
matrimonios.set(setKey1, setValue1);
matrimonios.set(setKey2, setValue2);
console.log(`===============`);
console.log(`Con el metodo set(), añadimos las parejas de clave valor al mapa.
let setKey1 = "Alberto";
let setValue1 = "Sandra";
let setKey2 = "Cesar";
let setValue2 = "Nadie";
matrimonios.set(setKey1, setValue1)
matrimonios.set(setKey2, setValue2)`);
for (let [key, value] of matrimonios) {
    console.log(key + " esta casado con " + value);
};
console.log(`===============`);
console.log(`===============`);
matrimonios.delete(setKey2)
console.log(`Con el metodo delete(), eliminamos mediante la clave, el objeto del mapa correspodiente.
matrimonios.delete("${setKey2}")`);

for (let [key, value] of matrimonios) {
    console.log(key + " esta casado con " + value);
};
console.log(`===============`);
console.log(`===============`);
console.log(`Con el metodo has(), podemos comprobar si algo se encuentra en el mapa.`);
console.log(`matrimonios.has(${setKey1})=${matrimonios.has(setKey1)}`);
console.log(`matrimonios.has(${setKey2})=${matrimonios.has(setKey2)}`);
console.log(`===============`);
matrimonios.set(setKey2,setValue2)
console.log(`Al volver a utilizar el metodo set(), ahora matrimonios.has(${setKey2})=${matrimonios.has(setKey2)}`);
console.log(`===============`);
console.log(`===============`);
console.log(`Con el metodo get() obtenemos el valor para una clave, matrimonios.get(${setKey2})=${matrimonios.get(setKey2)}.`);
console.log(`===============`);
console.log(`===============`);
console.log(`Con el metodo size() obtenemos el valor del tamaño del mapa, matrimonios.size=${matrimonios.size}.`);
console.log(`===============`);
console.log(`===============`);
matrimonios.clear();
console.log(`Con el metodo clear() limpiamos el mapa, matrimonios.clear() = matrimonios.size = ${matrimonios.size}.`);
console.log(`===============`);

//Set:
console.log(`===============`);
let mySet = new Set();
let setValue3 = 1;
let setValue4 = "algún texto";
let setValue5 = "foo";
mySet.add(setValue3);
mySet.add(setValue4);
mySet.add(setValue5);
console.log(`Un objeto Set, se declara:
let mySet = new Set();.
Estos son colecciones de valores, con el metodo add() añadimos valores.
let setValue3 = 1;
let setValue4 = "algún texto";
let setValue5 = "foo";
mySet.add(${setValue3});
mySet.add(${setValue4});
mySet.add(${setValue5});`)
for (let item of mySet) console.log(item);
console.log(`===============`);
console.log(`mySet.has(${setValue3}) = ${mySet.has(setValue3)}`); // true
console.log(`===============`);
mySet.delete("foo");
mySet.size; // 2
for (let item of mySet) console.log(item);
console.log(`===============`);
const { copyFileSync } = require('fs');
/*
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

//Creacion de interactividad con consola.
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,

});
//Variables
let agenda = [
    {"nombre":"alberto", "tel":"638432255", "email":"esteya92@gmail.com"},
]

let nombre;
let tel;
let email;
let busqueda;
let contacto;
let select;

//Funciones
function insertAgenda(nombre,tel,email){
        const esTelefonoValido = (telefono) => {
            // Verifica que el teléfono solo contenga dígitos
            const contieneSoloDigitos = Array.from(telefono).every(caracter => '0123456789'.includes(caracter));
            return contieneSoloDigitos && telefono.length <= 11;
        };
        if (esTelefonoValido(tel)){
            contacto={
                "nombre":nombre,
                "tel":tel,
                "email":email,
            };
            agenda.push(contacto);
            console.log(`===============`);
            console.log("Contacto añadido con exito.");
            console.log(`===============`);
            main();
        }else{
            console.log(`===============`);
            console.log("Telefono no valido, deve contener solo numeros y maximo 11.");
            console.log(`===============`);
            main();
        };
};

function buscar(busqueda){
        let contacto= agenda.find(contacto=>contacto.nombre===busqueda);
        if (contacto){
            console.log(`===============`);
            console.log("Buscando····");
            console.log(`===============`);
            console.log("Contacto Encotrado: ");
            console.log(`===============`);
            console.log(contacto);
            console.log(`===============`);
        }else{
            console.log(`===============`);
            console.log("Contacto no encotrado, Pruebe de nuevo.");
            console.log(`===============`);
        };
};

function actualizar(nombre, tel, email){
    contacto= agenda.findIndex(contacto=>contacto.nombre === nombre, tel, email);
    if (contacto !== -1){
        if (tel){
            agenda[contacto].tel = tel;
        }
        if(email){
            agenda[contacto].email = email;
        }
        console.log(`===============`);
        console.log(`Informacion actualizada: ${JSON.stringify(agenda[contacto])}`);
        console.log(`===============`);
    }else{
        console.log(`===============`);
        console.log("Contacto no encotrado, Pruebe de nuevo.");
        console.log(`===============`);
    }

}

function eliminar(nombre){
    
    const agendaActualizada = agenda.filter(contacto => contacto.nombre !== nombre);
    
    if (agenda.length !== agendaActualizada.length){
        console.log(`===============`);
        console.log('Contacto eliminado con exito');
        console.log(`===============`);
        agenda = agendaActualizada;
        console.log(`===============`);
        console.log(agenda);
        console.log(`===============`);
    }else{
        console.log(`===============`);
        console.log('Persona no encontrada');
        console.log(`===============`);
    };
};

function listaContactos(){
    console.log(`===============`);
    console.log("Esta es tu agenda completa:");
    console.log(agenda);
    console.log(`===============`);
};

//Menu de seleccion.
function main(){
    console.log(`===============`);
        rl.question("Eliga una opcion: \nopcion 1, insertar contacto, \nopcion 2, buscar contacto, \nopcion 3, mostrar agenda completa, \nopcion 4, actualizar, \nopcion 5, eliminar, \nopcion 6, salir, \n¿Cual elige?:", (respuesta) =>{
            select = respuesta;
            switch(select){
                case "1":
                    console.log(`===============`);
                    rl.question("Nombre del contacto: ", (respuesta) =>{
                        nombre = respuesta
                        let contacto=agenda.find(contacto=>contacto.nombre===nombre);
                        if (contacto){
                            console.log(`===============`);
                            console.log(contacto);
                            console.log(`===============`);
                            console.log(`Existe un contacto con nombre ${nombre}, instroduzca nombre diferente.`);
                            console.log(`===============`);
                            main();
                        }else{
                            console.log(`===============`);
                            console.log(`Tu contacto se llama ${respuesta}`)
                            console.log(`===============`);
                            rl.question("Telefono del contacto: ", (respuesta) =>{
                                tel = respuesta
                                console.log(`===============`);
                                console.log(`Tu contacto tiene el telefono ${respuesta}`);
                                console.log(`===============`);
                                rl.question("Email del contacto: ", (respuesta) =>{
                                    email = respuesta
                                    console.log(`===============`);
                                    console.log(`Tu contacto tiene el email ${respuesta}`);
                                    console.log(`===============`);
                                    insertAgenda(nombre,tel,email);
                                    main();
                                });
                            });
                        };
                    });
                    break;
                case "2":
                    console.log(`===============`);
                    rl.question("Nombre del contacto a buscar: ",(respuesta)=>{
                        busqueda=respuesta;
                        buscar(busqueda);
                        main();
                    });
                    break;
                case "3":
                    listaContactos();
                    main();
                    break;
                case "4":
                    console.log(`===============`);
                    rl.question("Nombre del contacto a actualizar: ", (respuesta) =>{
                        nombre = respuesta
                        let contacto= agenda.find(contacto=>contacto.nombre===nombre);
                        if (contacto){
                            console.log(`===============`);
                            console.log(`Tu contacto se llama ${respuesta}`);
                            console.log(`===============`);
                            rl.question("Nuevo Telefono del contacto: ", (respuesta) =>{
                                tel = respuesta
                                if (tel){
                                    console.log(`===============`);
                                    console.log(`Tu contacto tiene ahora el telefono ${respuesta}`);
                                }else{
                                    console.log(`===============`);
                                    console.log(`Tu contacto tiene ahora el mismo telefono que antes ${contacto["tel"]}`);
                                    console.log(`===============`);
                                }
                                console.log(`===============`);
                                rl.question("Email del contacto: ", (respuesta) =>{
                                    email = respuesta
                                    if (email){
                                        console.log(`===============`);
                                        console.log(`Tu contacto tiene ahora el email ${respuesta}`);
                                        actualizar(nombre,tel,email);
                                        main();
                                    }else{
                                        console.log(`===============`);
                                        console.log(`Tu contacto tiene ahora el mismo email que antes ${contacto["email"]}`);
                                        console.log(`===============`);
                                        actualizar(nombre,tel,email);
                                        main();
                                    }
                                });
                            });
                        }else{
                            console.log(`===============`);
                            console.log("Contacto no Encontrado.");
                            console.log(`===============`);
                            main();
                        };
                    });
                    break;
                case "5":
                    console.log(`===============`);
                    rl.question("Nombre del contacto a eliminar: ",(respuesta)=>{
                        busqueda=respuesta;
                        eliminar(busqueda);
                        main();
                    });
                    break;
                case "6":
                    console.log(`===============`);
                    console.log("Te veo pronto, Adios.");
                    console.log(`===============`);
                    rl.close();
                    break;
                default:
                    console.log(`===============`);
                    console.log("Inserte opcion valida");
                    console.log(`===============`);
                    main();
                    
            };

        });
};
main();










