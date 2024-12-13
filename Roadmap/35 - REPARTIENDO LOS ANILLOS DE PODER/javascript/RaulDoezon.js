/*
  EJERCICIO:
  ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
  ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
  entre las razas de la Tierra Media?
  Desarrolla un programa que se encargue de distribuirlos.
  Requisitos:
  1. Los Elfos recibirán un número impar.
  2. Los Enanos un número primo.
  3. Los Hombres un número par.
  4. Sauron siempre uno.
  Acciones:
  1. Crea un programa que reciba el número total de anillos
     y busque una posible combinación para repartirlos.
  2. Muestra el reparto final o el error al realizarlo.
*/

const ringDistribution = (totalRings) => {
  const sauronRing = 1;
  let allPrimeNumbers = [],
    primeNumber,
    indexNumber,
    isPrime;

  console.log(`Anillos totales: ${totalRings}`);
  console.log(`Anillos para Sauron: ${sauronRing}`);

  totalRings = totalRings - sauronRing;

  do {
    elvesRings = Math.floor(Math.random() * totalRings);
  } while(elvesRings % 2 === 0);

  totalRings = totalRings - elvesRings;

  console.log(`Anillos para los Elfos: ${elvesRings}`);

  for (primeNumber = 2; primeNumber <= totalRings; primeNumber++) {
    if (primeNumber == 1 || primeNumber == 0) {
      continue;
    }

    isPrime = true;

    for (indexNumber = 2; indexNumber <= primeNumber / 2; indexNumber++) {
      if (primeNumber % indexNumber == 0) {
        isPrime = false;

        break;
      }
    }

    if (isPrime) {
      allPrimeNumbers.push(primeNumber);
    }
  }

  let selectPrimeNumber = Math.floor(Math.random() * allPrimeNumbers.length);
  let dwarvesRings = allPrimeNumbers[selectPrimeNumber];
  totalRings = totalRings - dwarvesRings;

  console.log(`Anillos para los Enanos: ${dwarvesRings}`);

  do {
    menRings = Math.floor((Math.random() * totalRings) + 1);
  } while(menRings % 2 !== 0);

  totalRings = totalRings - menRings;

  if (totalRings > 0 && totalRings % 2 === 0) {
    menRings = menRings + totalRings;
    totalRings = totalRings - totalRings;
  }

  console.log(`Anillos para los Hombres: ${menRings}`);

  if (totalRings > 0 && totalRings % 2 !== 0) {
    console.error(`Los anillos no se distribuyeron correctamente. El restante fue de: ${totalRings}`);
  }
}

ringDistribution(100);
