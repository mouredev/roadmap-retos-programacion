const fsPromises = require('fs').promises;
const fileName = "parababire.txt";

const fileOps = async () => {
  try {
    await fsPromises.writeFile(fileName, 'Ángel Narváez');//Crear archivo.
    const data = await fsPromises.readFile(fileName, 'utf8');//Leer Archivo.
    console.log(data);
    await fsPromises.appendFile(fileName, '\n36\nJavascript');//Agregar contenido.
    const newData = await fsPromises.readFile(fileName, 'utf8');
    //await fsPromises.unlink(fileName);
    console.log(newData);
  } catch (error) {
    console.error(error);
  }
}
fileOps();

const finalArchivo = async () => {
  try {
    await fsPromises.unlink(fileName);
  } catch (error) {
    console.error(error);
  }
}
setTimeout(finalArchivo, 5000);
