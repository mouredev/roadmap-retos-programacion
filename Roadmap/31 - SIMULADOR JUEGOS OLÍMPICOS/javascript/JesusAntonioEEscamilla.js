/** #31 - JavaScript -> Jesus Antonio Escamilla */

/**
 * SIMULADOR JUEGOS OLÍMPICOS
 * Utilizando la Terminal para pedir datos y agregarlos.
 */

const readline = require('readline');

const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
});

class Participant{
   constructor(nombre, pais) {
      this.nombre = nombre;
      this.pais = pais;
   }

   equals(other){
      if (other instanceof Participant) {
         return this.nombre === other.nombre && this.pais === other.pais;
      }
      return false;
   }

   hashCode(){
      return `${this.nombre}-${this.pais}`.hashCode();
   }
}

class Olympics {
   constructor() {
      this.events = [];
      this.participants = {};
      this.eventResults = {};
      this.paisResults = {};
   }

   registerEvent(callback) {
      rl.question("Introduce el nombre del evento deportivo: ", (event) => {
         event = event.trim();

         if (this.events.includes(event)) {
            console.log(`El evento ${event} ya está registrado.`);
         } else {
            this.events.push(event);
            console.log(`Evento ${event} registrado correctamente.`);
         }

         callback();
      });
   }

   registerParticipant(callback) {
      if (this.events.length === 0) {
         console.log("No hay eventos registrados. Por favor, registra uno primero.");
         callback();
         return;
      }

      rl.question("Introduce el nombre del participante: ", (nombre) => {
         rl.question("Introduce el país del participante: ", (pais) => {
            const participant = new Participant(nombre.trim(), pais.trim());

            console.log("Eventos deportivos disponibles:");
            this.events.forEach((event, index) => {
               console.log(`${index + 1}. ${event}`);
            })

            rl.question("Selecciona el número del evento para asignar al participante: ", (eventChoice) => {
               eventChoice = parseInt(eventChoice) - 1;

                  if (eventChoice >= 0 && eventChoice < this.events.length) {
                     const event = this.events[eventChoice];

                     if (this.participants[event] && this.participants[event].some(p => p.equals(participant))) {
                        console.log(`El participante ${nombre} de ${pais} ya está registrado en el evento deportivo ${event}.`);
                     } else {
                        if (!this.participants[event]) {
                           this.participants[event] = [];
                        }

                        this.participants[event].push(participant);
                        console.log(`El participante ${nombre} de ${pais} se ha registrado en el evento deportivo ${event}.`);
                     }
                  } else {
                     console.log("Selección de evento deportivo inválido. El participante no se ha registrado.");
                  }
               callback();
            });
         });
      });
   }

   simulateEvents(callback) {
      if (this.events.length === 0) {
         console.log("No hay eventos registrados. Por favor, registra uno primero.");
         callback();
         return;
      }

      this.events.forEach(event => {
         if (!this.participants[event] || this.participants[event].length < 3) {
            console.log(`No hay participantes suficientes para simular el evento ${event} (mínimo 3).`);
            return;
         }

         const eventParticipants = [...this.participants[event]];
         const shuffledParticipants = this.shuffleArray(eventParticipants).slice(0, 3);

         const [gold, silver, bronze] = shuffledParticipants;
         this.eventResults[event] = [gold, silver, bronze];

         this.updateCountryResults(gold.pais, "gold");
         this.updateCountryResults(silver.pais, "silver");
         this.updateCountryResults(bronze.pais, "bronze");

         console.log(`Resultados simulación del evento: ${event}`);
         console.log(`Oro: ${gold.nombre} (${gold.pais})`);
         console.log(`Plata: ${silver.nombre} (${silver.pais})`);
         console.log(`Bronce: ${bronze.nombre} (${bronze.pais})`);
      });

      callback();
   }

   shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
           const j = Math.floor(Math.random() * (i + 1));
         [array[i], array[j]] = [array[j], array[i]];
      }
      return array;
   }

   updateCountryResults(pais, medal) {
      if (!this.paisResults[pais]) {
         this.paisResults[pais] = { gold: 0, silver: 0, bronze: 0 };
      }
      this.paisResults[pais][medal] += 1;
   }

   showReport(callback) {
      console.log("Informe Juegos Olímpicos:");

      if (Object.keys(this.eventResults).length > 0) {
         console.log("Informe por evento:");

         for (const [event, winners] of Object.entries(this.eventResults)) {
            console.log(`Evento: ${event}`);
            console.log(`Oro: ${winners[0].nombre} (${winners[0].pais})`);
            console.log(`Plata: ${winners[1].nombre} (${winners[1].pais})`);
            console.log(`Bronce: ${winners[2].nombre} (${winners[2].pais})`);
         }
      } else {
         console.log("No hay resultados registrados.");
      }

      console.log();

      if (Object.keys(this.paisResults).length > 0) {
         console.log("Informe por país:");

         const sortedCountries = Object.entries(this.paisResults).sort((a, b) => {
            const [paisA, medalsA] = a;
            const [paisB, medalsB] = b;
            return medalsB.gold - medalsA.gold || medalsB.silver - medalsA.silver || medalsB.bronze - medalsA.bronze;
         });

         for (const [pais, medals] of sortedCountries) {
            console.log(`${pais}: Oro ${medals.gold}, Plata ${medals.silver}, Bronce ${medals.bronze}`);
         }
      } else {
         console.log("No hay medallas por país registradas.");
      }

      callback();
   }
}

olympic = new Olympics()

function mostrarMenu(){
   console.log("\nSimulador de Juegos Olímpicos\n");
   console.log(`
      1. Registro de eventos.
      2. Registro de participantes.
      3. Simulación de eventos.
      4. Creación de informes.
      5. Salir.
      `);
      
      rl.question('Selecciona una opción: ', (option) => {
         switch (option) {
            case "1":
               olympic.registerEvent(mostrarMenu)
               break;
      
            case "2":
               olympic.registerParticipant(mostrarMenu)
               break;
      
            case "3":
               olympic.simulateEvents(mostrarMenu)
               break;
      
            case "4":
               olympic.showReport(mostrarMenu)
               break;
      
            case "5":
               console.log("Saliendo del programa.....");
               rl.close();
               break;
         
            default:
               console.log("Opción invalida. Por favor, seleccione una nueva");
               mostrarMenu();
         }
      });
}

mostrarMenu()