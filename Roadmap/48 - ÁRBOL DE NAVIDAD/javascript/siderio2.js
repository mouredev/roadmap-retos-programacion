/**
 * @author Desiderio Martínez Silva aka siderio2
 * @version 1.0
 * @description "Javascript implementation of the Christmas Tree exercise 48 from MoureDev Roadmap"
 * @see https://retosdeprogramacion.com/roadmap/
 *
 */

/**
 * Module for reading data from the terminal
 *
 * @see https://nodejs.org/api/readline.html
 */
const readline = require("readline");

class ChristmasTree {
  /**
   * Creates a new Christmas tree.
   *
   * By default, the tree has 5 rows, no star on top, no lights on, and no
   * decorations. The `readline` interface is also initialized for reading
   * user input from the terminal.
   */
  constructor() {
    this.rows = 5;
    this.hasStar = false;
    this.lightsOn = false;
    this.lights = [];
    this.balls = [];

    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  /**
   * Prints the Christmas tree to the console.
   * The tree consists of an optional star or top decoration, rows of branches,
   * and a trunk at the bottom. Decorations such as lights and balls
   * can be displayed based on the current state of the tree.
   *
   * @param {boolean} repeat - If true, allows for changing decorations
   *                           after printing the tree.
   */
  pintChristmasTree(repeat = true) {
    let offset = this.rows - 1;
    process.stdout.write(
      "\n" +
        " ".repeat(offset) +
        (this.hasStar ? "@" : this.lightsOn ? "+" : "*") +
        "\n"
    );
    for (let i = 2; i <= this.rows; i++) {
      offset--;
      process.stdout.write(" ".repeat(offset));
      const rowLength = 2 * i - 1;
      for (let j = 1; j <= rowLength; j++) {
        const coord = [i, j];
        const char = this.calculateChar(coord);
        process.stdout.write(char);
      }
      process.stdout.write("\n");
    }
    this.printTreeTrunk();
    if (repeat) {
      this.changeDecoration();
    }
  }

  /**
   * Prints the trunk of the Christmas tree to the console.
   * The trunk is represented by a combination of underscores and
   * pipe characters. The trunk is positioned at the bottom of the
   * tree, and is decorated with three small present boxes.
   */
  printTreeTrunk() {
    const offset = this.rows - 2;
    process.stdout.write(" ".repeat(offset) + "|||\u{1F381}\n");
    process.stdout.write(
      "_".repeat(offset - 1) +
        "// \u{1F381}\u{1F381}" +
        "_".repeat(offset - 3) +
        "\n"
    );
  }

  /**
   * Determines the character representation for a given coordinate on the Christmas tree.
   *
   * The character is determined based on the presence of balls and the state
   * of the lights on the tree. If the coordinate matches a ball location,
   * an 'O' is returned. If a light is matched, and the lights are on,  a '+' is returned.
   * Otherwise, if the lights are off a '*' is returned.
   *
   * @param {Array<number>} coord - The coordinate on the tree in the format [row, column].
   * @returns {string} The character representing the decoration at the given coordinate.
   */
  calculateChar(coord) {
    coord = JSON.stringify(coord);
    const balls = JSON.stringify(this.balls);

    if (balls.indexOf(coord) != -1) {
      return "O";
    } else if (this.lightsOn) {
      return "+";
    } else {
      return "*";
    }
  }

  /**
   * Creates the default decorations for the Christmas tree with the given number of rows.
   *
   * The tree is decorated by assigning a light to each coordinate
   * on the tree. The tree is then printed to the console.
   *
   * @param {number} rows - The number of rows to decorate the tree with.
   */
  decorateTree(rows) {
    if (rows < 2) {
      console.log("Rows must be greater than 1.");
      return;
    }
    this.rows = rows;
    for (let i = 2; i <= this.rows; i++) {
      const rowLength = 2 * i - 1;
      for (let j = 1; j <= rowLength; j++) {
        const coord = [i, j];
        this.lights.push(coord);
      }
    }
    this.pintChristmasTree();
  }

  /**
   * Changes the state of the star on top of the Christmas tree.
   *
   * If the star is currently on, it is removed. If the star is currently off,
   * it is added. After changing the state, the tree is redrawn.
   */
  changeStarState() {
    this.hasStar = !this.hasStar;
    this.pintChristmasTree();
  }

  /**
   * Changes the state of the lights on the Christmas tree.
   *
   * If the lights are currently on, they are turned off. If the lights are currently off,
   * they are turned on. After changing the state, the tree is redrawn.
   */
  changeLightsState() {
    this.lightsOn = !this.lightsOn;
    this.pintChristmasTree();
  }

  /**
   * Adds balls to the Christmas tree. If possible, two balls are added at a time.
   * The coordinates of the added balls are calculated randomly.
   *
   * The balls are added in place of the lights on the tree. If there are
   * no lights on the tree (i.e., the tree is full of balls), no balls are added.
   * After adding the balls, the tree is redrawn.
   */
  addBalls() {
    const positions = this.lights.length > 1 ? 2 : this.lights.length;

    if (!positions) {
      console.log("Ball-Full-Tree!!! There are no space to add balls.");
      return;
    }

    for (let i = 0; i < positions; i++) {
      const index = Math.floor(Math.random() * this.lights.length);
      this.balls.push(this.lights[index]);
      this.lights.splice(index, 1);
    }
    this.pintChristmasTree();
  }

  /**
   * Removes balls from the Christmas tree. If possible, two balls are removed at a time.
   * The coordinates of the removed balls are calculated randomly.
   *
   * The balls are removed from the tree and replaced by lights. If there are
   * no balls on the tree (i.e., the tree is full of lights), no balls are removed.
   * After removing the balls, the tree is redrawn.
   */
  removeBalls() {
    const positions = this.balls.length > 1 ? 2 : this.balls.length;

    if (!positions) {
      console.log("Ball-Empty-Tree!!! There are no balls to remove.");
      return;
    }

    for (let i = 0; i < positions; i++) {
      const index = Math.floor(Math.random() * this.balls.length);
      this.lights.push(this.balls[index]);
      this.balls.splice(index, 1);
    }
    this.pintChristmasTree();
  }

  /**
   * Adds lights to the Christmas tree. If possible, three lights are added at a time.
   * The coordinates of the added lights are calculated randomly.
   *
   * The lights are added to the tree and replace balls. If there are
   * no balls on the tree (i.e., the tree is full of lights), no lights are added.
   * After adding the lights, the tree is redrawn.
   */
  addLights() {
    const positions = this.balls.length > 2 ? 3 : this.balls.length;

    if (!positions) {
      console.log("Lights-Full-Tree!!! There are no space to add lights.");
      return;
    }

    for (let i = 0; i < positions; i++) {
      const index = Math.floor(Math.random() * this.balls.length);
      this.lights.push(this.balls[index]);
      this.balls.splice(index, 1);
    }
    this.pintChristmasTree();
  }

  /**
   * Removes lights from the Christmas tree. If possible, three lights are removed at a time.
   * The coordinates of the removed lights are calculated randomly.
   *
   * The lights are removed from the tree and replaced by balls. If there are
   * no lights on the tree (i.e., the tree is full of balls), no lights are removed.
   * After removing the lights, the tree is redrawn.
   */
  removeLights() {
    const positions = this.lights.length > 2 ? 3 : this.lights.length;

    if (!positions) {
      console.log("Lights-Empty-Tree!!! There are no lights to remove.");
      return;
    }

    for (let i = 0; i < positions; i++) {
      const index = Math.floor(Math.random() * this.lights.length);
      this.balls.push(this.lights[index]);
      this.lights.splice(index, 1);
    }
    this.pintChristmasTree();
  }

  /**
   * Prompts the user to define the size of the Christmas tree.
   *
   * The user is asked to input a number between 5 and 25, which represents
   * the number of rows for the tree. If the input is not a valid integer
   * within this range, the function will prompt again. Once a valid
   * size is provided, the tree is decorated with the specified number of rows.
   */
  defineSize() {
    this.rl.question(
      "How big do you want the tree?? Minimum is 5 and Maximum is 25 rows high: ",
      (rows) => {
        rows = parseInt(rows.trim());

        if (isNaN(rows) || !Number.isInteger(rows)) {
          console.log("Please, enter an integer value.");
          this.defineSize();
        } else if (rows < 5 || rows > 25) {
          console.log("Please, enter a value between 5 and 25.");
          this.defineSize();
        } else {
          this.decorateTree(rows);
        }
      }
    );
  }

  /**
   * Allows the user to interactively change the decorations of the Christmas tree.
   *
   * The user is presented with a menu of options to change the decorations of the tree.
   * The options are:
   * 1. Add/Remove Star
   * 2. Lights On/Off
   * 3. Add 2 balls
   * 4. Remove 2 balls
   * 5. Add 3 lights
   * 6. Remove 3 lights
   * 7. Exit
   *
   * The user is asked to input a number between 1 and 7, which
   * corresponds to one of the options above. If the input is not a valid
   * integer within this range, the function will prompt again. Once a valid
   * option is selected, the tree is decorated with the corresponding
   * change. If the user selects 7, the function will exit and the Christmas
   * tree will be printed with a message on an empty console.
   */
  changeDecoration() {
    this.rl.question(
      "\nSelect what changes do you want to make:\n1) Add/Remove Star.\n2) Lights On/Off.\n3) Add 2 balls.\n4) Remove 2 balls.\n5) Add 3 lights.\n6) Remove 3 lights.\n7) Exit.\n",
      (option) => {
        option = parseInt(option.trim());
        if (isNaN(option) || !Number.isInteger(option)) {
          console.log(
            "\nPlease, enter an valid option (an integer between 1 and 7)."
          );
          this.changeDecoration();
        }
        if (parseInt(option) < 1 || parseInt(option) > 7) {
          console.log(
            "\nPlease, enter a valid option (an integer between 1 and 7)."
          );
          this.changeDecoration();
        } else {
          switch (option) {
            case 1:
              this.changeStarState();
              this.changeDecoration();
              break;
            case 2:
              this.changeLightsState();
              this.changeDecoration();
              break;
            case 3:
              this.addBalls();
              this.changeDecoration();
              break;
            case 4:
              this.removeBalls();
              this.changeDecoration();
              break;
            case 5:
              this.addLights();
              this.changeDecoration();
              break;
            case 6:
              this.removeLights();
              this.changeDecoration();
              break;
            case 7:
              console.clear();
              console.log("\nGoodbye and enjoy your Christmas Tree!\n");
              this.pintChristmasTree(false);
              console.log("\n");
              this.rl.close();
              break;
          }
        }
      }
    );
  }
}

const tree = new ChristmasTree();
tree.defineSize();
