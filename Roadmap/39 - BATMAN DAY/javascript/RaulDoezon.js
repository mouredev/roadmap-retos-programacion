/*
  EJERCICIO:
  Cada año se celebra el Batman Day durante la tercera semana de septiembre... 
  ¡Y este año cumple 85 años! Te propongo un reto doble:
 
  RETO 1:
  Crea un programa que calcule cuándo se va a celebrar el Batman Day hasta 
  su 100 aniversario.
 
  RETO 2:
  Crea un programa que implemente el sistema de seguridad de la Batcueva. 
  Este sistema está diseñado para monitorear múltiples sensores distribuidos
  por Gotham, detectar intrusos y activar respuestas automatizadas. 
  Cada sensor reporta su estado en tiempo real, y Batman necesita un programa 
  que procese estos datos para tomar decisiones estratégicas.
  Requisitos:
  - El mapa de Gotham y los sensores se representa con una cuadrícula 20x20.
  - Cada sensor se identifica con una coordenada (x, y) y un nivel
    de amenaza entre 0 a 10 (número entero).
  - Batman debe concentrar recursos en el área más crítica de Gotham.
  - El programa recibe un listado de tuplas representando coordenadas de los 
    sensores y su nivel de amenaza. El umbral de activación del protocolo de
    seguridad es 20 (sumatorio de amenazas en una cuadrícula 3x3).
  Acciones: 
  - Identifica el área con mayor concentración de amenazas
    (sumatorio de amenazas en una cuadrícula 3x3).
  - Si el sumatorio de amenazas es mayor al umbral, activa el 
    protocolo de seguridad.
  - Calcula la distancia desde la Batcueva, situada en (0, 0). La distancia es
    la suma absoluta de las coordenadas al centro de la cuadrícula amenazada.
  - Muestra la coordenada al centro de la cuadrícula más amenazada, la suma de
    sus amenazas, la distancia a la Batcueva y si se debe activar el
    protocolo de seguridad.
*/

console.log('+++++++++ RETO 1: BATMAN DAY HASTA EL ANIVERSARIO 100 +++++++++');

let initialDate = new Date(2024, 9, 0).getDate();
let yearsCounter = 0;
let saturdayIndex = 0;

for (let year = 85; year <= 100; year++) {
  for (let day = 1; day <= initialDate; day++) {
    let newDate = new Date(new Date().getFullYear() + yearsCounter, new Date().getMonth(), day);

    if (newDate.getDay() === 6) {
      saturdayIndex++;

      if (saturdayIndex === 3) {
        console.log(`Aniversario ${year}: ${day} de Septiembre del ${new Date().getFullYear() + yearsCounter}`);

        saturdayIndex = 0;
        break;
      }
    }
  }

  yearsCounter++;
}

console.log('\n+++++++++ RETO 2: SISTEMA DE SEGURIDAD DE LA BATICUEVA +++++++++');

let gothamMap = [];

for (let row = 0; row < 20; row++) {
  gothamMap[row] = [];

  for (let column = 0; column < 20; column++) {
    let threatLevel = Math.round((Math.random() * (10 - 0) + 0));

    gothamMap[row][column] = threatLevel;
  }
}

function securityProtocol(matrix, subMatrix) {
  let activationThreshold = 0;
  let axisX = 0;
  let axisY = 0;

  for (let firstRow = 0; firstRow <= matrix.length - subMatrix; firstRow++) {
    for (let firstColumn = 0; firstColumn <= matrix[0].length - subMatrix; firstColumn++) {
      let sumOfThreats = 0;

      for (let row = 0; row < subMatrix; row++) {
        for (let column = 0; column < subMatrix; column++) {
          sumOfThreats += matrix[firstRow + row][firstColumn + column];
        }
      }

      if (activationThreshold < sumOfThreats) {
        activationThreshold = sumOfThreats;
        axisX = firstRow + 1;
        axisY = firstColumn + 1;
      }
    }
  }

  return [activationThreshold, axisX, axisY];
}

function calculateDistance(x2, y2) {
  let distance = Math.sqrt(Math.pow(x2 - 0, 2) + Math.pow(y2 - 0, 2));

  return distance;
}

let [activationThreshold, centerSensorX, centerSensorY] = securityProtocol(gothamMap, 3);

console.table(gothamMap);
console.log(`Coordenadas del centro de la amenaza: ${centerSensorX}, ${centerSensorY}`);
console.log(`Suma de amenazas: ${activationThreshold}`);
console.log(`Distancia desde la Baticueva: ${calculateDistance(centerSensorX, centerSensorY)}`);

if (activationThreshold >= 20) {
  console.log('\nActivando el procolo de seguridad...');
} else {
  console.log('\nEl protocolo de seguridad no será activado.');
}
