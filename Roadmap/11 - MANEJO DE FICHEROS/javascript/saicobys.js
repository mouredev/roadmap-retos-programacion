const nombreUsuarioGitHub = "SaicoBys";
const fs = require("fs");
const nombreArchivo = `${nombreUsuarioGitHub}.txt`;

fs.writeFileSync(
  nombreArchivo,
  `Nombre: Jacob\nEdad: 24\nLenguaje de programacion favorito: JavaScript`
);

const contenido = fs.readFileSync(nombreArchivo, "utf-8");
console.log(contenido);

fs.unlinkSync(nombreArchivo);
