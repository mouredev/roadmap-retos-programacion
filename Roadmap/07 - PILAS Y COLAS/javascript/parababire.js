//Stack

let stackArr = [];

/*push*/
stackArr.push("Luis");
stackArr.push("María");
stackArr.push("Luisa");
console.log(stackArr);

/*pop*/
console.log(stackArr.pop());
console.log(stackArr);

//Queue

let queueArr = [];

/*enqueue*/

queueArr.push("Corolla");
queueArr.push("Ford");
queueArr.push("Chevrolet");
console.log(queueArr);

/*dequeue*/

console.log(queueArr.shift());
console.log(queueArr);

//Extra

/*Navegador*/

function navegadorWeb() {

  let url;
  let on = true;
  let stack = [];

  while (on) {

    console.log("");
    console.log("1.- Ingresar URL");
    console.log("2.- Adelantar Web");
    console.log("3.- Atras Web");
    console.log("4.- Salir");

    let comand = prompt("\nSelecciona una operación: ", "");

    switch (comand) {
      case "1":
        url = prompt("Ingresa la URL deseada: ", "");
        stack.push(url);
        console.log(`Has ingresado a: ${stack[stack.length - 1]}`);
        break;
      case "2":
        if (stack.length !== 0) {
          console.log(`Te encuentras actualmente en la página: ${stack[stack.length - 1]}`);
        } else {
          console.log("Estas en la página de inicio");
        }
        break;
      case "3":
        if (stack.length !== 0) {
          stack.pop();
          if (stack.length > 0) {
            console.log(`Has retornado a la página ${stack[stack.length - 1]}`);
          } else {
            console.log("El registro ahora está vacio.");
          }
        } else {
          console.log("No existen url's en el registro");
        }
        break;
      case "4":
        console.log("Salir del programa.");
        on = false;
        break;
      default:
        console.log("Tu elección no es válida. Elige un número del 1 al 4.");
        break;
    }
  }
}
navegadorWeb();

/*Copiadora*/

function impresoraCompartida() {

  let on = true;
  let stack = [];

  while (on) {
    
    console.log("");
    console.log("1.- Ingresar documento en cola");
    console.log("2.- Imprimir documento");
    console.log("3.- Salir");

    let comand = prompt("\nSelecciona una operación: ", "");

    switch (comand) {
      case "1":
        stack.push(prompt("Ingresa documento: "))
        console.log(`Documentos en cola: ${stack}`);
        break;
      case "2":
        if (stack.length !== 0) {
          if (stack.length > 0) {
            console.log(`Se imprimió el primer elemento de la cola: ${stack.shift()}`);
          } 
        } else {
          console.log("No existen documentos en cola");
        }
        break;
      case "3":
        console.log("Salir del programa");
        on = false;
        break;
    
      default:
        console.log("Solicitud inválida. Elige números de 1 al 3.");
        break;
    }
  }
}

impresoraCompartida();