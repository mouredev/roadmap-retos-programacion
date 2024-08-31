/*
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 */

//Pila / Stacks (LIFO)
//Principio: LIFO (Last In, First Out) - El último elemento que se añade es el primero en salir.

let stack = [];
stack.push('1');
stack.push('2');
stack.push('3');

console.log(stack);

let elemento = stack.pop();

console.log(elemento);
console.log(stack);

//Colas (Queues)
//Principio: FIFO (First In, First Out) - El primer elemento que se añade es el primero en salir.

let cola = [];
cola.push(1);
cola.push(2);
cola.push(3);

console.log(cola);
let elementoC = cola.shift();
console.log(elementoC);
console.log(cola);


 /* DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 */
 const readline = require('readline');

 const rl = readline.createInterface({
   input: process.stdin,
   output: process.stdout
 });

let paginaGuardada =  [];
let paginaEliminada = [];

let paginaB = () => {
  
  if(paginaGuardada.length>1){
    let penultimaW = paginaGuardada[paginaGuardada.length-2];
    let ultimaW = paginaGuardada.pop();
    paginaEliminada.push(ultimaW);
    console.log(penultimaW);
    }
  else if (paginaGuardada ===1){
    let ultimaW = paginaGuardada.pop();
    paginaEliminada.push(ultimaW);
    console.log('No hay paginas web anteriores ');}
  else {
        console.log('no hay paginas web ');
  }
  
}



let paginaw = () =>{
    
    rl.question('ingrese una pagina web',(pweb) => {

       paginaGuardada.push(pweb); 
       console.log('Página guardada:', paginaGuardada);
       website();


    });
} ;



 let website = () => {

    rl.question(' interactua con las palabras adelante, atras, salir, insertar: ', (instruccion) => {
  
      if (instruccion === 'salir') {
        console.log('Saliendo del programa');
        rl.close();
        return;
      }

      else if (instruccion === 'insertar'){
        paginaw();
        
      }
      else if (instruccion === 'adelante'){
        if(paginaEliminada.length>0){
          let ultimaW = paginaEliminada.pop();
          paginaGuardada.push(ultimaW);
          console.log(ultimaW);
        }
        else{
          console.log('No haya paginas para avanzar');
        }
       website();

      }
      else if (instruccion === 'atras'){
        
        paginaB();
      
        website();      
        
      }

      
      else {
        console.log('ingrese otra instruccion por favor.')
        website ();
      }
    
  
    });
    
  }
  paginaw();
 

  



/*
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 */

let impresoraGua   = [];

let impresi = () => {
  rl.question ('Indique un documento a guardar o escribe CONTINUAR para imprimir : ',(palabra) => {
    
    if (palabra === 'CONTINUAR'){
      imprime();
      return
    }

    let numeroElemento = impresoraGua.length + 1;
    impresoraGua.push({numero:numeroElemento, palabra:palabra});
    impresoraGua.forEach(item => {
      console.log(`${item.numero}.${item.palabra}`)
    });

    console.log('siga el proceso')
    impresi();

    
   
     
    

     
  });
};



let imprime = () =>
rl.question('indique la palabra IMPRIMIR para mostrar el primer elemento,ITEM para imprimir un numero segun la seleccion de la lista, SALIR para cerrar el programa y RETORNAR para volver agregar elementos: ',(imprimir)=>{

  if (imprimir === 'IMPRIMIR'){
    let ultimaP = impresoraGua.shift();
    console.log(`El elemento de la cola es: ${ultimaP.numero}. ${ultimaP.palabra}`);
    imprime();
  }
  else if (imprimir === 'SALIR') {
    console.log('saliendo del programa');
    rl.close();
  
  }
  else if (imprimir === 'RETORNAR'){
    impresi()
    
  }
  else if( imprimir ==='ITEM'){
   
    rl.question('indique el numero de la lista que desea imprimir',(numero)=>{

      numero = parseInt(numero)-1;
      if(numero>=0  && numero <impresoraGua.length){
        let item= impresoraGua[numero];
        console.log(`El elemento seleccionado es: ${item.numero}. ${item.palabra}`)
      }else{
        console.log('Numero no valido');
      }

        imprime();  

    })

    


  }
  else {
    console.log('Comando no reconocido. Inténtalo de nuevo.');
    imprime();  
  }

})

impresi();
