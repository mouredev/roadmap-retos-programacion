/*Arrays, colección de datos ordenados por indices*/

let names = ["maria", "angel", "pedro", "luisa"];
names.push("rogelio");//Insertar dato
names.pop();//Eliminar dato
names[0] = "lupita";//Actualizar dato
names.sort();//Reordenar datos

/*Objectos literales, colección de datos ordenados por pares (clave:valor)*/

const joy = {
  raza: "poodle",
  color: "blanco",
  patas: 4,
  ladra: function () {
    console.log("woof, woof, woof");
  }
}
joy.raza = "mixed";//Actualizar propiedad
joy.cola = true;//Crear propiedad
joy.vive = false;
delete joy.vive;//Eliminar propiedad
//Objetos literales no poseen un método que reordene sus pares.

/*Date*/

//Esta estructura de datos posee muchos métodos que permiten su manipulación. Esto permite la representación de los datos en diferentes formatos, acceder a datos por separado (año, día, mes...).

let diaActual = new Date().toString();

/*Map, colección de datos ordenados por pares*/

const map1 = new Map();
map1.set("a", 1);//Crear dato
map1.set("b", true);
map1.set("a", 44);//Modificar dato
map1.delete("b");//Borrar dato
//El objeto Map() no posee un método que reordene sus pares.

/*Set, colección de datos únicos, primitivos u objetos*/

const mySet1 = new Set();

mySet1.add(1); //Crear dato
mySet1.add(5); // Set(2) { 1, 5 }
mySet1.add(5); // Set(2) { 1, 5 }, los datos son únicos. No se repíten.
mySet1.add("some text");
const o = { a: 1, b: 2 };
mySet1.add(o);
//Los datos en el objeto creado no pueden ser actualizados o reordenarse su posición.
mySet1.add({ a: 1, b: 2 }); // o hace referencia a un objeto diferente.
mySet1.delete(5);//Borrar dato

/*Weakset, colección de datos tipo objeto y Symbol*/

