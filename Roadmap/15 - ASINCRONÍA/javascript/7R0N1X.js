const funcionAsincrona = async (nombre, tiempo) => {
  console.log(`La función "${nombre}" comienza. Duración esperada: ${tiempo} segundos.`)
  const inicio = new Date();
  console.log(`Inicio: ${inicio.toLocaleTimeString()}`);

  await new Promise(resolve => setTimeout(resolve, tiempo * 1000))

  const fin = new Date();
  console.log(`La función "${nombre}" ha finalizado.`);
  console.log(`Fin: ${fin.toLocaleTimeString()}`);
}

funcionAsincrona("Proceso 1", 5)

// DIFICULTAD EXTRA
const funcionC = async () => {
  console.log('La función C comienza. Duración esperada: 3 segundos.')
  const inicio = new Date();
  console.log(`Inicio: ${inicio.toLocaleTimeString()}`);

  await new Promise(resolve => setTimeout(resolve, 3000))

  const fin = new Date();
  console.log(`La función C ha finalizado.`);
  console.log(`Fin: ${fin.toLocaleTimeString()}`);
}

const funcionB = async () => {
  console.log('La función B comienza. Duración esperada: 2 segundos.')
  const inicio = new Date();
  console.log(`Inicio: ${inicio.toLocaleTimeString()}`);

  await new Promise(resolve => setTimeout(resolve, 2000))

  const fin = new Date();
  console.log(`La función B ha finalizado.`);
  console.log(`Fin: ${fin.toLocaleTimeString()}`);
}

const funcionA = async () => {
  console.log('La función A comienza. Duración esperada: 1 segundos.')
  const inicio = new Date();
  console.log(`Inicio: ${inicio.toLocaleTimeString()}`);

  await new Promise(resolve => setTimeout(resolve, 1000))

  const fin = new Date();
  console.log(`La función A ha finalizado.`);
  console.log(`Fin: ${fin.toLocaleTimeString()}`);
}

const funcionD = async () => {
  console.log('La función D comienza. Duración esperada: 1 segundos.')
  const inicio = new Date();
  console.log(`Inicio: ${inicio.toLocaleTimeString()}`);

  await new Promise(resolve => setTimeout(resolve, 1000))

  const fin = new Date();
  console.log(`La función D ha finalizado.`);
  console.log(`Fin: ${fin.toLocaleTimeString()}`);
}

const main = async () => {
  const C = funcionC()
  const B = funcionB()
  const A = funcionA()

  await Promise.all([C, B, A])

  const D = funcionD()
}

main()