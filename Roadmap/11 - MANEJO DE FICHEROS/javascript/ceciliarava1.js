
// const writeStream = fs.createWriteStream('ceciliarava1.txt', { flags: 'a' }) // a - Appending data

// const lines = ["Name: Cecilia Rava", "Age: 22 Years old", "Favorite programming language: Javascript"]
// lines.forEach(line => {
//     writeStream.write(line + '\n')
// })
// writeStream.end()


// fs.readFile("ceciliarava1.txt", (err, data) => {
//     if (err) throw err
//     console.log(data.toString())

//     fs.unlink("ceciliarava1.txt", (err) => {
//         if (err) throw err
//         console.log("File deleted!")
//     })
// })

const fs = require('fs');
const readline = require('readline')
const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
})

class Product {
    constructor(name, quantitySold, price) {
        this.name = name
        this.quantitySold = quantitySold
        this.price = price
    }
}


let products = []

function addProduct(name, quantitySold, price) {
    let newProduct = new Product(name, quantitySold, price)
    products.push(newProduct)
    fs.appendFile("products.txt", `Product: ${name}, Quantity sold: ${quantitySold}, Price: ${price}`, (err) => {
        if (err) throw err
    })
}

function showProducts() {
    fs.readFile("products.txt", (err, data) => {
        if (err) throw err
        console.log(data.toString())
        console.log(products)
    })
}

function exitProgram() {
    fs.unlink("products.txt", (err) => {
        if (err) throw err
        console.log("File deleted!")
    })
}


function showMenu() {

    console.log('----------------------------------------------')
    console.log('1. Add product')
    console.log('2. Show products')
    console.log('3. Update product')
    console.log('4. Delete product')
    console.log('5. Calculate total sales')
    console.log('6. Calculate total sales per product')
    console.log('7. Exit')

    rl.question('Choose an option: ', (option) => {

        console.log('----------------------------------------------')

        switch (option) {

            case '1':
                // something code
                console.log('add product')
                showMenu()
                break

            case '2':
                // something code
                console.log('show product')
                showMenu()
                break

            case '3':
                // something code
                showMenu()
                break

            case '4':
                // something code
                showMenu()
                break

            case '5':
                // something code
                showMenu()
                break

            case '6':
                // something code
                showMenu()
                break

            case '7':
                // something code
                rl.close()
                break

            default:
                console.log('Invalid option, type a number between 1-7')
                showMenu()
        }
    })
}

showMenu()




function updateProduct(name) {

}

function deleteProduct(name) {

}

// addProduct('coca', 1, 1000)
// showProducts()
// exitProgram()

/* NO OK:
- Function show menu
- Update product in Array
- Delete product in Array
- Update product in txt
- Delete product in txt
- Class SalesManager with functions like methods
- Calculate total sales
- Calculate total sales per product
*/