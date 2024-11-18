//Array normal
var numeros = [10, 15, 54, 70, 64, 13]
numeros.pop() //Elimina el último elemento de un array
numeros.push(40) //Agrega un elemento al final de un array
numeros[2] = 52 //Actualizar un número
numeros.sort() //Ordena los elementos
for (i = 0; i < numeros.length; i++) {
    console.log(numeros[i])
}

var colores = ["rojo", "amarillo", "azul", "morado"]
colores.pop() //Elimina el último elemento de un array
colores.push("verde") //Agrega un elemento al final de un array
colores[2] = "naranja" //Actualizar un string
colores.sort() //Ordena los elementos por orden alfabético
for (i = 0; i < colores.length; i++) {
    console.log(colores[i])
}

//Array bidimencional
var matriz = [[1, 2, 3], [4, 5, 6]]
for(i = 0; i < matriz[i].length; i++) {
    for(j = 0; j < matriz.length; j++) {
      console.log(matriz[j][i]);
    }
}

//Objetos
var persona = {
    nombre: "Marcos",
    edad: 24,
    estudiante: false,
}
persona.edad = 25 //Actualizar una propiedad
persona["profesión"] = "Analista de Datos" //Agregar una propiedad
delete persona.estudiante //Eliminar una propiedad
console.log(persona)


//Sets
var miSet = new Set([51, 84, 34]) //Los sets no pueden tener elementos repetidos
miSet.add(17) //agregar un int
miSet.add("texto") //agregar un string
let unObjeto = {a: 14, b:74} 
miSet.add(unObjeto) //agregar un objeto
miSet.delete(51) //eliminar un elemento
for (let item of miSet.keys()) console.log(item)

//Mapas
const mapa = new Map();
//Agregar elementos
mapa.set('a', "primero"); 
mapa.set('b', "segundo");
mapa.set('c', "tercero");
mapa.set('d', "cuarto");
mapa.set('c', "medio") //Actualizar según la key
mapa.delete('d'); //eliminar un elemento
console.log(mapa)

/* DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.
 */
const agenda = function () {
  let agenda = [
    { nombre: "Marcos", numero: "1234567894" },
    { nombre: "Andrea", numero: "1478523690" },
    { nombre: "Carlos", numero: "4893175451" }
  ];

  let leave = false;

  while (!leave) {
    let opcion = prompt(`Elija una opción:
        1 - Buscar contacto
        2 - Añadir contacto 
        3 - Actualizar contacto
        4 - Eliminar contacto
        5 - Salir`);

    switch (opcion) {
      case '1':
        let search_contacto = prompt("Ingrese el nombre del contacto: ");
        let contactoEncontrado = agenda.find(contacto => contacto.nombre === search_contacto);
        if (contactoEncontrado) {
          console.log(`Nombre: ${contactoEncontrado.nombre}, Número: ${contactoEncontrado.numero}`);
        } else {
          console.log("Contacto no encontrado");
        }
        break;

      case '2':
        let nombre = prompt("Nombre del contacto: ");
        let numero = prompt("Número del contacto: ");
        if (numero.length <= 12) {
          agenda.push({ nombre: nombre, numero: numero });
          console.log("Contacto agregado");
        } else {
          console.log("El número de teléfono debe tener 12 dígitos o menos");
        }
        break;

      case '3':
        let nombreAntiguo = prompt("Ingrese el nombre del contacto que deseas actualizar: ");
        let nombreNuevo = prompt("Ingrese el nuevo nombre del contacto: ");
        let nuevoNumero = prompt("Ingrese el nuevo número de teléfono para este contacto: ");
        let contactoParaActualizar = agenda.find(contacto => contacto.nombre === nombreAntiguo);
        if (contactoParaActualizar) {
          contactoParaActualizar.nombre = nombreNuevo;
          contactoParaActualizar.numero = nuevoNumero;
          console.log("Contacto actualizado");
        } else {
          console.log("Contacto no encontrado");
        }
        break;

      case '4':
        let eliminar_contacto = prompt("Nombre del contacto que desea eliminar: ");
        let index = agenda.findIndex(contacto => contacto.nombre === eliminar_contacto);
        if (index !== -1) {
          agenda.splice(index, 1);
          console.log("Contacto eliminado");
        } else {
          console.log("Contacto no encontrado");
        }
        break;

      case '5':
        leave = true;
        console.log("Haz salido de la agenda")
        break;

      default:
        console.log('Opción no existente, por favor ingrese una opción válida');
    }
  }
}
agenda();