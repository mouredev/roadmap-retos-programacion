/**
 * Retosdeprogramacion #31 { retosparaprogramadores } - Simulador Juegos Olímpicos
 * 
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
 *  */

const log = console.log;

// Check if running in a browser environment
const isBrowser = typeof window !== 'undefined';

// Conditional check for browser environment
if (isBrowser) {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #31.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #31. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #31');
    });
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #31');
}

/**
 * Shuffles an array in place using the Fisher-Yates algorithm.
 * @param array - The array to shuffle.
 * @returns The shuffled array.
 */
function shuffleArray<T>(array: T[]): T[] {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

/**
 * Represents an Olympic event.
 */
class Events {
    public events: { [key: string]: Player[] };
    public prizes: Prizes;

    constructor() {
        this.events = {};
        this.prizes = new Prizes();
    }

    /**
     * Adds a new event to the registry.
     * @param event - The name of the event.
     */
    addEvent(event: string): void {
        if (this.events[event]) {
            log(`There's a ${event} event already registered.`);
        } else {
            this.events[event] = [];
            log(`Event ${event} registered.`);
        }
    }

    /**
     * Adds a player to a specific event.
     * @param player - The player to add.
     */
    addPlayer(player: Player): void {
        if (!this.events[player.event]) {
            log(`Event ${player.event} is not registered.`);
            return;
        }

        const isPlayer = this.events[player.event].find(p => p.name === player.name);
        if (!isPlayer) {
            this.events[player.event].push(player);
            log(`Player ${player.name} added to ${player.event} event.`);
        } else {
            log(`The player ${player.name} is already registered to ${player.event} event.`);
        }
    }

    /**
     * Randomizes the order of events.
     * @returns A shuffled list of events.
     */
    randomEvents(): string[] {
        const eventsList = Object.keys(this.events);
        return shuffleArray(eventsList);
    }

    /**
     * Displays participants for a specific event.
     * @param event - The event to display participants for.
     */
    showParticipantsForEvent(event: string): void {
        if (this.events[event]) {
            log(`Participants for ${event} event:`);
            this.events[event].forEach(p => log(`${p.name} from ${p.country}`));
        } else {
            log(`There's no participant registered for the ${event} event.`);
        }
    }

    /**
     * Displays all registered events and their participants.
     */
    showRegistryData(): void {
        for (const key in this.events) {
            log(`${key} event:`);
            this.events[key].forEach(element => {
                log(`${element.name} from ${element.country}`);
            });
        }
    }
}

/**
 * Represents a participant in an Olympic event.
 */
class Player {
    constructor(public name: string, public event: string, public country: string) {}
}

/**
 * Manages the awarding of medals and tracking of country medal counts.
 */
class Prizes {
    public gold: { [key: string]: Player[] };
    public silver: { [key: string]: Player[] };
    public bronze: { [key: string]: Player[] };
    public countryMedals: { [key: string]: { gold: number, silver: number, bronze: number } };

    constructor() {
        this.gold = {};
        this.silver = {};
        this.bronze = {};
        this.countryMedals = {};
    }

    /**
     * Awards a gold medal to a player.
     * @param player - The player to award the gold medal to.
     */
    addGold(player: Player): void {
        this.addPrize(player, 'gold');
    }

    /**
     * Awards a silver medal to a player.
     * @param player - The player to award the silver medal to.
     */
    addSilver(player: Player): void {
        this.addPrize(player, 'silver');
    }

    /**
     * Awards a bronze medal to a player.
     * @param player - The player to award the bronze medal to.
     */
    addBronze(player: Player): void {
        this.addPrize(player, 'bronze');
    }

    /**
     * Adds a prize to a player and updates the country's medal count.
     * @param player - The player to award the prize to.
     * @param type - The type of prize (gold, silver, bronze).
     */
    private addPrize(player: Player, type: 'gold' | 'silver' | 'bronze'): void {
        if (!this[type][player.event]) {
            this[type][player.event] = [];
        }
        if (!this[type][player.event].find(p => p.name === player.name)) {
            this[type][player.event].push(player);
            this.countCountryMedal(player.country, type);
        }
    }

    /**
     * Updates the medal count for a country.
     * @param country - The country to update.
     * @param type - The type of medal (gold, silver, bronze).
     */
    private countCountryMedal(country: string, type: 'gold' | 'silver' | 'bronze'): void {
        if (!this.countryMedals[country]) {
            this.countryMedals[country] = { gold: 0, silver: 0, bronze: 0 };
        }
        this.countryMedals[country][type]++;
    }

    /**
     * Displays the winners for each event.
     */
    showWinners(): void {
        log('Winners:');
        for (const event in this.gold) {
            log(`${event}: Gold - ${this.gold[event].map(p => p.name).join(', ')}`);
            log(`       Silver - ${this.silver[event] ? this.silver[event].map(p => p.name).join(', ') : 'None'}`);
            log(`       Bronze - ${this.bronze[event] ? this.bronze[event].map(p => p.name).join(', ') : 'None'}`);
        }
    }

    /**
     * Displays the medal count for each country.
     */
    showCountryMedals(): void {
        log('Country Medal Count:');
        for (const country in this.countryMedals) {
            log(`${country}: Gold - ${this.countryMedals[country].gold}, Silver - ${this.countryMedals[country].silver}, Bronze - ${this.countryMedals[country].bronze}`);
        }
    }
}

/**
 * Simulates the events and assigns medals to the winners.
 * @param events - The events to simulate.
 */
const eventSimulator = (events: Events): void => {
    for (const key in events.events) {
        if (events.events[key].length >= 3) {
            const winners = shuffleArray(events.events[key]);
            events.prizes.addGold(winners[0]);
            events.prizes.addSilver(winners[1]);
            events.prizes.addBronze(winners[2]);
        } else {
            log(`Not enough participants for ${key} event.`);
        }
    }
    events.prizes.showWinners();
}

// Dummy data for testing
const dummyData: [string, string, string][] = [
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

// Create a new instance of Events
const firstRound = new Events();

// Register Olympic events
const olympicEvents = ['Archery', 'Swimming', 'Weightlifting', '100m Sprint', '200m Freestyle', '3000m Steeplechase', 'Discus Throw'];
olympicEvents.forEach(event => firstRound.addEvent(event));

// Register participants from dummy data
dummyData.forEach(d => firstRound.addPlayer(new Player(d[0], d[1], d[2])));

// Display registered data
firstRound.showRegistryData();

// Simulate events and display winners
eventSimulator(firstRound);

/* Output: 
Retosparaprogramadores #31
Event Archery registered.
Event Swimming registered.
Event Weightlifting registered.
Event 100m Sprint registered.
Event 200m Freestyle registered.
Event 3000m Steeplechase registered.
Event Discus Throw registered.
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
Archery: Gold - Bob Marley
       Silver - Shihiro
       Bronze - Bugs Bunny
Swimming: Gold - Lenny Kravitz
       Silver - Ruby
       Bronze - Asterix
Weightlifting: Gold - Crows
       Silver - Lucky Luke
       Bronze - John Lennon
100m Sprint: Gold - Devian
       Silver - Jerry Maguire
       Bronze - Lorenna McKennit
200m Freestyle: Gold - Peque
       Silver - Alice
       Bronze - Atreyo
3000m Steeplechase: Gold - Che Guevara
       Silver - Sophy
       Bronze - Simón Bolívar
Discus Throw: Gold - Goku
       Silver - Buda
       Bronze - Beth
*/