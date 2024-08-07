
const fs = require('fs').promises;
const prompt = require("prompt-sync")()
const path = require('path')

async function createFile(){
    let current_path = path.join(__dirname,"raulG91.txt");
    let content = "Raul\n33\nJavascript";
    await fs.writeFile(current_path,content);
    await fs.unlink(current_path)

}

createFile();

let finish = false;
const  sales_file = path.join(__dirname,"sales.txt");

async function addProduct(name,quantity,price){

    let information = `${name},${quantity},${price}\n`;
    await fs.appendFile(sales_file,information);
    menu();

}
async function checkProduct(name){

    let data = await fs.readFile(sales_file);
    data = String(data);
    let products = data.split("\n");
    let product = products.find((product)=>product.split(",")[0] == name);
    if(product){
        console.log(product);
    }
    else{
        console.log("Producto no existe")
    }
    menu();
}

async function deleteProduct(name){

    let data = await fs.readFile(sales_file);
    data = String(data);
    let products = data.split("\n");

   for(let i = 0; i< products.length;i++){
        product_name = products[i].split(",")[0];
        if(product_name == name){
            delete(products[i]);
        }
   }
    let products_string = products.join("\n");
    await fs.writeFile(sales_file,products_string);
    menu();

}
async function updateProduct(name,new_quantity,new_price){
    let data = await fs.readFile(sales_file);
    data = String(data);
    let products = data.split("\n");
    let found = false;

    for(let i=0;i<products.length;i++){
        product_name = products[i].split(",")[0];
        if(product_name == name){
            found = true;
            delete(products[i]);
            products[i] = `${product_name},${new_quantity},${new_price}`;
        }        
    }
    if(found){
        let products_string = products.join("\n")
        await fs.writeFile(sales_file,products_string);
    }
    else{
        console.log("Producto no existe")
    }
    menu();

}
async function getTotal(){

    let data = await fs.readFile(sales_file);
    data = String(data);
    let products = data.split("\n");
    let sum = 0;

    for(let i=0;i<products.length;i++){

        let [name,quantity,price] = products[i].split(",");
        if(name){
            
            sum = sum + (parseInt(quantity)*parseFloat(price));
        }
    }
    console.log("Suma total es "+String(sum));
    menu()
}
async function getTotalProduct(name){
    let data = await fs.readFile(sales_file);
    data = String(data);
    let products = data.split("\n");
    let sum = 0;

    let product = products.find((product)=>product.split(',')[0]==name);

    if(product){
        let[product_name,quantity,price] = product.split(',');
        sum = quantity*price;
        console.log("Suma product "+product_name+" "+String(sum))
    }
    else{
        console.log("Producto no encontrado");
    }
   menu();
}

function menu(){

    console.log("Introduzca 1 para añadir producto");
    console.log("Introduzca 2 para consultar producto");
    console.log("Introduzca 3 para actualizar producto");
    console.log("Intorduzca 4 para eliminar producto");
    console.log("Intorduzca 5 para obtener el total ventas");
    console.log("Intorduzca 6 para obtener total por producto");
    console.log("Introduzca 7 para salir")

    let input = prompt();
    input = parseInt(input);
    let name,quantity,price;
    switch(input){

        case 1: name = prompt("Introduzca nombre del producto ");
                quantity = parseInt(prompt("Introduzca la cantidad "));
                price = parseFloat(prompt("Introduzca el precio "));
                try{
                    addProduct(name,quantity,price);
                }catch (e){
                   console.log("Error añadiendo producto");     
                }
                break;
        case 2: name  = prompt("Introduzca nombre del producto ");
                checkProduct(name);
                break;
        case 3: name  = prompt("Introduzca nombre del producto ");   
                quantity = parseInt(prompt("Introduzca la nueva cantidad "));
                price = parseFloat(prompt("Introduzca el nuevo precio "));  
                updateProduct(name,quantity,price)
                break;
                
        case 4: name = prompt("Introduzca nombre del producto a eliminar ");
                deleteProduct(name);
                break;  
        case 5:  getTotal();
                break;  
        case 6: name = prompt("Introduzca el nombre del producto ");  
                getTotalProduct(name);
                break;                   

        case 7: finish = true;
                fs.unlink(sales_file);
                break;
        default: menu();        
    }

}

menu()