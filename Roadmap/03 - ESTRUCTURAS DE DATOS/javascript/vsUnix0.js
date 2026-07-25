//Estructuras de datos para JavaScript:

// 1. Array
console.log("-----------------------array------------------------");
let myArray = ["Manzana", "Pera", "Banano", "Sandía"];

for (let a = 0; a < myArray.length; a++) {
  console.log(myArray[a]);
} // Esto es para recorrerlo pero se puede utilizar foreach:

console.log("----------------------foreach-----------------------");

myArray.forEach((e, i, a) => {
  console.log(i, e);
});

console.log("---------------Operaciones habituales---------------");
//Añadir un elemento al final del array:
let addLastFruit = myArray.push("Zapote");
console.log(addLastFruit);

//Eliminar el ultimo elemento de un array
let deleteLastFruit = myArray.pop();
console.log(deleteLastFruit);

//Añadir un elemento al principio de un array:
let addFirstFruid = myArray.unshift("Fresa");
console.log(addFirstFruid);

//Eliminar el primer elemento de un array:
let deleteFirstFruit = myArray.shift();
console.log(deleteFirstFruit);

//Encontrar el índice de un array:
let pos = myArray.indexOf(2);
console.log(pos);

//eliminar cualquier elemento del array:
let deleteElement = myArray.splice(2);
console.log(deleteElement);

//2. Objeto
console.log("---------------------objetos------------------------");

let perro = {
  nombre: "dodis",
  edad: "9",
  raza: "pug",
};

console.log(JSON.stringify(perro, null, 3));

console.log(
  "---------------------función constructora para crear objetos------------------------",
);

function Car(make, model, year) {
  this.make = make;
  this.model = model;
  this.year = year;
} //para crear un constructor de un objeto

let myCar = new Car("Ford", "Mustang", "2025"); // crear nuevos vehículos
console.log(JSON.stringify(myCar, null, 3)); // Mostrarlos de manera organizada

console.log(
  "-----------------------clase en vez de función constructora----------------------",
);
//lo mejor es crearlo con class
class Lamp {
  constructor(color, forma, marca) {
    this.color = color;
    this.forma = forma;
    this.marca = marca;
  }
}

let lamp1 = new Lamp("Amarillo", "Redonda", "Pajarito");
console.log(JSON.stringify(lamp1, null, 3));

console.log(
  "------------------------enumeración de objetos------------------------",
);
let i = 1;
for (const prop in myCar) {
  console.log(i, myCar[prop]);
  i++;
} // para enumerarlos

//3. Set
console.log("------------------conjuntos o sets------------------");

let conjunto = new Set();

conjunto.add(2);
conjunto.add("mesa");
conjunto.add("libro");
conjunto.add("reloj");
conjunto.delete(2);
console.log(conjunto.has("lampara")); //Se usa para saber si contiene un valor

console.log(conjunto);

// Para recorrer un set se utiliza for of:
let o = 0;

for (const prop of conjunto) {
  console.log(o, prop);
  o++; /*a diferencia de un array con set no se puede hacer destructing, 
  así que el contador es manual pero por lo general no hay necesidad de 
  enumerarlo*/
}

//4. Map
console.log("--------------------maps----------------------------");

let mapa = new Map();

mapa.set("nombre", "Martín");
mapa.set("apellido", "Melo");
mapa.set("edad", 20);
mapa.set("comida preferida", "Hamburguesa");
mapa.set("Dónde ha viajado", [
  "Cali",
  "Barranquilla",
  "Buenaventura",
  "Medellín",
]);

console.log(mapa);
console.log(mapa.get("Dónde ha viajado"));

console.log("---------------Desafío extra------------------------");

let contacts = [
  {name: "Martín Melo", cel: "3045369321"},
  {name: "Sofía Gonzalez", cel: "3224326901"}
];


function cleanText(text) {
  return text.toString().trim().toLowerCase();
}

function agenda() {
  process.stdout.write(
    `
    1. Buscar contacto.\n
    2. Añadir contacto.\n
    3. Salir.\n\n
    Selecciona una opción\n> `
  )
  process.stdin.once("data", (data) => {
    let valor = cleanText(data);
    switch (valor) {
      case "1":
        searchContact();
        break;
      case "2":
        addContact();
        break;
      case "3":
        process.stdout.write("Saliendo...")
        setTimeout(()=>{
          process.exit();
        }, 2000)
        break;
      default:
        process.stdout.write("Por favor selecciona la opción correcta\n> ");
        agenda();
        break;
    }
  })
}

function searchContact() {
  process.stdout.write("Introduce el nombre de contacto: ")
  process.stdin.once("data", (data) => {
    valor = cleanText(data);
    let encontrado = false;
    for (const prop of contacts) {
      let name = prop.name;
      let formatName = name
        .toString()
        .trim()
        .toLowerCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g,"");
      if (formatName.includes(valor)){
        process.stdout.write(`El número de teléfono de ${prop.name} es ${prop.cel}\n`);
        encontrado = true;
        process.stdout.write("1. Eliminar contacto.\n2. Actualizar contacto.\n3. Regresar al menú\n>")
        process.stdin.once("data", (inputData) => {
          valor1 = cleanText(inputData)
          switch (valor1) {
            case "1":
              const index = contacts.indexOf(prop)
              if (index !== -1){
                contacts.splice(index, 1)
                process.stdout.write("Usuario eliminado\n")
              }
              agenda();
              break;
            case "2":
              process.stdout.write("Escribe el número de teléfono para actualizar el contacto: ")
              process.stdin.once("data", (updateHandler)=> {
                let valor2 = cleanText(updateHandler);
                prop.cel = valor2;
                agenda();
              });
              break;
            case "3":
              process.stdout.write("Regresando...");
              setTimeout(()=>{
                agenda();
              }, 2000)
          }
        })
      }
    }
    if (!encontrado) {
      process.stdout.write("No encontrado, deseas agregar uno nuevo? responde si o no: ");
      process.stdin.once("data", (data) => {
        valor = cleanText(data)
        switch (valor) {
          case "si":
            addContact();
            break;
          case "no":
            searchContact();
            break;
        }
      })
    }
  })
}

function addContact() {
  let temp = {};
  let counter = 0;

  function handleInput(data) {
  let valor = cleanText(data);
    switch (counter) {
      case 0:
        if (/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s'-]+$/.test(valor)) {
          counter = 1;
          temp.name = valor
          process.stdout.write("Por favor ingresa el número de teléfono: ")
        } else {
          process.stdout.write("Ingresa solo el nombre sin números o caracteres especiales: ")
        }
        break;
      case 1:
        if (/^\d{7,11}$/.test(valor)) {
          temp.cel = valor;
          contacts.push({...temp});
          temp = {};
          counter = 0;
          process.stdout.write("Agregado satisfactoriamente.\n")
          process.stdin.off("data", handleInput);
          agenda();
        } else {
          process.stdout.write("Debes agregar un número válido: ")
        }
        break;
    }
  }

  process.stdout.write("Por favor ingresa el nombre: ");
  process.stdin.on("data", handleInput)
}


agenda()
