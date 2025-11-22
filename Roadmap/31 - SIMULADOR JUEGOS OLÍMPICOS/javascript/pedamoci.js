import  readline  from "readline"

function shuffled(array) {
  const result = [...array];
  for (let i = result.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [result[i], result[j]] = [result[j], result[i]];
  }
  return result;
}

function getMedalCounts(m) {
  return {
    Gold: Number(m.Gold ?? 0),
    Silver: Number(m.Silver ?? 0),
    Bronze: Number(m.Bronze ?? 0)
  };
}

function sortRanking(rankingObj) {
  return Object.entries(rankingObj)
    .map(([Country, medals]) => {
      const { Gold, Silver, Bronze } = getMedalCounts(medals);
      return { Country, Gold, Silver, Bronze };
    })
    .sort((a, b) =>
      (b.Gold - a.Gold) || (b.Silver - a.Silver) || (b.Bronze - a.Bronze)
    );
}

class Event {
  constructor() {
    this.events = []
    this.participants = {}
    this.results = {}
  }

  addEvent(nameEvent) {
    if (!this.events.includes(nameEvent)) {
      this.events.push(nameEvent)
      this.participants[nameEvent] = []
      console.log("The event has been created")
    } else console.warn("Event already exist")
  }

  addParticipant(nameEvent, idParticipant) {
    if (!this.participants[nameEvent].includes(idParticipant)) {
      this.participants[nameEvent].push(idParticipant)
    } else console.warn("Participant already added to the event")
  }

  addResults(nameEvent, idParticipants) {
    this.results[nameEvent] = idParticipants
  }
}

class Participant {
  constructor() {
    this.participants = {}
  }

  addParticipant(id, name, country) {
    if (!this.participants[id]) {
      this.participants[id] = {'name': name, 'country': country}
      console.log("The participant has been added")
    } else console.warn("Participant already exist")
    
  }
}

class CountryMedals {
  constructor() {
    this.countryMedals = {}
  }

  addCountry(nameCountry) {
    if (!this.countryMedals[nameCountry]) {
      this.countryMedals[nameCountry] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    }
  }

  addMedal(nameCountry, typeMedal) {
    if (!!this.countryMedals[nameCountry]) {
      this.countryMedals[nameCountry][typeMedal] += 1
    } else console.warn("The country has not been added")
  }
}

class OlimpicsManager {
  constructor() {
    this.events = new Event()
    this.participants = new Participant()
    this.medals = new CountryMedals()
  }

  addEvent(nameEvent) {
    this.events.addEvent(nameEvent)
  }

  addParticipant(idParticipant, name, country) {
    this.participants.addParticipant(idParticipant, name, country)
    this.medals.addCountry(country)
  }

  addParticipantToEvent(nameEvent, idParticipant) {
    this.events.addParticipant(nameEvent, idParticipant)
  }

  simulateEvent(nameEvent) {
    if (!this.events.events.includes(nameEvent)) {console.warn("The event has not been created"); return}
    if (!!this.events.results[nameEvent]) {console.warn("The event has already been simulated"); return}

    const participants = this.events.participants[nameEvent]

    if (participants.length < 3) {console.warn("Three participants are needed to simulate this event"); return}

    let results = shuffled(participants)

    this.events.addResults(nameEvent, results)

    const podium = results.slice(0, 3)

    this.medals.addMedal(this.participants.participants[podium[0]].country, 'Gold')
    this.medals.addMedal(this.participants.participants[podium[1]].country, 'Silver')
    this.medals.addMedal(this.participants.participants[podium[2]].country, 'Bronze')

    console.log("The simulation of the event has ended")
  }

  printResultsEvent(nameEvent) {
    if (!this.events.results[nameEvent]) {console.warn("The event has not been simulated"); return}

    const participants = [...this.events.results[nameEvent]]

    for (let i = 0; i < participants.length; i++) {
      console.log(`${i + 1}° Puesto: ${this.participants.participants[participants[i]].name}`)
    }
  }

  printRankig() {
    console.table(sortRanking(this.medals.countryMedals))
  }
}

class Validation {
  constructor() {
    this.regexId = /^\w+$/
    this.regexEvent = /^\w+(\.?\s?\w+)+$/
    this.regexNames = /^\p{L}+(?:\s\p{L}+)*$/u
  }

  validateId(id) {
    if (!this.regexId.test(id)) {
      console.warn("The participant ID is incorrect")
    } return true
  }

  validateNameParticipant(nameParticipant) {
    if (!this.regexNames.test(nameParticipant)) {
      console.warn("The participant's name is incorrect")
    } return true
  }

  validateCountry(country) {
    if (!this.regexNames.test(country)) {
      console.warn("The name of the country is incorrect")
    } return true
  }

  validateEvent(event) {
    if (!this.regexEvent.test(event)) {
      console.warn("The name of the event is incorrect")
    } return true
  }
}

class Asks {
  constructor() {
    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  ask(question) {
    return new Promise((resolve) => {
      this.rl.question(question, (answer) => resolve(answer));
    });
  }

  close() {
    this.rl.close();
  }
}

const asks = new Asks()

async function startOlimpics() {
  const olimpicsManager = new OlimpicsManager()
  const validation = new Validation()

  let operation = ""

  while (operation.toUpperCase() !== 'E') {
    operation = (await asks.ask(
      'What operation would you like to perform?\n' + 
      'AE --> Add event\n' +
      'SE --> Simulate event\n' +
      'AP --> Add participant\n' +
      'RE --> View event classification\n' +
      'VR --> See country rankings\n' +
      'E --> Exit\n'
    )).toUpperCase()

    let event = ""; let id = ""; let participant = ""; let country = ""
  
    switch (operation) {
      case 'AE':
        event = await asks.ask("Enter the name of the event: ")
        if (validation.validateEvent(event)) 
          olimpicsManager.addEvent(event)
        break;
  
      case 'SE':
        event = await asks.ask("Enter the name of the event: ")
        if (validation.validateEvent(event)) 
          olimpicsManager.simulateEvent(event)
        break;
  
      case 'AP':
        participant = await asks.ask("Enter the participant's name: ")
        id = await asks.ask("Enter the participant ID: ")
        country = await asks.ask("Enter the name of the country: ")
        event = await asks.ask("Enter the name of the event: ")
  
        if (
          validation.validateNameParticipant(participant) &&
          validation.validateId(id) &&
          validation.validateCountry(country) &&
          validation.validateEvent(event)
        ) {
          olimpicsManager.addParticipant(id, participant, country)
          olimpicsManager.addParticipantToEvent(event, id)
        }
        break;
  
      case 'RE':
        event = await asks.ask("Enter the name of the event: ")
        if (validation.validateEvent(event)) 
          olimpicsManager.printResultsEvent(event)
        break;
  
      case 'VR':
        olimpicsManager.printRankig()
        break;
    
      default:break;
    }
  }

  asks.close()
}
startOlimpics()