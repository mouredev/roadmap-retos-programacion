/* 
  * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *

  """

# Creación de estructuras de datos

# Listas
*/

let lista = [1, 2, 3, 4, 5, 6, 7, 8, 9];

// Inserción
lista.push(10);
console.log(lista);

// Borrado

lista.pop();
console.log(lista);

// Actualización

lista[0] = 0;
console.log(lista);

// Ordenación

lista.sort();
console.log(lista);

// Diccionarios

let diccionario = {
  nombre: "Andres",
  apellido: "Cardenas",
  edad: 30,
};

// Inserción

diccionario["sexo"] = "Masculino";
console.log(diccionario);

// Borrado

delete diccionario["sexo"];
console.log(diccionario);

// Actualización

diccionario["edad"] = 31;
console.log(diccionario);

// Ordenación
 
// No aplica

// Tuplas

let tupla = [1, "Andres", 30];
console.log(tupla);

// Inserción

tupla.push("Cardenas");
console.log(tupla);

// Borrado

tupla.pop();
console.log(tupla);

// Actualización

tupla[0] = 0;
console.log(tupla);

// Ordenación

tupla.sort();
console.log(tupla);

// Conjuntos son estructuras de datos que no permiten elementos repetidos

let conjunto = new Set([1, 2, 3, 4, 5, 6, 7, 8, 9]);
console.log(conjunto);

// Inserción

conjunto.add(10);
console.log(conjunto);

// Borrado

conjunto.delete(10);
console.log(conjunto);

// Actualización no aplica dado que no permite dadp que no se tiene accesos a los elementos por indice

// Ordenación no aplica dado que no permite se tiene accesos a los elementos por indice

// Diccionarios ordenados

let diccionarioOrdenado = new Map([
  ["nombre", "Andres"],
  ["apellido", "Cardenas"],
  ["edad", 30],
]);

console.log(diccionarioOrdenado);

// busqueda

console.log(diccionarioOrdenado.get("nombre"));


// Inserción

diccionarioOrdenado.set("sexo", "Masculino");
console.log(diccionarioOrdenado);

// Borrado

diccionarioOrdenado.delete("sexo");
console.log(diccionarioOrdenado);

// Actualización

diccionarioOrdenado.set("edad", 31);
console.log(diccionarioOrdenado);

// Ordenación no se aplica dado que no tiene indice

// Pilas

let pila = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(pila);

// Inserción

pila.push(10);
console.log(pila);

// Borrado

pila.pop();
console.log(pila);

// Actualización

pila[0] = 0;
console.log(pila);

// Ordenación

pila.sort();
console.log(pila);

// Colas

let cola = [1, 2, 3, 4, 5, 6, 7, 8, 9];
console.log(cola);

// Inserción

cola.push(10);
console.log(cola);

// Borrado

cola.shift();
console.log(cola);

// Actualización

cola[0] = 0;
console.log(cola);

// Ordenación

cola.sort();
console.log(cola);

// Árboles son estructuras de datos no lineales que se componen de nodos o vértices y ramas u hojas

class Nodo {
  constructor(valor) {
    this.valor = valor;
    this.hijos = [];
  }
}

class Arbol {
  constructor(valor) {
    this.raiz = new Nodo(valor);
  }
}

let arbol = new Arbol(1);
console.log(arbol);

// Inserción

arbol.raiz.hijos.push(new Nodo(2));
console.log(arbol);

// Borrado

arbol.raiz.hijos.pop();
console.log(arbol);

// Actualización

arbol.raiz.valor = 0;
console.log(arbol);

// Ordenación no aplica dado que no tiene indice

// Grafos son estructuras de datos no lineales que se componen de nodos o vértices y aristas

// class Nodo {
//   constructor(valor) {
//     this.valor = valor;
//     this.hijos = [];
//   }
// }

// class Grafo {
//   constructor(valor) {
//     this.raiz = new Nodo(valor);
//   }
// }

// let grafo = new Grafo(1);
// console.log(grafo);

// Inserción

// grafo.raiz.hijos.push(new Nodo(2));
// console.log(grafo);

// // Borrado

// grafo.raiz.hijos.pop();
// console.log(grafo);

// // Actualización

// grafo.raiz.valor = 0;
// console.log(grafo);

// Ordenación no aplica dado que no tiene indice

// Matrices son estructuras de datos que se componen de filas y columnas

let matriz = [
  [1, 2, 3],
  [4, 5, 6],
];
console.log(matriz);

// Inserción

matriz.push([7, 8, 9]);
console.log(matriz);

// Borrado

matriz.pop();
console.log(matriz);

// Actualización

matriz[0][0] = 0;
console.log(matriz);

// Ordenación

matriz.sort();
console.log(matriz);

/*
"""
  * DIFICULTAD EXTRA(opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
  * y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 * y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
  * de 11 dígitos(o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.

"""
*/
