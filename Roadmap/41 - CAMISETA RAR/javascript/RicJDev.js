/*
  EJERCICIO:

  - Para crear el archivo .zip se ha instalado la libreria 'adm-zip'.
  - Se ejecuta en Node.js, importando los modulos 'node:path' y 'node:url' para trabajar con rutas.

  @RicJDev
*/

import AdmZip from 'adm-zip'

import * as path from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const zip = new AdmZip()

try {
  const filePath = path.join(__dirname, './gatito.png')
  const zipName = 'fotos.zip'

  zip.addLocalFile(filePath)
  zip.writeZip(zipName)

  console.log(`Se ha creado el archivo ${zipName} de manera exitosa!`)
} catch (error) {
  console.error(error.message)
}
