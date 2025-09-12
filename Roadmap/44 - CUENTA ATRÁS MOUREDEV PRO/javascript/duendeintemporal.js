//44 - CUENTA ATRAS MOUREDEV PRO 
/*
 * EJERCICIO:
 * ¡El 12 de noviembre lanzo mouredev pro!
 * El campus de la comunidad para estudiar programación de
 * una manera diferente: https://mouredev.pro
 *
 * Crea un programa que funcione como una cuenta atrás.
 *
 * - Al iniciarlo tendrás que indicarle el día, mes, año,
 *   hora, minuto y segundo en el que quieres que finalice.
 * - Deberás transformar esa fecha local a UTC.
 * - La cuenta atrás comenzará y mostrará los días, horas,
 *   minutos y segundos que faltan.
 * - Se actualizará cada segundo y borrará la terminal en
 *   cada nueva representación del tiempo restante.
 * - Una vez finalice, mostrará un mensaje.
 * - Realiza la ejecución, si el lenguaje lo soporta, en
 *   un hilo independiente.
 */

let log = console.log;

let styles = `
    body{
        background: #000;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-intems; center;
        color: #fff;
    }

    .wrapper{
        padding: 0 0 20px 0;
        display: flex;
        flex-flow: column;
    }

    .msgBox{
        height: 6vw;
        line-height: 6vw;
        text-align: center;
        font-size: 5vw;
        font-weight: 700;
        color: rgba(255,255,204,1);
        text-shadow: 1px 1px 1px #fff;
        margin-bottom: 60px;
    }

    .logBox{
        height: 6vw;
        line-height: 6vw;
        text-align: center;
        font-size: 5vw;
        font-weight: 700;
        color: rgba(7,55,99,1);
        text-shadow: -1px -1px 1px blue, -2px -2px 3px #fff;
        border: 2px solid rgba(255,255,204,1);
        border-radius: 7px;
    }
`

window.addEventListener('load', () => {
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    const wrapper = document.createElement('div');
    wrapper.classList.add('wrapper');
    const msgBox = document.createElement('h1');
    msgBox.classList.add('msgBox');
    msgBox.textContent = 'Days Remaining For The Initiation Day of MoureDev Pro';
    const logBox = document.createElement('h1');
    logBox.classList.add('logBox');

    // Create a <style> element and append the styles
    let styleSheet = document.createElement("style");
    styleSheet.type = "text/css";
    styleSheet.innerText = styles;
    document.head.appendChild(styleSheet);

  
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
  
    title.textContent = 'Retosparaprogramadores #44.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '20vh');
  
    body.appendChild(title);
    wrapper.appendChild(msgBox);
    wrapper.appendChild(logBox);
    body.appendChild(wrapper);
  
    console.log('Retosparaprogramadores #44');
  
    const countBackFromDate = (day, month, year, hour, minutes, seconds) => {
      // Create a new Date object
      const dateTime = new Date(year, month - 1, day, hour, minutes, seconds);
      // Convert the Date object to a UTC timestamp
      const utcTimestamp = dateTime.getTime();
  
      const interval = setInterval(() => {
        const currentTime = new Date().getTime();
        const timeRemaining = utcTimestamp - currentTime;
  
        if (timeRemaining <= 0) {
          clearInterval(interval);
          logBox.innerText = 'Mouredev Pro has launched! Welcome to the community campus to study programming in a different way!';
        } else {
          const days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
          const hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
          const minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
          const seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
  
          logBox.innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
        }
      }, 1000);
  
      // Return the UTC timestamp
      return utcTimestamp;
    };
  
    // Set the countdown to December 31, 2024 at 00:00:00 UTC
    countBackFromDate(31, 12, 2024, 0, 0, 0);
  });
  