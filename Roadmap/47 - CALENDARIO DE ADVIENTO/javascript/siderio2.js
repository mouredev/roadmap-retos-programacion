/**
 * @author Desiderio Martínez Silva aka siderio2
 * @version 1.0
 * @description "Javascript implementation of the Advent Calendar exercise 48 from MoureDev Roadmap"
 * @see https://retosdeprogramacion.com/roadmap/
 *
 */

/**
 * Module for reading data from the terminal
 *
 * @see https://nodejs.org/api/readline.html
 */
const readline = require("readline");

class AdventCalendar {
  /**
   * Constructor for the advent calendar class
   *
   * @returns {AdventCalendar}
   *
   * @property {Array<string>} calendar - Array of strings representing the days of the advent calendar
   * @property {Set<number>} openedDays - Set of numbers representing the days that have been opened
   * @property {Object} rl - Instance of the readline module to read data from the terminal
   */
  constructor() {
    this.calendar = [];
    this.openedDays = new Set();
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  /**
   * Populates the calendar array with string representations of days 1-24.
   * Each day is represented as a two-character string, with a leading zero for days 1-9.
   */
  populateCalendar() {
    for (let i = 1; i <= 24; i++) {
      if (i < 10) {
        this.calendar.push("0" + i.toString());
        continue;
      }
      this.calendar.push(i.toString());
    }
  }

  /**
   * Prints the advent calendar to the console.
   *
   * Each day is represented as a two-character string, with a leading zero for days 1-9.
   * Opened days are represented as '**** ' and unopened days are represented as '*XX* '.
   * The calendar is printed as a 4x6 grid of strings, with a space between each day and a newline between each row.
   */
  printCalendar() {
    process.stdout.write("\n");
    for (let i = 0; i < 4; i++) {
      process.stdout.write("**** ".repeat(6) + "\n");
      for (let j = 0; j < 6; j++) {
        const day = this.calendar[i * 6 + j];
        process.stdout.write(
          this.openedDays.has(parseInt(day)) ? "**** " : "*" + day + "* "
        );
      }
      process.stdout.write("\n" + "**** ".repeat(6) + "\n\n");
    }
  }

  /**
   * Prints the days that have been opened to the console.
   *
   * If no days have been opened, prints "Ninguno día abierto todavía.".
   * Otherwise, prints a comma-separated list of the opened days.
   */
  printOpenedDays() {
    if (this.openedDays.size == 0) {
      console.log("Ninguno día abierto todavía.\n");
      return;
    }
    console.log("Días abiertos: " + [...this.openedDays].join(", ") + "\n");
  }

  /**
   * Asks the user which day they want to open, and then opens that day
   * and prints the updated calendar and list of opened days.
   * If the user enters 'x', the program exits.
   * If the user enters a non-integer, an integer outside the range of 1-24,
   * or an integer that has already been opened, the program will print
   * an error message and ask again.
   */
  selectDay() {
    this.rl.question("Que día deseas abrir ('x' para salir): ", (dia) => {
      if (dia.toLowerCase() == "x") {
        this.rl.close();
        return;
      }

      dia = parseInt(dia);

      if (isNaN(dia) || !Number.isInteger(dia)) {
        console.log("El dia debe ser un entero");
        this.selectDay();
      } else if (dia < 1 || dia > 24) {
        console.log("El dia debe estar entre 1 y 24");
        this.selectDay();
      } else if (this.openedDays.has(dia)) {
        console.log("El dia ya estaba abierto");
        this.selectDay();
      } else {
        this.openedDays.add(dia);
        this.printCalendar();
        this.printOpenedDays();
        this.selectDay();
      }
    });
  }
}

const calendar = new AdventCalendar();
calendar.populateCalendar();
calendar.printCalendar();
calendar.printOpenedDays();
calendar.selectDay();
