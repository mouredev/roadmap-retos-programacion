/*
  EJERCICIO:
  ¡El 12 de noviembre lanzo mouredev pro!
  El campus de la comunidad para estudiar programación de
  una manera diferente: https://mouredev.pro
 
  Crea un programa que funcione como una cuenta atrás.
 
  - Al iniciarlo tendrás que indicarle el día, mes, año,
    hora, minuto y segundo en el que quieres que finalice.
  - Deberás transformar esa fecha local a UTC.
  - La cuenta atrás comenzará y mostrará los días, horas,
    minutos y segundos que faltan.
  - Se actualizará cada segundo y borrará la terminal en
    cada nueva representación del tiempo restante.
  - Una vez finalice, mostrará un mensaje.
  - Realiza la ejecución, si el lenguaje lo soporta, en
    un hilo independiente.
*/

let promptData = [];
const getDay = prompt('Por favor, ingresa el día (1 - 31):');
const getMonth = prompt('Ingresa el mes (0 - 11):');
const getYear = prompt('Ingresa el año:');
const getHour = prompt('Ingresa la hora:');
const getMinute = prompt('Ingresa los minutos:');
const getSecond = prompt('Ingresa los segundos:');

promptData.push(getDay, getMonth, getYear, getHour, getMinute, getSecond);

const utcData = promptData.map((dateElement) => parseInt(dateElement));
const [day, month, year, hour, minutes, seconds] = utcData;
const localDate = new Date(year, month, day, hour, minutes, seconds);
const releaseDate = Date.parse(localDate.toUTCString()) + 21600000;

const  countdown = setInterval(() => {
  const currentDate = new Date().getTime();
  const distance = releaseDate - currentDate;
  const days = Math.floor(distance / (1000 * 60 * 60 * 24));
  const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((distance % (1000 * 60)) / 1000);

  if (distance >= 0) {
    setTimeout(() => {
      console.clear();
    }, 999);

    console.log(`Cuenta regresiva: ${days} día${days !== 1 ? 's' : ''} ${hours}h ${minutes}m ${seconds}s`);
  }

  if (distance < 0) {
    clearInterval(countdown);

    console.log('¡La espera ha terminado!');
  }
}, 1000);
