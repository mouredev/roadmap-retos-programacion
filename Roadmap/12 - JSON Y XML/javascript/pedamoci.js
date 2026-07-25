import  fs  from "fs"
import  readline  from "readline";

function preguntar(pregunta) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  })

  return new Promise(resolve => {
    rl.question(pregunta, (respuesta) => {
      rl.close()
      resolve(respuesta)
    })
  })
}


async function crearArchivo(tipo) {
  if (tipo === 'JSON') {
    let nombre = await preguntar('Ingrese su nombre: ')
    let edad = await preguntar('Ingrese su edad: ')
    let fechaNacimiento = await preguntar('Ingrese su fecha de nacimiento (xx/xx/xx): ')
    let lenguajesProgramacion = await preguntar('Ingrese los lenguajes de programación (lenguaje1, lenguaje2, ...): ')
    fs.writeFileSync('archivo.json', `{ "usuario": {` + 
                                                    `\n    "nombre": "${nombre}",` + 
                                                    `\n    "edad": "${edad}",` +
                                                    `\n    "fechaDeNacimiento": "${fechaNacimiento}",` +
                                                    `\n    "lenguajes": {`)
    lenguajesProgramacion = lenguajesProgramacion.split(', ')
    for (let i = 0; i < lenguajesProgramacion.length; i++) {
      if (i === lenguajesProgramacion.length - 1) fs.appendFileSync('archivo.json', `\n      "lenguaje${i + 1}": "${lenguajesProgramacion[i]}"`)
      else fs.appendFileSync('archivo.json', `\n      "lenguaje${i + 1}": "${lenguajesProgramacion[i]}",`)
    }
    fs.appendFileSync('archivo.json', `\n    }` +
                                      `\n  }` +
                                      `\n}`)
    console.log(fs.readFileSync('archivo.json', 'utf-8'))
    fs.unlinkSync('./archivo.json')
  } else if (tipo === 'XML') {
    let nombre = await preguntar('Ingrese su nombre: ')
    let edad = await preguntar('Ingrese su edad: ')
    let fechaNacimiento = await preguntar('Ingrese su fecha de nacimiento (xx/xx/xx): ')
    let lenguajesProgramacion = await preguntar('Ingrese los lenguajes de programación (lenguaje1, lenguaje2, ...): ')
    fs.writeFileSync('archivo.xml', `<?xml version="1.0" encoding="UTF-8"?>` + 
                                                    `\n<usuario>` + 
                                                    `\n  <nombre>${nombre}</nombre>` + 
                                                    `\n  <edad>${edad}</edad>` +
                                                    `\n  <fechaDeNacimiento>${fechaNacimiento}</fechaDeNacimiento>` +
                                                    `\n  <lenguajes>`)
    lenguajesProgramacion = lenguajesProgramacion.split(', ')
    for (let i = 0; i < lenguajesProgramacion.length; i++) {
      fs.appendFileSync('archivo.xml', `\n    <lenguaje${i + 1}>${lenguajesProgramacion[i]}</lenguaje${i + 1}>`)
    }
    fs.appendFileSync('archivo.xml', `\n  </lenguajes>` +
                                      `\n</usuario>`)
    console.log(fs.readFileSync('archivo.xml', 'utf-8'))
    fs.unlinkSync('./archivo.xml')
  }
}

let tipo = await preguntar('Quieres crear el archivo en "XML" o "JSON"')
tipo = tipo.toUpperCase()
crearArchivo(tipo)

// ------------------------------------- DIFICULTAD EXTRA -------------------------------------
// los imports de fs y readline estan arriba
class Persona {
  constructor(nombre, edad, fechaNacimiento, lenguajes) {
    this.nombre = nombre
    this.edad = edad
    this.fechaNacimiento = fechaNacimiento
    this.lenguajes = lenguajes
  }

  mostrarDatos() {
    console.log(`nombre: ${this.nombre}`)
    console.log(`edad: ${this.edad}`)
    console.log(`fechaDeNacimiento: ${this.fechaNacimiento}`)
    console.log(`lenguajes: ${this.lenguajes.join(', ')}`)
  }
}

function transformar(nombreArchivo) {
  if (nombreArchivo.endsWith('.json')) {
    let archivo = fs.readFileSync(`${nombreArchivo}`, 'utf-8')
    let datos = JSON.parse(archivo)
    let lenguajes = Object.values(datos.usuario.lenguajes)
    const persona = new Persona (datos.usuario.nombre, datos.usuario.edad, datos.usuario.fechaDeNacimiento, lenguajes)
    persona.mostrarDatos()
    fs.unlinkSync(`./${nombreArchivo}`)
  } else if (nombreArchivo.endsWith('.xml')) {
    let archivo = fs.readFileSync(`${nombreArchivo}`, 'utf-8')
    let nombre = archivo.match(/<nombre>([^<]+)<\/nombre>/)[1] // busca las etiquetas <nombre></nombre> y devuelve lo que haya en el medio
    let edad = archivo.match(/<edad>([^<]+)<\/edad>/)[1]  // busca las etiquetas <edad></edad> y devuelve lo que haya en el medio
    let fecha = archivo.match(/<fechaDeNacimiento>([^<]+)<\/fechaDeNacimiento>/)[1] // busca las etiquetas <fechaDeNacimiento></fechaDeNacimiento> y devuelve lo que haya en el medio
    let lenguajes = archivo.match(/<lenguajes>([\s\S]*?)<\/lenguajes>/)[1] // busca las etiquetas <lenguajes></lenguajes> y devuelve lo que haya en el medio
    lenguajes = lenguajes.replace(/<\/?[^>]+>/g, '') // remplaza '<', '/', '>' y lo que haya entre medio de '<' y '>' junto con lo que esta entre '</' y '>'
    lenguajes = lenguajes.match(/(?<![\w#+])([\w#+]+)(?![\w#+])/g) // busca todas las palabras que tengan un salto de line o espacio antes y despues
    const persona = new Persona (nombre, edad, fecha, lenguajes)
    persona.mostrarDatos()
    fs.unlinkSync(`./${nombreArchivo}`)
  }
}
transformar(await preguntar('Ingrese el nombre del archivo con la extension (".json" o ".xml")'))