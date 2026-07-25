    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    class Participant {
        constructor(nombre, pais, evento){
            this.nombre = nombre;
            this.pais   = pais;
            this.evento = evento;
            this.medal  = "";
        }
    }

    class OlympicsGames {

        constructor(){
            this.participants = [];
            this.events       = [];
            this.countries    = [];
        }

        registrationEvents(){
            rl.question("|* Nombre del evento: ", (newNameEvent) => {
                let nameEvent = {nombre: newNameEvent, winners: []};
                this.events.push(nameEvent);
                console.log(`|== Se ha registrado el evento ${newNameEvent} correctamente`);
                console.log("|== Estos son todos tus eventos actuales: ");
                this.events.forEach((e, i) => console.log(`|${i + 1}.- ${e.nombre}`));
                this.showMessage();
            });
        }

        registrationParticipants(){
            if(this.events.length >= 1){
                let nombre = "";
                let pais   = "";
                let evento = "";
                rl.question("|* Nombre del participante: ", (nombreParticipant) => {
                    nombre = nombreParticipant;
                    rl.question("|* País del participante: ", (paisParticipant) => {
                        pais = paisParticipant;
                        rl.question("|* Nombre del evento: ", (nombreEvento) => {
                            this.events.forEach(e => evento = e.nombre === nombreEvento ? nombreEvento : "");
                            if(evento !== ""){
                                let participant = new Participant(nombre, pais, evento);
                                this.participants.push(participant);
                                this.countries.push(paisParticipant);
                                console.log(`|== Se ha registrado al participante ${nombre} correctamente`);
                                this.participants.forEach((p, i) => console.log(`|${i + 1}.- ${p.nombre}`));
                                this.showMessage();
                            } else {
                                console.log("|== No se encontro el evento, intentalo de nuevo");
                                this.registrationParticipants();
                            }
                        });
                    });
                });
    
            } else {
                console.log("=== No existe un evento para registrar al participante, intente de nuevo ===");
                this.showMessage();
            }
        }
        
        simulateEvents(){
            if(this.events.length <= 0){
                console.log("|== No existen eventos disponibles para simular");
            } else {
                console.log("|== Eventos que puedes simular");
                this.events.forEach((e, i) => console.log(`|${i + 1}.- ${e.nombre}`));
                rl.question("|* Selecciona una de las opciones: ", (accion) => {
                    let count = 0;
                    this.participants.forEach((participant) => {
                        if(participant.evento == this.events[accion - 1].nombre){
                            count++;
                        }
                    });
                    if(count >= 3){
                        console.log("|== Simulando...");
                        setTimeout(() => {
                            let position1 = parseInt(Math.random() * this.participants.length);
                            let position2 = parseInt(Math.random() * this.participants.length);
                            let position3 = parseInt(Math.random() * this.participants.length);
                            while(position1 === position2 || position1 == position3 || position2 == position3){
                                position1 = parseInt(Math.random() * this.participants.length);
                                position2 = parseInt(Math.random() * this.participants.length);
                                position3 = parseInt(Math.random() * this.participants.length);
                            }

                            console.log(`----- Tabla de ganadores del evento ${this.events[accion - 1].nombre} -----`);
                            console.log(`|1. ${this.participants[position1].nombre} (Oro)`);
                            console.log(`|2. ${this.participants[position2].nombre} (Plata)`);
                            console.log(`|3. ${this.participants[position3].nombre} (Bronce)`);
                            this.participants[position1].medal = "oro";
                            this.participants[position2].medal = "plata";
                            this.participants[position3].medal = "bronce";
                            this.events.find(index => index.nombre == this.events[accion - 1].nombre).winners.push(this.participants[position1]);
                            this.events.find(index => index.nombre == this.events[accion - 1].nombre).winners.push(this.participants[position2]);
                            this.events.find(index => index.nombre == this.events[accion - 1].nombre).winners.push(this.participants[position3]);
                            this.showMessage();
                        }, "1000");
                        
                    } else {
                        console.log("|== ¡ERROR! El evento no tiene minimo 3 participantes o no existe");
                        this.showMessage();
                    }
                });
            }
        }

        createData(){
            console.log("|----- Creación de informes -----");
            console.log("|1. Ganadores por evento");
            console.log("|2. Ranking de paises");
            rl.question("|* Selecciona una opcion: ", (op) =>{
                switch(op){
                    case '1':
                        this.rankingEvent();
                        break;
                    case '2':
                        this.rankingCountry();
                        break;
                    default:
                        console.log("|== Acción no permitida, intentelo de nuevo");
                        this.createData();
                }
            });
        }

        rankingCountry(){
            let countriesAndMelds = [];
            this.participants.forEach(participant => {
                let medalla = participant.medal;
                let score   = 0;
                let oro     = 0;
                let plata   = 0;
                let bronce  = 0;
                if(medalla == "oro"){
                    score = 3;
                    oro++;
                } else if(medalla == "plata"){
                    score = 2;
                    plata++;
                } else if(medalla == "bronce"){
                    score = 1;
                    bronce++;
                } 

                if(countriesAndMelds.includes(countriesAndMelds.find(index => index.nombre == participant.pais))){
                    countriesAndMelds.find(index => index.nombre == participant.pais).score += score;
                    countriesAndMelds.find(index => index.nombre == participant.pais).oro += oro;
                    countriesAndMelds.find(index => index.nombre == participant.pais).plata += plata;
                    countriesAndMelds.find(index => index.nombre == participant.pais).bronce += bronce;
                } else {
                    countriesAndMelds.push({nombre: participant.pais, score: score, oro: oro, plata: plata, bronce: bronce});
                }
            });

            countriesAndMelds.sort((a,b) => {
                if(a.score > b.score){
                    return -1;
                } else if(a.score < b.score){
                    return 1;
                } else {
                    return 0;
                }
            });

            console.log("|----- Ranking por país -----");
            countriesAndMelds.forEach((countryAndMedal, index) => {
                console.log(`|${index + 1}.  ${countryAndMedal.nombre}  Oro: ${countryAndMedal.oro}, Plata: ${countryAndMedal.plata}, Bronce: ${countryAndMedal.bronce}`);
            });
            this.showMessage();
        }

        rankingEvent(){
            console.log("|----- Ranking por Evento -----");
            this.events.forEach(e => {
                console.log(`|${e.nombre}`);
                e.winners.forEach((winner, index) => console.log(`|${index + 1}. ${winner.nombre}`))
            });
            this.showMessage();
        }

        showMessage(){
            let message = "|Acciones que puedes realizar:\n|1. Registro de eventos\n|2. Registro de participantes\n|3. Simulación de eventos\n|4. Creación de informes\n|5. Salir del programa";
            console.log("|-----------------------------------------------------");
            console.log(message.trim());
            rl.question("|Selecciona una de las opciones: ", (accion) => {
                switch(accion){
                    case '1':
                        this.registrationEvents();
                        break;
                    case '2':
                        this.registrationParticipants();
                        break;
                    case '3':
                        this.simulateEvents();
                        break;
                    case '4':
                        this.createData();
                        break;
                    case '5':
                        console.log("|Cerrando programa...");
                        rl.close();
                        break;
                    default:
                        console.log("|Acción no permitida, intentelo de nuevo");
                        this.showMessage();
                }
            });
        }
    }

    olympic = new OlympicsGames();
    olympic.showMessage();
