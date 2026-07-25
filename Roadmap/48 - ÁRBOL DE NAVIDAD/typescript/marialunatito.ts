// use this command for run npx ts-node "Roadmap/48 - ÁRBOL DE NAVIDAD/typescript/marialunatito.ts"

const readlline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

function start() {
  readlline.question(
    "Crea un arbol de navidad, ingresa la altura: ",
    (height: string) => {
      const treeModel = new Tree(parseInt(height));
      treeModel.create();
      menu(treeModel);
    }
  );
}

function menu(tree: Tree) {
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
        console.log(tree.Tree);
        menu(tree);
        break;
      case "1":
        tree.addStart();
        break;
      case "2":
        tree.removeStart();
        break;
      case "3":
        tree.addBalls();
        break;
      case "4":
        tree.removedBalls();
        break;
      case "5":
        tree.addLights();
        break;
      case "6":
        tree.removeLights();
        break;
      case "7":
        tree.turnOff();
        break;
      case "8":
        tree.turnOn();
        break;
      case "10":
        console.log("Ha salido del sistema");
        readlline.close();
        break;

      default:
        console.log(`La opción ${option} es invalida.. vuelva a intentar`);
        menu(tree);
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

  create() {
    let space = "";
    let asterisk = "";

    //   height = 2
    for (let i = 1; i <= this.height; i++) {
      Array.from({ length: this.height - i }).forEach((_) => {
        space += " ";
      });

      Array.from({ length: 2 * i - 1 }).forEach((_) => {
        asterisk += "*";
      });

      this.tree += `${space}${asterisk}\n`;
      space = "";
      asterisk = "";
    }

    let spaceTrunk = "";

    Array.from({ length: (2 * this.height - 1 - 3) / 2 }).forEach((_) => {
      spaceTrunk += " ";
    });
    const trunk = `${spaceTrunk}|||\n${spaceTrunk}|||`;

    this.tree += trunk;
    /// RESULT
    console.log("\n");
    console.log(this.tree);
    console.log("\n");

    return this.tree;
  }

  addStart() {
    if (this.tree.includes("@")) {
      console.log("El tree ya contiene la estrella");
    } else {
      const indexStart = this.getIndexStart();
      const treeWithStart =
        this.tree.substring(0, indexStart) +
        "@" +
        this.tree.substring(indexStart + 1, this.tree.length);
      this.tree = treeWithStart;
      console.log(this.tree);
    }

    menu(this);
  }

  private getIndexStart() {
    let index = this.tree.indexOf("*");
    if (index === -1) {
      index = this.tree.indexOf("+");
    }
    return index;
  }

  removeStart() {
    if (this.tree.includes("@")) {
      const treeWithStart = this.tree.replace("@", "*");
      this.tree = treeWithStart;
      console.log(this.tree);
    } else {
      console.log("***********Se quitó la estrella***********");
    }

    menu(this);
  }

  turnOn() {
    if (this.tree.includes("*")) {
      this.tree = this.tree.replaceAll("*", "+");
      console.log(this.tree);
    } else {
      console.log("El arbolito está encendido o tiene bolas!");
    }

    menu(this);
  }

  turnOff() {
    if (this.tree.includes("+")) {
      this.tree = this.tree.replaceAll("+", "*");
      console.log(this.tree);
    } else {
      console.log("El arbolito está apagado!");
    }

    menu(this);
  }

  addBalls() {
    let count = 0;
    let canBeBall = false;

    let cant = 0;
    Array.from({ length: this.tree.length }).forEach((_, i) => {
      if (this.tree.substring(i, i + 1).includes("*")) {
        cant++;
      }
    });

    if (cant >= 2) {
      canBeBall = true;
    } else {
      canBeBall = false;
      console.log(
        "************Ya no hay espacios posibles para colocar bolas************"
      );
    }

    while (canBeBall) {
      const index = this.indexRandom();
      const indexTreeForChange = this.tree.substring(index, index + 1);
      if (indexTreeForChange.includes("*")) {
        const newTree =
          this.tree.substring(0, index) +
          "o" +
          this.tree.substring(index + 1, this.tree.length);

        // set new tree
        this.tree = newTree;

        count++;
        if (count === 2) {
          // stop the while
          canBeBall = false;
        }
      }
    }

    console.log(this.tree);
    menu(this);
  }

  removedBalls() {
    let count = 0;
    let canBeRemoveBall = false;

    let cant = 0;
    Array.from({ length: this.tree.length }).forEach((_, i) => {
      if (this.tree.substring(i, i + 1).includes("o")) {
        cant++;
      }
    });

    if (cant >= 2) {
      canBeRemoveBall = true;
    } else {
      canBeRemoveBall = false;
      console.log("************Ya no hay bolas que quitar!************");
    }

    while (canBeRemoveBall) {
      const index = this.indexRandom();
      const indexTreeForChange = this.tree.substring(index, index + 1);
      if (indexTreeForChange.includes("o")) {
        const newTree =
          this.tree.substring(0, index) +
          "*" +
          this.tree.substring(index + 1, this.tree.length);

        // set new tree
        this.tree = newTree;

        count++;
        if (count === 2) {
          // stop the while
          canBeRemoveBall = false;
        }
      }
    }

    console.log(this.tree);
    menu(this);
  }

  addLights() {
    let count = 0;
    let canBeLights = false;

    let cant = 0;
    Array.from({ length: this.tree.length }).forEach((_, i) => {
      if (this.tree.substring(i, i + 1).includes("*")) {
        cant++;
      }
    });

    if (cant >= 3) {
      canBeLights = true;
    } else {
      canBeLights = false;
      console.log(
        "************Ya no hay espacios posibles para colocar más luces************"
      );
    }

    while (canBeLights) {
      const index = this.indexRandom();
      const indexTreeForChange = this.tree.substring(index, index + 1);
      if (indexTreeForChange.includes("*")) {
        const newTree =
          this.tree.substring(0, index) +
          "+" +
          this.tree.substring(index + 1, this.tree.length);

        // set new tree
        this.tree = newTree;

        count++;
        if (count === 3) {
          // stop the while
          canBeLights = false;
        }
      }
    }

    console.log(this.tree);
    menu(this);
  }

  removeLights() {
    let count = 0;
    let canBeLights = false;

    let cant = 0;
    Array.from({ length: this.tree.length }).forEach((_, i) => {
      if (this.tree.substring(i, i + 1).includes("+")) {
        cant++;
      }
    });

    if (cant >= 3) {
      canBeLights = true;
    } else {
      canBeLights = false;
      console.log("************No hay mas luces que quitar!!************");
    }

    while (canBeLights) {
      const index = this.indexRandom();
      const indexTreeForChange = this.tree.substring(index, index + 1);
      if (indexTreeForChange.includes("+")) {
        const newTree =
          this.tree.substring(0, index) +
          "*" +
          this.tree.substring(index + 1, this.tree.length);

        // set new tree
        this.tree = newTree;

        count++;
        if (count === 3) {
          // stop the while
          canBeLights = false;
        }
      }
    }

    console.log(this.tree);
    menu(this);
  }

  private indexRandom(): number {
    const indexRandom = Math.floor(Math.random() * this.tree.length);
    const indexStart = this.getIndexStart();
    if (indexRandom != indexStart) {
      return indexRandom;
    }
    return this.indexRandom();
  }

  get Tree() {
    return this.tree;
  }

  set Tree(tree: string) {
    this.tree = tree;
  }
}

start();
