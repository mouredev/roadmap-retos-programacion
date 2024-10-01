/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
*/
let alumno = function (nombre) {
  this.nombre = nombre;
  this.mostrar = function () {
    console.log(`Alumno: ${this.nombre}`);
  };
}

let alumnoDecorado = function (alumno, promedio, curso) {
  this.alumno = alumno;
  this.nombre = alumno.nombre; //igual a nombre de alumno
  this.promedio = promedio;
  this.curso = curso;

  this.mostrar = function() {
    console.log(`Alumno decorado: ${this.nombre}. Promedio: ${this.promedio}. Curso: ${this.curso}`);
  };
}
console.log('>>>Ejemplo Genérico')
let miAlumno = new alumno('Jaimito');
miAlumno.mostrar();

let miAlumnoDecorado = new alumnoDecorado(miAlumno, 7, "4to A");
miAlumnoDecorado.mostrar();

/*
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección.
*/

let numeroAleatorio = function (top = 10) {
  console.log(Math.floor(Math.random() * top));
}

let contarEjecuciones = function (func) {
  let count = 0;
  this.ejecutar = function (param){
    count ++;
    console.log(`Funcion <${func.name}> ejecutada ${count} veces`);
    func(param);
  }
}

console.log('\n>>>Dificultad Extra')
let contador = new contarEjecuciones(numeroAleatorio)
contador.ejecutar(5);
contador.ejecutar(3);
contador.ejecutar(4);
contador.ejecutar(10);
contador.ejecutar();
