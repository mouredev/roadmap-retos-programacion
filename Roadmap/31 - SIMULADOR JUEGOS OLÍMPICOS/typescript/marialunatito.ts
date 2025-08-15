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

  getEventById(eventId: number): IOlympics | undefined {
    return this.listEventsWithPlayers.find((e) => e.id == eventId);
  }

  getEvents(): IOlympics[] {
    return this.listEventsWithPlayers;
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

  randomMedal(): MedalEnum {
    const position = Math.round(Math.random() * 2);
    if (position === 0) return MedalEnum.gold;
    if (position === 1) return MedalEnum.silver;
    if (position === 2) return MedalEnum.bronze;
    return MedalEnum.gold;
  }

  getListPlayers(): IPlayer[] {
    return this.listPlayers;
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
          registerPlayers();
          open = false;
          break;
        case 3:
          simulateEvents();
          open = false;
          break;
        case 4:
          eventSummary();
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

function registerPlayers(addOther?: boolean) {
  rl.question(
    addOther
      ? "Ingrese otro jugador (Nombre) o ingrese X para volver al menu: "
      : "Ingrese nombre del jugador: ",
    (name: string) => {
      if (name.toLocaleLowerCase() === "x".toLocaleLowerCase()) {
        run();
      } else {
        rl.question("Ingrese país del jugador: ", (country: string) => {
          const events = olympic.getEvents();
          let message = "";

          events.forEach((event) => {
            message += `Id: ${event.id} - Evento: ${event.name}\n`;
          });

          rl.question(
            `Asigne el jugador a un evento,\n${message}\nIngrese el EventId: `,
            (eventId: string) => {
              const event = olympic.getEventById(parseInt(eventId));
              if (!event) throw new Error(`evento no encontrado`);
              // add playes
              player.addListPlayers({
                id: Math.round(Math.random() * 100),
                name,
                country,
                event,
                medal: player.randomMedal(),
              });

              console.log(
                "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
              );
              console.log(
                ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
              );
              console.log(
                `Player ${name} - ${country} - Evento: ${event?.name} registrado exitosamente!!`
              );
              console.log(
                "\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"
              );
              console.log(
                ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n"
              );
              registerPlayers(true);
            }
          );
        });
      }
    }
  );
}

function simulateEvents() {
  const players = player.getListPlayers();

  message("    EVENTOS    ");
  players.forEach((_player) => {
    console.log(
      `\nParticipante: ${_player.name}\nCountry: ${_player.country}\nEvento: ${
        _player.event?.name
      }\nMedalla: ${player.randomMedal()}\n`
    );
  });

  rl.question("\nVolver al menu (si o no): ", (response: string) => {
    if (response.toLocaleLowerCase() === "si".toLocaleLowerCase()) {
      run();
    } else {
      simulateEvents();
    }
  });
}

function eventSummary() {
  const players = player.getListPlayers();
  players.sort((a, b) => {
    const countryA = a.country ?? "";
    const countryB = b.country ?? "";

    return countryA.localeCompare(countryB);
  });

  console.log("players: ", players);

  let currenCountry = "";
  let count = 0;
  let medals = "";
  const result: { country: string; games: number; medals: string }[] = [];
  console.log("players length: ", players.length);
  players.forEach((player, i) => {
    console.log("index: ", i);
    if (!currenCountry) {
      currenCountry = player.country ?? "";
      medals = player.medal ?? "";
      count++;
    } else if (currenCountry === player.country) {
      medals += `, ${player.medal}`;
      count++;
    } else if (currenCountry !== player.country || i === players.length - 1) {
      console.log("entro?");
      result.push({
        country: currenCountry,
        games: count,
        medals,
      });
      medals = "";
      count = 0;

      // new country again
      currenCountry = player.country ?? "";
      medals = player.medal ?? "";
      count++;
    }
  });

  result.push({
    country: currenCountry,
    games: count,
    medals,
  });

  message("   Resumen de los JJOO   ");
  result.forEach((r) => {
    console.log(
      `\nCountry: ${r.country}\nJuegos Ganados: ${r.games}\nMedallas: ${r.medals}`
    );
  });

  rl.question("\nVolver al menu (si o no): ", (response: string) => {
    if (response.toLocaleLowerCase() === "si".toLocaleLowerCase()) {
      run();
    } else {
      simulateEvents();
    }
  });
}

// you can test this with next script
// npx ts-node  "Roadmap/31 - SIMULADOR JUEGOS OLÍMPICOS/typescript/marialunatito.ts"
