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

const fs = require("fs")
const readline = require("readline")
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

class Product {
    constructor(name, quantitySold, price) {
        this.name = name
        this.quantitySold = quantitySold
        this.price = price
    }
}

let products = []
let totalSales = []
let indexes = []

function addProduct(name, quantitySold, price) {

    let newProduct = new Product(name, quantitySold, price)
    products.push(newProduct)
    sales = quantitySold * price
    totalSales.push(sales)

    fs.appendFile(
        "products.txt",
        `Product: ${name}, Quantity sold: ${quantitySold}, Price: ${price} \n`,
        (err) => {
            if (err) throw err
        }
    )
}

function showProducts() {
    fs.readFile("products.txt", (err, data) => {
        if (err) throw err
        console.log(data.toString())
        showMenu()
    })
}

function deleteProduct(name) {
    let index = products.findIndex((product) => product.name === name)

    if (index !== -1) {
        products.splice(index, 1)
        totalSales.splice(index, 1)

        let fileContent = ""
        products.forEach((product) => {
            fileContent += `Product: ${product.name}, Quantity sold: ${product.quantitySold}, Price: ${product.price}\n`
        })

        fs.writeFile("products.txt", fileContent, (err) => {
            if (err) throw err
            console.log("Product deleted and file overwritten")
            showMenu()
        })

    } else {
        console.log("Product not found in the array")
    }
}

function findProduct(name) {
    const product = products.find((product) => product.name === name)
    return product
}

function findIndexOfProduct(name) {

    for (let i = 0; i < products.length; i++) {
        if (products[i].name === name) {
            indexes.push(i)
        }
    }
    console.log(indexes)
    return indexes
}

function exitProgram() {
    fs.unlink("products.txt", (err) => {
        if (err) throw err
        console.log("File deleted!")
    })
}

function calculateTotalSales() {
    sales = 0
    for (let i = 0; i < totalSales.length; i++) {
        sales += totalSales[i]
    }
    console.log(`Total sales: ${sales}`)
}

function calculateTotalSalesPerProduct(name) {
    sales = 0
    for (let i = 0; i < indexes.length; i++) {
        sales += totalSales[indexes[i]]
    }
    console.log(`Total sales for ${name}: ${sales}`)

}

function updateProduct(name, newQuantitySold, newPrice) {
    let product = findProduct(name)
    if (product) {
        product.quantitySold = newQuantitySold
        product.price = newPrice

        let fileContent = ""
        products.forEach((product) => {
            fileContent += `Product: ${product.name}, Quantity sold: ${product.quantitySold}, Price: ${product.price}\n`
        })

        fs.writeFile("products.txt", fileContent, (err) => {
            if (err) throw err
            console.log("Product updated and file overwritten")
            showMenu()
        })
       
    } else {
        console.log("Product not found")
    }
}

function showMenu() {
    console.log("----------------------------------------------")
    console.log("0. Show products")
    console.log("1. Add product")
    console.log("2. Show product")
    console.log("3. Update product")
    console.log("4. Delete product")
    console.log("5. Calculate total sales")
    console.log("6. Calculate total sales per product")
    console.log("7. Exit")

    rl.question("Choose an option: ", (option) => {
        console.log("----------------------------------------------")

        switch (option) {
            case "0":
                showProducts()
                break

            case "1":
                rl.question("Product name: ", (name) => {
                    rl.question("Quantity sold: ", (quantitySold) => {
                        rl.question("Product price: ", (price) => {
                            addProduct(name, quantitySold, price)

                            console.log("Product added")
                            showMenu()
                        })
                    })
                })
                break

            case "2":
                rl.question("Product name: ", (name) => {
                    let product = findProduct(name)
                    if (product) {
                        console.log(
                            `Product: ${product.name}, Quantity sold: ${product.quantitySold}, Price: ${product.price}`
                        )
                        showMenu()
                    } else {
                        console.log("Product not found")
                        showMenu()
                    }
                })

                break

            case "3":
                rl.question("Product name to modify: ", (name) => {
                    let product = findProduct(name)
                    if (product) {
                        console.log("Product found")

                        rl.question("Quantity sold: ", (newQuantitySold) => {
                            rl.question("Product price: ", (newPrice) => {
                                updateProduct(name, newQuantitySold, newPrice)
                            })
                        }) 
                    } else {
                        console.log("Product not found")
                        showMenu()
                    }
                })
                break

            case "4":
                rl.question("Product name to delete: ", (name) => {
                    let product = findProduct(name)

                    if (product) {
                        console.log("Product found")
                        deleteProduct(name)
                    } else {
                        console.log("Product not found")
                    }
                })
                break

            case "5":
                calculateTotalSales()
                showMenu()
                break

            case "6":
                rl.question("Product name to calculate sales: ", (name) => {
                    findIndexOfProduct(name)
                    calculateTotalSalesPerProduct(name)
                })
                showMenu()
                break

            case "7":
                exitProgram()
                rl.close()
                break

            default:
                console.log("Invalid option, type a number between 1-7")
                showMenu()
        }
    })
}

showMenu()

/* 
NO OK:
- Class SalesManager with functions like methods
*/
