const fs = require("fs");

// Datos a guardar
const datos = {
  nombre: "Oscar",
  edad: 29,
  fechaNacimiento: "11-09-1994",
  lenguajes: ["JavaScript", "Python"],
};

// Convertir datos a XML
const convertirAXML = (datos) => {
  let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
  xml += "<persona>\n";
  for (const key in datos) {
    if (Array.isArray(datos[key])) {
      xml += `<${key}>\n`;
      datos[key].forEach((item) => {
        xml += `<lenguaje>${item}</lenguaje>\n`;
      });
      xml += `</${key}>\n`;
    } else {
      xml += `<${key}>${datos[key]}</${key}>\n`;
    }
  }
  xml += "</persona>";
  return xml;
};

// Convertir datos a JSON
const convertirAJSON = (datos) => {
  return JSON.stringify(datos, null, 2);
};

// Crear archivos XML y JSON
fs.writeFileSync("datos.xml", convertirAXML(datos), "utf-8");
fs.writeFileSync("datos.json", convertirAJSON(datos), "utf-8");

// Mostrar contenido de archivos
console.log("Contenido de datos.xml:");
console.log(fs.readFileSync("datos.xml", "utf-8"));

console.log("\nContenido de datos.json:");
console.log(fs.readFileSync("datos.json", "utf-8"));

// Borrar archivos
fs.unlinkSync("datos.xml");
fs.unlinkSync("datos.json");

console.log("\nArchivos borrados.");
