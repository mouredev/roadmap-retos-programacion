/*
He presentado mi proyecto más importante del año: mouredev pro.
EJERCICIO:
  Un campus para la comunidad, que lanzaré en octubre, donde estudiar
  programación de una manera diferente.
  Cualquier persona suscrita a la newsletter de https://mouredev.pro
  accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 
  Desarrolla un programa que lea los registros de un fichero .csv y
  seleccione de manera aleatoria diferentes ganadores.
  Requisitos:
  1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
     o "inactivo" (y datos ficticios).
     Ejemplo: 1 | test@test.com | activo
              2 | test2@test.com | inactivo
     (El .csv no debe subirse como parte de la corrección)
  2. Recupera los datos desde el programa y selecciona email aleatorios.
  Acciones:
  1. Accede al fichero .csv y selecciona de manera aleatoria un email
     ganador de una suscripción, otro ganador de un descuento y un último
     ganador de un libro (sólo si tiene status "activo" y no está repetido).
  2. Muestra los emails ganadores y su id.
  3. Ten en cuenta que la primera fila (con el nombre de las columnas)
     no debe tenerse en cuenta.
*/

const fs = require('fs');
const readline = require('readline');
const stream = fs.createReadStream('/ruta-del/archivo.csv');
const reader = readline.createInterface({ input: stream });
const awards = ['Suscripción', 'Descuento', 'Libro'];
let participants = [];
let aleatoryNumbers = [];
let selectedEmails = [];
let assignedAwards = -1;

reader.on('line', (line) => {
  const row = line.split(',');

  participants.push(row);
});

reader.on('close', () => {
  console.table(participants);

  const numberOfParticipants = participants.length - 1;

  while(aleatoryNumbers.length < numberOfParticipants) {
    let randomNumber = Math.round((Math.random() * (numberOfParticipants - 1) + 1));

    if (aleatoryNumbers.indexOf(randomNumber)  === -1) {
      aleatoryNumbers.push(randomNumber);
    }
  }

  for (let index = 0; assignedAwards < 2; index++) {
    let selectedNumber = aleatoryNumbers[index];
    let currentEmail = selectedEmails.find((email) => {
      return email === participants[selectedNumber][1];
    });

    if (currentEmail === undefined && participants[selectedNumber][2] === 'activo') {
      selectedEmails.push(participants[selectedNumber][1]);
      assignedAwards++;

      console.log(`🎁 El participante con correo ${participants[selectedNumber][1]} y ID ${participants[selectedNumber][0]} recibe el premio de ${awards[assignedAwards]}.`);
    } else {
      console.log(`⚠️ El participante con correo ${participants[selectedNumber][1]} salió premiado, pero no se le puede entregar premio porque está inactivo y/o repetido.`);
    }
  }

  console.log(`\nOrden de números aleatorios: ${aleatoryNumbers}`);
  console.log(`Correos seleccionados: ${selectedEmails}`);
});
