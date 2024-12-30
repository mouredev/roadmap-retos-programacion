/*
_____________________________________
https://github.com/kenysdev
2024 - JavaScript
_______________________________________
#11 MANEJO DE FICHEROS
---------------------------------------
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un
 * archivo .txt.
 * - Cada producto se guarda en una línea del arhivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
*/

// ________________________________________________________
const fs = require("fs/promises");
const path = require("path");

class File {
    constructor(filePath) {
        this._path = filePath;
    }

    async writeLine(line) {
        try {
            await fs.appendFile(this._path, line + "\n");
        } catch (error) {
            console.error("Error -> writeLine ->", error.message);
        }
    }

    async writeLines(lines) {
        try {
            await fs.writeFile(this._path, lines.join("\n"));
        } catch (error) {
            console.error("Error -> writeLines ->", error.message);
        }
    }

    async readLine() {
        try {
            const data = await fs.readFile(this._path, "utf-8");
            const lines = data.split("\n").filter(Boolean);
            return lines[lines.length - 1] || null;
        } catch (error) {
            console.error("Error -> readLine ->", error.message);
            return null;
        }
    }

    async readLines() {
        try {
            const data = await fs.readFile(this._path, "utf-8");
            return [...data.split("\n").filter(Boolean)];
        } catch (error) {
            console.error("Error -> readLines ->", error.message);
            return [];
        }
    }

    async deleteFile() {
        try {
            await fs.unlink(this._path);
            console.log(`${this._path} -> eliminado.`);
        } catch (error) {
            console.error("Error -> deleteFile ->", error.message);
        }
    }

    async printAll() {
        try {
            const data = await fs.readFile(this._path, "utf-8");
            console.log(data);
        } catch (error) {
            console.error("Error -> printAll ->", error.message);
        }
    }

    async queryFile(query) {
        try {
            const lines = await this.readLines();
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i];
                const productName = line.split(",")[0].trim();
                if (productName === `[${query}]`) {
                    console.log(line);
                    return i;
                }
            }
            console.log("No existe.");
            return null;
        } catch (error) {
            console.error("Error -> queryFile ->", error.message);
            return null;
        }
    }
}

// __________________________
async function ejmp() {
    const user = new File(path.resolve("kenysdev.txt"));
    await user.writeLine("Name: ken");
    await user.writeLine("Age: 121");
    await user.writeLine("PL: JS");
    await user.printAll();
    const name = await user.readLine()
    console.log(name);
    await user.deleteFile();
}

// ________________________________________________________
// DIFICULTAD EXTRA

const sale = new File(path.resolve("sale_mgt.txt"));

async function addProduct(product = null, qty = null, price = null) {
    while (true) {
        if (!product || !/^[a-zA-Z]+$/.test(product)) {
            console.log("Debe ingresar un nombre de producto válido.");
            product = await Input("Producto: ");
        } else if (!qty || !/^[0-9]+$/.test(qty)) {
            console.log("Debe ingresar una cantidad válida.");
            qty = await Input("Cantidad: ");
        } else if (!price || isNaN(parseFloat(price))) {
            console.log("Debe ingresar un precio válido.");
            price = await Input("Precio: ");
        } else {
            const line = `[${product}], [${qty}], [${price}]`;
            await sale.writeLine(line);
            console.log("\nGuardado.");
            return;
        }
    }
}

async function queryProduct(query = "") {
    if (!query) {
        query = await Input("\nConsultar Producto.\nNombre: ");
    }
    await sale.queryFile(query);
}

async function deleteProduct(query = "") {
    if (!query) {
        query = await Input("\nEliminar Producto.\nNombre: ");
    }
    const lineIndex = await sale.queryFile(query);
    if (lineIndex !== null) {
        const lines = await sale.readLines();
        lines.splice(lineIndex, 1);
        lines.push('')
        await sale.writeLines(lines);
        console.log("Producto eliminado");
    }
}

async function updateProduct(query = "") {
    if (!query) {
        query = await Input("\nEditar Producto.\nNombre: ");
    }
    const lineIndex = await sale.queryFile(query);
    if (lineIndex !== null) {
        const lines = await sale.readLines();
        console.log("Ingrese los nuevos datos del producto:");
        await addProduct();
        lines[lineIndex] = await sale.readLine();
        lines.push('')
        await sale.writeLines(lines);
    }
}

async function invoice() {
    console.log("\nFactura\n-------------------------");
    const lines = await sale.readLines();
    let totalAmount = 0;

    for (const line of lines) {
        const [product, qty, price] = line.split(",").map(item => item.trim().replace(/\[|\]/g, ""));
        const subTotal = parseInt(qty) * parseFloat(price);
        console.log(`${line} -> $${subTotal.toFixed(2)}`);
        totalAmount += subTotal;
    }

    console.log("\nMonto Total -> $" + totalAmount.toFixed(2));
}

// __________________________
const menu = (`
        Gestión de Ventas:
╔═════════════════════════════════╗
║ 1. Agregar        4. Editar     ║  
║ 2. Consultar      5. Facturar   ║
║ 3. Eliminar       6. Salir      ║
╚═════════════════════════════════╝
`);

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function Input(query) {
    return new Promise(resolve => rl.question(query, resolve));
}

(async () => {
    await ejmp();
    while (true) {
        console.log(menu)
        const option = await Input("\nOpción: ");
        switch (option) {
            case "1":
                await addProduct();
                break;
            case "2":
                await queryProduct();
                break;
            case "3":
                await deleteProduct();
                break;
            case "4":
                await updateProduct();
                break;
            case "5":
                await invoice();
                break;
            case "6":
                console.log("Adiós");
                await sale.deleteFile();
                rl.close();
                return;
            default:
                console.log("Seleccione una opción entre 1 y 6.");
        }
    }
})();
