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
}
