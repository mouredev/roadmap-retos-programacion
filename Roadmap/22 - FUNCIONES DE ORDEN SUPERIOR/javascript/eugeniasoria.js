/*
# #22 FUNCIONES DE ORDEN SUPERIOR
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 */

console.log("Función de orden superior que pase una función como argumento");
//En este caso la función de Orden superior funciona como un filtro y se pasa como argumento 
//una función con el filtro que se quiere aplicar
function vocalesMinuscula(letra) {
  return (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u') ? true : false;
}

function vocalesMayuscula(letra) {
  return (letra == 'A' || letra == 'E' || letra == 'I' || letra == 'O' || letra == 'U') ? true : false;
}
function numero(num) {
  return (num == '0' || num == '1' || num == '2' || num == '3' || num == '4' || num == '5' || 
    num == '6' || num == '7' || num == '8' || num == '9' || num == '0') ? true : false;
}

function funcionOrdenSuperiorCadenas(cadena, funcOrdenInferior) {
  let resultado = '';
  for (i=0; i<cadena.length; i++) {
    if (funcOrdenInferior(cadena[i]))
      resultado += cadena[i]
  }
  return resultado
}

const cadena1 = 'murcielago';
const vocalesMinusculasResultado = funcionOrdenSuperiorCadenas(cadena1, vocalesMinuscula); 
console.log(`Cadena original <${cadena1}> filtrando vocales minúsculas <${vocalesMinusculasResultado}>`);

const cadena2 = 'Ernesto come Ananá en su casa en Roma junto a Oscar';
const vocalesMayusculasResultado = funcionOrdenSuperiorCadenas(cadena2, vocalesMayuscula); 
console.log(`Cadena original <${cadena2}> filtrando vocales Mayúsculas <${vocalesMayusculasResultado}>`);

const cadena3 = 'C3PO y R2D2'
const numerosResultado = funcionOrdenSuperiorCadenas(cadena3, numero); 
console.log(`Cadena original <${cadena3}> filtrando vocales Mayúsculas <${numerosResultado}>`);

console.log("\n\nFunción de orden superior que retorna una función");

function funcionOrdenSuperiorSaludo(idioma) {
  
  switch (idioma) {
    case 'francais':
      return function (nombre) {
        return `Bonjour ${nombre}`
      };
      break;
    case 'english':
      return function (nombre) {
        return `Hello ${nombre}`
      };
      break;
        
    default:
      return function (nombre) {
        return `Hola ${nombre}`
      };      
      break;
  }
  
}

//Usando las funciones retornadas por la funcion de orden superior
const saludarFrances = funcionOrdenSuperiorSaludo('francais');
console.log(saludarFrances);
console.log(saludarFrances('Pierre'));
console.log(funcionOrdenSuperiorSaludo('francais')('Juliette'));

const saludarIngles = funcionOrdenSuperiorSaludo('english');
console.log(saludarIngles);
console.log(saludarIngles('Peter'));
console.log(funcionOrdenSuperiorSaludo('english')('Melanie'));

const saludarDefault = funcionOrdenSuperiorSaludo('nose');
console.log(saludarDefault);
console.log(saludarDefault('Pedro'));
console.log(funcionOrdenSuperiorSaludo('español')('Lucia'));


/*
* DIFICULTAD EXTRA (opcional):
* Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
* lista de calificaciones), utiliza funciones de orden superior para 
* realizar las siguientes operaciones de procesamiento y análisis:
* - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
*   y promedio de sus calificaciones.
* - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
*   que tienen calificaciones con un 9 o más de promedio.
* - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
* - Mayor calificación: Obtiene la calificación más alta de entre todas las
*   de los alumnos.
* - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
*/

const listaEstudiantes = [
  {
    nombre: 'Rafaella Carra',
    fechaNacimiento: '05/05/1976',
    calificaciones: {
      matematica: 2,
      lengua: 10,
      programación: 8.5
    }
  },
  {
    nombre: 'Esteban Quito',
    fechaNacimiento: '04/08/1999',
    calificaciones: {
      matematica: 5,
      lengua: 10,
      programación: 1
    }
  },
  {
    nombre: 'Guillermo Puertas',
    fechaNacimiento: '01/01/2000',
    calificaciones: {
      matematica: 10,
      lengua: 10,
      programación: 1
    }
  },    
  {
    nombre: 'Jorgito Alfajor',
    fechaNacimiento: '15/05/2015',
    calificaciones: {
      matematica: 8,
      lengua: 8,
      programación: 8
    }
  },
  {
    nombre: 'Susana Dieta',
    fechaNacimiento: '13/09/2017',
    calificaciones: {
      matematica: 3,
      lengua: 2,
      programación: 1
    }
  },
  {
    nombre: 'Lana Oveja',
    fechaNacimiento: '28/02/1999',
    calificaciones: {
      matematica: 10,
      lengua: 10,
      programación: 10
    }
  },   
];
console.log('\n\nDIFICULTAD EXTRA');
console.log('Lista de estudiantes', listaEstudiantes);

function calcularPromedio(arrayNumeros) {  
  return arrayNumeros.reduce((acum, elem) => acum += elem, 0)/arrayNumeros.length;
}

function calcularPromedioEstudiantes(estudiantes, funcionPromedio) {  
  let resultado = [];
  estudiantes.forEach(element => {        
    resultado.push({ nombre: element.nombre, promedio: funcionPromedio(Object.values(element.calificaciones)) })
  });
  return resultado;
}
console.log('\nPromedio por estudiante');
let promedios = calcularPromedioEstudiantes(listaEstudiantes, calcularPromedio);
console.log(promedios);

function mejoresEstudiantes (estudiantes, funcionPromedio, notaRequerida) {
  let promedioPorEstudiante = calcularPromedioEstudiantes(estudiantes, funcionPromedio);  
  let resultado = promedioPorEstudiante.filter((x) => (x.promedio > notaRequerida));
  console.log(resultado);  
}
console.log('\nMejores alumnos (promedio mayor a 9)');
mejoresEstudiantes(listaEstudiantes, calcularPromedio, 9);

function ordenarfechasNacimientoAlumnos(fechasNacimientoAlumnos) {

  let resultado = [];
  fechasNacimientoAlumnos.forEach(element => {    
    const elemSplit = element.fechaNacimiento.split('/')
    resultado.push(
      {
        nombre: element.nombre,
        fechaOriginal: element.fechaNacimiento,
        fechaConFormato: new Date(elemSplit[2], elemSplit[1]-1, elemSplit[0])
      });    
  });

  resultado.sort((a, b) => (a.fechaConFormato - b.fechaConFormato));
  
  resultado.forEach(element => {
    delete element.fechaConFormato
  });

  return resultado;  
}


function ordenarEstudiantesPorNacimiento(estudiantes, funcionOrdenarFecha) {
  let fechas = [];
  estudiantes.forEach(element => {          
    fechas.push({ nombre: element.nombre, fechaNacimiento: element.fechaNacimiento }) });
  let resultado = funcionOrdenarFecha(fechas);
  console.log(resultado);
}
console.log('\nAlumnos ordenados por fecha de nacimiento');
ordenarEstudiantesPorNacimiento(listaEstudiantes, ordenarfechasNacimientoAlumnos);

function obtenerCalificacionMasAlta(calificacionesAlumnos) {
  //Espera un array de objectos alumno/materia/calificacion  
  let todasLasNotas = [];
  calificacionesAlumnos.forEach(element => {
    todasLasNotas.push(element.nota);
  }); 
  let notaMaxima = Math.max(...todasLasNotas);

  return calificacionesAlumnos.filter((x) => (x.nota === notaMaxima))  
}

function calificacionMasAlta(estudiantes, funcionMaxCalificacion) {
  let estudianteNotas = []
  estudiantes.forEach(estudiante => {
    
    Object.keys(estudiante.calificaciones).forEach(element => {
      let item = {
        nombre: estudiante.nombre,
        materia: element,
        nota: estudiante.calificaciones[element]
      } 
      estudianteNotas.push(item)
    });            
  });

  console.log(funcionMaxCalificacion(estudianteNotas));
}
console.log('\nAlumnos con la calificación más alta');
calificacionMasAlta(listaEstudiantes, obtenerCalificacionMasAlta)
