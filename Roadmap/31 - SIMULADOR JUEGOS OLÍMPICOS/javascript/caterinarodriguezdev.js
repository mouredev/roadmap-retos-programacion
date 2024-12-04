const { stdin, stdout } = require("process");
const readline = require("readline");
const rl = readline.createInterface(stdin, stdout);

const events = [];
const participantes = [];

console.log("¡Bienvenido a los JJOO!");

const menu = () => {
  console.log(`
    1. Registrar evento
    2. Registar participantes
    3. Simular Evento
    4. Creación de informe
    5. Salir del programa
    `);

  rl.question("Elija una opción -> ", (resp) => {
    switch (resp) {
      case "1":
        registerEvent();
        break;
      case "2":
        registerPlayer();
        break;
      case "3":
        startEvent();
        break;
      case "4":
        createReport();
        break;
      case "5":
        rl.close();
        break;
      default:
        console.log("Opción no válida");
        menu();
    }
  });
};

const registerEvent = () => {
  rl.question("Nombre del evento -> ", (resp) => {
    events.push(resp);
    console.log(`Evento ${resp} registrado con éxito`);
    menu();
  });
};

const registerPlayer = () => {
  rl.question("Nombre del participante -> ", (nombre) => {
    rl.question("País -> ", (pais) => {
      const participante = {
        nombre: nombre,
        pais: pais,
        eventos: {},
      };
      events.forEach((evento) => {
        participante.eventos[evento] = { puntuacion: 0, medalla: null };
      });
      participantes.push(participante);
      console.log(`Participante ${nombre} - ${pais} registrado con éxito`);
      menu();
    });
  });
};

const startEvent = () => {
  if (events.length === 0) {
    console.log("No hay eventos registrados");
    return menu();
  }
  console.log("Eventos disponibles:");
  events.forEach((e, index) => console.log(`${index + 1}. ${e}`));
  rl.question("¿Qué evento deseas simular? (Ingrese el número) -> ", (resp) => {
    const eventoIndex = parseInt(resp) - 1;
    if (eventoIndex >= 0 && eventoIndex < events.length) {
      const evento = events[eventoIndex];
      if (participantes.length >= 3) {
        console.log(`Simulando el evento: ${evento}`);
        participantes.forEach((p) => {
          p.eventos[evento].puntuacion = Math.floor(Math.random() * 10) + 1;
        });
        const participantesOrdenados = [...participantes].sort(
          (a, b) => b.eventos[evento].puntuacion - a.eventos[evento].puntuacion
        );

        ["Oro", "Plata", "Bronce"].forEach((medalla, index) => {
          if (participantesOrdenados[index]) {
            participantesOrdenados[index].eventos[evento].medalla = medalla;
            console.log(
              `El participante ${
                participantesOrdenados[index].nombre
              } ha ganado la medalla de ${medalla.toLowerCase()}!`
            );
          }
        });

        console.log("¡El evento ha finalizado!");
      } else {
        console.log("Debe haber mínimo 3 participantes");
      }
    } else {
      console.log("Evento no válido");
    }
    menu();
  });
};

const createReport = () => {
  events.forEach((event) => {
    console.log(`EVENTO ${event}`);
    participantes.forEach((p) => {
      if (p.eventos[event].medalla) {
        console.log(
          `El participante ${p.nombre} ha ganado la medalla de ${p.eventos[
            event
          ].medalla.toLowerCase()}`
        );
      }
    });
    console.log("\n");
  });

  const medallasPorPais = {};

  participantes.forEach((p) => {
    if (!medallasPorPais[p.pais]) {
      medallasPorPais[p.pais] = { oro: 0, plata: 0, bronce: 0, total: 0 };
    }
    Object.values(p.eventos).forEach((evento) => {
      if (evento.medalla) {
        medallasPorPais[p.pais][evento.medalla.toLowerCase()]++;
        medallasPorPais[p.pais].total++;
      }
    });
  });

  const rankingPaises = Object.entries(medallasPorPais)
    .map(([pais, medallas]) => ({ pais, ...medallas }))
    .sort((a, b) => {
      if (a.oro !== b.oro) return b.oro - a.oro;
      if (a.plata !== b.plata) return b.plata - a.plata;
      if (a.bronce !== b.bronce) return b.bronce - a.bronce;
      return b.total - a.total;
    });

  console.log("RANKING DE PAÍSES");
  rankingPaises.forEach((elemento, index) => {
    console.log(
      `${index + 1}. ${elemento.pais} - Oro: ${elemento.oro}, Plata: ${
        elemento.plata
      }, Bronce: ${elemento.bronce}, Total: ${elemento.total}`
    );
  });

  menu();
};

menu();
