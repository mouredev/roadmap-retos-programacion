/*
  EJERCICIO:
  ¡Los JJOO de París 2024 han comenzado!
  Crea un programa que simule la celebración de los juegos.
  El programa debe permitir al usuario registrar eventos y participantes,
  realizar la simulación de los eventos asignando posiciones de manera aleatoria
  y generar un informe final. Todo ello por terminal.
  Requisitos:
  1. Registrar eventos deportivos.
  2. Registrar participantes por nombre y país.
  3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
  4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
  5. Mostrar los ganadores por cada evento.
  6. Mostrar el ranking de países según el número de medallas.
  Acciones:
  1. Registro de eventos.
  2. Registro de participantes.
  3. Simulación de eventos.
  4. Creación de informes.
  5. Salir del programa.
*/

let selectedOption = 0;
const options = `Por favor, selecciona una opción:
  1. Registrar eventos deportivos y participantes por nombre y país.
  2. Mostrar el ranking de países.
  3. Salir del programa.`;
const olympicGames = [];

function showPositions() {
  console.log("+++++++++ RESULTADOS POR EVENTO +++++++++");

  let sortByEvent = olympicGames.reduce((accumulator, currentValue) => {
    accumulator[currentValue.event] = accumulator[currentValue.event] || [];
    accumulator[currentValue.event].push(currentValue);

    return accumulator;
  }, []);

  for (const key in sortByEvent) {
    const eachEvent = sortByEvent[key];
    let setNumbers = new Set();
    let numberOfAthletes = eachEvent.length;

    console.log(`\n${eachEvent[0].event}`);

    if (numberOfAthletes > 2) {
      while(setNumbers.size !== numberOfAthletes) {
        setNumbers.add(Math.floor(Math.random() * numberOfAthletes) + 1);
      }

      let aleatoryPositions = Array.from(setNumbers);

      for (let index = 0; index < eachEvent.length; index++) {
        const athletePerEvent = eachEvent[index];
        athletePerEvent.position = aleatoryPositions[index];

        if (athletePerEvent.position === 1) {
          athletePerEvent.medal = "Oro";
        } else if (athletePerEvent.position === 2) {
          athletePerEvent.medal = "Plata";
        } else if (athletePerEvent.position === 3) {
          athletePerEvent.medal = "Bronce";
        }
      }

      eachEvent.sort((a, b) => a.position - b.position);

      for (const finalPosition of eachEvent) {
        console.log(`Nombre: ${finalPosition.name} | País: ${finalPosition.country} | Posición: ${finalPosition.position} ${finalPosition.medal !== undefined ? '- ' + finalPosition.medal : ''}`);
      }
    } else {
      console.log(`Mínimo, deben participar 3 atletas en ${eachEvent[0].event}`);
    }
  }
}

function medalTable() {
  let medalTableByCountry = [];
  let sortByCountry = olympicGames.reduce((accumulator, currentValue) => {
    accumulator[currentValue.country] = accumulator[currentValue.country] || [];

    if (currentValue.medal !== undefined) {
      accumulator[currentValue.country].push(currentValue.medal);
    }

    return accumulator;
  }, []);

  for (const key in sortByCountry) {
    const eachCountry = sortByCountry[key];
    const eachCountryMedals = eachCountry.length;

    medalTableByCountry.push({country: key, medals: eachCountryMedals});
  }

  console.log("\n+++++++++ MEDALLERO OLÍMPICO +++++++++");

  medalTableByCountry.sort((a, b) => b.medals - a.medals);

  for (let countryIndex = 0; countryIndex < medalTableByCountry.length; countryIndex++) {
    const position = medalTableByCountry[countryIndex];

    console.log(`${countryIndex + 1}. ${position.country} | Medallas: ${position.medals}`);
  }
}

do {
  selectedOption = parseInt(prompt(options));

  switch (selectedOption) {
    case 1:
      const event = prompt("Registra el evento deportivo:");
      const athleteName = prompt("Registra el nombre del atleta:");
      const athleteCountry = prompt("Registra el país del atleta:");

      olympicGames.push({event: event, name: athleteName, country: athleteCountry});
      break;

    case 2:
      alert("Visualiza el medallero en la consola del navegador.");

      showPositions();
      medalTable();
      break;

    case 3:
      alert("Saliendo del programa...");
      break;

    default:
      alert("Debes seleccionar una de las opciones disponibles.");
      break;
  }
} while (selectedOption !== 3);
