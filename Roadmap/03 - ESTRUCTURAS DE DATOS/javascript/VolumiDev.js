/**
 * Tipos de estructuras de datos:
 *  ➡️ Objetos 
 *  ➡️ Arreglos (array)
 *  ➡️ Mapas (map)
 *  ➡️ Conjuntos (set) 
 */

// Objetos, podemos almacenar en los atributos distinto tipos de datos primitivos
  var persona1 = {
    nombre: 'Diego',
    edad: 34,
    grado: 'DAM'
  }

  // Podemos acceder a cada uno de los atributos del objeto de la siguiente manera
  console.log('Atributo nombre de persona1', persona1.nombre)
  console.log('Atributo edad de persona1', persona1.edad)
  console.log('Atributo grado de persona 1', persona1.grado)
  console.log('Aqui vemos el objeto completo', persona1)

// Arrays, coleccion de datos, pueden ser de destintos tipos
var array1 = ['hola', 23, true, 'datos variables']
console.log('Mostramos el array completo', array1)
console.log('Accedemos a la segunda posicion del array desde el indice.', array1[1])

// Mapas 
var mapa = new Map()
  // ➕ agregacion de elementos al mapa
mapa.set('edad', 35)
mapa.set('nombre', 'Diego')
mapa.set(25, 'piso')
mapa.set(true, 'estudios')
console.log(mapa)
  
  // ➡️ accedemos al valor por su key.
console.log(mapa.get('edad'))
console.log(mapa.get('nombre'))
console.log(mapa.get(25))
console.log(mapa.get(true))
  // ➡️ comprobar si una clave existe
  console.log('Comprobamos que existe la clave "edad"', mapa.has('edad'))
  // ➖ Elimiar un elemento por su key
  console.log(mapa)
  mapa.delete('nombre')
  console.log(mapa)

// Conjuntos set
  var conjunto = new Set(['Diego', 'Laura', 'Eren', 'Laia', 'Diego'])
  console.log('Vemos los elementos del conjunto, Diego lo metimos dos veces pero como no es posible que haya elementos repetido no lo incluye', conjunto)
  // Añadimos un elemento al conjunto
  conjunto.add(35)
  console.log(conjunto)
  console.log('Comprobamos si exite el valor "Diego" en el conjunto', conjunto.has('Diego'))
  console.log(conjunto)
  //Eliminamos un elemento al conjunto
  conjunto.delete('Laura')
  console.log(conjunto)


  // Dificultad extra AGENDA
  function menuAgenda(){
    console.log('Elige una de las opciones\n1. Busqueda\n2. Inserción')
    
  }

  // do {
  //   var opcion = menuAgenda
  // } while (condition);
  var dato = prompt('introduce')