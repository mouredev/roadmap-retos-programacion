// EJERCICIO:
//  * ¡Los JJOO de París 2024 han comenzado!
//  * Crea un programa que simule la celebración de los juegos.
//  * El programa debe permitir al usuario registrar eventos y participantes,
//  * realizar la simulación de los eventos asignando posiciones de manera aleatoria
//  * y generar un informe final. Todo ello por terminal.
//  * Requisitos:
//  * 1. Registrar eventos deportivos. listo
//  * 2. Registrar participantes por nombre y país. Listo
//  * 3. Simular eventos de manera aleatoria en base a los participantes (mínimo 3). listo 
//  * 4. Asignar medallas (oro, plata y bronce) basándose en el resultado del evento.listo + sin medalla
//  * 5. Mostrar los ganadores por cada evento. listo
//  * 6. Mostrar el ranking de países según el número de medallas.
//  * Acciones:
//  * 1. Registro de eventos.
//  * 2. Registro de participantes.
//  * 3. Simulación de eventos.
//  * 4. Creación de informes.
//  * 5. Salir del programa.

const readline = require('readline');
 const rl = readline.createInterface({
        input: process.stdin, // For user input from the console
        output: process.stdout // For displaying output to the console
    });

    

function CelebracionDeLosJuegosOlimpicos () {

    const participantes = [
        {nombre: "David",pais: "Mexico"},
        { nombre: 'Pepe', pais: 'Colombia'},
        { nombre: 'Juan', pais: 'Chile'},
        
    ] //participante: nombre, pais
    const eventos = ["Acletismo", "Salto","Natacion","ciclismo" ] //eventos: 

    let resultadoDeJuegos= []
    let medallas = ["Oro", "Plata", "Cobre"]
    let totaldeMedallas ={} // 6 Mostrar el ranking de países según el número de medallas.

    //----------------------------------------------Paises y sus medallas----------------------------
    function medallasDePaises(){
        if(resultadoDeJuegos.length < 1){
            console.log("Favor de simular un juegos")
        }else {
            resultadoDeJuegos.forEach(participantes => {
                participantes.equipos.forEach(info => {
                    const pais = info.pais
                    const medalla = info.medalla

                    //si no esta el pais lo agregamos e inicializamos en 0
                    if(!totaldeMedallas[pais]){
                        totaldeMedallas[pais] = {Oro:0, Plata:0, Cobre:0}
                    }
                    if(totaldeMedallas[pais][medalla] !== undefined){
                        totaldeMedallas[pais][medalla]++
                       
                    }
                    console.log(totaldeMedallas)

                })
                
            })
            
        }
}


    //--------------------------------------------informe de todos los juegos pasados-------------
    function informe(){
        if(resultadoDeJuegos.length == 0){
            console.log("Aun no hay ningun juego favor de simular 1")
        }else {
            console.log("-------------Lista de ganadores en los juegos----------")
            
            resultadoDeJuegos.forEach(participantes => {
                console.log(participantes.nombredeljuego)
                participantes.equipos.forEach(info => {
                    console.log(info)

                })
                
                
            })

                
            init()

        }
    }
    //simulando eventos-------------------------------------------------------
    function simular (){
        
        if(participantes.length < 3) {
            console.log(`Tenemos ${participantes.length} y los participantes deben ser por lo menos 3, porfavor registra mas partcicpantes`)
            registros("participante")
        }else{
            console.log("-----------------------simulacion de juego-----------------")
            // sacarlo un numero del 1 al evento.leng despues mapear y selecionar ese evento en la posicion
            let seleccionarJuego= eventos[Math.floor(Math.random()*eventos.length)]

            let puntuajeDeParticipantes = participantes.map(participante => {
                
                return {
                    ...participante,
                    puntuaje:Math.floor(Math.random()*10)+1
                }
                
            })         
            

            resultadoDeJuegos.push({nombredeljuego:seleccionarJuego, equipos:puntuajeDeParticipantes}) 
            
            
              resultadoDeJuegos.forEach(juego => {
                

                juego.equipos.sort((a, b) => {
                    return b.puntuaje - a.puntuaje
                });
                
                
                let contadorMedallas = 0
                juego.equipos.forEach(participante => {
                    if(contadorMedallas <= 2){
                        let guardarVueltas = contadorMedallas
                    participante.medalla =medallas[guardarVueltas]
                    contadorMedallas ++
                    }else {
                        let sinMedellas = "sin medalla"
                        participante.medalla =sinMedellas
                    }
                 
                });
                                
            });

            let simulacionActual = resultadoDeJuegos.at(-1)
            console.log(simulacionActual)
            
            
            init()
        }
        
    }
    // funciones para simular los eventos-------------------------


    //Registro de eventos y personas ---------------------------------------------------
    function registros (respuesta){
        if(respuesta === "salir"){
            console.log("Saliendo de los juegos olimpicos")
            rl.close()
            return
        }else if (respuesta === "participante"){
            rl.question("cual es tu nombre?",(respuesta) => {
                rl.question("Cual es tu pais?", (respuesta2)=> {
                    let savedb = {nombre: respuesta, pais: respuesta2}
                    participantes.push(savedb) 
                    console.log(participantes)
                    init()
                })
            })
        }else if(respuesta === "evento"){
            rl.question("que evento deportivo gustas registrar", (respuesta) => {
                eventos.push(respuesta)
                console.log(eventos)
                init()
            })
        }

    }

    function init (){

        rl.question("Bienvenido a los juegos olimpicos acciones: 'registros', 'simular', 'ganadores', 'medallas' ", (respuesta)=>{
            if(respuesta === "registros"){
                rl.question("Puedes registrar a un participante o un evento: 'participante' o 'evento' ", (respuesta) => {
                    registros(respuesta)
                    respuesta !== "salir" ? init() : console.log("accion no permitida vuelve a intentar", init()) 
                })
                
            } else if(respuesta === "simular"){
            simular()
             respuesta !== "salir" ? init() : console.log("accion no permitida vuelve a intentar", init())
        } else if(respuesta === "medallas"){
            medallasDePaises()
             respuesta !== "salir" ? init() : console.log("accion no permitida vuelve a intentar", init())
        } else if(respuesta === "ganadores"){
            informe()
             respuesta !== "salir" ? init() : console.log("accion no permitida vuelve a intentar", init())
        }else if(respuesta === "salir"){
            console.log("Saliendo de los juegos olimpicos")
            rl.close()
            return
        } else {
            console.log("accion no permitida vuelve a intentar")
            init()
        }
            })
    }
    init()

}
CelebracionDeLosJuegosOlimpicos()