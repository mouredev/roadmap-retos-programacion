function date() {
  const inicio = new Date().toLocaleTimeString();
  return inicio;
}

function task(name, timer) {
  const seg = timer / 1000;
  console.log(`Tarea: ${name}, Duración: ${seg}seg, Inicio: ${date()}`);
  setTimeout(function () {
    console.log(`Tarea: ${name}, Fin: ${date()}`);
  }, 3000);
}

task('1', 3000);