const frutas = ['Manzana', 'Banana', 'Fresa', 'Uva', 'Mango', 'Pera', 'Kiwi', 'Durazno', 'Sandía', 'Naranja', 'Cereza']

const crearFiltroPorLetra = (letra) => {
  return function (fruta) {
    return fruta.startsWith(letra)
  }
}

const filtrarPorM = crearFiltroPorLetra('M')
const frutasConM = frutas.filter(filtrarPorM)

console.log(frutasConM)

// DIFICULTAD EXTRA
const estudiantes = [
  { nombres: 'Eduardo Molina', fechaNacimiento: '1999-08-30', calificaciones: [10, 8, 9, 10] },
  { nombres: 'Lucía Torres', fechaNacimiento: '2001-05-15', calificaciones: [9, 7, 8, 10] },
  { nombres: 'Carlos Jiménez', fechaNacimiento: '2000-11-22', calificaciones: [6, 9, 8, 7] },
  { nombres: 'Ana Pérez', fechaNacimiento: '1998-12-10', calificaciones: [10, 10, 9, 8] },
  { nombres: 'Juan Rodríguez', fechaNacimiento: '2002-04-05', calificaciones: [7, 6, 7, 8] },
  { nombres: 'María López', fechaNacimiento: '2000-03-18', calificaciones: [8, 9, 10, 9] },
  { nombres: 'Sofía García', fechaNacimiento: '1999-09-12', calificaciones: [9, 8, 8, 9] },
  { nombres: 'Miguel Castro', fechaNacimiento: '2003-01-25', calificaciones: [6, 7, 6, 7] },
  { nombres: 'Laura Fernández', fechaNacimiento: '2001-06-30', calificaciones: [10, 9, 9, 10] },
  { nombres: 'Andrés Martínez', fechaNacimiento: '2002-02-14', calificaciones: [8, 8, 7, 8] }
]

const obtenerPromedio = (estudiante) => {
  const { nombres, calificaciones } = estudiante
  const promedio = calificaciones.reduce((acumulador, nota) => acumulador + nota / calificaciones.length, 0)
  return {
    nombres,
    promedio
  }
}

const mejoresEstudiantes = (estudiante) => {
  const { nombres, promedio } = estudiante
  if (promedio >= 9) {
    return { nombres }
  }
}

const ordenarFechaNacimiento = (estudianteA, estudianteB) => {
  return new Date(estudianteB.fechaNacimiento) - new Date(estudianteA.fechaNacimiento)
}

const calificacionMasAlta = (estudiante) => {
  const { nombres, calificaciones } = estudiante
  const calificacionAlta = Math.max(...calificaciones)
  return {
    nombres,
    calificacionAlta
  }
}

const promedios = estudiantes.map(obtenerPromedio)
console.log(promedios)

const mejoresNotas = promedios.filter(mejoresEstudiantes)
console.log(mejoresNotas)

const estudiantesPorFechaNacimiento = estudiantes.sort(ordenarFechaNacimiento)
console.log(estudiantesPorFechaNacimiento)

const calificacionMasAltaPorEstudiante = estudiantes.map(calificacionMasAlta)
console.log(calificacionMasAltaPorEstudiante)
