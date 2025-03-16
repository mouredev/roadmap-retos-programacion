function ejecutarFuncion(nombre, segundos) {
  console.log(`Función "${nombre}" empezando...`);

  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(
        `Función "${nombre}" finalizada después de ${segundos} segundos.`
      );
      resolve();
    }, segundos * 1000);
  });
}

async function ejecucionAsincrona() {
  try {
    await ejecutarFuncion("Función 1", 3);
    await ejecutarFuncion("Función 2", 2);
    await ejecutarFuncion("Función 3", 4);
  } catch (error) {
    console.error("Ocurrió un error:", error);
  }
}

ejecucionAsincrona();

// Ejercicio extra

async function ejecutarFuncion(nombre, segundos) {
  console.log(`Función "${nombre}" empezando...`);

  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log(
        `Función "${nombre}" finalizada después de ${segundos} segundos.`
      );
      resolve();
    }, segundos * 1000);
  });
}

async function funcionA() {
  console.log("Función A empezando...");
  await ejecutarFuncion("Función A", 1);
}

async function funcionB() {
  console.log("Función B empezando...");
  await ejecutarFuncion("Función B", 2);
}

async function funcionC() {
  console.log("Función C empezando...");
  await ejecutarFuncion("Función C", 3);
}

async function funcionD() {
  await Promise.all([funcionA(), funcionB(), funcionC()]);
  console.log("Función D empezando...");
  await ejecutarFuncion("Función D", 1);
}

async function main() {
  await funcionD();
}

main();
