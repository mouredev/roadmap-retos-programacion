import readline from "readline";
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

enum MedalEnum {
  gold = "gold",
  silver = "silver",
  bronze = "bronze",
}

interface IPlayer {
  id: number | undefined;
  name: string | undefined;
  country: string | undefined;
  event: IOlympics | undefined;
  medal: MedalEnum | undefined;
}

interface IOlympics {
  id: number | undefined;
  name: string | undefined;
}

class Olympics implements IOlympics {
  id: number | undefined;
  name: string | undefined;

  private listEventsWithPlayers: IOlympics[] = [];

  addEvents(data: IOlympics) {
    this.id = data.id;
    this.name = data.name;

    this.listEventsWithPlayers.push({
      id: this.id,
      name: this.name,
    });
  }
}

class Player implements IPlayer {
  id: number | undefined;
  name: string | undefined;
  country: string | undefined;
  event: IOlympics | undefined;
  medal: MedalEnum | undefined;

  private listPlayers: IPlayer[] = [];

  addListPlayers(data: IPlayer) {
    this.id = data.id;
    this.name = data.name;
    this.country = data.country;
    this.event = data.event;
    this.medal = data.medal;

    this.listPlayers.push({
      id: this.id,
      name: this.name,
      country: this.country,
      event: this.event,
      medal: this.medal,
    });
  }
}

const player = new Player();
const olympic = new Olympics();

function run() {
  console.log("\n");
  console.log("::::::::::::::::::::::::::::::::::::::::::::");
  console.log(":::::::INICIO DE LOS JUEGOS OLIMPICOS:::::::");
  console.log("::::::::::::::::::::::::::::::::::::::::::::");
  console.log("1. Registro de eventos.");
  console.log("2. Registro de participantes.");
  console.log("3. Simulación de eventos.");
  console.log("4. Creación de informes.");
  console.log("5. Salir del programa.");
  console.log("::::::::::::::::::::::::::::::::::::::::::::");
  console.log("::::::::::::::::::::::::::::::::::::::::::::");
  console.log("\n");

  let open = true;
  rl.question("Seleccione una opción: ", (option: string) => {
    while (open) {
      switch (parseInt(option)) {
        case 1:
          registerEvent();
          open = false;
          break;
        case 2:
          console.log("Option 2");
          open = false;
          break;
        case 3:
          console.log("Option 3");
          open = false;
          break;
        case 4:
          console.log("Option 4");
          open = false;

          break;
        case 5:
          message("Ha salido del sistema.");
          open = false;
          rl.close();
          break;
        default:
          message("***Opción incorrecta, intente de nuevo***");
          open = false;
          run();
      }
    }
  });
}

run();

function message(msg: string) {
  const arr = Array.from(msg);
  let border = "";

  arr.forEach((e) => {
    border += ":";
  });

  console.log(`\n${border}\n${msg}\n${border}\n`);
}

function registerEvent(addOther?: boolean) {
  rl.question(
    addOther
      ? "Ingrese otro evento o ingrese X para volver al menu \nNombre del evento: "
      : "Nombre del evento: ",
    (name: string) => {
      // add olympic
      if (name.toLocaleLowerCase() === "x".toLocaleLowerCase()) {
        run();
      } else {
        olympic.addEvents({
          id: Math.round(Math.random() * 100),
          name,
        });
        console.log(`Evento ${name} registrado exitosamente!!`);
        registerEvent(true);
      }
    }
  );
}
