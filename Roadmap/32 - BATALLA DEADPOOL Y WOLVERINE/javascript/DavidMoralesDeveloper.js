const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin, // For user input from the console
  output: process.stdout, // For displaying output to the console
});


let deadPool = [
  {
    nombre: "DeadPool",
    vida: 1000,
    ataque() {
      return Math.floor(Math.random() * 100) + 1;
    },
    regeneracion() {
      const vidaRecuperada = Math.round(this.ataque() * 0.1);
      this.vida += vidaRecuperada;
      // console.log(`¡${this.nombre} se regenera ${vidaRecuperada} de vida! Vida actual: ${this.vida}`);
      return vidaRecuperada;
    }, //10 porciento del ataque,
    evasion() {
      return Math.floor(Math.random() * 100) + 1 < 25 ? 1 : 0;
    }, //25% de evasion 1 acerti la evasion 0 recive el ataque
  },
];
let wolverin = [
  {
    nombre: "Wolverin",
    vida: 1000,
    ataque() {
      return Math.floor(Math.random() * 120) + 1;
    },
    regeneracion() {
      const vidaRecuperada = Math.round(this.ataque() * 0.1);
      this.vida += vidaRecuperada;
      // console.log(`¡${this.nombre} se regenera ${vidaRecuperada} de vida! Vida actual: ${this.vida}`);
      return vidaRecuperada;
    }, //10 porciento del ataque,
    evasion() {
      return Math.floor(Math.random() * 100) + 1 < 20 ? 1 : 0;
    }, //25% de evasion
  },
];
let pierdeturnoDeadPool = false;
  let pierdeturnoWolverin = false;

function batallaDvsW() {
  console.log("--------------------------comienza ataque-------------");

  let turno = 1;

  while (wolverin[0].vida > 0 && deadPool[0].vida > 0) {
    console.log(`Turno ${turno}`);

    //turno de deadpool
    if (deadPool[0].vida > 0 ) {
        if (pierdeturnoDeadPool) {
      console.log(" Dead poolRegenerandome");
      pierdeturnoDeadPool = false;
    }else{
      let dañoDeadpool = deadPool[0].ataque();
      console.log(`DeadPool ataca con ${dañoDeadpool}`);
      if (dañoDeadpool === 100) {
        console.log(
          `¡ATAQUE CRÍTICO DE ${deadPool[0].nombre}! ${wolverin[0].nombre} pierde su próximo turno.`
        );
        pierdeturnoWolverin = true;

        let vidaRegeneradaDeadPool = deadPool[0].regeneracion(); // Deadpool se regenera
        console.log(
          `${deadPool[0].nombre} gana ${vidaRegeneradaDeadPool} de recuperación. Vida de ${deadPool[0].nombre}: ${deadPool[0].vida}`
        );
      } else {
        if (wolverin[0].evasion()) {
          console.log("Wolverin a evadido el daño");
        } else {
          wolverin[0].vida -= dañoDeadpool;
          console.log(
            `Wolverin recibe ${dañoDeadpool} daño. Vide de Wolverin ${wolverin[0].vida}`
          );
        }
      }
    }
    }

    //vemos si wolverin sigue vivo
    if (wolverin.vida <= 0) {
      console.log(`¡Wolverin ha sido derrotado!`);
      break; // Salimos del bucle si Wolverin muere
    }

    //tueno de wolverin
    if (wolverin[0].vida > 0 ) {
        if (pierdeturnoWolverin) {
      console.log("Wolverin regenerandome");
      pierdeturnoWolverin = false;
    }else {
      let dañoWolverin = wolverin[0].ataque();
      console.log(`Wolverin ataca con ${dañoWolverin}`);
      if (dañoWolverin === 120) {
        console.log(
          `¡ATAQUE CRÍTICO DE ${wolverin[0].nombre}! ${deadPool[0].nombre} pierde su próximo turno.`
        );
        pierdeturnoDeadPool = true; // Deadpool pierde el siguiente turno
        let vidaRegeneradaWolverin = wolverin[0].regeneracion(); // Wolverine se regenera
        console.log(
          `${wolverin[0].nombre} gana ${vidaRegeneradaWolverin} de recuperación. Vida de ${wolverin[0].nombre}: ${wolverin[0].vida}`
        );
      } else {
        if (deadPool[0].evasion()) {
          console.log("Deadpool a evadido el ataque");
        } else {
          deadPool[0].vida -= dañoWolverin;
          console.log(
            `DeadPool recibe ${dañoWolverin} daño. Vide de DeadPool ${deadPool[0].vida}`
          );
        }
      }
    }
    }

    if (deadPool[0].vida < 0) {
      console.log(`DeadPool ha sido derrotado!`);
      break; // Salimos del bucle si Wolverin muere
    }

    turno++;
}
init()
  //-------------------------preguntas de vida-------------inicia funcion 
  
}

function init() {
    rl.question(
      "para comenzar La batalla asigna la vida de los  dead pool ",
      (respuesta1) => {
        deadPool[0].vida = respuesta1;
        rl.question("Asignar vida a Wolverin ", (respuesta) => {
          wolverin[0].vida = respuesta;
          batallaDvsW()
          respuesta !== "salir" ? batallaDvsW() : console.log("accion no permitida vuelve a intentar", init())
        });
      }
    );
  }

init();






  
 



//--------------------------------------------------------------wile metodo------------------------------------

