const readlline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

function start() {
  readlline.question(
    "Crea un arbol de navidad, ingresa la altura: ",
    (height: string) => {
      menu();
    }
  );
}

function menu() {
  console.log(`
    0. Mostrar arbolito
    1. Añade la estrella en la copa (@)
    2. Elimina la estrella en la copa (@)
    3. Añade bolas de dos en dos (o) aleatoriamente
    4. Elimina bolas de dos en dos (o) aleatoriamente
    5. Añade luces de tres en tres (+) aleatoriamente
    6. Eliminar luces de tres en tres (+) aleatoriamente
    7. Apagar (*) las luces (conservando su posición)
    8. Encender (+) las luces (conservando su posición)
    10. Salir del sistema
    `);

  readlline.question("Seleccione una option: ", (option: string) => {
    switch (option) {
      case "0":
        break;
      case "1":
        break;
      case "2":
        break;
      case "3":
        break;
      case "4":
        break;
      case "5":
        break;
      case "6":
        break;
      case "7":
        break;
      case "8":
        break;
      case "10":
        console.log("Ha salido del sistema");
        readlline.close();
        break;

      default:
        console.log(`La opción ${option} es invalida.. vuelva a intentar`);
        menu();
        break;
    }
  });
}

class Tree {
  private tree: string;
  private height: number;

  constructor(height: number) {
    this.height = height;
    this.tree = "";
  }
}
