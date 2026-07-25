// Módulos requeridos, necesitamos este paquete https://github.com/archiverjs/node-archiver
const fs = require("fs")
const archiver = require("archiver")

// Crear un flujo de escritura para el archivo ZIP de salida
const output = fs.createWriteStream(__dirname + "/archivo.zip")
const archive = archiver("zip", {
  zlib: { level: 9 }, // Establece el nivel de compresión
})

// Comprobar si hay errores
archive.on("error", function (err) {
  throw err
})

// Redirigir los datos del archivo comprimido al archivo de salida
archive.pipe(output)

// Agregar archivos al archivo comprimido
archive.file("/path/to/file0.txt", {
  name: "file0-or-change-this-whatever.txt", // Nuevo nombre en el archivo ZIP
})
archive.file("example.txt", { name: "example.txt" })

// Finalizar el archivo comprimido (no olvides escuchar el evento close)
archive
  .finalize()
  .then(() => {
    console.log("Archivo comprimido finalizado con éxito.")
  })
  .catch((err) => {
    console.error("Error al finalizar el archivo comprimido:", err)
  })

// Opcionalmente, escuchar el evento finish del flujo de salida
output.on("close", function () {
  console.log(archive.pointer() + " bytes totales escritos en archivo.zip")
})
