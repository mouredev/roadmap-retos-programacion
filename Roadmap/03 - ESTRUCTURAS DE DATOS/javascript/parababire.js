/*Arrays, colección de datos ordenados por indices*/

let names = ["maria", "angel", "pedro", "luisa"];
names.push("rogelio");//Insertar dato
console.log(names);
names.pop();//Eliminar dato
console.log(names);
names[0] = "lupita";//Actualizar dato
console.log(names);
names.sort();//Reordenar datos
console.log(names);

/*Objectos literales, colección de datos ordenados por pares (clave:valor)*/

const joy = {
  raza: "poodle",
  color: "blanco",
  patas: 4,
  ladra: function () {
    console.log("woof, woof, woof");
  }
}
console.log(joy);
joy.raza = "mixed";//Actualizar propiedad
console.log(joy);
joy.cola = true;//Crear propiedad
console.log(joy);
joy.vive = false;
console.log(joy);
delete joy.vive;//Eliminar propiedad
console.log(joy);
//Objetos literales no poseen un método que reordene sus pares.

/*Date*/

//Esta estructura de datos posee muchos métodos que permiten su manipulación. Esto permite la representación de los datos en diferentes formatos, acceder a datos por separado (año, día, mes...).

let diaActual = new Date().toString();
console.log(diaActual);

/*Map, colección de datos ordenados por pares*/

const map1 = new Map();
map1.set("a", 1);//Crear dato
map1.set("b", true);
console.log(map1);
map1.set("a", 44);//Modificar dato
console.log(map1.get("a"));
map1.delete("b");//Borrar dato
console.log(map1);
//El objeto Map() no posee un método que reordene sus pares.