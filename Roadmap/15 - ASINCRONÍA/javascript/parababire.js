function inicio() {
  return new Date().toLocaleTimeString();
}

function task(name, timer) {
  const seg = timer / 1000;
  console.log(`Tarea: ${name}, Duración: ${seg}seg, Inicio: ${inicio()}`);
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(`Tarea: ${name}, Fin: ${inicio()}`);
    }, timer);
  });
}

function manejoDePromesa(resultado) {
  return console.log(resultado);
}

//Extra

async function esperaTask() {
  await Promise.all([task('C', 3000).then(manejoDePromesa), task('B', 2000).then(manejoDePromesa), task('A', 1000).then(manejoDePromesa)]);
  await task('D', 1000).then(manejoDePromesa);
}

esperaTask();