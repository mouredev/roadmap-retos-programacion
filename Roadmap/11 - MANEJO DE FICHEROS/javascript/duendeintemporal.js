//#11 MANEJO DE FICHEROS
//Bibliography
//Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)
//GPT

/*  The File Type
The File API is still based around the file input field of a form but adds the ability to access the file
information directly. HTML5 adds a files collection to DOM for the file input element. When one
or more files are selected in the field, the files collection contains a sequence of File objects that
represent each file. Each File object has several read-only properties, including:
➤➤ name—The file name on the local system.
➤➤ size—The size of the file in bytes.
Blob and File APIs ❘ 759
➤➤ type—A string containing the MIME type of the file.
➤➤ lastModifiedDate—A string representing the last time the file was modified. This property
has been implemented only in Chrome. */

/* The FileReader Type
The FileReader type represents an asynchronous file-reading mechanism. You can think of File-
Reader as similar to XMLHttpRequest, only it is used for reading files from the file system as opposed
to reading data from the server. The FileReader type offers several methods to read in file data:
➤➤ readAsText(file, encoding)—Reads the file as plain text and stores the text in the
result property. The second argument, the encoding type, is optional.
➤➤ readAsDataURL(file)—Reads the file and stores a data URI representing the files in the
result property.
➤➤ readAsBinaryString(file)—Reads the file and stores a string where each character repre-
sents a byte in the result property.
➤➤ readAsArrayBuffer(file)—Reads the file and stores an ArrayBuffer containing the file
contents in the result property. */


//How ever we will use Node.js to facilitate the files manipulation, so you have to run this file in Node to interact with the console

//short for console.log
let log = console.log;

const fs = require('fs');
const path = require('path');

const githubUser = 'duendeintemporal';
const f_path = path.join(__dirname, `${githubUser}.txt`);

// Data to write in the file
const name = 'Niko Zen';
const age = '41';
const favoriteLanguage = 'JavaScript';

// Create and write to the file
fs.writeFile(f_path, `Name: ${name}\nAge: ${age}\nFavoriteLanguage: ${favoriteLanguage}\n`, (err) => {
    if (err) {
        console.error('Error creating the file: ', err);
        return;
    }
    log(`File ${githubUser}.txt created successfully.`);

    // Read the content of the file
    fs.readFile(f_path, 'utf8', (err, data) => {
        if (err) {
            error(`Error reading the file ${githubUser}.txt: `, err);
            return;
        }
        log('Content of the file: ');
        log(data);

        // Delete the file
        fs.unlink(f_path, (err) => {
            if (err) {
                error(`Error deleting the file ${githubUser}.txt: `, err);
                return;
            }
            log(`File ${githubUser}.txt deleted successfully.`);
        });
    });
});

//Extra Dificulty Exercise

const readline = require('readline');

const filePath = 'sales.txt';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const menu = () => {
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

const handleMenuOption = (option) => {
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

const addProduct = () => {
    rl.question('Product Name: ', (name) => {
        rl.question('Quantity Sold: ', (quantity) => {
            rl.question('Price: ', (price) => {
                const product = `${name}, ${quantity}, ${price}\n`;
                fs.appendFile(filePath, product, (err) => {
                    if (err) throw err;
                    log('Product added.');
                    menu();
                });
            });
        });
    });
};

const viewProducts = () => {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) throw err;
        log('\nProducts:\n' + (data || 'No products registered.'));
        menu();
    });
};

const updateProduct = () => {
    rl.question('Product Name to Update: ', (name) => {
        rl.question('New Quantity Sold: ', (newQuantity) => {
            rl.question('New Price: ', (newPrice) => {
                fs.readFile(filePath, 'utf8', (err, data) => {
                    if (err) throw err;
                    const products = data.split('\n').map(line => {
                        if (line.startsWith(name)) {
                            return `${name}, ${newQuantity}, ${newPrice}`;
                        }
                        return line;
                    }).join('\n');
                    fs.writeFile(filePath, products, (err) => {
                        if (err) throw err;
                        log('Product updated.');
                        menu();
                    });
                });
            });
        });
    });
};

const deleteProduct = () => {
    rl.question('Product Name to Delete: ', (name) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) throw err;
            const products = data.split('\n').filter(line => !line.startsWith(name)).join('\n');
            fs.writeFile(filePath, products, (err) => {
                if (err) throw err;
                log('Product deleted.');
                menu();
            });
        });
    });
};

const calculateTotalSales = () => {
    fs.readFile(filePath, 'utf8', (err, data) => {
        if (err) throw err;
        const total = data.split('\n').reduce((sum, line) => {
            const parts = line.split(', ');
            return sum + (parseInt(parts[1] || 0) * parseFloat(parts[2] || 0));
        }, 0);
        log(`Total Sales: ${total.toFixed(2)}`);
        menu();
    });
};

const calculateSalesByProduct = () => {
    rl.question('Product Name: ', (name) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) throw err;
            const total = data.split('\n').reduce((sum, line) => {
                const parts = line.split(', ');
                if (parts[0] === name) {
                    return sum + (parseInt(parts[1] || 0) * parseFloat(parts[2] || 0));
                }
                return sum;
           
            }, 0);
            log(`Total Sales for ${name}: ${total.toFixed(2)}`);
            menu();
        });
    });
};

const exitProgram = () => {
    fs.unlink(filePath, (err) => {
        if (err) {
            error('Error deleting the file:', err);
            return;
        }
        log('Exiting the program and deleting the sales data file.');
        rl.close();
    });
};

setTimeout(()=>{
    menu();
}, 1200);
