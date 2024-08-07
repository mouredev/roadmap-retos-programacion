const fs = require('fs');

// let nombre = 'jeronimocardu';
// let archivo = `${nombre}.txt`;

// let datos = [
//     "nombre: Jeronimo Cardu",
//     "edad: 20 años",
//     "lenguaje: JavaScript"
//     ].join('\n');

// // Añado el contenido
// fs.writeFileSync(archivo, datos);

// // Imprimo el contenido
// console.log(fs.readFileSync(archivo, 'utf-8'));

// // Borro el archivo
// fs.unlinkSync(archivo);
// console.log(`\n${archivo} ha sido eliminado con exito`);

//////////////////////////////////////////////////////////////
//          Extra
let salesFile = 'ventas.txt';
let products = [];

let readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout,
});

function addProduct(){
    readline.question('\n¿Qué producto desea agregar? ', nameProduct => {
        for(let i of products){
            if(i.name === nameProduct){
                console.log('Este producto ya existe');
                saveProductsToFile();
                return;
            }
        }
        readline.question(`\n¿Cuál es la cantidad de ${nameProduct} que se vendieron? `, soldProducts => {
            readline.question(`\n¿Cuál es el precio unitario de cada ${nameProduct}? `, price => {
                products.unshift({name: nameProduct, sold: parseInt(soldProducts), unitPrice: parseInt(price)});
                console.log(`\nLos datos de '${nameProduct}' se han agregado correctamente.`);
                saveProductsToFile();
            })
        })
    })
}
function consult(){
    if(products.length > 0){
        readline.question('\nIngrese el nombre del producto que desea ver los datos: ', nameProduct => {
            for(let i of products){
                if(i.name === nameProduct){
                    console.log(`\nName: ${nameProduct}\nQuantity Sold: ${i.sold}\nUnit Price: $${i.unitPrice}`);
                    saveProductsToFile();
                    return;
                }
            }
            console.log('\nProducto no encontrado');
            saveProductsToFile();
        })
    } else console.log('\nNo hay productos registrados todavia.');
    saveProductsToFile();
}
function update(){
    let = found = false;
    if(products.length > 0){
        readline.question('\n¿Qué producto quiere modificar? ', nameProduct => {
            for(let i of products){
                if(i.name === nameProduct){
                    found = true;
                    readline.question('\nIngrese el nombre nuevo del producto (si no lo quiere cambiar presione ENTER): ', newNameProduct => {
                        for(let i of products){
                            if(i.name === newNameProduct){
                                console.log('\nNombre no disponible');
                                break;
                            }
                        }
                        if(newNameProduct !== '') i.name = newNameProduct;
                        readline.question(`\n¿Qué cantidad de ${i.name} se vendieron? (si no lo quiere cambiar presione ENTER) `, soldProducts => {
                            if(soldProducts !== '') i.sold = parseInt(soldProducts);
                            readline.question(`\n¿Cuál es el precio unitario de cada ${i.name}? (si no lo quiere cambiar presione ENTER) `, price => {
                                if(price !== '') i.unitPrice = parseInt(price);
                                console.log('\nProducto actualizado con exito!');
                                saveProductsToFile();
                                return;
                            })
                        })
                    })
                }
                break;
            }
            if(!found) console.log('\nProducto no encontrado');
            saveProductsToFile();
        })
    } else console.log('\nNo hay productos registrados todavia.');
    saveProductsToFile();
}
function removeProduct(){
    if(products.length > 0){
        readline.question('\n¿Cuál es el nombre del producto que quiere eliminar? ', nameProduct => {
            for(let i of products){
                if(i.name === nameProduct){
                    found = true;
                    products.splice(products.indexOf(i), 1);
                    console.log('\nProducto eliminado con exito!');
                    saveProductsToFile();
                    return;
                }
            }
            console.log('\nProducto no encontrado');
            saveProductsToFile();
        })
    } else{
        console.log('\nNo hay productos registrados todavia.');
        saveProductsToFile();
    }
}
function showProducts(){
    if(products.length > 0){
        const content = products.map(i => `Name: ${i.name} | Quantity Sold: ${i.sold} | Unit Price: $${i.unitPrice}`).join('\n');
        console.log(content);
    } else{
        console.log('\nNo hay productos registrados todavia.');
    }
    saveProductsToFile();
}
function totalSales(){
    let suma = 0;
    if(products.length > 0){
        for(let i of products){
            suma += i.sold * i.unitPrice;
        }
        console.log('\nHay una venta total de $',suma);
    } else console.log('\nNo hay productos todavia');
    saveProductsToFile();
}
function productsSales(){
    if(products.length > 0){
        readline.question('\n¿De que producto deseas ver la venta? ', nameProduct => {
            let suma = 0;
            for(let i of products){
                if(i.name === nameProduct){
                    suma = i.sold * i.unitPrice;
                    console.log(`${nameProduct} recaudó en total $${suma}`);
                    saveProductsToFile();
                    return;
                }
            }
            console.log('\nProducto no encontrado');
        })
    } else console.log('\nNo hay productos todavia');
    saveProductsToFile();
}
function saveProductsToFile(){
    const content = products.map(i => `Name: ${i.name} | Quantity Sold: ${i.sold} | Unit Price: $${i.unitPrice}`).join('\n');
    fs.writeFileSync(salesFile, content);
    readline.question('\nPrecione ENTER para continuar...', tecla => {
        if(tecla === '') management();
            else saveProductsToFile();
    })
}
function management(){
    console.clear();
    console.log(`
\t\t/// INGRESE UNA OPCIÓN ///\n
1. Añadir producto.
2. Consultar datos de productos.
3. Actualizar datos de productos.
4. Eliminar productos.
5. Ver productos.
6. Ver total.
7. Ver total de X producto.
8. Salir ( Elimina el archivo )`);
    readline.question('\nIngrese una opción: ', op => {
        switch (op){
            case '1':
                addProduct();
                break;
            case '2':
                consult();
                break;
            case '3':
                update();
                break;
            case '4':
                removeProduct();
                break;
            case '5':
                showProducts();
                break;
            case '6':
                totalSales();
                break;
            case '7':
                productsSales();
                break;
            case '8':
                fs.unlinkSync(salesFile);
                readline.close();
                return;
            default:
                console.log('\nOpción no valida');
                saveProductsToFile();
        }
    })
}
management();