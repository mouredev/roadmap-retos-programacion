/** #11 - JavaScript ->Jesus Antonio Escamilla */
/**
 * Usando Node para poder realizar los ficheros en JavaScript
 */

//---EJERCIÓ SIMPLE---
// Extension de para realizar el archivo plano
const { error } = require('console');
const fs = require('fs');

// El contenido del archivo de texto
const nombre = "Jesus Antonio Escamilla Escamilla";
const edad = "24";
const lenguajeP = "JavaScript, Python, Java y C#"
const contenido = `Mi nombre es ${nombre} y mi edad es ${edad} y mi lenguaje de programación favorito es: ${lenguajeP}`;

// La Ruta y Nombre del archivo plano
const rutaArchivo = 'JesusAntonioEEscamilla.txt';

// Aquí hacemos un try-catch para evitar los errores
try {
    //  Aquí creamos el archivo con el contenido
    fs.writeFileSync(rutaArchivo, contenido);
    console.log('Archivo creado exitosamente el archivo plano.');
    console.log(fs.readFileSync(rutaArchivo, 'utf-8'));

    //  Aquí lo eliminamos el archivo plano
    fs.unlinkSync(rutaArchivo);
    console.log('Archivo eliminado correctamente el archivo plano.');
} catch (error) {
    console.error('Error al crear el archivo:', error);
}



/**-----DIFICULTAD EXTRA-----*/

//  Nuestras Variables que usaremos para leer la consola y para el texto plano
const readline = require('readline');

//  El Texto Plano
const venta = 'JesusAntonioEEscamilla_Venta.txt';

//  Obtener los datos
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


//  Para agregar en el texto plano
function agregarProducto() {
    rl.question("\nIngrese el nombre del producto: ", (nombre) => {
        rl.question("Ingrese la cantidad del producto: ", (cantidad) => {
            rl.question("Ingrese el precio del producto: ", (precio) => {
                const producto = `${nombre}, ${cantidad}, ${precio}\n`;
                try {
                    fs.appendFileSync(venta, producto);
                    console.log('\nSe agrego correctamente');
                    menuVenta();
                } catch (error) {
                    console.error('Error, no se puedo agregar:', error);
                }
            });
        });
    });
}

//  Consultar producto
function consultarProducto() {
    rl.question("\nIngrese el nombre del producto: ", (nombre) =>{
        let data = fs.readFileSync(venta, 'utf-8');
        let lines = data.split('\n');
        for (const producto of lines) {
            producto.split(', ')[0] === nombre
                ? console.log(`\n${producto}`)
                : false
        }
        menuVenta();
    });
}

//  Actualizar Producto
function actualizarProducto() {
    rl.question("\nIngrese el nombre del producto: ", (nombre) => {
        rl.question("Ingrese la cantidad del producto: ", (cantidad) => {
            rl.question("Ingrese el precio del producto: ", (precio) => {
                let data = fs.readFileSync(venta, 'utf-8');
                let lines = data.split('\n');
                let productoNuevo = '';
                for (const producto of lines) {
                    producto.split(', ')[0] === nombre 
                        ? productoNuevo += `${nombre}, ${cantidad}, ${precio}\n` 
                        : productoNuevo += `${producto}\n`
                }
                fs.writeFileSync(venta, productoNuevo);
                console.log('\nSe actualizo correctamente');
                menuVenta();
            });
        });
    });
}

//  Borrar el producto
function eliminarProducto() {
    rl.question("\nIngrese el nombre del producto: ", (nombre) => {
        let data = fs.readFileSync(venta, 'utf-8');
        let lines = data.split('\n');
        let productoNuevo = '';
        for (const producto of lines) {
            if (producto.split(', ') !== nombre) {
                productoNuevo += `\n${producto}`
            }
        }
        fs.writeFileSync(venta, productoNuevo, 'utf-8');
        console.log('\nSe elimino correctamente');
        menuVenta();
    });
}

//  Calcular la Venta Total
function totalVenta() {
    let total = 0;
    let data = fs.readFileSync(venta, 'utf-8');
    let lines = data.split('\n');
    for(const producto of lines){
        componentes = producto.split(', ');
        cantidad = parseFloat(componentes[1]);
        precio = parseFloat(componentes[2]);
        total += cantidad * precio;
    }
    console.log(`\nVenta Total es: ${total}`);
    menuVenta();
}

//  Calcular Venta Producto
function productoVenta() {
    rl.question('\nIngrese el nombre del producto: ', (nombre) =>{
        let total = 0;
        let data = fs.readFileSync(venta, 'utf-8');
        let lines = data.split('\n');
        for(const producto of lines){
            componentes = producto.split(', ');
            cantidad = parseFloat(componentes[1]);
            precio = parseFloat(componentes[2]);
            producto.split(', ')[0] === nombre 
                ? total += parseFloat(cantidad) * parseFloat(precio)
                : console.log('No se puedo calcular')
        }
        console.log(`\nVenta del Producto es: ${total}`);
        menuVenta();
    });
}

//  Se crea la lista del menu
function menuVenta() {
    console.log("\n--- Gestión de Ventas ---");
    console.log("1. Agregar producto");
    console.log("2. Consultar producto");
    console.log("3. Actualizar producto");
    console.log("4. Eliminar producto");
    console.log("5. Consultar todos los productos")
    console.log("6. Calcular venta total");
    console.log("7. Calcular venta por producto");
    console.log("8. Salir");

    rl.question("\nSelecciona una opción: ", (option) => {
        switch (option) {
            case '1':
                agregarProducto();
                break;
            case '2':
                consultarProducto();
                break;
            case '3':
                actualizarProducto();
                break;
            case '4':
                eliminarProducto();
                break;
            case '5':
                console.log("\nLos productos son los siguientes: \n" + fs.readFileSync(venta, 'utf-8'));
                menuVenta();
                break;
            case '6':
                totalVenta();
                break;
            case '7':
                productoVenta();
                break;
            case '8':
                try {
                    fs.unlinkSync(venta);
                    console.log("\nSe elimino correctamente");
                    rl.close();
                } catch (error) {
                    console.error('Se encontró un error: ', error);
                }
                rl.close();
                break;
            default:
                console.log("\nOpción no valida, por favor una opción valida");
                menuVenta();
                break;
        }
    });
}

//Inicia el programa
menuVenta();

/**-----DIFICULTAD EXTRA-----*/