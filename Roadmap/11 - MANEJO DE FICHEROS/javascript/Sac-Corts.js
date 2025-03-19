// Exercise //
const fs = require('fs');
const readline = require('readline');

const userName = "Sac-Corts";  
const name = "Isaac"; 
const age = 22;  
const favoriteLanguage = "JavaScript";  

const fileName = `${userName}.txt`;

fs.writeFileSync(fileName, `Name: ${name}\n`);
fs.appendFileSync(fileName, `Age: ${age}\n`);
fs.appendFileSync(fileName, `Favorite programming language: ${favoriteLanguage}\n`);

const content = fs.readFileSync(fileName, 'utf8');
console.log(content);

fs.unlinkSync(fileName);

// Extra Exercise //

const file = 'products.txt';

const readData = () => {
    try {
        const data = fs.readFileSync(file, 'utf8');
        return data.split('\n').filter(line => line.trim() !== '');
    } catch (err) {
        return [];
    }
};

const writeData = (data) => {
    fs.writeFileSync(file, data.join('\n'), 'utf8');
};

const addProduct = (name, quantity, price) => {
    const data = readData();
    data.push(`${name}, ${quantity}, ${price}`);
    writeData(data);
    console.log('Product added successfully.');
};

const viewProduct = (name) => {
    const data = readData();
    const product = data.find(line => line.startsWith(name));
    if (product) {
        console.log(`Product found: ${product}`);
    } else {
        console.log('Product not found.');
    }
};

const updateProduct = (name, quantity, price) => {
    const data = readData();
    const index = data.findIndex(line => line.startsWith(name));
    if (index !== -1) {
        data[index] = `${name}, ${quantity}, ${price}`;
        writeData(data);
        console.log('Product updated successfully.');
    } else {
        console.log('Product not found.');
    }
};

const deleteProduct = (name) => {
    const data = readData();
    const newData = data.filter(line => !line.startsWith(name));
    if (data.length !== newData.length) {
        writeData(newData);
        console.log('Product deleted successfully.');
    } else {
        console.log('Product not found.');
    }
};

const calculateTotalSales = () => {
    const data = readData();
    let total = 0;
    data.forEach(line => {
        const [, quantity, price] = line.split(', ');
        total += parseInt(quantity) * parseFloat(price);
    });
    console.log(`Total sales: ${total.toFixed(2)}`);
};

const calculateProductSales = (name) => {
    const data = readData();
    const product = data.find(line => line.startsWith(name));
    if (product) {
        const [, quantity, price] = product.split(', ');
        const sales = parseInt(quantity) * parseFloat(price);
        console.log(`Sales for ${name}: ${sales.toFixed(2)}`);
    } else {
        console.log('Product not found.');
    }
};

const clearFile = () => {
    fs.unlinkSync(file);
    console.log('File cleared.');
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const main = () => {
    rl.question('Choose an option: (add/view/update/delete/total/individual/exit) ', (option) => {
        switch (option.toLowerCase()) {
            case 'add':
                rl.question('Enter product name: ', (name) => {
                    rl.question('Enter quantity sold: ', (quantity) => {
                        rl.question('Enter price: ', (price) => {
                            addProduct(name, quantity, price);
                            main();
                        });
                    });
                });
                break;
            case 'view':
                rl.question('Enter product name: ', (name) => {
                    viewProduct(name);
                    main();
                });
                break;
            case 'update':
                rl.question('Enter product name: ', (name) => {
                    rl.question('Enter new quantity sold: ', (quantity) => {
                        rl.question('Enter new price: ', (price) => {
                            updateProduct(name, quantity, price);
                            main();
                        });
                    });
                });
                break;
            case 'delete':
                rl.question('Enter product name: ', (name) => {
                    deleteProduct(name);
                    main();
                });
                break;
            case 'total':
                calculateTotalSales();
                main();
                break;
            case 'individual':
                rl.question('Enter product name: ', (name) => {
                    calculateProductSales(name);
                    main();
                });
                break;
            case 'exit':
                clearFile();
                rl.close();
                break;
            default:
                console.log('Invalid option. Please try again.');
                main();
                break;
        }
    });
};

main();