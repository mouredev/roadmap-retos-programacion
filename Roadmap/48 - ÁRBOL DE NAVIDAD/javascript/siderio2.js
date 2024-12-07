/**
 * @author Desiderio Martínez Silva aka siderio2
 * @version 1.0
 * @description "Javascript implementation of the Christmas Tree exercise 48 from MoureDev Roadmap"
 * @see https://retosdeprogramacion.com/roadmap/
 *
 */

const readline = require("readline");

class ChristmasTree {
  constructor() {
    this.hasStar = false;
    this.lightsOn = false;
    this.balls = [];

    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  pintChristmasTree(rows) {
    let offset = rows - 1;
    // let coord = [1,1];
    process.stdout.write(
      " ".repeat(offset) +
        (this.hasStar ? "@" : this.lightsOn ? "+" : "*") +
        "\n"
    );
    for (let i = 2; i <= rows; i++) {
      offset--;
      const rowLength = 2 * i - 1;
      const char = "*";
      process.stdout.write(" ".repeat(offset));
      process.stdout.write(char.repeat(rowLength) + "\n");
    }
    this.printTreeTrunk(rows);
  }

  printTreeTrunk(rows) {
    const offset = rows - 2;
    process.stdout.write(" ".repeat(offset) + "|||\n");
    process.stdout.write(" ".repeat(offset) + "|||\n");
  }
}

const tree = new ChristmasTree();
tree.pintChristmasTree(8);

var a = [
  [1, 2],
  [3, 4],
];
var b = [1, 2];
a = JSON.stringify(a);
b = JSON.stringify(b);
console.log(a);
console.log(b);
var c = a.indexOf(b);
if (c != -1) {
  console.log("element present");
}
