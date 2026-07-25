import { randomUUID } from 'crypto';
import * as fs from 'fs';
import * as path from 'path';


const rutaArchivo = path.resolve('david-git-dev.txt');

fs.appendFileSync(rutaArchivo,'Nombre: David\n');
fs.appendFileSync(rutaArchivo,'Edad: 25 años\n',);
fs.appendFileSync(rutaArchivo,'Lenguajes de programacion favoritos: Javascript , Typescript,PHP,Flutter,Java\n',);//agregando datos
const data = fs.readFileSync(rutaArchivo,'utf8')//leyendo archivo
console.log(`Archivo creado en: ${rutaArchivo}\n con el contenido: \n ${data}`);
fs.unlinkSync(rutaArchivo) // borrando el archivo
//DIFICULTAD EXTRA
type Product ={
  name:string
  price:number
  qty:number
}
class SalesManager{
  private _db:{
   [key:string]:Product
  } = {
    product1:{
      name:'coca cola espuma',
      price:100,
      qty:10
    },
    product2:{
      name:'coca cola lata',
      price:300,
      qty:30
    }
  }
  constructor(){}
  add(data:{name:string,price:string,qty:string}){
    try{
        if(Number(data.qty)){
      const product:Product={
      name: data.name,
      price: Number(data.price),
      qty: Number(data.qty)
      }
      this._db[self.crypto.randomUUID()] = product;
      alert('Producto Agregado')
      }


      }catch(e){
      if(e instanceof Error) console.log(e.name,e.message)
      }
   // this._db.product!.id = self.crypto.randomUUID();
    //this._db.product = product
  }
  getProducts(){
     console.log(this._db)
     alert(JSON.stringify(this._db))
  }
  update(id:string,name:string,price:string,qty:string){

    try{
    this._db[id].name = name
    this._db[id].price = Number(price)
    this._db[id].qty = Number(qty)
    alert('Producto actualizado')
    }catch(e){
    if(e instanceof Error) console.log(e.name,e.message)
    }
    }
  delete(id:string){
        delete this._db[id]
  }
  getTotal(){
     let total = Object.values(this._db).reduce((total,product)=>{
      return total + (product.price * product.qty)
     },0)
    alert(`Total en caja:${total}`)
  }
  getTotalByProduct(id:string){
try{
  alert(`Total de ${this._db[id].name} -> ${this._db[id].price * this._db[id].qty}`)

}catch(e){
  if(e instanceof Error) console.log(e.name,e.message)
}
  }
  get data(){
    return this._db;
  }
}
let option: string | null
const sales = new SalesManager();
 do {
  alert('Bienvenido a tu gestor de ventas digital!!!');
  option = prompt(`
    ¿Que quieres hacer hoy?
    1-Agregar producto.
    2-consultar productos.
    3-Actualizar productos.
    4-Eliminar productos.
    5-calcular venta total
    6-calcular venta por producto.
    *-Salir del programa.
    `)
    option ??='5';
  let name
  let price
  let qty
    switch(option){
        case '1':
         {
              name = prompt('dame el nombre del producto')
              price = prompt('dame el precio del producto')
              qty = prompt('dame la cantidad del producto')

          if(name&&price&&qty) sales.add({name:name!,price:price!,qty:qty!})
        }


        break;
        case '2':
        sales.getProducts()
        break;
        case '3':
        {
        let id = prompt('dame el id del producto')
            name = prompt('dame el nombre del producto')
            price = prompt('dame el precio del producto')
            qty = prompt('dame la cantidad del producto')
          if(id&&name&&price&&qty) sales.update(id,name,price,qty)
        }

        break;
        case '4':
        {
        let id = prompt('dame el id del producto')
        if(id) sales.delete(id)
        }
        break;
        case '5':
        sales.getTotal()
        break;
        case '6':
        {
          let id = prompt('dame el id del producto')
          if(id) sales.getTotalByProduct(id)
        }
        break;
        default:
        break;
    }
    sales.getProducts()
} while (option);
const ruta = path.resolve('db.txt');
let json = "producto,cantidad,precio\n";
Object.values(sales.data).forEach((product) => {
  json += `${product.name},${product.qty},${product.price}\n`
});
fs.writeFileSync(ruta,json)

