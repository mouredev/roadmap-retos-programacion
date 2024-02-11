//Listas

console.log("----LISTAS----");

lista = [1, 2, "hola", 3, 4];
console.log(lista);

//Inserción
//Añade el valor indicado al final de la lista
lista.push("manzana");
console.log(lista);

//Añade el valor indicado al principio de la lista
lista.unshift(true);
console.log(lista);

//Borrado
//Elimina el último valor de la lista
lista.pop();
console.log(lista);

//Elimina el primer valor de la lista
lista.shift();
console.log(lista);

//Actualización
//Se actualiza el valor de la posición indicada
lista[3] = "Python"
console.log(lista);

/*
Con el método slice() se pueden actualizar los valores del array
- Primer parámetro la posición a modificar
- Segundo parámetro el número de valores a modificar
- Tercer parámetro el nuevo valor
*/
lista.splice(4, 1, 54);
console.log(lista);

//Ordenación
lista.sort();
console.log(lista);

//Objetos

console.log("----OBJETOS----");

let objeto = {
    nombre: "Mario",
    edad: 33,
    altura: 1.80
};

console.log(objeto);

//Inserción
objeto.developer = true;

console.log(objeto);
//Borrado
delete objeto.altura;

console.log(objeto);

//Actualizado
objeto.nombre = "Laura";

console.log(objeto);

objeto["nombre"] = "Mario";
console.log(objeto);

//Ordenación
//Los objetos no pueden ser ordenados

//Map

console.log("----MAP----");

let mapa = new Map();

console.log(mapa);

//Inserción
//Método set(clave, valor) 
mapa.set("1", "str1");
mapa.set(1, 'num1');
mapa.set(true, 'bool1');

console.log(mapa);

//Borrado
//Método delete(clave)
mapa.delete(1);

console.log(mapa);

//Actualizado
mapa.set(true, "bool2");

console.log(mapa);

//Ordenación
//Los mapas no pueden ser ordenados

//Set

console.log("----SET----");

let miSet = new Set();

console.log(miSet);

//Inserción
//Método add(valor)
miSet.add(true);
miSet.add(2);
miSet.add("str");

console.log(miSet)

//Borrado
//Método delete(valor)
miSet.delete(2);

console.log(miSet);

//Los Set no pueden ser actualizados ni ordenados

//Extra

console.log("----EXTRA----");

function contactList() {
    //Creamos un objeto , que contendrá el nombre y el teléfono de los contactos
    let agenda = {
        Mario: 123456678,
        Sara: 1423423435
    };

    //Creamos una variable booleana para poder controlar el bucle del menu de opciones
    let leave = true;

    //Creamos el bucle que contendra el menu de opciones
    while (leave) {
        //Mostramos las opciones del menu y preguntamos al usuario que desea hacer
        let ask = prompt(`¿Qué desea hacer? 
        1 - Búsqueda de contacto 
        2 - Añadir contacto 
        3 - Actualizar contacto
        4 - Eliminar contacto
        5 - Salir` );

        let answer = parseInt(ask);

        //Dependiendo de la opción seleccionada el menu entrará en dicha opción
        switch (answer) {
            case 1:
                //Se introduce por consola el nombre del usuario a buscar
                let search = prompt("Introduce el nombre del contacto a buscar ");
                if (agenda[search] == undefined) {
                    console.log("Usuario no encontrado");
                } else {
                    console.log(agenda[search]);
                }
                break;
            case 2:
                //Añadimos el nombre y el número de teléfono del nuevo contacto
                let add = prompt("Añade el nombre del nuevo contacto ");
                let condition = true;
                //Si el número de teléfono no tiene 9 dígitos o no es un número, se le pedirá al usuario que vuelva a introducir el número
                while (condition) {
                    let number = prompt("Añade el número de teléfono ");
                    if (number.length == 9) {
                        number = parseInt(number);
                        if (Number.isInteger(number)) {
                            agenda[add] = number;
                            console.log("Contacto añadido");
                            condition = false;
                        } else {
                            console.log("No has introducido un número");
                        }
                    } else {
                        console.log("La longitud del número es menor o superior a 9 dígitos");
                    };
                };
                break;
            case 3:
                //Se pide por consola el nombre del contacto y el número de teléfono que se actualizará
                let update_name = prompt("Añade el nombre del contacto ");
                let update_phone = prompt("Añade el número de teléfono a actualizar ");
                agenda[update_name] = parseInt(update_phone);
                console.log("Actualizado el número de teléfono del contacto");
                break;
            case 4:
                //Se pide por consola el nombre del contacto a eliminar
                let remove = prompt("Añade el nombre del contacto a eliminar ")
                delete agenda.remove;
                console.log(`Eliminado el contacto de ${remove}`);
                break;
            case 5:
                //Finalizar el programa
                leave = false;
                break;
            default:
                console.log("Introduce un número entre 1 y 5");
        }
    }
};

contactList();
