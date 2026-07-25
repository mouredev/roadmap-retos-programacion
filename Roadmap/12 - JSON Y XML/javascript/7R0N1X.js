const fs = require('fs');
const xml2js = require('xml2js');

const datos = {
  nombre: 'Eduardo Molina',
  edad: 25,
  fechaNacimiento: '30-08-1999',
  lenguajes: ['JavaScript', 'Python', 'Java']
};

const crearJSON = () => {
  fs.writeFileSync('datos.json', JSON.stringify(datos, null, 2), 'utf-8');
  console.log('Archivo JSON creado:\n', fs.readFileSync('datos.json', 'utf-8'));
};

const crearXML = () => {
  const builder = new xml2js.Builder({ headless: true, rootName: 'persona' });
  const xml = builder.buildObject({
    nombre: datos.nombre,
    edad: datos.edad,
    fechaNacimiento: datos.fechaNacimiento,
    lenguajes: { lenguaje: datos.lenguajes }
  });
  fs.writeFileSync('datos.xml', xml, 'utf-8');
  console.log('Archivo XML creado:\n', fs.readFileSync('datos.xml', 'utf-8'));
};


class Persona {

  constructor(nombre, edad, fechaNacimiento, lenguajes) {
    this.nombre = nombre;
    this.edad = edad;
    this.fechaNacimiento = fechaNacimiento;
    this.lenguajes = lenguajes;
  }

  mostrarDatos() {
    console.log(`Nombre: ${this.nombre}`);
    console.log(`Edad: ${this.edad}`);
    console.log(`Fecha de Nacimiento: ${this.fechaNacimiento}`);
    console.log(`Lenguajes: ${this.lenguajes.join(', ')}`);
  }
}

const leerYTransformarJSON = () => {
  const dataJSON = fs.readFileSync('datos.json', 'utf-8');
  const datosJSON = JSON.parse(dataJSON);
  const personaJSON = new Persona(
    datosJSON.nombre,
    datosJSON.edad,
    datosJSON.fechaNacimiento,
    datosJSON.lenguajes
  );
  console.log('\nDatos leídos del archivo JSON:');
  personaJSON.mostrarDatos();
};

const leerYTransformarXML = () => {
  const dataXML = fs.readFileSync('datos.xml', 'utf-8');
  xml2js.parseString(dataXML, (err, result) => {
    if (err) throw err;
    const datosXML = result.persona;
    const personaXML = new Persona(
      datosXML.nombre[0],
      datosXML.edad[0],
      datosXML.fechaNacimiento[0],
      datosXML.lenguajes[0].lenguaje
    );
    console.log('\nDatos leídos del archivo XML:');
    personaXML.mostrarDatos();
  });
};

const borrarArchivos = () => {
  fs.unlinkSync('datos.json');
  fs.unlinkSync('datos.xml');
  console.log('\nArchivos borrados.');
};

crearJSON();
crearXML();
leerYTransformarJSON();
leerYTransformarXML();
borrarArchivos();