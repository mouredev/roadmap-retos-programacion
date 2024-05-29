//Arreeglos
//Son estructuras de datos que almacenana valores de manera indexada
//En JS los arreglos son dinámicos, su longitud se puede aumentar o disminur sin restricciones
//Además en JS los arreglos pueden almacenar datos de distinto tipo no es necesario definir
//que tipo de datos se van a almacenar 

//La longitud de un arreglo es un dato muy importante a la hora de reealizar operaciones. En los arreglos
//se puede obtener por medio de la atributo length
const longitud = miarreglo.length;
//Declaración de un arreglo
const miarreglo = ["item", "item2", "item3"];
//insertar valores (al final del arreglo)
miarreglo.push("item4");
//insertar valor al principio del arreglo
miarreglo.unshift("item0");
//Eliminar el ultimo elemento del arreglo (además este método recupera el valor)
const itemRemovido = miarreglo.pop();
//Eliminar el primer valor del arreglo
const firstItem = miarreglo.shift();
//cambia el contenido de un array añadiendo o remplazando elementos
miarreglo.splice(2,1,"nItem3");
//actualizar valor
miarreglo[0]= "item1";
//ordenación 
//El método sort ordena los elementos del arreglo y regresa una referenica la mismo arreglo. 
const miarreglo2= [0,5,6,7,8,12,15];
miarreglo2.sort((a,b)=>{
  return a-b;
});
console.log(miarreglo2);

//Objetos
//son una colección de datos y funcionalidades
//están constituidos por variables y funciones que reciben el nombre de atributos y métodos respectivamente.
//Los objetos almacenan sus valores (atributos) de manera similar a los arreglos, utilizán el formato clave/valor
//en el caso de los arreglos es el indice, mientras que en los objetos es el "key", por ello a los ojetos 
//tambiíen se les conoce como arreglos asociativos.
//Declaración de un objeto
const miobjeto ={
  nombre: "ocram1304",
  edad: 24,
  estatus: "aprendiendo",
  saludos: function (){
    console.log("hola soy: ", this.nombre);
  }
  
}
//acceso a las popoiedades de un objeto
console.log(miobjeto.nombre)
//acceso a los métodos de un objeto
miobjeto.saludos();
//Notación de corchetes, es una alternativa para acceder a los atributos de un objeto
console.log(miobjeto["edad"]);
//Agregar una nueva propiedead al objeto
miobjeto["lenguje"] = "JavaScript";
//Agregar un nuevo método
miobjeto.presentacion = function(){
  console.log("Tengo", this.edad,  "años y estudio", this.lenguje)
}

//Set permite almacenar valores únicos de cualquier tipo, ya sea primitivos o referencias de objetos
//Son colecciones de valores, se puede iterar a traves de los valores en órden de insercion
//un valor en un set solo puede ocurrir una vez

//Declaración de un set
const myset = new Set();
//añadir un vaor
myset.add("valor1");
myset.add("valor2");
myset.add("valor3");
myset.add("valor4");
//has, este método verifica si existe un valor en el objeto set, y devuelve un valor booleano.
const exist = myset.has("valor1");
//size devuelbe el numero de valores del objeto set 
const longitudset = myset.size;
//Eliminar un valor especifico de un set. Para ello se utiliza el método delete() que además devuelve un 
//valor booleano que afirma si el valor se elimino correctamente o no.
const velorBorrado = myset.delete("valor3");
//Borrar todos los valores. Se puede eliminar todos los valores del objeto set por medio del método clear()
myset.clear();
//Objetos iterables
//Entries. Devuleve un objeto iterable que contiene una arreglo con todos los elementos del set
const arregloDeSet = myset.entries();
console.log(arregloDeSet);

//Maps
//El objeto map permite almacenar pares clave-valor y recuerda el orden de inserción de las clave (keys). 
//Se direncia de set ya que este admite claves y no solo valores como en el caso del primero.
//Las claves en los objetos son únicas y no se pueden repetir

//Declaración de un Map
let myMapa = new Map();
//Agregar valores de un map
myMapa.set("mykey1", "valor1");
myMapa.set("mykey2", "valor2");
myMapa.set("mykey3", "valor3");
console.log(myMapa);
//Tamaño de un map. Se puede conocer el tamaño de un map por medio del método size
const longitudmap = myMapa.size();
//Get regresa un elemento en especifico de un map, si el valor asociado es un objeto entonces
// cualquier cambio en el objeto modificara al objeto en el map
console.log(myMapa.get("mykey3"));
//Eliminar valores de un map
myMapa.delete("mykey2");
//Map también cuenta con el método has al igual que set
const existInMap = myMapa.has("mykey2");
//Eliminar todas las claves del map
myMapa.clear();
//Objetos iterables, se puden obtener objetos iterables de un map, tanto para las claves como para los valores
//como para la claves
//Método entries. Rgresa un  objeto (map) iterador  que contiene los pares clave-valor para  cada elemento
//en el orden de inserción
const mapaIterador = myMapa.entries();
console.log(mapaIterador.next().value);
//El medot keys. Regresa un objeto iterador que contien la claves de cada uno de los elementos en orden de inserción
const mapaclaves = myMapa.keys();
console.log(mapaclaves.next().value);
//El método values. Funciona igual que el método kes() pero regresa los valors en lugar de las claves
const mapavalores = myMapa.values();
console.log(mapavalores.next().value);

//Difucultad extra

function miagenda(){
  let  continuar = "s";
  let agenda = new Map([
    ["Marco",526711139082],
    ["Antonio",526711139049]
  ]);
    let contacto = "";
    let numTel = 0;
  while(continuar==="s"){
    console.log("Bienvenido, ¿qué deseas hacer?");
    console.log("1.buscar 2.agregar  3.actulalizar 4.eliminar ");

    let option = prompt("Seleccione una opción");
    
    if (option > 0 && option < 5){

      switch(option){
        case 1://Buscar
        contacto = prompt("Ingresa el nombre de contacto");
        if(agenda.has(contacto)){
            console.log(`Contacto ${contacto} # ${agenda.get(contacto)}`);
        }
        else{
          console.log("contacto no existente")
        }
        break;
        case 2://agregar
        contacto = prompt("Ingrese el nombre del contacto");
        numTel = Number(prompt("Ingrese el numero de telefono"));
        if(contacto !=="" && !isNaN(numTel) && numTel.toString().length>=11){
          agenda.set(contacto,numTel);
          console.log("Contacto guardado")

        }
        else{
          console.log("Ingrese los datos correctamente");

        }
        break;
        case 3://actualizar
        contacto = prompt("Ingrese el nombre de contacto");
        numTel = Number(prompt("Ingrese el nuevo numero de telefono"));
        if(agenda.has(contacto) && contacto !=="" && !isNaN(numTel) && numTel.toString().length>=11){
          agenda.set(contacto,numTel);
          console.log("Contacto actualizado");

        }
        else{
          console.log("Ingrese los datos correctamente");

        }
        break;
        case 4://Eliminar
        let contactoEliminar = prompt("Ingrese el nombre del contacto a eliminar");
        if (agenda.has(contactoEliminar) && contactoEliminar !== "") {
        agenda.delete(contactoEliminar);
        if (!agenda.has(contactoEliminar)) {
          console.log("Contacto eliminado");
        } else {
          console.log("No se pudo eliminar el contacto");
        }
      } else {
        console.log("El contacto no existe o el nombre está vacío");
      }
      break;

        

      }

    }
    else{
      console.log("Elija una opción correta");
    }

    continuar = prompt("Desea continuar s/n");

  }
 

}
miagenda();
