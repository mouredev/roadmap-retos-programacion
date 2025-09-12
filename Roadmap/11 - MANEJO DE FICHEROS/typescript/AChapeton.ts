import { error } from "console"

const fs = require('fs')
const readlineSync = require('readline-sync');

//writeFile permite escribir en un fichero, y tambien lo crea si este aun no existe
fs.writeFile(
  'achapeton.txt', 
  `
    - Nombre: Andres Chapeton
    - Edad: 26
    - Lenguaje favorito: TypeScript
  `, 
  (error:  NodeJS.ErrnoException | null) => {
  if(error) throw error
  console.log('File created')
})

//Leer contenido del fichero
fs.readFile('achapeton.txt', (error:  NodeJS.ErrnoException | null, data: any) => {
  if(error) throw error
  console.log(data.toString())
})

//Eliminar un fichero
fs.unlink('achapeton.txt', (error:  NodeJS.ErrnoException | null) => {
  if(error) throw error
  console.log('File deleted')
})



// DIFICULTAD EXTRA

const guardarVenta = () => {
  const nombreProducto: string = readlineSync.question('Nombre del producto ');
  const cantidadVendida: number = readlineSync.question('Cantidad vendida: ');
  const precioTotal: string = readlineSync.question('Precio: ');
  fs.appendFile(
    'ventas.txt', 
    `${nombreProducto}, ${cantidadVendida}, $${precioTotal}]`
    , 
    (error:  NodeJS.ErrnoException | null) => {
    if(error) throw error
  })
}
const listarVentas = () => {
  fs.readFile('ventas.txt', (error:  NodeJS.ErrnoException | null, data: any) => {
    if(error) throw error
    console.log(data.toString())
  })
}

const gestionarVentas = () => {
  let option: string | null = ''
  const menu: string = 'MENU: \n 1. Agregar nueva venta \n 2. Listar ventas \n 3. Salir \n Escoger una opcion: '

  while (option !== '3') {
    option = readlineSync.question(menu)

    switch (option) {
      case '1':
        guardarVenta()
        break;
      case '2':
        listarVentas()
        break;
      case '3':
        fs.unlink('ventas.txt', (error:  NodeJS.ErrnoException | null) => {
          if(error) throw error
          console.log('Fichero eliminado')
        })
        break;
      default:
        console.log('Opcion no valida. Intentar de nuevo.')
        break;
    }
  }
}

gestionarVentas()