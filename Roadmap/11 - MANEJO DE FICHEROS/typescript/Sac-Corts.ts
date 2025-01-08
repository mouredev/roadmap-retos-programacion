import * as fs from 'fs';
import * as readline from 'readline';

const githubUser = 'Sac-Corts';
const fileName = `${githubUser}.txt`;
const data = `Name: Isaac\nAge: 22\nProgramming Language: TypeScript`;

fs.writeFileSync(fileName, data, 'utf8');
console.log('File created and data written');

const fileContent = fs.readFileSync(fileName, 'utf8');
console.log('File content:');
console.log(fileContent);

fs.unlinkSync(fileName);
console.log(`File ${fileName} deleted`);

// ** Extra Exercise ** //
const file = 'products.txt';

const readData = (): string[] => {
    try {
        const data = fs.readFileSync(file, 'utf8');
        return data.split('\n').filter(line => line.trim() !== '');
    } catch (err) {
        return [];
    }
};

const writeData = (data: string[]): void => {
    fs.writeFileSync(file, data.join('\n'), 'utf8');
};

const addProduct = (name: string, quantity: string, price: string): void => {
    const data = readData();
    data.push(`${name}, ${quantity}, ${price}`);
    writeData(data);
    console.log('Product added successfully.');
};

const viewProduct = (name: string): void => {
    const data = readData();
    const product = data.find(line => line.startsWith(name));
    if (product) {
        console.log(`Product found: ${product}`);
    } else {
        console.log('Product not found.');
    }
};

const updateProduct = (name: string, quantity: string, price: string): void => {
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

const deleteProduct = (name: string): void => {
    const data = readData();
    const newData = data.filter(line => !line.startsWith(name));
    if (data.length !== newData.length) {
        writeData(newData);
        console.log('Product deleted successfully.');
    } else {
        console.log('Product not found.');
    }
};

const calculateTotalSales = (): void => {
    const data = readData();
    let total = 0;
    data.forEach(line => {
        const [, quantity, price] = line.split(', ');
        total += parseInt(quantity) * parseFloat(price);
    });
    console.log(`Total sales: ${total.toFixed(2)}`);
};

const calculateProductSales = (name: string): void => {
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

const clearFile = (): void => {
    if (fs.existsSync(file)) {
        fs.unlinkSync(file);
        console.log('File cleared.');
    } else {
        console.log('File does not exist.');
    }
};

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const main = (): void => {
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