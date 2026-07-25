#44 { Retos para Programadores } CUENTA ATRAS MOUREDEV PRO 

# Bibliography reference:
# I use GPT as a reference and sometimes to correct or generate proper comments.

"""
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

"""
from flask import Flask, render_template_string

app = Flask(__name__)

# HTML and CSS as a string
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Countdown Timer</title>
    <style>
        body {
            background: #000;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center; /* Fixed typo from align-intems to align-items */
            color: #fff;
        }

        .wrapper {
            padding: 0 0 20px 0;
            display: flex;
            flex-flow: column;
        }

        .msgBox {
            height: 6vw;
            line-height: 6vw;
            text-align: center;
            font-size: 5vw;
            font-weight: 700;
            color: rgba(255, 255, 204, 1);
            text-shadow: 1px 1px 1px #fff;
            margin-bottom: 60px;
        }

        .logBox {
            height: 6vw;
            line-height: 6vw;
            text-align: center;
            font-size: 5vw;
            font-weight: 700;
            color: rgba(7, 55, 99, 1);
            text-shadow: -1px -1px 1px blue, -2px -2px 3px #fff;
            border: 2px solid rgba(255, 255, 204, 1);
            border-radius: 7px;
        }
    </style>
</head>
<body>
    <h1 id="title">Retosparaprogramadores #44.</h1>
    <div class="wrapper">
        <h1 class="msgBox">Days Remaining For The Initiation Day of MoureDev Pro</h1>
        <h1 class="logBox" id="logBox"></h1>
    </div>
    <script>
        const logBox = document.getElementById('logBox');

        const countBackFromDate = (day, month, year, hour, minutes, seconds) => {
            const dateTime = new Date(year, month - 1, day, hour, minutes, seconds);
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
        };

        // Set the countdown to December 31, 2024 at 00:00:00 UTC
        countBackFromDate(31, 12, 2024, 0, 0, 0);
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
