//Array
var lista = [4,6,1,7,5,8,2,3]
console.log("Lista original: " + lista)
//Inserción
lista.push(0) //Agrego un elemento al final de la lista 
console.log("Nuevo elemento: " + lista)
lista.unshift(9) //Agrego un elemento al principio de la lista
console.log("Nuevo elemento: " + lista)
lista.splice(2,0,10) //Agrego el 10 en la posición 3
console.log("Nuevo elemento: " + lista)
//Borrado
lista.pop() //Elimino el ultimo elemento de la lista
console.log("Elemento borrado: " + lista)
lista.shift() //Elimino el primer elemento de la lista
console.log("Elemento borrado: " + lista)
lista.splice(3,1) //Elimino el elemento en la posición 4
console.log("Elemento borrado: " + lista)
//Actualización
lista[6] = 9 //Reemplazo el elemento de la posición 7
console.log("Lista actualizada: " + lista)
//Ordenación
lista.sort(function(a,b){return a-b}) //Ordeno la lista de menor a mayor
console.log("Lista ordenada: " + lista)
lista.reverse(function(a,b){return a-b}) //Ordeno la lista de mayor a menor
console.log("Lista ordenada: " + lista)

//Objet
var persona = 
{
    nombre: "Fernando",
    apellido: "Gomez",
    edad: 29
}
console.log(persona)
//Inserción
persona["ciudad"] = "Rosario"
console.log("Objeto con nueva propiedad: " + persona)
//Borrado
delete persona.apellido
console.log("Objeto con propiedad borrada: " + persona)
//Actualización
persona.nombre = "Fer"
console.log("Objeto con propiedad actualizada: " + persona)

//Map
var mapa = new Map()
//Inserción
mapa.set("rojo", "red")
mapa.set("verde", "green")
mapa.set("azul", "blue")
console.log(mapa)
//Borrado
mapa.delete("verde")
console.log(mapa)
//Actualización
mapa.set("rojo", "vermelho")
console.log(mapa)

//Set
var numeros = new Set([4,6,1,7])
console.log(numeros)
//Inserción
numeros.add(0)
console.log(numeros)
//Borrado
numeros.delete(1) 
console.log(numeros)

/*DIFICULTAD EXTRA (opcional):
Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización
  y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar,
  y a continuación los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más
 de 11 dígitos (o el número de dígitos que quieras).
- También se debe proponer una operación de finalización del programa.*/


var agenda = new Map()
var nombre
var telefono
var op

import readline from 'readline'


function obtenerInput(pregunta) 
{ 
  const rl = readline.createInterface
  (
    { 
      input: process.stdin, output: process.stdout
    })
    return new Promise((resolve) => 
      { rl.question(pregunta, (respuesta) => 
        { resolve(respuesta); rl.close(); 

        }); 
      });
}


console.log("\n1- Buscar contacto")
console.log("2- Insertar contacto")
console.log("3- Actualizar contacto")
console.log("4- Eliminar contacto")
console.log("5- Salir")


do
{
  op = await obtenerInput('Por favor, ingresa un valor: ') 

  switch (op)
  {
    case "1":
      nombre = await obtenerInput("Ingrese nombre a buscar: ")
      if (agenda.get(nombre))
        console.log("El telefono de " + nombre + " es: " + agenda.get(nombre))
      else console.log("El contacto " + nombre + " no exixte en la agenda")
      break
    case "2":
      nombre = await obtenerInput('Nombre: ')
      telefono = await obtenerInput('Telefono: ')
      if (!isNaN(telefono) && telefono.length > 0 && telefono.length < 12)
      {
        agenda.set(nombre, telefono)
        console.log("El contacto fue credo con exito")
      }
      else console.log("Tiene que ingresar un numero con menos de 12 digitos")
      break
    case "3":
      nombre = await obtenerInput('Ingrese el nombre del contacto a actualizar: ')
      if (agenda.get(nombre))
      {
        telefono = await obtenerInput('Ingrese el nuevo numero de telefono: ')
        if (!isNaN(telefono) && telefono.length > 0 && telefono.length < 12)
        {
          agenda.set(nombre, telefono)
          console.log("El contacto fue actualizado con exito")
        }
        else console.log("Tiene que ingresar un numero con menos de 12 digitos")
      }
      else console.log("El contacto " + nombre + " no exixte en la agenda")
      break
    case "4":
      nombre = await obtenerInput('Ingrese el nombre del contacto a eliminar: ')
      if (agenda.get(nombre))
      {
        agenda.delete(nombre)
        console.log("El contacto " + nombre + " fue eliminado con éxito")
      }
      else console.log("El contacto " + nombre + " no exixte en la agenda")
      break
  }
}while (op != 5)


  

