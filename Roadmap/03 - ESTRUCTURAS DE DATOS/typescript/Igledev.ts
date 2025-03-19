// 1º Ejemplos de creación de todas las estructuras soportadas.
// En TypeScript hay tanto estructuras de datos como de tipos, vamos a verlos!
    // -- Boolean
    let dev: boolean = true;
    // -- Number
    let decimal : number = 6;
    let hexadecimal : number = 0xf35d;
    let binario : number = 0o1010;
    let octal : number = 0o272;
    // -- String
    let username : string = 'IgleDev';
    // -- Array
    let notas : number[] = [9, 4, 8, 5];
    let frutas : Array<string> = ['manzana', 'kiwi', 'platano'];
    // -- Tupla
    let nombreEdad : [string, number];
    nombreEdad = ['Igledev', 19]; // Si hicieramos 'x = [10, "hello"];' daría error.
    // -- Enum
    enum Color{Rojo, Verde, Azul}
    let color : Color = Color.Rojo;
    // -- Any
    let gatos : any = 4;
    // -- Void
    function gustar() : void {
        console.log('Me gusta TypeScript!');
    }
    // -- Undefined
    let sin_definir : undefined = undefined;
    // -- Null
    let vacio : null = null;
    // -- Never
    function error(mensaje_error: string): never {
        throw new Error(mensaje_error);
    }
    // -- Objeto
    let obj : object = { Igledev: 'Programador Web' };
    // -- Union Type
    let estado : number | string;
    estado = 10;
    estado = 'Con muchas ganas';
    //Intersection Type
    interface Programador {
        nombre : string;
    }
    
    interface Tecnologia {
        lenguaje : string;
    }
    
    let coder : Programador & Tecnologia = {
        nombre: 'Igledev',
        lenguaje: 'TypeScript',
    };
// 2º Operaciones de inserción, borrado, actualización y ordenación.
    // -- Insercción
    let numeros_favoritos : number[] = [];

        // -- Insertar al final
        numeros_favoritos.push(8);

        // -- Insertar al principio
        numeros_favoritos.unshift(5);

        // -- Insertar en una posición específica
        numeros_favoritos.splice(1,0,4);
        // Nos saldría el 4 en la mitad de los números: 5/4/8

    // -- Lo mostramos
    console.log('Array utilizando insercción' + numeros_favoritos);

    // -- Borrado
        // Borra el final
        numeros_favoritos.pop();

        // Borra el principio
        numeros_favoritos.shift();

        // Borra una posición específica
        numeros_favoritos.splice(2, 1);
        // Nos quedaríamos solo con 4

    // -- Lo mostramos
    console.log("Array después del borrado:" + numeros_favoritos);

    // -- Actualizar
        numeros_favoritos[1] = 10;

    // -- Lo mostramos
    console.log("Array después de la actualización:" + numeros_favoritos);

    // -- Ordenacion
    // Tenemos 2 tipos
        // -- Numérica
            let notas_desordenadas : number[] = [9,4,8,2,5,6];

            // -- De forma Ascendente
            let notas_ascendentes : number[] = notas_desordenadas.slice().sort((a,b) => a - b);
                // El Slice sin pasarle argumentos nos devuelve una copia del Array original
                /**El argumento que se pasa a sort() es una función de comparación. 
                 * La función (a, b) => a - b indica que los elementos se deben ordenar de manera ascendente. 
                 * Si el resultado de la resta a - b es negativo, significa que a es menor que b, 
                 * por lo que a debe ir primero 
                 *
                */

            // -- De forma Descendente
            let notas_descendentes : number[] = notas_desordenadas.slice().sort((a, b) => b - a);
        
        // -- Las mostramos
        console.log('Array sin modificaciones: ' + notas_desordenadas);
        console.log('Array con las notas ascendentes: ' + notas_ascendentes);
        console.log('Array con las notas descendentes: ' + notas_descendentes);

        // -- String
            let tecnologias_desordenadas : string[] = ['TypeScript' , 'JavaScript' , 'Git' , 'Angular' , 'HTML'];

            // Ordenar alfabéticamente
            let tecnologias_ordenadas: string[] = tecnologias_desordenadas.slice().sort();
        // -- Las mostramos
        console.log('Array original: ' + tecnologias_desordenadas);
        console.log('Array ordenado alfabéticamente: ' + tecnologias_ordenadas);

// 3º Ejercicio Extra
// Definimos un tipo para los contactos
type Contactos = {
    nombre: string;
    telefono: string;
};

let salir = false;
const agenda : Contactos[] = [];

while(salir == false){
    console.log("\nOperaciones disponibles:");
    console.log("1. Buscar contacto");
    console.log("2. Insertar contacto");
    console.log("3. Actualizar contacto");
    console.log("4. Eliminar contacto");
    console.log("5. Salir");

    let opcion : string = prompt('Elija que quiere hacer') as string;

    switch(opcion){
        case '1':
            let nombreUsuario = prompt('Ingresa el nombre del Usuario');
            let encontrado = agenda.find(c => c.nombre === nombreUsuario);

            if(encontrado){
                console.log('Nombre: ' + encontrado.nombre + ' - Teléfono: ' + encontrado.telefono);
            }else{
                console.log('Usuario no encontrado');
            }
        break;
        case '2':
            let nombre = prompt('Ingresa el nombre del nuevo contacto') as string;
            let telefono = '';

            while(!/^\d+$/.test(telefono) || telefono.length > 11){
                telefono = prompt('Ingrese el número de teléfono del contacto: ') as string;
                if(!/^\d+$/.test(telefono) || telefono.length > 11){
                    console.log("Número de teléfono no válido. Debe contener dígitos y tener 11 dígitos.");
                }
            }

            agenda.push({nombre , telefono});
            console.log('Contacto Agreado');
        break;
        case '3':
            let nombreActulizado = prompt("Ingrese el nombre del contacto que desea actualizar: ");
            let nContacto = agenda.findIndex(c => c.nombre === nombreActulizado);
          
            if (nContacto !== -1) {
                let nTelefono = '';
          
                while (!/^\d+$/.test(nTelefono) || nTelefono.length > 11) {
                    nTelefono = prompt("Ingrese el nuevo número de teléfono: ") as string;
                    if (!/^\d+$/.test(nTelefono) || nTelefono.length > 11) {
                      console.log("Número de teléfono no válido. Debe contener solo dígitos y tener como máximo 11 dígitos.");
                    }
                }
          
              agenda[nContacto].telefono = nTelefono;
              console.log("Contacto actualizado correctamente.");
            } else {
              console.log("Contacto no encontrado.");
            }

        break;
        case '4':
            let nombreBorrar = prompt("Ingrese el nombre del contacto que desea eliminar: ");
            let nContactoBorrar = agenda.findIndex(c => c.nombre === nombreBorrar);
          
            if (nContactoBorrar !== -1) {
              // Eliminamos el contacto del array
              agenda.splice(nContactoBorrar, 1);
              console.log("Contacto eliminado correctamente.");
            } else {
              console.log("Contacto no encontrado.");
            }

        break;
        case '5':
            console.log('Un placer haberte servido de ayuda');
            salir = true;

        break;
        default:
            console.log('Te equivocaste de numero')
    }
}