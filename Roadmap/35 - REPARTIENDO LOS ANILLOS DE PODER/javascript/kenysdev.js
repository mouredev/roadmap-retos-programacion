/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________________________
#35 REPARTIENDO LOS ANILLOS DE PODER
-------------------------------------------------------
 * EJERCICIO:
 * ¡La temporada 2 de "Los Anillos de Poder" está a punto de estrenarse! 
 * ¿Qué pasaría si tuvieras que encargarte de repartir los anillos
 * entre las razas de la Tierra Media?
 * Desarrolla un programa que se encargue de distribuirlos.
 * Requisitos:
 * 1. Los Elfos recibirán un número impar.
 * 2. Los Enanos un número primo.
 * 3. Los Hombres un número par.
 * 4. Sauron siempre uno.
 * Acciones:
 * 1. Crea un programa que reciba el número total de anillos
 *    y busque una posible combinación para repartirlos.
 * 2. Muestra el reparto final o el error al realizarlo.
*/
// ________________________________________________________

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const getInput = async (prompt) => {
  return new Promise((resolve) => {
    rl.question(prompt, (input) => {
      resolve(input.trim());
    });
  });
};

const getTotalRings = async () => {
  while (true) {
    const input_ = await getInput("Cantidad de anillos: ");
    const total = parseInt(input_, 10);
    if (!isNaN(total) && total >= 1) {
      return total;
    }
    console.log("Debe ser un valor entero '>= 1'.");
  }
};

const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
};

const distribute = (total) => {
  const combinations = [];
  for (let elves = 1; elves < total; elves += 2) {
    for (let men = 2; men < total; men += 2) {
      const dwarves = total - (men + elves);
      if (dwarves > 0 && isPrime(dwarves)) {
        combinations.push([elves, men, dwarves]);
      }
    }
  }
  return combinations;
};

const standardDeviation = (tuple) => {
  const mean = tuple.reduce((sum, val) => sum + val, 0) / tuple.length;
  const variance =
    tuple.reduce((sum, val) => sum + Math.pow(val - mean, 2), 0) /
    tuple.length;
  return Math.sqrt(variance);
};

const theMostBalanced = (combinations) => {
  const deviations = combinations.map(standardDeviation);
  const indexOfLeastDeviation = deviations.indexOf(Math.min(...deviations));
  return combinations[indexOfLeastDeviation];
};

const printResult = (distribution, sauron) => {
  if (!distribution) {
    console.log("Error en la selección equitativa.");
    return;
  }

  const [elves, men, dwarves] = distribution;
  console.log("_________________________");
  console.log(`Elfos   -> ${elves} : # Impar`);
  console.log(`Enanos  -> ${dwarves} : # Primo`);
  console.log(`Hombres -> ${men} : # Par`);
  console.log(`Sauron  -> ${sauron} : # Fijo`);
  console.log("-------------------------");
};

const main = async () => {
  console.log("REPARTIENDO LOS ANILLOS DE PODER");
  let total = await getTotalRings();
  const sauron = 1;
  total -= sauron;

  const combinations = distribute(total);

  if (combinations.length === 0) {
    console.log("No existe una combinación posible.");
    rl.close();
    return;
  }

  const distribution = theMostBalanced(combinations);
  printResult(distribution, sauron);

  rl.close();
};

main();
