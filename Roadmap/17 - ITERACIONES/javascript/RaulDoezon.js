/*
  EJERCICIO:
  Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
  números del 1 al 10 mediante iteración.
*/

console.log("Imprimir números del 1 al 10 mediante:");
console.log("\n+++++++++ FOR +++++++++");

for (let iteration1 = 1; iteration1 < 11; iteration1++) {
  const element = iteration1;

  console.log(element);
}

console.log("\n+++++++++ WHILE +++++++++");

let iteration2 = 1;

while (iteration2 < 11) {
  console.log(iteration2++);
}

console.log("\n+++++++++ DO WHILE +++++++++");

let iteration3 = 1;

do {
  console.log(iteration3++);
} while (iteration3 < 11);

/*
  EJERCICIO:
  DIFICULTAD EXTRA (opcional):
  Escribe el mayor número de mecanismos que posea tu lenguaje
  para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/
console.log("\nMECANISMOS PARA ITERAR:");
console.log("\n+++++++++ 1. FOR +++++++++");

const dbCharacters = ["Goku", "Vegeta", "Piccolo", "Gohan"];

for(let index = 0; index < dbCharacters.length; index++) {
  const character = dbCharacters[index];

  console.log(character);
}

console.log("\n+++++++++ 2. FOR...IN +++++++++");
for (const forInCharacter in dbCharacters) {
  const element = dbCharacters[forInCharacter];

  console.log(element);
}

console.log("\n+++++++++ 3. FOR...OF +++++++++");
for (const dbIterator of dbCharacters) {
  console.log(dbIterator);
}

console.log("\n+++++++++ 4. FOREACH +++++++++");
dbCharacters.forEach((element) => {
  console.log(element);
});

console.log("\n+++++++++ 5. WHILE +++++++++");

let whileIndex = 0;

while (whileIndex < dbCharacters.length) {
  console.log(dbCharacters[whileIndex]);

  whileIndex++;
}

console.log("\n+++++++++ 6. DO WHILE +++++++++");

let doWhileIndex = 0;

do {
  console.log(dbCharacters[doWhileIndex]);

  doWhileIndex++;
} while (doWhileIndex < dbCharacters.length);

console.log("\n+++++++++ 7. FUNCIÓN RECURSIVA +++++++++");

function recursiveFunction(number) {
  if (number === 11) {
    return;
  }

  console.log(dbCharacters[number]);

  return recursiveFunction(number + 1)
}

recursiveFunction(0);

console.log("\n+++++++++ 8. MAP +++++++++");
dbCharacters.map(function(character){
  console.log(character);
});
