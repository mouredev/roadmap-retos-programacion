const fs = require('fs')
const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
})

/*
  * EJERCICIO:
  * Desarrolla un programa capaz de crear un archivo que se llame como
  * tu usuario de GitHub y tenga la extensión .txt.
  * Añade varias líneas en ese fichero:
  * - Tu nombre.
  * - Edad.
  * - Lenguaje de programación favorito.
  * Imprime el contenido.
  * Borra el fichero.
*/

fs.writeFileSync('victor-Casta.txt', 'Victor\n21\nJavaScript', 'utf8')
console.log(fs.readFileSync('victor-Casta.txt', 'utf8'))
fs.unlinkSync('victor-Casta.txt')

/*
  * DIFICULTAD EXTRA (opcional):
  * Desarrolla un programa de gestión de ventas que almacena sus datos en un
  * archivo .txt.
  * - Cada producto se guarda en una línea del archivo de la siguiente manera:
  *   [nombre_producto], [cantidad_vendida], [precio].
  * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
  *   actualizar, eliminar productos y salir.
  * - También debe poseer opciones para calcular la venta total y por producto.
  * - La opción salir borra el .txt.
*/

function promptInput(question: string): Promise<string> {
  return new Promise((resolve) => rl.question(question, (input) => resolve(input.trim())))
}

async function addProduct(): Promise<void> {
  const name = await promptInput('Nombre del producto: ')
  const quantity = await promptInput('Cantidad vendida: ')
  const price = await promptInput('Precio: ')

  fs.appendFileSync('sales.txt', `${name}, ${quantity}, ${price}\n`, 'utf8')
  console.log('✅ Producto añadido correctamente.')
  salesManagement()
}

async function consult(): Promise<void> {
  const name = await promptInput('Ingresa el nombre del producto a consultar: ')

  if (!fs.existsSync('sales.txt')) {
    console.log('⚠️ Archivo de ventas no encontrado.')
    return salesManagement()
  }

  const lines = fs.readFileSync('sales.txt', 'utf8').trim().split('\n')
  const foundProducts = lines.filter(line => line.toLowerCase().includes(name.toLowerCase()))

  if (foundProducts.length === 0) {
    console.log('❌ Producto no encontrado en la lista.')
  } else {
    foundProducts.forEach(product => {
      const [productName, quantity, price] = product.split(', ')
      console.log(`\nNombre: ${productName}\nCantidad vendida: ${quantity}\nPrecio: ${price}`)
    })
  }
  salesManagement()
}

async function updateProduct(): Promise<void> {
  const name = await promptInput('Nombre del producto a actualizar: ')

  if (!fs.existsSync('sales.txt')) {
    console.log('⚠️ Archivo de ventas no encontrado.')
    return salesManagement()
  }

  const lines = fs.readFileSync('sales.txt', 'utf8').trim().split('\n')
  const productIndex = lines.findIndex(line => line.toLowerCase().includes(name.toLowerCase()))

  if (productIndex === -1) {
    console.log('❌ Producto no encontrado para actualizar.')
    return salesManagement()
  }

  const newQuantity = await promptInput('Nueva cantidad vendida: ')
  const newPrice = await promptInput('Nuevo precio: ')
  lines[productIndex] = `${name}, ${newQuantity}, ${newPrice}`

  fs.writeFileSync('sales.txt', lines.join('\n'), 'utf8')
  console.log('✅ Producto actualizado correctamente.')
  salesManagement()
}

async function deleteProduct(): Promise<void> {
  const name = await promptInput('Ingresa el nombre del producto a eliminar: ')

  if (!fs.existsSync('sales.txt')) {
    console.log('⚠️ Archivo de ventas no encontrado.')
    return salesManagement()
  }

  const lines = fs.readFileSync('sales.txt', 'utf8').trim().split('\n')
  const filteredProducts = lines.filter(line => !line.toLowerCase().includes(name.toLowerCase()))

  if (filteredProducts.length === lines.length) {
    console.log('❌ Producto no encontrado en la lista.')
  } else {
    fs.writeFileSync('sales.txt', filteredProducts.join('\n'), 'utf8')
    console.log('✅ Producto eliminado correctamente.')
  }
  salesManagement()
}

function displayMenu(): void {
  console.log('\n--- Gestión de Ventas ---')
  console.log('1 - Añadir Producto')
  console.log('2 - Consultar Producto')
  console.log('3 - Actualizar Producto')
  console.log('4 - Eliminar Producto')
  console.log('0 - Salir')
}

async function salesManagement(): Promise<void> {
  displayMenu()

  const option = await promptInput('Seleccione una opción: ')
  switch (option) {
    case '1':
      await addProduct()
      break
    case '2':
      await consult()
      break
    case '3':
      await updateProduct()
      break
    case '4':
      await deleteProduct()
      break
    case '0':
      console.log('Saliendo del programa...')
      rl.close()
      fs.unlinkSync('sales.txt')
      break
    default:
      console.log('⚠️ Opción no válida. Intente nuevamente.')
      salesManagement()
  }
}

salesManagement()