function date() {
  const inicio = new Date().toLocaleTimeString();
  return inicio;
}

function task(name, timer) {
  const seg = timer / 1000;
  console.log(`Tarea: ${name}, Duración: ${seg}seg, Inicio: ${date()}`);
  return new Promise((resolve) => {
    setTimeout(() => {
      console.log(`Tarea: ${name}, Fin: ${date()}`);
      resolve();
    }, timer);
  });
}

async function esperaTask() {
  await Promise.all([task('C', 3000), task('B', 2000), task('A', 1000)]);
  await task('D', 1000);
}

esperaTask();