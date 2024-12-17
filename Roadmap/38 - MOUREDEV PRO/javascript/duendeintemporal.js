//#38 - MOUREDEV PRO 
/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */

/*  Example of csv:
id,email,status
1,test3@test.com,active
2,test4@test.com,active
3,test5@test.com,inactive
4,test6@test.com,active
5,test1@test.com,active
6,test2@test.com,inactive
7,test3@test.com,active
8,test4@test.com,active
9,test5@test.com,inactivo
10,test6@test.com,active
*/

/* In a console run the next comands:
mkdir mouredev-pro
cd mouredev-pro
npm init -y
npm install csv-parser
*/

let log = console.log;

const fs = require('fs');
const csv = require('csv-parser');

const winners = {
    subscription: null,
    discount: null,
    book: null
};

const activeEmails = [];

// Read the CSV file
fs.createReadStream('subscribers.csv')
    .pipe(csv())
    .on('data', (row) => {
        if (row.status === 'active') {
            activeEmails.push({ id: row.id, email: row.email });
        }
    })
    .on('end', () => {
        selectWinners();
        displayWinners();
    });

function selectWinners() {
    // Shuffle the array of active emails
    const shuffled = activeEmails.sort(() => 0.5 - Math.random());

    // Select unique winners
    winners.subscription = shuffled[0];
    winners.discount = shuffled[1];
    winners.book = shuffled[2];
}

function displayWinners() {
    log('Winners:');
    log(`Subscription: ID: ${winners.subscription.id}, Email: ${winners.subscription.email}`);
    log(`Discount: ID: ${winners.discount.id}, Email: ${winners.discount.email}`);
    log(`Book: ID: ${winners.book.id}, Email: ${winners.book.email}`);
}

/*
Possible Output: 
Winners:
Subscription: ID: 1, Email: test3@test.com
Discount: ID: 4, Email: test6@test.com
Book: ID: 5, Email: test1@test.com
*/