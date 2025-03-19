//#31 - Simulador Juegos Olímpicos
/*
 * EJERCICIO:
 * ¡Los JJOO de París 2024 han comenzado!
 * Crea un programa que simule la celebración de los juegos.
 * El programa debe permitir al usuario registrar eventos y participantes,
 * realizar la simulación de los eventos asignando posiciones de manera aleatoria
 * y generar un informe final. Todo ello por terminal.
 * Requisitos:
 * 1. Registrar eventos deportivos.
 * 2. Registrar participantes por nombre y país.
 * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3).
 * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.
 * 5. Mostrar los ganadores por cada evento.
 * 6. Mostrar el ranking de países según el número de medallas.
 * Acciones:
 * 1. Registro de eventos.
 * 2. Registro de participantes.
 * 3. Simulación de eventos.
 * 4. Creación de informes.
 * 5. Salir del programa.
 */

let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #31.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #31. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #31'); 
});

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

class Events {
    constructor() {
        this.events = {};
        this.prizes = new Prizes();
    }

    addEvent(event) {
        if (this.events[event]) {
            log(`There's a ${event} event already registered.`);
        } else {
            this.events[event] = [];
            log(`Event ${event} registered.`);
        }
    }

    addPlayer(player) {
        if (!this.events[player.event]) {
            log(`Event ${player.event} is not registered.`);
            return;
        }

        let isPlayer = this.events[player.event].find(p => p.name === player.name);
        if (!isPlayer) {
            this.events[player.event].push(player);
            log(`Player ${player.name} added to ${player.event} event.`);
        } else {
            log(`The player ${player.name} is already registered to ${player.event} event.`);
        }
    }

    randomEvents() {
        let eventsList = Object.keys(this.events);
        return shuffleArray(eventsList);
    }

    showParticipantsForEvent(event) {
        if (this.events[event]) {
            log(`Participants for ${event} event:`);
            this.events[event].forEach(p => log(`${p.name} from ${p.country}`));
        } else {
            log(`There's no participant registered for the ${event} event.`);
        }
    }

    showRegistryData() {
        for (let key in this.events) {
            log(`${key} event:`);
            this.events[key].forEach(element => {
                log(`${element.name} from ${element.country}`);
            });
        }
    }
}

class Player {
    constructor(name, event, country) {
        this.name = name;
        this.country = country;
        this.event = event;
    }
}

class Prizes {
    constructor() {
        this.gold = {};
        this.silver = {};
        this.bronze = {};
        this.countryMedals = {};
    }

    addGold(player) {
        this.addPrize(player, 'gold');
    }

    addSilver(player) {
        this.addPrize(player, 'silver');
    }

    addBronze(player) {
        this.addPrize(player, 'bronze');
    }

    addPrize(player, type) {
        if (!this[type][player.event]) {
            this[type][player.event] = [];
        }
        if (!this[type][player.event].find(p => p.name === player.name)) {
            this[type][player.event].push(player);
            this.countCountryMedal(player.country, type);
        }
    }

    countCountryMedal(country, type) {
        if (!this.countryMedals[country]) {
            this.countryMedals[country] = { gold: 0, silver: 0, bronze: 0 };
        }
        this.countryMedals[country][type]++;
    }

    showWinners() {
        log('Winners:');
        for (let event in this.gold) {
            log(`${event}: Gold - ${this.gold[event].map(p => p.name).join(', ')}`);
            log(`       Silver - ${this.silver[event] ? this.silver[event].map(p => p.name).join(', ') : 'None'}`);
            log(`       Bronze - ${this.bronze[event] ? this.bronze[event].map(p => p.name).join(', ') : 'None'}`);
        }
    }

    showCountryMedals() {
        log('Country Medal Count:');
        for (let country in this.countryMedals) {
            log(`${country}: Gold - ${this.countryMedals[country].gold}, Silver - ${this.countryMedals[country].silver}, Bronze - ${this.countryMedals[country].bronze}`);
        }
    }
}

const eventSimulator = (events) => {
    for (let key in events.events) {
        if (events.events[key].length >= 3) {
            let winners = shuffleArray(events.events[key]);
            events.prizes.addGold(winners[0]);
            events.prizes.addSilver(winners[1]);
            events.prizes.addBronze(winners[2]);
        } else {
            log(`Not enough participants for ${key} event.`);
        }
    }
    events.prizes.showWinners();
}

let dummyData = [
    ['Bob Marley', 'Archery', 'Jamaica'],
    ['Lenny Kravitz', 'Swimming', 'USA'],
    ['John Lennon', 'Weightlifting', 'England'],
    ['Lorenna McKennit', '100m Sprint', 'Somewhere in Europe'],
    ['Alice', '200m Freestyle', 'The Rabbit Hole'],
    ['Che Guevara', '3000m Steeplechase', 'Argentina'],
    ['Buda', 'Discus Throw', 'India'],
    ['Bugs Bunny', 'Archery', 'Disney'],
    ['Asterix', 'Swimming', 'Comics'],
    ['Lucky Luke', 'Weightlifting', 'Comics'],
    ['Jerry Maguire', '100m Sprint', 'Comics'],
    ['Atreyo', '200m Freestyle', 'Book'],
    ['Simón Bolívar', '3000m Steeplechase', 'Venezuela'],
    ['Goku', 'Discus Throw', 'Anime'],
    ['Shihiro', 'Archery', 'Anime'],
    ['Ruby', 'Swimming', 'Book'],
    ['Crows', 'Weightlifting', 'Book'],
    ['Devian', '100m Sprint', 'Book'],
    ['Peque', '200m Freestyle', 'My World'],
    ['Sophy', '3000m Steeplechase', 'My World'],
    ['Beth', 'Discus Throw', 'My World']
];


let firstRound = new Events();

const olympicEvents = ['Archery', 'Swimming', 'Weightlifting', '100m Sprint', '200m Freestyle', '3000m Steeplechase', 'Discus Throw'].forEach(event => firstRound.addEvent(event));

dummyData.forEach(d => firstRound.addPlayer(new Player(d[0], d[1], d[2])));

firstRound.showRegistryData();

eventSimulator(firstRound);

/* Possible Output: 

                 Register events
                 Updated list of events
 
 Event Archery registered.
 Event Swimming registered.
 Event Weightlifting registered.
 Event 100m Sprint registered.
 Event 200m Freestyle registered.
 Event 3000m Steeplechase registered.
 Event Discus Throw registered.

                 Register players

Player Bob Marley added to Archery event.
Player Lenny Kravitz added to Swimming event.
Player John Lennon added to Weightlifting event.
Player Lorenna McKennit added to 100m Sprint event.
Player Alice added to 200m Freestyle event.
Player Che Guevara added to 3000m Steeplechase event.
Player Buda added to Discus Throw event.
Player Bugs Bunny added to Archery event.
Player Asterix added to Swimming event.
Player Lucky Luke added to Weightlifting event.
Player Jerry Maguire added to 100m Sprint event.
Player Atreyo added to 200m Freestyle event.
Player Simón Bolívar added to 3000m Steeplechase event.
Player Goku added to Discus Throw event.
Player Shihiro added to Archery event.
Player Ruby added to Swimming event.
Player Crows added to Weightlifting event.
Player Devian added to 100m Sprint event.
Player Peque added to 200m Freestyle event.
Player Sophy added to 3000m Steeplechase event.
Player Beth added to Discus Throw event.     

                    Show registered data

                    Simulate events
Archery event:
 Bob Marley from Jamaica
 Bugs Bunny from Disney
 Shihiro from Anime
 Swimming event:
 Lenny Kravitz from USA
 Asterix from Comics
 Ruby from Book
 Weightlifting event:
 John Lennon from England
 Lucky Luke from Comics
 Crows from Book
 100m Sprint event:
 Lorenna McKennit from Somewhere in Europe
 Jerry Maguire from Comics
 Devian from Book
 200m Freestyle event:
 Alice from The Rabbit Hole
 Atreyo from Book
 Peque from My World
 3000m Steeplechase event:
 Che Guevara from Argentina
 Simón Bolívar from Venezuela
 Sophy from My World
 Discus Throw event:
 Buda from India
 Goku from Anime
 Beth from My World
Winners:
 Archery: Gold - Shihiro
          Silver - Bob Marley
          Bronze - Bugs Bunny
 Swimming: Gold - Lenny Kravitz
           Silver - Ruby
           Bronze - Asterix
 Weightlifting: Gold - Crows
                Silver - John Lennon
                Bronze - Lucky Luke
 100m Sprint: Gold - Jerry Maguire
              Silver - Lorenna McKennit
              Bronze - Devian
 200m Freestyle: Gold - Peque
                 Silver - Alice
                 Bronze - Atreyo
 3000m Steeplechase: Gold - Simón Bolívar
                     Silver - Sophy
                     Bronze - Che Guevara
 Discus Throw: Gold - Goku
               Silver - Buda
               Bronze - Beth                    
*/
