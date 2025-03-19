/*
  EJERCICIO:
  ¡Ha comenzado diciembre! Es hora de montar nuestro
  árbol de Navidad...

  Desarrolla un programa que cree un árbol de Navidad
  con una altura dinámica definida por el usuario por terminal.
  
  Ejemplo de árbol de altura 5 (el tronco siempre será igual):

      *
     ***
    *****
   *******
  *********
     |||
     |||

  El usuario podrá seleccionar las siguientes acciones:

  - Añadir o eliminar la estrella en la copa del árbol (@)
  - Añadir o eliminar bolas de dos en dos (o) aleatoriamente
  - Añadir o eliminar luces de tres en tres (+) aleatoriamente
  - Apagar (*) o encender (+) las luces (conservando su posición)
  - Una luz y una bola no pueden estar en el mismo sitio

  Sólo puedes añadir una estrella, y tantas luces o bolas
  como tengan cabida en el árbol. El programa debe notificar
  cada una de las acciones (o por el contrario, cuando no
  se pueda realizar alguna).
*/

class ChristmasTree {
  constructor() {
    this.treePlan = [];
    this.spaces = [];
    this.spheresSpaces = [];
    this.lightsSpaces = [];
    this.lighsOffSpaces = [];
    this.lightsOnSpaces = [];
    this.treeHeight = parseInt(prompt("Ingresa un número mayor a 0 (cero) para definir la altura del árbol:"), 10);
    this.treeWidth = this.treeHeight * 2 - 1;
    this.pin = ".";
  }

  structure() {
    let rangeStart = this.treeHeight - 1;
    let rangeEnd = this.treeHeight;
    let rangeCenter = Math.floor(this.treeWidth / 2) - 1;

    for (let row = 0; row < this.treeHeight + 2; row++) {
      let space = " ";
      let pipe = "|";

      this.treePlan[row] = [];

      for (let column = 0; column < this.treeWidth; column++) {
        this.treePlan[row].push(space);
      }

      if (row < this.treeHeight) {
        this.treePlan[row].fill(this.pin, rangeStart, rangeEnd);

        rangeStart = rangeStart - 1;
        rangeEnd = rangeEnd + 1;
      }

      if (row >= this.treeHeight) {
        this.treePlan[row].fill(pipe, rangeCenter, rangeCenter + 3);
      }
    }
  }

  availablePositions(destinyArray, firstElement, secondElement) {
    for (let column = 1; column < this.treePlan.length; column++) {
      for (let row = 0; row < this.treePlan[column].length; row++) {
        if (secondElement == undefined) {
          if (this.treePlan[column][row] === firstElement) {
            destinyArray.push([column, row]);
          }
        } else {
          if (this.treePlan[column][row] === firstElement || this.treePlan[column][row] === secondElement) {
            destinyArray.push([column, row]);
          }
        }
      }
    }
  }

  shufflePositions(array) {
    for (let index = array.length - 1; index > 0; index--) {
      const shufflePosition = Math.floor(Math.random() * (index + 1));

      [array[index], array[shufflePosition]] = [array[shufflePosition], array[index]];
    }
  }

  star(option) {
    let star = "@";
    let checkStar = this.treePlan[0].findIndex((starElement) => starElement === star);
    let starPosition = Math.floor(this.treeWidth / 2);

    if (option === 1) {
      if (checkStar === -1) {
        this.treePlan[0][starPosition] = star;

        alert("La estrella fue colocada.");
      } else {
        alert("No puede realizarse la acción porque la estrella ya está colocada.");
      }
    } else if (option === 2) {
      if (checkStar > -1) {
        this.treePlan[0][starPosition] = this.pin;

        alert("La estrella fue retirada.");
      } else {
        alert("No puede realizarse la acción porque la estrella no ha sido colocada.");
      }
    } else {
      alert("Debes ingresar un número dentro de las opciones.");
    }
  }

  spheres(option) {
    const sphere = "o";

    if (option === 1) {
      if (this.spaces.length > 1) {
        this.treePlan[this.spaces[0][0]][this.spaces[0][1]] = sphere;
        this.treePlan[this.spaces[1][0]][this.spaces[1][1]] = sphere;

        alert("Se colocaron 2 esferas.");
      } else {
        alert("No hay espacio para colocar las esferas.");
      }
    } else if (option === 2) {
      this.spheresSpaces = [];

      this.availablePositions(this.spheresSpaces, sphere);
      this.shufflePositions(this.spheresSpaces);

      if (this.spheresSpaces.length > 1) {
        this.treePlan[this.spheresSpaces[0][0]][this.spheresSpaces[0][1]] = this.pin;
        this.treePlan[this.spheresSpaces[1][0]][this.spheresSpaces[1][1]] = this.pin;

        alert("Se retiraron dos esferas.");
      } else {
        alert("No puede realizarse la acción porque no hay esferas para eliminar.");
      }
    } else {
      alert("Debes ingresar un número dentro de las opciones.");
    }
  }

  lights(option) {
    const lightOn = "+";
    const lightOff = "-";

    if (option === 1) {
      if (this.spaces.length > 1) {
        this.treePlan[this.spaces[0][0]][this.spaces[0][1]] = lightOn;
        this.treePlan[this.spaces[1][0]][this.spaces[1][1]] = lightOn;
        this.treePlan[this.spaces[2][0]][this.spaces[2][1]] = lightOn;

        alert("Se colocaron 3 luces.");
      } else {
        alert("No hay espacio para colocar las luces.");
      }
      
    } else if (option === 2) {
      this.lighsOffSpaces = [];

      this.availablePositions(this.lighsOffSpaces, lightOff);

      if (this.lighsOffSpaces.length > 0) {
        for (let index = 0; index < this.lighsOffSpaces.length; index++) {
          this.treePlan[this.lighsOffSpaces[index][0]][this.lighsOffSpaces[index][1]] = lightOn;
        }

        alert("Se encendieron las luces.");
      } else {
        alert("No hay luces por encender.");
      }
    } else if (option === 3) {
      this.lightsOnSpaces = [];

      this.availablePositions(this.lightsOnSpaces, lightOn);

      if (this.lightsOnSpaces.length > 0) {
        for (let index = 0; index < this.lightsOnSpaces.length; index++) {
          this.treePlan[this.lightsOnSpaces[index][0]][this.lightsOnSpaces[index][1]] = lightOff;
        }

        alert("Se apagaron las luces.");
      } else {
        alert("No hay luces por apagar.");
      }
    } else if (option === 4) {
      this.lightsSpaces = [];

      this.availablePositions(this.lightsSpaces, lightOn, lightOff);
      this.shufflePositions(this.lightsSpaces);

      if (this.lightsSpaces.length > 1) {
        this.treePlan[this.lightsSpaces[0][0]][this.lightsSpaces[0][1]] = this.pin;
        this.treePlan[this.lightsSpaces[1][0]][this.lightsSpaces[1][1]] = this.pin;
        this.treePlan[this.lightsSpaces[2][0]][this.lightsSpaces[2][1]] = this.pin;

        alert("Se retiraron tres luces.");
      } else {
        alert("No puede realizarse la acción porque no hay luces para eliminar.");
      }
    } else {
      alert("Debes ingresar un número dentro de las opciones.");
    }
  }

  userActions() {
    let menu = 0;

    this.structure();

    do {
      this.spaces = [];
      menu = parseInt(prompt("Ingresa el número de la acción a realizar:\n1) Estrella.\n2) Esferas.\n3) Luces.\n4) Salir."), 10);

      this.availablePositions(this.spaces, this.pin);
      this.shufflePositions(this.spaces);

      switch (menu) {
        case 1:
          let starOption = parseInt(prompt("1) Colocar estrella.\n2) Retirar estrella."), 10);

          this.star(starOption);

          break;

        case 2:
          let spheresOption = parseInt(prompt("1) Colocar esferas.\n2) Retirar esferas."), 10);

          this.spheres(spheresOption);

          break;

        case 3:
          let lightsOption = parseInt(prompt("1) Colocar luces.\n2) Encender luces.\n3) Apagar luces.\n4) Retirar luces."), 10);

          this.lights(lightsOption);

          break;

        case 4:
          alert("Saliendo del programa...");
          break;

        default:
          alert("Por favor, ingresa un número del 1 al 4 para realizar alguna de las acciones del menú.");
          break;
      }

      console.table(this.treePlan);
    } while (menu !== 4);
  }
}

let christmasTree = new ChristmasTree();

christmasTree.userActions();
