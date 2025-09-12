// *** ESTRUCTURAS DE DATOS EN TYPESCRIPT


// Array: Es una colección ordenada de elementos, puede almacenar cualquier tipo de datos.
let persona : (number | string)[] = ['Sharah', 22, 'Hola!'];
let numeros = [5, 3, 6, 1];

numeros.push(8);
numeros.splice(2, 0, 7); //Inserción.
numeros[2] = 3; //Actualización.
numeros[2]; //Acceder
numeros.splice(2, 1); //Eliminación.
numeros.sort((a,b)=> a - b); //Ordenación.

//Tuplas: son como arrays con un número fijo de elementos y tipos específicos de datos.
let miTupla: [string, number];
miTupla=["Sharah", 19];
console.log(miTupla[1]); //acceder
miTupla[1]= 20; //actualizar

/** Objetos: Sirve para almacenar y organizar datos como pares clave-valor.
 *  Los objetos son una colección de datos (propiedades) y/o comportamientos (métodos),
 * cada propiedad de un objeto tiene un nombre (clave) y un valor.
 * ( Los métodos son como propiedades que albergan una función como valor, en lugar de contacto. )
 */
const personaSaludar = {
    nombre: 'Sharah',
    edad: 20,
    saludar: function(){
        console.log('Hola, ',this.nombre,'!');
    }
};
//Objetos anidados. Son objetos que contienen más objetos.
//(Básicamente estos objetos tienen propiedades que contienen más propiedades.) 
const infoPersona ={
    nombre: 'Sharah',
    edad: 20,
    ubicacion:{
        pais: 'Colombia',
        departamento: 'Valle de Cauca'
    }
}
infoPersona['email'] = 'sharah@gmail'; //Inserción.
infoPersona.ubicacion.departamento = 'Valle Del Cauca'; //Actualización.
delete infoPersona.email; //Eliminación.

/** Mapas: Son colecciones de datos clave-valor, a diferencia de los objetos estos permiten cualquier tipo de dato
 *  como clave(incluyendo objetos) y mantienen el orden de inserción de las claves.
 *  Las claves no pueden repetirse. 
 */

let miMapa = new Map<string, number>();
miMapa.set("Sharah", 20); //Insertar
miMapa.set("Juan", 31);
miMapa.set("Sofia", 26); 
console.log(miMapa.get("Sofia")); //Acceder
console.log(miMapa.has("julia")); //verificar si existe
miMapa.delete("Sofia"); //eliminar
miMapa.set("Juan", 32); //actualizar
//mapa inicializado con valores usando un Array de Tuplas
let miMapa2 =new Map([
    ["Julia", 32],
    ["David", 27],
    ["Oscar", 22]
]);

/** Sets: Permiten almacenar una colección de valores únicos.
 * Los valores no pueden repetirse, permite cualquier tipo de datos y mantiene el orden de inserción.
 */

const miSet = new Set<number>([2,8,4]);
miSet.add(5).add(7).add(9); //Insertar valores
miSet.delete(5) //Eliminación.
console.log(miSet.has(7)); //verificar existencia
let setOrdenado = new Set([... miSet].sort((a,b)=> a-b));// ordenar(hay q convertirlo en array)
let nuevoSet = new Set(setOrdenado);
console.log(nuevoSet);
//Actualización:(No se puede actualizar directamente un set. Eliminas un elemento y agregas el otro.)

//Extra

function miAgenda(){
    
    const readline = require("readline");
    
    process.stdin.resume();
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });
    rl.on("SIGINT", () => {
        console.log("\nInterrupción detectada. Cerrando el programa...");
        rl.close();
        process.exit(0);
      });
    const agenda = new Map();
    function preguntarAccion(){
        rl.question('Desea salir del programa?', (salir) =>{
            const salir2 = salir.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
            if(salir2.toLowerCase() == 'si'){
                console.log('Cerrando programa...');
                return rl.close();
                
            }
            console.log('1. Añadir contacto.');
            console.log('2. Buscar contacto.');
            console.log('3. Actualizar contacto.');
            console.log('4. Eliminar contacto.');
            console.log('5. Ver agenda.');
        
            rl.question("Qué acción desea realizar? ", (accionRealizar) => {
                const valorRecibido = parseInt(accionRealizar)
                switch(valorRecibido){
                    case 1:
                        rl.question('Ingrese el nombre:', (nombre) => {
                            rl.question('Ingrese el número:', (numero) =>{
                                const esNumero = parseInt(numero);
                                if(isNaN(esNumero) || numero.length > 11){
                                console.log('Información no valida');
                                return preguntarAccion();
                                }
                                agenda.set(nombre, esNumero);
                                console.log('contacto añadido');
                                preguntarAccion();
                            });
                        }); 
                        break;
                    case 2:
                        rl.question('Ingrese el nombre que desea buscar.', (buscar) =>{
                            if(agenda.has(buscar)){
                                console.log('nombre: ' + buscar + ', número: '+ agenda.get(buscar));
                                preguntarAccion();

                            }else{
                                console.log('contacto no encontrado');
                                preguntarAccion();
                            }
                        });
                        break;
                    case 3:
                        rl.question('Ingrese el nombre del contacto a actualizar.', (actualizar)=>{
                            agenda.delete(actualizar)
                            rl.question('Ingrese nueva información, nombre:', (nuevoNombre)=>{
                                rl.question('número:', (nuevoNumero)=>{
                                    const esNumero = parseInt(nuevoNumero);
                                    if(isNaN(esNumero) || nuevoNumero.length > 11 ){
                                    console.log('Información no valida');
                                    preguntarAccion(); 
                                    }
                                    agenda.set(nuevoNombre, esNumero);
                                    console.log('contacto actualizado')
                                    preguntarAccion();
                                   

                                } );
                            });
                        });
                        break;
                    case 4:
                        rl.question('Ingrese el nombre que desea eliminar.', (eliminar)=>{
                            agenda.delete(eliminar);
                            console.log('contacto eliminado.')
                            preguntarAccion();
                        });
                        break;
                    case 5:
                        console.log(agenda);
                        preguntarAccion();
                        break;
                    default:
                        console.log('valor incorrecto.');
                        preguntarAccion();
                        break;
                }
                
                
            });
        })
    }   
    preguntarAccion();
}

miAgenda();