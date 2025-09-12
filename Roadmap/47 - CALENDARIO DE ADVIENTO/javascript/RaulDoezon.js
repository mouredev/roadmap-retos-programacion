/*
  EJERCICIO:
  ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
  developers. Del 1 al 24 de diciembre: https://adviento.dev

  Dibuja un calendario por terminal e implementa una
  funcionalidad para seleccionar días y mostrar regalos.
  - El calendario mostrará los días del 1 al 24 repartidos
    en 6 columnas a modo de cuadrícula.
  - Cada cuadrícula correspondiente a un día tendrá un tamaño 
    de 4x3 caracteres, y sus bordes serán asteríscos.
  - Las cuadrículas dejarán un espacio entre ellas.
  - En el medio de cada cuadrícula aparecerá el día entre el
    01 y el 24.
 
  Ejemplo de cuadrículas:
  **** **** ****
  *01* *02* *03* ...
  **** **** ****
 
  - El usuario seleccioná qué día quiere descubrir.
  - Si está sin descubrir, se le dirá que ha abierto ese día
    y se mostrará de nuevo el calendario con esa cuadrícula
    cubierta de asteríscos (sin mostrar el día).
 
  Ejemplo de selección del día 1
  **** **** ****
  **** *02* *03* ...
  **** **** ****

  - Si se selecciona un número ya descubierto, se le notifica
    al usuario.
*/

class Calendar {
  constructor() {
    this.daysRevealed = [];
  }

  build() {
    let dayCounter = 1;

    console.log("********* aDEViento 2024 *********");

    for ( let row = 0; row < 4; row++) {
      let top = "";
      let center = "";
      let bottom = "";

      for ( let column = 0; column < 6; column++) {
        let findDay = this.daysRevealed.findIndex((number) => number === dayCounter);
        let dayNumber = `${findDay === -1 ? `*${dayCounter < 10 ? 0 : ''}${dayCounter}*` : "****"}`;

        top = top + " " + "****";
        center = center + " " + dayNumber;
        bottom = bottom + " " + "****";
        dayCounter++;
      }

      console.log(top);
      console.log(center);
      console.log(bottom);
      console.log("\n");
    }
  }

  reveal(day) {
    if (day > 0 && day <= 24) {
      const checkDay = this.daysRevealed.findIndex((number) => number === day);

      if (checkDay === -1) {
        this.daysRevealed.push(day);

        alert(`Revelaste el número: ${day}`);
      } else {
        alert("El día ingresado ya fue revelado.");
      }
    } else {
      alert("Debes ingresar un número que esté dentro del rango");
    }
  }

  markDay() {
    let menu = 0;

    do {
      menu = parseInt(prompt("1). Selecciona un día del calendario.\n2). Cerrar el calendario."), 10);

      this.build();

      switch (menu) {
        case 1:
          let selectDay = parseInt(prompt("Ingresa un número del 01 al 24"), 10);

          this.reveal(selectDay);

          break;

        case 2:
          alert("Cerrando el calendario...");

          break;

        default:
          alert("Ingresa alguno de los números 1 o 2.");

          break;
      }
    } while (menu !== 2);
  }
}

let calendar = new Calendar();

calendar.markDay();
