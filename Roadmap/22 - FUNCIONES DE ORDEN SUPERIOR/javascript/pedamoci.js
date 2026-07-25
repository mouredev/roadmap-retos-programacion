// FUNCIONES DE ORDEN SUPERIOR
  // Reciben una función como parametro
    function calcular(a, b, metodo) {
      console.log(metodo(a, b))
    }

    const sumar = (num1, num2)=> {
      return num1 + num2
    }

    calcular(5, 62, sumar)

  // Devuelven una función
    function devolverMetodo(num) {
      if (num > 10) {
        return multiplicar = (num1, num2)=>{
          console.log(num1 * num2)
        }
      } else {
        return sumar = (num1, num2)=> {
          console.log(num1 + num2)
        }
      }
    }

    let metodo = devolverMetodo(23)

    metodo(45, 32)
// ----------------------------------- DIFICULTAD EXTRA -----------------------------------
const listaEstudiantes = [{
  nombre: "Juan",
  fechaNacimiento: "12/05/04",
  notas: [6.75, 1.22, 3.47, 3.01, 7.62]
}, {
  nombre: "Agus",
  fechaNacimiento: "23/02/05",
  notas: [7.08, 9.02, 1.78, 4.79, 1.27]
}, {
  nombre: "Victor",
  fechaNacimiento: "26/12/04",
  notas: [2.97, 5.54, 1.24, 2.79, 6.84]
}, {
  nombre: "Caterina",
  fechaNacimiento: "04/06/04",
  notas: [10.0, 9.45, 9.06, 9.5, 9.76]
}, {
  nombre: "Raul",
  fechaNacimiento: "13/11/05",
  notas: [1.06, 8.24, 7.28, 4.06, 2.4]
}, {
  nombre: "David",
  fechaNacimiento: "08/08/05",
  notas: [9.61, 4.03, 1.83, 1.87, 8.62]
}, {
  nombre: "Jesus",
  fechaNacimiento: "18/07/04",
  notas: [9.6, 9.8, 9.72, 9.53, 9.96]
}, {
  nombre: "Eugenia",
  fechaNacimiento: "01/04/05",
  notas: [9.37, 9.55, 9.82, 9.61, 9.85]
}]


const listaPromedios = listaEstudiantes.map((estudiante) => {
  let prom = estudiante.notas.reduce((p, nota) => (p += nota / estudiante.notas.length), 0)
  return {nombre: estudiante.nombre, promedio: prom.toFixed(2)}
})
console.log(listaPromedios)

const mejoresPromedios = listaPromedios.filter((estudiante) => estudiante.promedio >= 9)
console.log(mejoresPromedios)

const listaNacimiento = listaEstudiantes
  .map((estudiante) => ({
    nombre: estudiante.nombre, 
    fecha: estudiante.fechaNacimiento.split('/')
  }))
  .sort((a, b) => 
    parseInt(a.fecha[2]) - parseInt(b.fecha[2]) ||  // los ordena en forma creciente por año, si es el mismo pasa a comparar el mes
    parseInt(a.fecha[1]) - parseInt(b.fecha[1]) ||  // los ordena en forma creciente por mes, si es el mismo pasa a comparar el día
    parseInt(a.fecha[0]) - parseInt(b.fecha[0])     // los ordena en forma creciente por día
  )
console.log(listaNacimiento)

const mejorNota = listaEstudiantes.filter((estudiante) => sacoDiez(estudiante.notas))
function sacoDiez(notas) {
  return notas.includes(10)
}
console.log(mejorNota)