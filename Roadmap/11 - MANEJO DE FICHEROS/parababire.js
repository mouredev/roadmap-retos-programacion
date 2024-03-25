//const prompt = require('prompt-sync')();
//const fsPromises = require('fs').promises;
const fs = require('fs');
const readline = require('readline');
const userName = "parababire";
const fileName = `${userName}.txt`;
const fileContent = "Nombre: Ángel Narváez.\n Edad: 44 años.\n Lenguaje de programación: Javascript."

/*const fileOps = async () => {
  try {
    await fsPromises.writeFile(fileName, fileContent);//Crear archivo.
    const data = await fsPromises.readFile(fileName, 'utf8');//Leer Archivo.
    console.log(data);
    await fsPromises.appendFile(fileName, '\nHello World');//Agregar contenido.
    const newData = await fsPromises.readFile(fileName, 'utf8');
    console.log(newData);
  } catch (error) {
    console.error(error);
  }
}


const finalArchivo = async () => {
  try {
    await fsPromises.unlink(fileName);//Borrar archivo.
  } catch (error) {
    console.error(error);
  }
}
setTimeout(finalArchivo, 5000);*/

//Extra
let rl = readline.createInterface(process.stdin, process.stdout);

const writeFile = async (name, quantity, price) => {
  try {
    await fsPromises.writeFile(fileName, `${name + ", " + quantity + ", " + price + "\n"}`);//Crear archivo.
    /*const data = await fsPromises.readFile(fileName, 'utf8');//Leer Archivo.
    console.log(data);*/
  } catch (error) {
    console.error(error);
  }
}
const readFile = async () => {
  try {
    /*await fsPromises.writeFile(fileName, `${name + quantity + price}`);//Crear archivo.*/
    const data = await fsPromises.readFile(fileName, 'utf8');//Leer Archivo.
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}

const menu = () => {
  console.log("");
  console.log("1.- Anadir producto");
  console.log("2.- Consultar producto");
  console.log("3.- Actualizar producto");
  console.log("4.- Borrar producto");
  console.log("5.- Calcular venta total");
  console.log("6.- Calcular venta por producto");
  console.log("7.- Salir");
  selecionarOperacion();
}

const selecionarOperacion = () => {
  rl.question("Elige una opción ", opcion => {
    switch (opcion) {
      case "1":
        rl.question("Nombre del producto ", nombre => {
          rl.question("Cantidad del producto ", cantidad => {
            rl.question("Precio del producto ", precio => {
              const producto = `${nombre + ", " + cantidad + ", " + precio}`;
              fs.writeFile("producto.txt", producto, err => {
                if (err) throw err;
                console.log("Producto creado");
                menu();
                selecionarOperacion();
              })
            });
          });
        });
        break;
      case "2":
        fs.readFile("producto.txt", "utf8", (err, data) => {
          if (err) throw err;
          console.log(data);
          menu();
          selecionarOperacion();
        });
        break;
      case "3":
        
        break;
      case "4":
        
        break;
      case "5":
        
        break;
      case "6":
        
        break;
      case "7":
        fs.unlink("producto.txt", err => {
          if (err) throw err;
          console.log("Saliste del programa");
        })
        rl.close(); 
        break;
    
      default:
        break;
    }
  });
}
menu();

