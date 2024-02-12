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

/*Esta estructura de datos posee muchos métodos que permiten su manipulación. 
Esto permite la representación de los datos en diferentes formatos, acceder a 
datos por separado (año, día, mes...).*/

let diaActual = new Date().toString();

/*Map, colección de datos ordenados por pares*/

const map1 = new Map();
map1.set("a", 1);//Crear dato
map1.set("b", true);
map1.set("a", 44);//Modificar dato
map1.delete("b");//Borrar dato
//El objeto Map() no posee un método que reordene sus pares.

/*WeakMap, colección de datos por par donde las keys pueden ser objetos o
symbols no registrados*/

const wm1 = new WeakMap();//Crear objeto WeakMap
const wm2 = new WeakMap();
const wm3 = new WeakMap();
const o1 = {};//Crear keys
const o2 = function () {};
const o3 = window;

wm1.set(o1, 37);//Añadir values a las keys
wm1.set(o2, "azerty");
wm2.set(o1, o2); //Cualquier valor, incluidos objetos y funciones
wm2.set(o2, undefined);
wm2.set(wm1, wm2); //Otro WeakMap puede ser key

wm1.get(o2); // "azerty"
wm2.get(o2); // undefined, ya que ese valor recibió
wm2.get(o3); // undefined, ya que no existe key para o3 en wm2

wm1.has(o2); // true
wm2.has(o2); // true (aunque el valor mismo sea 'undefined')
wm2.has(o3); // false

wm3.set(o1, 37);
wm3.get(o1); // 37

wm1.has(o1); // true
wm1.delete(o1);
wm1.has(o1); // false
//No se pueden reordenar o mutar los pares en WeakMaps

/*Set, colección de datos únicos, primitivos u objetos*/

const mySet1 = new Set();

mySet1.add(1); //Crear dato
mySet1.add(5); // Set(2) { 1, 5 }
mySet1.add(5); // Set(2) { 1, 5 }, los datos son únicos. No se repíten.
mySet1.add("some text");
const o = { a: 1, b: 2 };
mySet1.add(o);
/*Los datos en el objeto creado no pueden ser actualizados o reordenarse 
su posición.*/
mySet1.add({ a: 1, b: 2 }); // o hace referencia a un objeto diferente.
mySet1.delete(5);//Borrar dato

/*WeakSet, esta colección solo permite datos de tipo objeto y Symbol*/

const ws = new WeakSet();
const foo = {};
const bar = {};

ws.add(foo);//Añadir dato
ws.add(bar);

ws.has(foo); //true
ws.has(bar); //true

ws.delete(foo); //Eliminar dato
ws.has(foo); //false
ws.has(bar); //true
/*Esta estructura solo permite guardar objetos y eliminarlos cuando se les deja 
de hacer referencia en el código*/

/*JSON*/

/*JSON es un objeto utilizado para tranferir data entre diferentes ambientes 
incluso lenguajes, sus métodos son estático lo que permite únicamente su parseo*/

/*
{
  "browsers": {
    "firefox": {
      "name": "Firefox",
      "pref_url": "about:config",
      "releases": {
        "1": {
          "release_date": "2004-11-09",
          "status": "retired",
          "engine": "Gecko",
          "engine_version": "1.7"
        }
      }
    }
  }
}*/

//Extra

function my_agenda() {

  let name, phone;
  let on = true;
  let phoneRegex = /^\s{0}\b\d{11}\b\s{0}$/;
  let agenda = {};
  function phone_Regex() {
    phone = prompt("Ingresa número telefónico del contacto: ", "");
        if (phoneRegex.test(phone)) {
          agenda[name] = phone;
        } else {
          console.log("El número debe tener 11 dígitos, sin espacios.");
        }
  }
  function msjError() {
    console.log(`El contacto ${name} no existe.`);
  }

  while (on) {

    console.log("");
    console.log("1.- Buscar contacto");
    console.log("2.- Insertar contacto");
    console.log("3.- Actualizar contacto");
    console.log("4.- Borrar contacto");
    console.log("5.- Salir");

    let operacion = prompt("\nSelecciona una operación: ", "");

    switch (operacion) {
      case "1":
        console.log("");
        name = prompt("Ingresa nombre del contacto a buscar: ", "");
        if (agenda.hasOwnProperty(name)) {
          console.log(`El número de ${name} es: ${agenda[name]}`);
        } else {
          msjError();
        }
        break;
      case "2":
        name = prompt("Ingresa nombre del contacto: ", "");
        phone_Regex();
        break;
      case "3":
        name = prompt("Ingresa nombre del contacto a actualizar: ", "");
        if (agenda.hasOwnProperty(name)) {
          phone_Regex();
        } else {
          msjError();
        }
        break;
      case "4":
        name = prompt("Ingresa nombre del contacto a eliminar: ", "");
        if (agenda.hasOwnProperty(name)) {
          delete agenda[name];
        } else {
          msjError();
        }
        break;
      case "5":
        console.log("Salir del programa.");
        on = false;
        break;
      default:
        console.log("Tu elección no es válida. Elige un número del 1 al 5.");
        break;
    }
  }
}

my_agenda();