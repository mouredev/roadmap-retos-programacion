// #11 { retosparaprogramadores } Manejo de Ficheros (File Handling in TypeScript)
// Bibliography:
// Professional JavaScript for Web Developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
// GPT & Deepseek

/**
 * The File Type
 * The File API is based around the file input field of a form but adds the ability to access file information directly.
 * HTML5 adds a `files` collection to the DOM for the file input element. When one or more files are selected,
 * the `files` collection contains a sequence of `File` objects representing each file. Each `File` object has several
 * read-only properties, including:
 * - `name`: The file name on the local system.
 * - `size`: The size of the file in bytes.
 * - `type`: A string containing the MIME type of the file.
 * - `lastModifiedDate`: A string representing the last time the file was modified (implemented only in Chrome).
 */

/**
 * The FileReader Type
 * The `FileReader` type represents an asynchronous file-reading mechanism. It is similar to `XMLHttpRequest`,
 * but it is used for reading files from the file system instead of reading data from a server. The `FileReader`
 * type offers several methods to read file data:
 * - `readAsText(file, encoding)`: Reads the file as plain text and stores the text in the `result` property.
 * - `readAsDataURL(file)`: Reads the file and stores a data URI representing the file in the `result` property.
 * - `readAsBinaryString(file)`: Reads the file and stores a string where each character represents a byte in the `result` property.
 * - `readAsArrayBuffer(file)`: Reads the file and stores an `ArrayBuffer` containing the file contents in the `result` property.
 */

// We will use Node.js to facilitate file manipulation. Run this file in Node to interact with the console.

import * as fs from 'fs';
import * as path from 'path';
import * as readline from 'readline';

// Short for console.log
const log = console.log;

const githubUser: string = 'duendeintemporal';
const f_path: string = path.join(__dirname, `${githubUser}.txt`);

// Data to write in the file
const name: string = 'Niko Zen';
const age: string = '41';
const favoriteLanguage: string = 'JavaScript';

// Create and write to the file
fs.writeFile(f_path, `Name: ${name}\nAge: ${age}\nFavoriteLanguage: ${favoriteLanguage}\n`, (err: NodeJS.ErrnoException | null) => {
    if (err) {
        console.error('Error creating the file: ', err);
        return;
    }
    log(`File ${githubUser}.txt created successfully.`);

    // Read the content of the file
    fs.readFile(f_path, 'utf8', (err: NodeJS.ErrnoException | null, data: string) => {
        if (err) {
            console.error(`Error reading the file ${githubUser}.txt: `, err);
            return;
        }
        log('Content of the file: ');
        log(data);

        // Delete the file
        fs.unlink(f_path, (err: NodeJS.ErrnoException | null) => {
            if (err) {
                console.error(`Error deleting the file ${githubUser}.txt: `, err);
                return;
            }
            log(`File ${githubUser}.txt deleted successfully.`);
        });
    });
});

// Extra Difficulty Exercise: Sales Management System

const filePath: string = 'sales.txt';

const rl: readline.Interface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const menu = (): void => {
    log('\n--- Sales Management ---');
    log('1. Add Product');
    log('2. View Products');
    log('3. Update Product');
    log('4. Delete Product');
    log('5. Calculate Total Sales');
    log('6. Calculate Sales by Product');
    log('7. Exit');
    rl.question('Select an option: ', handleMenuOption);
};

const handleMenuOption = (option: string): void => {
    switch (option) {
        case '1':
            addProduct();
            break;
        case '2':
            viewProducts();
            break;
        case '3':
            updateProduct();
            break;
        case '4':
            deleteProduct();
            break;
        case '5':
            calculateTotalSales();
            break;
        case '6':
            calculateSalesByProduct();
            break;
        case '7':
            exitProgram();
            break;
        default:
            log('Invalid option, choose a number between 1 and 7. Please try again.');
            menu();
            break;
    }
};

const addProduct = (): void => {
    rl.question('Product Name: ', (name: string) => {
        rl.question('Quantity Sold: ', (quantity: string) => {
            rl.question('Price: ', (price: string) => {
                const product: string = `${name}, ${quantity}, ${price}\n`;
                fs.appendFile(filePath, product, (err: NodeJS.ErrnoException | null) => {
                    if (err) throw err;
                    log('Product added.');
                    menu();
                });
            });
        });
    });
};

const viewProducts = (): void => {
    fs.readFile(filePath, 'utf8', (err: NodeJS.ErrnoException | null, data: string) => {
        if (err) throw err;
        log('\nProducts:\n' + (data || 'No products registered.'));
        menu();
    });
};

const updateProduct = (): void => {
    rl.question('Product Name to Update: ', (name: string) => {
        rl.question('New Quantity Sold: ', (newQuantity: string) => {
            rl.question('New Price: ', (newPrice: string) => {
                fs.readFile(filePath, 'utf8', (err: NodeJS.ErrnoException | null, data: string) => {
                    if (err) throw err;
                    const products: string = data.split('\n').map(line => {
                        if (line.startsWith(name)) {
                            return `${name}, ${newQuantity}, ${newPrice}`;
                        }
                        return line;
                    }).join('\n');
                    fs.writeFile(filePath, products, (err: NodeJS.ErrnoException | null) => {
                        if (err) throw err;
                        log('Product updated.');
                        menu();
                    });
                });
            });
        });
    });
};

const deleteProduct = (): void => {
    rl.question('Product Name to Delete: ', (name: string) => {
        fs.readFile(filePath, 'utf8', (err: NodeJS.ErrnoException | null, data: string) => {
            if (err) throw err;
            const products: string = data.split('\n').filter(line => !line.startsWith(name)).join('\n');
            fs.writeFile(filePath, products, (err: NodeJS.ErrnoException | null) => {
                if (err) throw err;
                log('Product deleted.');
                menu();
            });
        });
    });
};

const calculateTotalSales = (): void => {
    fs.readFile(filePath, 'utf8', (err: NodeJS.ErrnoException | null, data: string) => {
        if (err) throw err;
        const total: number = data.split('\n').reduce((sum: number, line: string) => {
            const parts: string[] = line.split(', ');
            return sum + (parseInt(parts[1] || '0') * parseFloat(parts[2] || '0'));
        }, 0);
        log(`Total Sales: ${total.toFixed(2)}`);
        menu();
    });
};

const calculateSalesByProduct = (): void => {
    rl.question('Product Name: ', (name: string) => {
        fs.readFile(filePath, 'utf8', (err: NodeJS.ErrnoException | null, data: string) => {
            if (err) throw err;
            const total: number = data.split('\n').reduce((sum: number, line: string) => {
                const parts: string[] = line.split(', ');
                if (parts[0] === name) {
                    return sum + (parseInt(parts[1] || '0') * parseFloat(parts[2] || '0'));
                }
                return sum;
            }, 0);
            log(`Total Sales for ${name}: ${total.toFixed(2)}`);
            menu();
        });
    });
};

const exitProgram = (): void => {
    fs.unlink(filePath, (err: NodeJS.ErrnoException | null) => {
        if (err) {
            console.error('Error deleting the file:', err);
            return;
        }
        log('Exiting the program and deleting the sales data file.');
        rl.close();
    });
};

setTimeout(() => {
    menu();
}, 1200);