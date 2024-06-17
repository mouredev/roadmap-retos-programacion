// ** EJERCICIO

const fs = require('node:fs');
const { stringify } = require('node:querystring');

const contenido = 'Nombre: Bernat\nEdad: 22\nLenguaje de progamación favorito: MaxMSP'

const fileName = 'bernatcs.txt'

fs.writeFile(fileName, contenido, (err) => {
        if (err) {
        console.error('Error al escribir el archivo', err);
        return;
        }
        console.log(`El archivo ${fileName} ha sido creado correctamente.`)
})

// ** DIFICULTAD EXTRA ** -------------------------------------------------------------------------------------------------------------------------------------------------

let gestionVentas = []

function createFile() {
    fs.writeFile('gestion-ventas.txt', 'Este es el documento de gestion de ventas. A continuación se observan los productos ordenados de la siguiente manera:\n[nombre_producto], [cantidad_vendida], [precio].', (err) => {
        if (err) {
            console.error('Error al escribir el archivo', err);
            return;
        }
    })
}

// function addProducto(nombre_producto, cantidad_vendida, precio){
//     gestionVentas.push([nombre_producto, cantidad_vendida, precio])
    
// }

// addProducto('Ordenador', 40, 1200)


const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let textoInicio = false

function gestionVentasInit(){
    if (!textoInicio) {
        readline.question('Bienvenido al programa de gestión de ventas que almacena los datos en el archivo gestión-ventas.txt.\nPodrá ejecutar los siguientes comandos:\n[nuevo]: Donde debe introducir el nuevo producto, seguidamente, la cantidad vendida y finalmente el precio.\n[consultar]: Donde puede consultar por nombre del producto las demás características.\n[actualizar]: Donde podrá actualizar los datos de los productos (incluido el precio completo).\n[eliminar]: Donde podrá eliminar productos.\n[total]: Para saber cuál es el precio total.\n[salir]: Saldrá del programa y el txt se desvanecerá como si nunca hubiera existido.\nIntroduce el comando: ', (respuesta) => {
            gestionVentasPreguntas(respuesta)
        });
        textoInicio = true
    } else {
        readline.question('', (respuesta) => {
            gestionVentasPreguntas(respuesta)
        });
    }
}

function gestionVentasPreguntas(respuesta) {
    switch (respuesta) {
        case 'nuevo':
            readline.question('Introduce el nombre del producto: ', (nombre_producto) => {
                readline.question('Introduce la cantidad vendida: ', (cantidad_vendida) => {
                    readline.question('Introduce el precio: ', (precio) => {
                        gestionVentas.push([nombre_producto, cantidad_vendida, precio]);
                        fs.appendFile("gestion-ventas.txt", `\n${gestionVentas[gestionVentas.length-1]}`, (err) => {
                            if (err) {
                                console.error(err)
                            }
                        })
                        console.log(`Producto ${nombre_producto} agregado correctamente.`);
                        gestionVentasInit();
                    });
                });
            });
            break;
        case 'consultar':
            // Lógica para consultar productos
            console.log('Comando consultar');
            gestionVentasInit();
            break;

        case 'actualizar':
            // Lógica para actualizar productos
            console.log('Comando actualizar');
            gestionVentasInit();
            break;

        case 'eliminar':
            // Lógica para eliminar productos
            console.log('Comando eliminar');
            gestionVentasInit();
            break;

        case 'total':
            // let sumaTotal = 0
            // gestionVentas.forEach(element => {
            //     sumaTotal += gestionVentas.precio
            // });
            // console.log(`La cantidad completa es: ${sumaTotal}`);
            console.log('Comando total');
            gestionVentasInit();
            break;

        case 'salir':
            fs.unlink('gestion-ventas.txt', (err) => {
                if (err) {
                    console.error(`Error al eliminar el archivo 'gestion-ventas.txt':`, err);
                    return;
                }
                console.log(`El archivo 'gestion-ventas.txt' ha sido eliminado correctamente.`);
                readline.close(); // Cierra la interfaz readline
            });
            break;

        default:
            console.log('Comando no reconocido. Por favor, introduce uno válido.');
            gestionVentasInit();
    }
}


createFile()
gestionVentasInit()




// El código se podría mejorar incluyendo validaciones de los datos, pero ya no tenía tiempo ni ganas