import fs from 'fs'
const info = ['Pedro', 23, 'JavaScript']


function archivoTxt(operation) {
  switch (operation) {
    case 'crearEnUnaLinea':
      fs.writeFileSync('pedamoci.txt', `Nombre: ${info[0]}\nEdad: ${info[1]}\nLenguaje favorito: ${info[2]}`)
      break;
    case 'crearEnVariasLineas':
      fs.writeFileSync('pedamoci.txt', `Nombre: ${info[0]}`)
      fs.appendFileSync('pedamoci.txt', `\nEdad: ${info[1]}`)
      fs.appendFileSync('pedamoci.txt', `\nLenguaje favorito: ${info[2]}`)
      break;
    case 'imprimir':
      console.log(fs.readFileSync('pedamoci.txt', 'utf8'))
      break;
    case 'borrar':
      fs.unlinkSync('./pedamoci.txt')
      console.log('Archivo borrado')
      break;
    default:
      break;
  }
}

archivoTxt('crearEnUnaLinea')
archivoTxt('imprimir')
archivoTxt('borrar')
archivoTxt('crearEnVariasLineas')
archivoTxt('imprimir')
archivoTxt('borrar')

// ---------------------------------------------- DIFICULTAD EXTRA ----------------------------------------------
import readline from 'readline' // importe fs arriba

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

function actualizarDatos(info) { // borra la base de datos y la vuelve a crear con los estos actualizados
  let i = 0
  while (i < info.length) {
    if (i === 0) {
      fs.unlinkSync('./productos.txt')
      fs.writeFileSync('productos.txt', `[${info[i++]}], [${info[i++]}], [${info[i++]}]`) // lo ordena por nombre,cantidad vendida,precio
    } else {
      fs.appendFileSync('productos.txt', `\n[${info[i++]}], [${info[i++]}], [${info[i++]}]`)
    }
  }
}

async function consultar() {
  let consultar = await preguntar('Ingrese "todo" o el "nombre de producto" según lo que quiera consultar: ')
  if (consultar === 'todo') {
    console.log(fs.readFileSync('productos.txt', 'utf8').replaceAll('[', '').replaceAll(']', '')) // imprime toda la base de datos
  } else {
    let info = fs.readFileSync('productos.txt', 'utf8').replaceAll("\n", ',').replace(/[\[\]\s]/g, '').split(',') // transforma el string de datos en un array con todos ellos separados
    console.log(info)
    if (info.includes(consultar)) {
      index = info.indexOf(consultar) // busca el index del nombre del producto
      console.log(`${consultar}, ${info[++index]}, ${info[++index]}`) // al index del producto se le suma 1 para saber la cantidad vendida y 2 para el precio
    } else console.log('El producto no existe')
  }
}

async function actualizar() {
  let producto = await preguntar('Ingrese el nombre del producto que desea actualizar: ')
  let info = fs.readFileSync('productos.txt', 'utf8').replaceAll("\n", ',').replace(/[\[\]\s]/g, '').split(',') // transforma el string de datos en un array con todos ellos separados
  if (info.includes(producto)) {
    let update
    do {
      update = await preguntar('Que desea actualizar precio o cantidad?' + "\n")
      if (update === 'precio') {
        let precio = await preguntar('Ingrese el nuevo precio: ')
        info.splice(info.indexOf(producto) + 2, 1, precio) // remplaza el precio viejo por el nuevo
      } else if (update === 'cantidad') {
        let cantidad = await preguntar('Ingrese la nueva cantidad de ventas: ')
        info.splice(info.indexOf(producto) + 1, 1, cantidad)// remplaza la cantidad vendida vieja por la nueva
      }
    } while (update !== 'precio' && update !== 'cantidad')
    console.log(info)
    actualizarDatos(info)
    console.log('Producto actualizado')
  } else console.log('El producto no existe')
}

async function borrar() {
  let producto = await preguntar('Ingrese el nombre del producto que quiere borrar: ')
  let info = fs.readFileSync('productos.txt', 'utf8').replaceAll("\n", ',').replace(/[\[\]\s]/g, '').split(',') // transforma el string de datos en un array con todos ellos separados
  if (info.includes(producto)) {
    index = info.indexOf(producto)
    info = info.slice(0,index).concat(info.slice(index + 3)) // al array de productos los separa en dos dejando fuera el producto que se desea eliminar y une las otras dos partes
    actualizarDatos(info)
  } else console.log('El producto no existe')
}

async function calcular() {
  let calc = await preguntar('Ingresa:' + '\n' + 'total --> si queres calcular el total recaudado' + '\n' + 'producto --> si queres calcular lo recaudado de un producto' + '\n' + 'cantidad --> si queres calcular toda la cantidad vendida' + "\n")
  let result = 0
  let info = fs.readFileSync('productos.txt', 'utf8').replaceAll("\n", ',').replace(/[\[\]\s]/g, '').split(',') // transforma el string de datos en un array con todos ellos separados
  if (calc === 'total') {
    for (let i = 4; i < info.length; i++) { // empieza en 4 ya que los primero 3 valores son palabras y el cuarto es el nombre del primer producto
      result = result + (parseInt(info[i]) * parseInt(info[++i]))
      ++i
    }
    console.log(`El total recaudado es de: $${result}`)
  } else if (calc === 'producto') {
    let producto = await preguntar('Ingrese el nombre del producto: ')
    if (info.includes(producto)) {
      let index = info.indexOf(producto)
      console.log(`Lo recaudado de ${producto} es $${parseInt(info[++index]) * parseInt(info[++index])}`)
    } else {
      console.log('El producto no existe')
    }
  } else if (calc === 'cantidad') {
    for (let i = 4; i < info.length; i++) { // empieza en 4 ya que los primero 3 valores son palabras y el cuarto es el nombre del primer producto
      result = result + parseInt(info[i])
      i = i + 2
    }
    console.log(`Se han vendido ${result} productos`)
  }
}

async function program(operacion) {
  switch (operacion) {
    case 'añadir':
      let addProducto = await preguntar('Ingrese el nombre del producto: ')
      let addCantidadVendida = await preguntar('Ingrese la cantidad de ventas del producto: ')
      let addPrecio = await preguntar('Ingrese el precio del producto: ')
      fs.appendFileSync('productos.txt', `\n[${addProducto}], [${addCantidadVendida}], [${addPrecio}]`)
      console.log('El pruducto se ha añadido')
      break;
    case 'consultar':
      await consultar()
    break;
    case 'actualizar':
      await actualizar()
      break;
    case 'borrar':
      await borrar()
      break;
    case 'calcular':
      await calcular()
      break;
    case 'salir':
      fs.unlinkSync('./productos.txt')
      break;
    default:
      console.log('La operacion no existe')
      break;
  }
}

async function start() {
  fs.writeFileSync('productos.txt', `[Producto], [Cantidad-Vendida], [Precio]`)
  let operacion
  do {
    operacion = await preguntar('Que operación desea realizar? (añadir, consultar, actualizar, borrar, calcular, salir)' + "\n")
    await program(operacion)
  } while (operacion !== 'salir')
}

start()