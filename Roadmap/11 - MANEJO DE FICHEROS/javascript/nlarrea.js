/*
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
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */


const fs = require('fs');

let filePath = 'nlarrea.txt';
const data = [
    'Name: Naia',
    'Age: 25',
    'Favorite programming language: JavaScript'
];

// Write data to the file
fs.writeFileSync(filePath, data.join('\n'));
console.log('The file has been written successfully!');

// Read the file and print the content
const readData = fs.readFileSync(filePath, 'utf-8');
console.log('\nPrinting read data:');
console.log(readData);

// Remove the file
fs.unlinkSync(filePath);
console.log('\nThe file has been removed.');


/*
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */


const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

filePath = 'sales.txt';

function askOption(options) {
    console.log('\nMENU');
    for (let i = 0; i < options.length; i++) {
        console.log(`${i}. ${options[i]}`);
    }
}


function run() {
    const options = [
        'Exit',
        'Add products',
        'See single product',
        'See all products',
        'Update products',
        'Remove products',
        'Calculate total sales',
        'Calculate sales by product'
    ];

    askOption(options);
    
    rl.question('What do you want to do?\n> ', option => {
        try {
            // Check if the option is valid
            if (isNaN(option)) {
                throw new Error('The selected option must be a number.');
            }
            
            option = parseInt(option);
            
            if (option < 0 || option > options.length - 1) {
                throw new Error(`Chosen option must be a number between 0-${len(options) - 1}!`)
            }

            // Run
            console.log('\nChosen option:', options[option], '\n');
    
            if (option === 0) {
                // EXIT

                rl.close();
                fs.unlinkSync(filePath);
                return;

            } else if (option === 1) {
                // ADD PRODUCTS

                rl.question('Product name:\n > ', productName => {
                    rl.question('Amount sold:\n > ', amountSold => {
                        amountSold = parseInt(amountSold);
                        if (isNaN(amountSold)) {
                            throw new Error('Amount Sold must be a number.')
                        }

                        rl.question('Price:\n > ', price => {
                            price = parseFloat(price);
                            if (isNaN(price)) {
                                throw new Error('Price must be a number.')
                            }
                            
                            const newProduct = `${productName}, ${amountSold}, ${price}\n`;
                            fs.appendFileSync(filePath, newProduct);

                            run();
                        });
                    });
                });

            } else if (option === 2) {
                // SEE SINGLE PRODUCT

                rl.question('Product name:\n > ', productName => {
                    const products = fs.readFileSync(filePath, 'utf-8').split('\n');

                    for (let productData of products) {
                        const name = productData.split(', ')[0].trim();

                        if (name === productName.trim()) {
                            console.log('\n', productData);
                        }
                    }

                    run();
                });
            } else if (option === 3) {
                // SEE ALL PRODUCTS

                console.log(fs.readFileSync(filePath, 'utf-8'));
                run();

            } else if (option === 4) {
                // UPDATE PRODUCT

                rl.question('Product name:\n > ', productName => {
                    rl.question('New amount sold:\n > ', newAmount => {
                        newAmount = parseInt(newAmount);
                        if (isNaN(newAmount)) {
                            throw new Error('Amount Sold must be a number.')
                        }

                        rl.question('New price:\n > ', newPrice => {
                            newPrice = parseFloat(newPrice);
                            if (isNaN(newPrice)) {
                                throw new Error('Price must be a number.')
                            }

                            const products = fs.readFileSync(filePath, 'utf-8').split('\n');
                            fs.unlinkSync(filePath)
                            for (let productData of products) {
                                const name = productData.split(', ')[0].trim();

                                if (name === productName.trim()) {
                                    const updatedData = `${productName}, ${newAmount}, ${newPrice}\n`
                                    fs.appendFileSync(filePath, updatedData);
                                } else {
                                    fs.appendFileSync(filePath, `${productData.trim()}\n`);
                                }
                            }

                            run();
                        });
                    });
                });

            } else if (option === 5) {
                // REMOVE PRODUCT

                rl.question('Product name:\n > ', productName => {
                    const products = fs.readFileSync(filePath, 'utf-8').split('\n');
                    
                    fs.unlinkSync(filePath);
                    for (let productData of products) {
                        const name = productData.split(', ')[0].trim();

                        if (name !== productName.trim()) {
                            fs.appendFileSync(filePath, `${productData.trim()}\n`);
                        }
                    }

                    run();
                });
            } else if (option === 6) {
                // CALCULATE TOTAL SALES

                const products = fs.readFileSync(filePath, 'utf-8').split('\n');

                let sales = 0;
                for (let productData of products) {
                    const [_, amount, price] = productData.split(', ');

                    if (amount !== undefined && price !== undefined) {
                        sales += parseInt(amount) * parseFloat(price);
                    }
                }

                console.log('Total sales:', sales);

                run();
            } else if (option === 7) {
                // CALCULATE SINGLE PRODUCT'S SALES

                rl.question('Product name:\n > ', productName => {
                    const products = fs.readFileSync(filePath, 'utf-8').split('\n');

                    for (let productsData of products) {
                        const [name, amount, price] = productsData.split(', ');

                        if (name === productName.trim()) {
                            console.log('Product sales:', parseInt(amount) * parseFloat(price));
                            break;
                        }
                    }

                    run();
                });
            } else {

            }
        } catch (error) {
            console.error(error);

            rl.question('\nPress any KEY to continue.', () => {run()});
        }
    });
}

run();