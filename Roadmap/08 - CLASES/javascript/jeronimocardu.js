class Auto{
    constructor(marca, color){
        this.marca = marca;
        this.color = color;
    }

    imprimirDatos(){
        console.log(`El auto es marca ${this.marca} y es de color ${this.color}.`);
    }
}

let auto1 = new Auto('peugeout', 'rojo');
auto1.imprimirDatos()

auto1.marca = 'fiat';
auto1.color = 'azul';
auto1.imprimirDatos()




/////////////////////////////////////////
//              Extra

class Pila{
    constructor(){
        this.arr = [];
    }

    add(elem){
        this.arr.push(elem);
    }
    delete(){
        this.arr.pop();
    }
    cantElem(){
        console.log('\n',this.arr.length);
    }
    mostrar(){
        console.log('\n',this.arr);
    }
}

class Cola{
    constructor(){
        this.arr = [];
    }
    add(elem){
        this.arr.push(elem);
    }
    delete(){
        this.arr.shift();
    }
    cantElem(){
        console.log('\n',this.arr.length);
    }
    mostrar(){
        console.log('\n',this.arr);
    }

}

console.log('//////// Pila')
let pilas = new Pila();
pilas.add(2);
pilas.add(3);
pilas.add(4);
pilas.mostrar();
pilas.cantElem();
pilas.delete();
pilas.mostrar();
pilas.cantElem();

console.log('//////// Cola')
let colas = new Cola();
colas.add(2);
colas.add(3);
colas.add(4);
colas.mostrar();
colas.cantElem();
colas.delete();
colas.mostrar();
colas.cantElem();

