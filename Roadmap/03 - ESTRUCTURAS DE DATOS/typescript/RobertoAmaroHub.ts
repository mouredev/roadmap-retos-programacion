import * as readline from 'readline';

/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
**/
function printArray(array: any[],text?:string){
    if(text){
        console.log("\n"+text);
    }
    for(let i of array){
        console.log(i);
    }
}
//**************Arrays************************
let animales: string[] = ["Perro","Gato","Pez"]
printArray(animales);
//Agregar un elemento utilizando push -> Te permite agregar un elemento al final del array.
animales.push("Cocodrilo");
printArray(animales, "nuevo dato agregado:");

//Acceder a un elemento
let primerAnimal: string=animales[0];
console.log("\n"+primerAnimal);

//Saber la longitud del array
console.log(`\ntotal de elementos en el array: ${animales.length}`) //Imprimirá cuantas cadenas de texto que hay dentro del array

//Modificar contenido
animales[animales.length-1] = "Castor"
printArray(animales,"Último elemento modificado:")

//Readonly -Previene que el array sea editado después de haber sido creado e inicializado. Evitando así problemas futuros en la estructura del programa por modificaciones indebidas.
let ints: readonly number[]=[3,2,1];
//ints.push(2); //Error: Property "push" does not exist on type "readonly number[]".

//Eliminar elemento utilizando pop -> Te permite eliminar el último elemento que hay en el array.
animales.pop() //eliminamos al Castor que es el último elemento
printArray(animales,"Último elemento eliminado:")

//Funciones disponibles de un array
//Concat -Devolverá un array con los nuevos valores que le pasemos cómo parámetros a esta función. Dichos parámetros podrán ser un valor suelto u otra array con valores del mismo tipo de dato:
//concat(value1, value2, value3, ..... , valueN);
let autos:string[]=["Civic","Hilux","F150"];
let masAutos:string[]=["Corvette","M3","Oddysey"];
let autosTotal=autos.concat(masAutos);
printArray(autosTotal,"\nLista de autos:");

//every -> Nos permite conocer, mediante una función dada que tiene que devolver un booleano, si todos los elementos del array pasan la prueba.
//every(callback[, thisObject]);
let everyArray:number[]=[3,4,5,6,7,8];
let resEvery=everyArray.every((value)=>value>2); //Preguntamos si cada elemento dentro del array es mayor a 2
console.log(`\nel resultado de la prueba es: ${resEvery}`); //Para este caso la respuesta es true

//filter -> Devolverá un array con el contenido que pase correctamente por la función de filtro. Dicha función de filtro tendrá el mismo funcionamiento que la función "every".
//filter (callback[, thisObject]);
let filterArray:number[] = [23,4,6,72,1,100,3];
let resFilter = filterArray.filter((value)=>value%3==0);
printArray(resFilter,"\nNuevo arreglo filtrando solo multiplos de 3: ");

//forEach -> Nos permite recorrer todos los índices de un array mediante una función callback. Dicha función tendrá como parámetro el valor del índice del array según se vaya ejecutando de manera secuencial.
//forEach(callback[, thisObject]);
//NOTA: Hay que tener especial cuidado con esto. Se ejecutará de manera asíncrona y no detendrá el flujo de ejecución de la aplicación a menos que nosotros se lo indiquemos explícitamente.
let forEachArray: number[]=[34,5,6,1,3,4,100];
function printForEach(value:number){
    console.log(value);
}
console.log("\nValores del forEach:");
forEachArray.forEach(printForEach);

//indexOf -> Nos devolverá el índice donde se encuentra el valor dado cómo parámetro. Devolverá -1 en caso de que no exista. El parámetro "fromIndex" nos permite definir desde que índice del array comenzar siendo 0 el valor por defecto:
//indexOf(searchElement[, fromIndex]);
let indexOfArray:number[]=[34,5,22,66,2,1,9];
console.log("\nPosición del indexOfArray 22:");
for(let i in indexOfArray){
    console.log(`${i} : ${indexOfArray[i]}`);
}
console.log(indexOfArray.indexOf(22));

//join -> Nos permite convertir el contenido del array en una cadena de texto con un separador que le daremos a la función como parámetro:
//join(separator);
let joinArray:string[] = ["Primero", "Segundo", "Tercero"];
console.log("\nElementos de la función join:")
console.log(joinArray.join(" / "));

//lastIndexOf -> Similar a indexOf pero comenzando por el final del array en dirección al comienzo de esta. Nos devolverá le número del índice donde se encuentra el valor dado como parámetro. 
//El parámetro "fromIndex" nos permite definir un offset desde donde comenzará a contar.
//lastIndexOf(searchElement[, fromIndex]);
let lastIndexOfArray: number[] = [32,45,1,3,56,2];
console.log("\nLastIndexOf de 56:")
for(let i in lastIndexOfArray){
    console.log(`${i} : ${lastIndexOfArray[i]}`);
}
let resLastIndexOf=lastIndexOfArray.lastIndexOf(56)
console.log(resLastIndexOf);

//map -> Devolverá un array con los valores que retorna la función dada cómo parámetro por cada uno de los elementos del array.
//map(callback[, thisObject])
let mapArray:number[] = [2,46,72,2,1];
printArray(mapArray.map((value)=>(value*2)),"mapArray valores por 2:");

//reduce -> Este método aplica una función simultáneamente contra dos valores de la matriz (de izquierda a derecha) para reducirla a un solo valor. El parámetro "initalValue" será el valor inicial al que se empezará a sumar.
//reduce(callback[, initialValue]);
let reduceArray:number[] = [2,4,62,0,1];
console.log(`reduce result: ${reduceArray.reduce((v1, v2)=>v1-v2)}`);

//reduceRight -> Similar a "reduce" pero comenzará a reducir de derecha a izquierda.
//reduceRight(callback[, initialValue]);
let reduceRightArray:number[] = [2,4,62,0,1];
console.log(`reduceRight result: ${reduceRightArray.reduceRight((v1, v2)=>v1-v2)}`);

//reverse -> Esta función devolverá una copia del array pero con los elementos al revés. El primero pasando a ser el último, y viceversa.
//reverse();
let reverseArray:number[]=[1,2,3,4,5];
printArray(reverseArray.reverse(),"Resultado del array en reversa:");

//shift -> Elimina el primer elemento del array.
//shift();
let shiftArray:number[] = [3,2,1];
console.log(`Elemento eliminado: ${shiftArray.shift()}`);

//slice -> Nos permite extraer una porción del array en cuestión. El parámetro "begin" es el índice desde el que partirá y "end" donde terminará. Si "end" no existe la función devolverá desde "begin" hasta el final del array.
//slice( begin [,end] );
let sliceArray:number[] = [4,3,1,3,5,6,4,6,78,9,0]
printArray(sliceArray.slice(8),"Nuevo arreglo cortando desde el índice 8:");
printArray(sliceArray.slice(3,8),"Nuevo arreglo cortando desde el índice 3 hasta el 8:");

//some -> Nos permite conocer si alguno de los elementos del array pasa la prueba que le especificaremos en la función dada como parámetro.
//some(callback[, thisObject]);
let someArray:number[] = [32,4,6,37,0,3]
console.log(`el arreglo contiene el número 37: ${someArray.some((value)=>value==37)}`);

//sort -> Nos permite ordenar un array mediante la comparación sobre una función dada.
//sort( compareFunction );
//Al no pasarle una función de ordenación, y ser cadenas de texto los valores, los ordenará alfabéticamente.
let sortArray:string[]=["zorro","gato","araña","pavo"];
printArray(sortArray.sort(),"Ordenado alfabéticamente:")

//splice -> Nos permite modificar el contenido de los elementos de un array. Los nuevo elementos modificarán el valor de los antiguos elementos. "Index" será el índice desde donde comenzaremos a modificar, "howMany" cuantos elementos se modificarán a partir del index.
//splice(index, howMany, [element1][, ..., elementN]);
var spliceArray = ["orange", "mango", "banana", "sugar", "tea"];  
var removed = spliceArray.splice(2, 0, "water");  
console.log("\nAfter adding 1: " + spliceArray );  
console.log("removed is: " + removed); 
          
removed = spliceArray.splice(3, 1);  
console.log("\nAfter removing 1: " + spliceArray );  
console.log("removed is: " + removed);

//unshift -> Nos permite agregar uno, o más, elementos al comienzo del array y nos retornará la nueva longitud.
//unshift( element1, element2, ..., elementN );
let unshiftArray:number[]=[3,4,5,2];
let resUnshift=unshiftArray.unshift(9);
console.log(`\n nueva longitud del array: ${resUnshift}`)
printArray(unshiftArray);


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
var prompt = require("prompt-sync")();

class Contacto {
    private _nombre: string;
    private _telefono: number;

    constructor(){
        this._nombre="";
        this._telefono=0;
    }

    get nombre(): string {
        return this._nombre;
    }
    set nombre(value: string) {
       this._nombre=value;
    }
    
    get telefono(): number{
        return this._telefono;
    }
    set telefono(value: number){
        this._telefono=value;
    }
    
}

let contactos:Contacto[]=[];
let nuevoContacto= new Contacto();
nuevoContacto.nombre="Roberto";
nuevoContacto.telefono=23244;
contactos.push(nuevoContacto);

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let optionsArray:string[]=["Buscar","Insertar", "Actualizar", "Eliminar", "Cerrar Aplicación"];
function menuOpciones(value, i){
    console.log(`[${i}] - ${value}`)
}

function respuestaIncorrecta(){
    console.log('Respuesta incorrecta');
    regresarAlMenu();
}

function regresarAlMenu(){
    let answer=prompt(`\n¿Desea regresar al menú principal? [Y/N]`)
    if(answer.trim().toLocaleLowerCase()=="n"){
        cerrarAplicacion();
    } else if(answer.trim().toLocaleLowerCase()=="y"){
        menuPrincipal();
    } else {
        respuestaIncorrecta();
    }
}

function findContactByName(nombre:string):Contacto{
    return contactos.find(contact=>contact.nombre.trim().toLocaleLowerCase().includes(nombre.trim().toLocaleLowerCase()));;
}

function buscarContacto(){
    let res=prompt(`Escribe el nombre del contacto a buscar:`);
    let _contacto=findContactByName(res);
    if(_contacto){
        console.log(`Datos del contacto, nombre: ${_contacto.nombre}, teléfono: ${_contacto.telefono}`)
    } else {
        console.log(`No fue posible encontrar al contacto "${res}".`)
    }
    regresarAlMenu();
}

function eliminarContacto(){
    printArray(contactos, "Contactos registrados:")
    let res = prompt(`Escribe el nombre del contacto a eliminar:`)
    let _contacto=findContactByName(res);
    if(_contacto){
        contactos.splice(contactos.indexOf(_contacto),1);
        console.log(`El contacto "${_contacto.nombre}" con número de telefono ${_contacto.telefono} fue eliminado con éxito`)
        console.log(contactos);
    } else {
        console.log(`El contacto ${res} no se encuentra en la agenda`)
    }
    regresarAlMenu();
}

function modificarContacto(){
    printArray(contactos, "Contactos registrados:")
    let contactoModificar = prompt(`Escribe el nombre del contacto a modificar:`)
    let nombre=prompt("Ingrese el nuevo nombre del contacto:");
    let numero=prompt("Ingrese el nuevo teléfono del contacto:")
    let _contacto=findContactByName(contactoModificar);
    let _newCont: Contacto= validarContacto(nombre, numero);
    if(_newCont!=null){
        contactos[contactos.indexOf(_contacto)]=_newCont;
        console.log(`Los datos del contacto "${_contacto.nombre}" fueron modificados`)
        console.log(contactos);
        regresarAlMenu();
    } else {
        modificarContacto();
    }
}

function validarContacto(nombre:string, numero: number): Contacto{
    let _cont: Contacto= new Contacto();
    if(nombre.length>0){
        _cont.nombre=nombre;
    }else{
        console.log("Nombre invalido, inténtelo de nuevo")
        return null;
    }
    if(isNaN(numero)){
        console.log("El número de teléfono solo puede contener números sin espacios, inténtelo de nuevo")
        return null;
    } else if(numero.toString().length>11){
        console.log("El número de teléfono no puede ser mayor a 11 dígitos, inténtelo de nuevo")
        return null;
    } else {
        _cont.telefono=+numero;
    }
    return _cont;
}

function agregarContacto(){
    let _cont:Contacto= new Contacto();
    let nombre=prompt("Ingrese el nombre del contacto:");
    let numero=prompt("Ingrese el teléfono del contacto:")
    _cont=validarContacto(nombre, numero);
    if(_cont!=null){
        let res=contactos.push(_cont);
        console.log(contactos)
        console.log(`Contacto agregado correctamente: ${contactos[res-1].nombre}, ${contactos[res-1].telefono}`);
        regresarAlMenu();
    } else {
        agregarContacto();
    }
   
}

function menuPrincipal(){
    console.log("\n*********Agenda de contactos*********");
optionsArray.forEach(menuOpciones);
    let answer = prompt("Elige el número de la opción que necesitas:");
        switch(answer) {
        case "0":
            console.log("\n********Buscador de contactos*********")
            buscarContacto();
            break;
        case "1":
            console.log("\n********Agregar nuevo contacto*********")
            agregarContacto();
            break;
        case "2":
            console.log("\n********Modificar Contacto*********")
            modificarContacto();
            break;
        case "3":
            console.log("\n********Eliminar contacto*********")
            eliminarContacto();
            break;
        case "4":
            console.log("\n")
            cerrarAplicacion();
            break;
        default:
            console.log("\n")
            respuestaIncorrecta();
        }
}
function cerrarAplicacion(){
    console.log('Aplicación Finalizada');
    rl.close();
}
menuPrincipal();
