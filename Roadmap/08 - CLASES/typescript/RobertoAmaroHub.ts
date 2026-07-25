class Imprimir{

    private nombre:string;
    constructor(){
        this.nombre="";
    }

    public getNombre(){
        return this.nombre;
    }
    public setNombre(_nombre:string){
        if(_nombre.trim().length>0){
            this.nombre=_nombre;
        } else {
            throw new Error("El nombre no puede estar vacío.");
            
        }
    }

    public bienvenida(): void{
        console.log(`Hola ${this.nombre} bienvenido al curso de programación`)
    }
}

let imprime:Imprimir= new Imprimir();
imprime.setNombre("Roberto");
imprime.bienvenida();


//EXTRA
class Estructuras{

    protected elementos:string[];
    constructor(){
        this.elementos=[];
    }

    public setElementos(value:string[]){
        this.elementos=value;
    }
    public getElementos(){
        return this.elementos;
    }

    public validarPalabra(value:string):boolean{
        if(value.trim().length<0){
            return false;
        } else {
            return true;
        }
    }
    public añadir(value:string){
        this.elementos.push(value)
        console.log(`\nElemento ${value} agregado correctamente!`)
    }
    public printLengthOfElements(){
        console.log(`\nTotal de elementos: ${this.elementos.length}`);
    }
    public printElements(){
        console.log("\nElementos actuales:")
        console.log(this.elementos);
    }
}

class Pilas extends Estructuras{
    
    constructor(){
        super();
    }

    public eliminar(){
        let removed=this.elementos.pop();
        console.log(`\nElemento ${removed} eliminado correctamente!`)
    }
}

class Colas extends Estructuras{
    
    constructor(){
        super();
    }

    public eliminar(){
        let removed=this.elementos.shift();
        console.log(`\nElemento ${removed} eliminado correctamente!`)
    }
}

var prompt = require("prompt-sync")();
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let pila:Pilas= new Pilas();
let cola:Colas= new Colas();
let menu:string[]=["Añadir","Eliminar", "Total de elementos", "Ver elementos", "Salir"]

function getResponseFromMenu():string{
    for(let item in menu){
        console.log(`[${item}]: ${menu[item]}`)
    }
    let accion=prompt("Escribe el número de la acción que necesites:");
    return accion;
}

function initPilas(){
    console.log("\n******PILAS******");
   let accion=+getResponseFromMenu();
    if(!isNaN(accion) && accion>=0 && accion<menu.length){
        switch(accion){
            case 0:
                let res=prompt("Escribe una palabra: ");
                if(pila.validarPalabra(res)){
                    pila.añadir(res);
                    initPilas();
                } else {
                    respuestaIncorrectaPilas();
                }
            break;
            case 1:
                pila.eliminar();
                initPilas();
            break;
            case 2:
                pila.printLengthOfElements();
                initPilas();
            break;
            case 3:
                pila.printElements();
                initPilas();
            break;
            case 4:
                rl.close();
            break;
            default:
                respuestaIncorrectaPilas();
                break;
        }
    } else {
        respuestaIncorrectaPilas();
    }
}

function respuestaIncorrectaPilas(){
    console.log("Respuesta incorrecta");
    initPilas();
}

function initColas(){
    console.log("\n******COLAS******");
    let accion=+getResponseFromMenu();
    if(!isNaN(accion) && accion>=0 && accion<menu.length){
        switch(accion){
            case 0:
                let res = prompt("Escribe una palabra: ")
                if(cola.validarPalabra(res)){
                    cola.añadir(res);
                    initColas();
                } else {
                    respuestaIncorrectaColas();
                }
                break;
            case 1:
                cola.eliminar();
                initColas();
                break;
            case 2:
                cola.printLengthOfElements();
                initColas();
                break;
            case 3:
                cola.printElements();
                initColas();
                break;
            case 4:
                rl.close()
                break;
            default:
                respuestaIncorrectaColas
                break;
        }
    } else {
        respuestaIncorrectaColas();
    }
}
function respuestaIncorrectaColas(){
    console.log("Respuesta incorrecta");
    initPilas();
}

initPilas();

initColas();

