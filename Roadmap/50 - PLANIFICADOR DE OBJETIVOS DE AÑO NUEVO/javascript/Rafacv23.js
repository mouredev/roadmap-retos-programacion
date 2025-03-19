// Autor: Rafael Canosa, Github: https://github.com/rafacv23

/* crear objetivo con los siguientes atributos:
 * meta
 * cantidad
 * unidades
 * plazo
 */

let objectives = []

const months = [
  {
    name: "enero",
    value: 1,
  },
  {
    name: "febrero",
    value: 2,
  },
  {
    name: "marzo",
    value: 3,
  },
  {
    name: "abril",
    value: 4,
  },
  {
    name: "mayo",
    value: 5,
  },
  {
    name: "junio",
    value: 6,
  },
  {
    name: "julio",
    value: 7,
  },
  {
    name: "agosto",
    value: 8,
  },
  {
    name: "septiembre",
    value: 9,
  },
  {
    name: "octubre",
    value: 10,
  },
  {
    name: "noviembre",
    value: 11,
  },
  {
    name: "diciembre",
    value: 12,
  },
]

class Objective {
  constructor(meta, cantidad, unidades, plazo) {
    this.meta = meta
    this.cantidad = cantidad
    this.unidades = unidades
    this.plazo = plazo

    // comprobramos que el plazo no sea superior a 12
    if (this.plazo > 12) {
      console.log("❌ El plazo no puede ser superior a 12 meses.")
      return
    }
    // agregar objetivo a la lista
    objectives.push(this)
  }

  // crear funcion que imprima el objetivo
  show() {
    console.log(`Objetivo: ${this.meta}`)
    console.log(`Cantidad: ${this.cantidad}`)
    console.log(`Unidades: ${this.unidades}`)
    console.log(`Plazo: ${this.plazo}`)
  }
}

function printObjectives() {
  for (let i = 0; i < objectives.length; i++) {
    console.log(`Objetivo ${i + 1}: ${objectives[i].meta}`)
  }
}

function calculate() {
  months.forEach((month) => {
    // calculamos las tareas de cada mes
    console.log(`📅 ${month.name}`)
    objectives.forEach((objective) => {
      const target = objective.cantidad / objective.plazo // calculamos el objetivo a lo largo de los 12 meses

      if (objective.plazo >= month.value) {
        console.log(
          `${objective.meta} (${target} ${objective.unidades}/mes). Total: ${objective.cantidad}`
        )
      }
    })
  })
}

new Objective("leer libros", 12, "libros", 12)
new Objective("escribir artículos", 12, "artículos", 6)
new Objective("escribir informes", 24, "informes", 12)
new Objective("programar", 24, "programas", 8)
//new Objective("programar", 24, "informes", 69)

printObjectives()
calculate()
