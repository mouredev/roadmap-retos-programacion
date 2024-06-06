/*---Pila---*/
//Last-in First-out

let lista= new Array();

//insert elemento al final.
lista.push(1);
lista.push(2);
lista.push(3);
lista.push(4);
//elimina el ultimo elemento.
lista.pop();//4

// Muestra el ultimo elmento
console.log(lista[lista.length - 1]); //5

console.log(lista);//[ 1, 2, 3 ]


/*---Cola---*/
//First-in First-out
let lista2= new Array();

//Inserta elemento al inicio
lista2.push(10);
lista2.push(20);
lista2.push(30);

//Elimiana 1er elemento shift()
lista2.shift(); //30

// Muestra el primer elmento
console.log(lista2[0]) // 20

console.log(lista2);//[ 20, 30 ]


/*---Dificultad extra---*/

function navegar_web(){
    let url_webs= new Array()
    while(true){
        let texto= prompt("introduce una url para navegar o las palabras atras/adelante/salir: ");
        if (texto==="adelante"){
          console.log(`Navegando en la pagina principal` );
        }
        else if(texto==="atras"){
            if(url_webs.length>0){
                url_webs.pop()
            }
        }
        else if(texto==="salir"){
            console.log("Saliendo de la web ");
            break;
        }
        else{
            url_webs.push(texto);
        }
        
        if(url_webs.length>0){
          console.log("Navegando a: "+ (url_webs[url_webs.length- 1]));
        }
        else{
            console.log(`Navegando en la pagina principal` );
        }
    }
}

navegar_web();
// https://www.programiz.com/javascript/online-compiler/


//programa de impresora compartida --> Cola

function impresoraCompartida(){
    
    let documento = new Array();
    while(true){
        let opcion = prompt("Añada un documento o selecciona imprimir/salir: ");
        
        if(opcion==="imprimir"){
            if(documento.length>0){
                console.log(`Imprimiendo... ${documento.shift()}`);
                
            }else{
                console.log("Cola de impresion vacia.");
            }
        }
        else if(opcion==="salir"){
            console.log("Apangando impresora...");
            break
        }
        else{
            documento.push(opcion);
        }
        
    }
}

impresoraCompartida();