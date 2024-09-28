// Si quieres ver que es fs y propiedades https://www.w3schools.com/nodejs/nodejs_filesystem.asp

const fs = require("fs");

// fs.writeFile('DavidMoralesDeveloper.txt', 'Nombre: David \nEdad: 30 \nLenguaje : javascript', function(error){
//     if(error) console.log(error, 'ocurrio un error ')
//     console.log('Fue creado satisfactoriamente')
// })

// Imprimir

// fs.readFile('DavidMoralesDeveloper.txt', function ( error, data){
// if (error) console.log(error + 'algo salio mal')
// return console.log(data.toString()) //tostring para que me imprima correctamente
// // me da como respuesta (data) <Buffer 4e 6f 6d 62 72 ...> se corrige con utf8
// })

// eliminar

// fs.unlink('DavidMoralesDeveloper.txt', function(err){
//     if (err) throw err;
//     console.log('documento eliminado')
// })

// Extra
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function miTiendita() {
  function miAcciones(respuesta) {
    if (respuesta == 1) {
      rl.question("¿cual es el nombre del producto? ", (nombre) => {
        rl.question("¿cual es la cantidad del producto? ", (cantidad) => {
          rl.question("¿cual es el precio de el producto? ", (precio) => {
            fs.appendFile(
              "miTienda.txt",
              `${nombre}, ${cantidad}, ${precio}\n`,
              (error) => {
                if (error) throw error;
                console.log("fueron agregados exitosamente: " + nombre);
                gestionDeInventario();
              }
            );
          });
        });
      });
    } else if (respuesta == 2) {
      rl.question("Nombre de producto que buscas : ", (producto) => {
        fs.readFile("miTienda.txt", (error, data) => {
          if (error) throw error;
          const allData = data.toString().split("\n");
          const resultado = allData.find(
            (line) => line.split(",")[0] === producto
          );
          if (resultado) {
            console.log(`Producto encontrado: ${resultado}`);
          } else {
            console.log(`Producto "${producto}" no encontrado.`);
          }

          gestionDeInventario();
        });
      });
    } else if (respuesta == 3) {
      rl.question("Nombre de producto que actualizaras : ", (producto) => {
        fs.readFile("miTienda.txt", "utf8", (error, data) => {
          if (error) throw error;
          let lines = data.split("\n");
          let lineIndex = lines.findIndex(
            (line) => line.split(",")[0] === producto
          );

          if (lineIndex !== -1) {
            rl.question("¿Cuál es el nuevo nombre del producto? ", (nombre) => {
              rl.question(
                "¿Cuál es la nueva cantidad del producto? ",
                (cantidad) => {
                  rl.question(
                    "¿Cuál es el nuevo precio del producto? ",
                    (precio) => {
                      lines[lineIndex] = `${nombre}, ${cantidad}, ${precio}`;
                      const updatedLines = lines.join("\n");
                      fs.writeFile("miTienda.txt", updatedLines, (error) => {
                        if (error) throw error;
                        console.log("El archivo fue actualizado exitosamente.");
                        gestionDeInventario();
                      });
                    }
                  );
                }
              );
            });
          } else {
            console.log(`Producto "${producto}" no encontrado.`);
          }

          gestionDeInventario();
        });
      });
    } else if (respuesta == 4) {
      rl.question("Nombre de el producto que desea eliminar: ", (producto) => {
        fs.readFile("miTienda.txt", "utf8", (error, data) => {
          if (error) throw error;
          const lines = data.split("\n");
          const buscar = lines.find((line) => line.split(",")[0] === producto);
          if (buscar) {
            const upDateLines = lines.filter((line) => {
              const [name] = line.split(",");
              return name !== producto;
            });
            const deleteProduct = upDateLines.join("\n");
            fs.writeFile("miTienda.txt", deleteProduct, (error) => {
              if (error) throw error;
              console.log("se borro exitosamente");
              gestionDeInventario();
            });
          } else {
            console.log(`${producto} no encontrado`);
          }
          gestionDeInventario();
        });
      });
    } else if (respuesta == 5) {
      rl.question(
        "Producto que desea calcular su valor total: ",
        (producto) => {
          fs.readFile("miTienda.txt", "utf8", (error, data) => {
            if (error) throw error;
            const lines = data.split("\n");
            const busquedaDeProduc = lines.find(
              (line) => line.split(",")[0] == producto
            );
            if (busquedaDeProduc) {
              const cantidadDeProducto = busquedaDeProduc.split(",")[1];
              const valorXproduc = busquedaDeProduc.split(",")[2];
              console.log(
                `El valor total del producto: ${producto} es = ${
                  cantidadDeProducto * valorXproduc
                }` 
              );

              gestionDeInventario();
            } else {
              console.log(
                `${producto} no existe intenta denuevo consulta el #8 para ver todos los productos`
              );
            }
            gestionDeInventario();
          });
        }
      );
    } else if (respuesta == 6) {
      fs.readFile("miTienda.txt", "utf8", (error, data) => {
        if (error) throw error;
        const lines = data.split("\n");
        const cantidadDeProducto = lines.map(
          (line) => parseInt(line.split(",")[1]) * parseInt(line.split(",")[2])
        );
        // console.log(cantidadDeProducto)
        const sumacantidad = cantidadDeProducto.reduce((sum, act) => sum + act);
        return console.log(`El valor de todos los productos sumados es de ${sumacantidad} `);
        
        
      });
      gestionDeInventario();
    } else if (respuesta == 7) {
      fs.unlink("miTienda.txt", function (err) {
        if (err) throw err;
        rl.close();
        console.log("salir y borraer el miTienda.txt");
      });
      
    } else if (respuesta == 8) {
      fs.readFile("miTienda.txt", (error, data) => {
        if (error) throw error;
        console.log(data.toString());
        gestionDeInventario();
      });
    } else {
      console.log("Seleccione un numero de las acciones permitidas");
    }
  }

  function gestionDeInventario() {
    rl.question(
      " Selecciona un numero: 1. Añadir un producto, 2. Consultar un producto, 3.Actualizar, 4.Eliminar, 5.Calcular Venta Por Producto, 6.Calcular Venta Totla, 7.Salir, 8.Mostrar Productos. - Respuesta: ",
      (respuesta) => {
        miAcciones(respuesta);
        if (respuesta !== 7) {
          gestionDeInventario();
        }
      }
    );
  }

  gestionDeInventario();
}

miTiendita();
