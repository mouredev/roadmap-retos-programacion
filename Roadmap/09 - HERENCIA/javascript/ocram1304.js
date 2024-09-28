class Animal{

    especie;
    tamano;
    color;
    amo;
    constructor(especie,tamano,color,amo){
        this.especie = especie;
        this.tamano = tamano;
        this.color = color;
        this.amo = amo;

    }

    sonido(){//Este método puede se puede sobreescribir en las clases  que recigan herencia de está,
             //lo que significa que puede tomar direntes formas (polimorfismo)
        console.log("Sonidos de animales");
    }

}
class Perro extends Animal(){//La clase perro es hija de la superclase animal
    raza;
    constructor(especie,tamano,color,amo,raza){
        super(especie,tamano,color,amo);
        this.raza = raza;
    }
    sonido(){//Se sobreescribe el método herdado de la clase padre
        console.log("gua,gua,gua");
    }
}
class Gato extends Animal(){//La clase perro es hija de la superclase animal
    raza;
    constructor(especie,tamano,color,amo,raza){
        super(especie,tamano,color,amo);
        this.raza = raza;
    }
    sonido(){//Se sobreescribe el método herdado de la clase padre
        console.log("miau,miau,miau");
    }
}
//Herencia y objetos en el sismema de objetos y prototipos de JS
//En JS existen las cadenas de prototipos, están son una manera de implentar el polimorfismo y la herencia en 
//objetos, aunque en realidad en JS, más que herencia se trata de delegación,  si se intenta acceder a un método
//pero este no está definido dentro de el, se busca en su prototipo. Todos los objetos tienen un atributo llamado
//__proto__ el cual es el ultimo valor en la cadena de prototipos, si se recorre toda la cadeena de prototipos y se
//llega hasta el final de está (__proto__)
const objetoAnimal= {
    especie: "",
    sonidoAnimal(){
    console.log("sonido animal");
  },
};
//Las funciones tienen un atributo  llamdo prototipe, cuando la función se llama como constructor, está propiedad
//se establece como el prototipo del nuevo objeto creado.
//Un patrón muy común a la hora de utilizar prototipos es el de deninir los métodos en este último, mientras que 
//las propiedades se asignan en los objetos ya que generalmente los métodos son comunes a todos los objetos. 
function ObjetoPerro(nombre){
 this.nombre = nombre;

}
ObjetoPerro.prototype = Object.create(objetoAnimal); // Asignar prototipo
ObjetoPerro.prototype.sonidoAnimal = function() {
    console.log("gua,gua,gua");
};
//Los métodos en el prototipos se pueden sobreescribir, cuando se llama a un métedo se recurre simpre primero al 
//que está definodo dentro del objeto, sino lo encuentra o no está defindo; se recurre al prototipo.
function ObjetoGato(nombre) {
    this.nombre = nombre;
}
ObjetoGato.prototype = Object.create(objetoAnimal); // Asignar prototipo

ObjetoGato.prototype.sonidoAnimal = function() {
    console.log("miau,miau,miau");
};
// Probando los métodos
const perro = new ObjetoPerro("Darwin");
const gato = new ObjetoGato("Fiona");
perro.sonidoAnimal(); // Debería imprimir "gua,gua,gua"
gato.sonidoAnimal();  // Debería imprimir "miau,miau,miau"

//Difucultad extra
class Empleado {
    #nombre;
    #id;
    constructor(nombre,id){
        this.#nombre = nombre;
        this.#id = id;
    }
}
class Gerente extends Empleado{
 #area;
 constructor(nombre,id,area){
    super(nombre,id)
    this.#area = area;
 }
 supervisar(){
    console.log("Supervisar tareas");
 }

}
class GerenteProyecto extends Gerente{
 #proyecto;
 constructor(nombre,id, area, proyecto){
  super(nombre,id,area,proyecto);
  this.#proyecto = proyecto;
 }
 gestionar(){
    console.log("Gestionar proyecto");
 }
}
class Programador extends Empleado{
 #ParteProyecto;
 constructor(nombre,id,ParteProyecto){
    super(nombre,id);
    this.#ParteProyecto = ParteProyecto;
 }
 programar(){
    console.log("Programar");
 }

}
