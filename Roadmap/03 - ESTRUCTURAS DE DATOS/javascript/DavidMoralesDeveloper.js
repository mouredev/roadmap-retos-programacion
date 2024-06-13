//1 - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
// en object lo valores se pasan por referencia y en primitivos por valor****

console.log(typeof null) //object,  (e la teoria deberia ser null primitivo)***
// objects
console.log(typeof {}) //object : objeto
console.log(typeof []) //object :array
const set = new Set()
console.log(typeof set) //object : añadir datos a la array

// cada constructor de las funciones se deriaba del contructor object pero es un objeto especial
// function 
console.log(typeof function(){}) //function pero por detras es un objeto especial
    
//tipdos en un array
let numbers = [1, 2, 3, 4];
let letters = ['a', 'b', 'c', 'd'];
let combined = ['abc', true, 'def', false]; 
let users = [  //array de objetos
    {
        id: 1,
        name: 'Andres',
        subscribed: true
    },
    {
        id: 2,
        name: 'Brais',
        subscribed: false
    }
];
console.log('users', users);

//2- Utiliza operaciones de inserción, borrado, actualización y ordenación.

let frutas = ["Manzana", "Banana"];
console.log(frutas.length); //2

frutas.push('uva') //inserción
console.log(frutas + ' metodo push'); //[ 'Manzana', 'Banana', 'uva' ]
frutas.pop() //borrado
console.log(frutas + ' metodo pop'); //[ 'Manzana', 'Banana',  ]

let mejoresCarros2023 = ["audi", "ferrari", "renol", "nisan", "honda"]
console.log(mejoresCarros2023)
mejoresCarros2023[2] = 'suzuki' //actualización
console.log(mejoresCarros2023)

const numeros = [10, 21, 13, 45, 5, 26] //ordenación

const descNumeros = numeros.sort((a,b) => a > b ? -1 : 1) //[ 45, 26, 21, 13, 10, 5 ]
console.log(descNumeros)

const asenNumeros = numeros.sort((a,b) => a > b ? 1 : -1) //[ 5, 10, 13, 21, 26, 45 ]
console.log(asenNumeros)

//set
// es una estructura de datos qe nos permite almacenar colecciones de datos especificamente que no se van a repetir
console.log('-----------------set')
const set1 = new Set()

set1.add(1)
set1.add(2)
set1.add(false)
set1.add([1,5,6]) // guardado por valor - console.log(set1.has([1,5,6])) : false
const arr = [1,5,6] //guardado por referencia
set1.add(arr) // console.log(set1.has(arr)) : true
set1.delete(false)

console.log(set1.has(arr))
for( item of set1){
    console.log(item)
}

//map
console.log('-----------------map')
const map = new Map()

map.set(1, 'lunes')
map.set('2', 3)
map.set(false, 10)
console.log(map.has(1))
console.log(map.size)
map.delete(false)
console.log(map.size)

for(item of map){
    console.log(item)
}
for(const [key, value] of map){
    console.log(key, value)
}

console.log(map.get('2'))


//3 EXTRA
// Crea una agenda de contactos por terminal.
//  * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
//  * - Cada contacto debe tener un nombre y un número de teléfono.
//  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
//  *   los datos necesarios para llevarla a cabo.
//  * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
//  *   (o el número de dígitos que quieras)
//  * - También se debe proponer una operación de finalización del programa.


const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  let agenda = {}

function miAgenda  () {

   

    rl.question("¿Qué operación quieres realizar? (buscar, insertar, actualizar, agenda, eliminar, salir): ", (operacion) => {
    switch (operacion) {
        case 'buscar':
            rl.question('¿nombre de contacto?', (nombre)=> {
                if(agenda[nombre]){
                    console.log(`Nombre: ${nombre} Telefono: ${agenda[nombre]}`)
                    miAgenda  ()
                }else {
                    console.log("Contacto no encontrado.");
                    miAgenda  ()
                  }
            })
            miAgenda  ()
            break;
        case 'insertar':
           rl.question('¿cuales el nombre?:', (nombre) =>{
             rl.question('¿cual es el telfono?:', (telefono) =>{
                if( !isNaN(telefono) && telefono.toString().length <= 11){

                    agenda[nombre] = telefono
                    console.log("Contacto agrego correctamente.");
                    miAgenda  ()
                }else{
                    console.log('Error, el telefono solo acepta numeros, hasta 11 digitos')
                    miAgenda  ()
                }
             })
            } )
            
            
            break;
        case 'actualizar':
            rl.question('nombre de contacto ', (nombre) => {
                if(agenda[nombre]){
                    rl.question('introducel el nuevo numero de telefono',(telefono) => {
                        agenda[nombre] = telefono
                        console.log('se actualice exitosamente')
                        miAgenda()
                    })
                }else{
                    console.log("Contacto no encontrado.");
                    miAgenda  ()
                }
            })
            console.log('actualizar')
            break;
        case 'eliminar':
            rl.question('Escriba el nombre de el contacto que se quiera eliminar',(nombre) => {
                if(agenda[nombre] ){
                    delete agenda[nombre]
                    console.log( 'fue eliminado eliminado' )
                    miAgenda()
                }
            })
            break;
        case 'agenda':
            console.log(agenda)
            miAgenda()
            break;
        case 'salir':
            rl.close();
            console.log('saliendo de la agenda')
            break;
    
        default:
            console.log('Error al leer su respuesta , eliga una opcion valida')
            miAgenda  ()
            break;
    }

})
 
}

miAgenda()