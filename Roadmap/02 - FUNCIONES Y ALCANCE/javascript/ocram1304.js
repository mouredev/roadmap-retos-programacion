//Variable global
const usuGlobal = "ocram1304"
let fecha = "20/04/2024";
//función sencilla
//funciones que no retornan
function mifunction(){
  console.log("hello world");
}
mifunction();
//función con parámetros
function mifunctionV2(author, date){
  console.log(`hola soy ${author} saludos desde el dia ${date}`);
}
mifunctionV2(usuGlobal, fecha);

function actualizarFecha(nFecha){
  fecha = nFecha;
 
}
//funcion con retorno
function FunRetorno(num1, num2){

  return num1 * num2;
}
console.log(FunRetorno(2,3));

//funcióne anónima
const cuadrado = function(){
  return  "función anónima";
}
console.log(cuadrado);
//función flecha
const pares = [1,2,3,4];
const pares2=  pares.map((par)=>{
  return par*2;
});
console.log(pares2);

//JS si soporta crear funciones dentro de funciones
function funcionAnidada(numero){
//Ambito de varibles: las variables declaradas dentro de una función no pueden ser accedidas desde fuera
//su ámbito es local a la función en donde fueron declaradas, en este ejemplo "num" no puede ser accedido 
//fuera delámbito de "iPrimo"  aunque está función este dentro de otra función (funcionAnidada).
  for(let i=0; i<=numero;i++){
    if(isPrimo(i)){
       console.log(i);
    }
   
  }

  function isPrimo(num){
    if(num<=1){
     return false;
    }
    for(let i =2;i<num;i++){
     if (num % i===0){
         return false;
     }
      
    }
    return true; 

 }
 
}
funcionAnidada(20);

//Dificultad extra
function difExtra(para1,para2){
  let onlyNumber = 0;
  for(let i= 0; i<=100;i++){

   
    if(i%5===3){
      console.log(para1);
    }
    else if(i%5===0){
      console.log(para2)
    }
    else if(i%3===0 && i%5===0){
        console.log(`${para1}, ${para2} `);
    }
    else{
      console.log(i);
      onlyNumber++;
    }
  }
  console.log("Numeros en lugar de texto", onlyNumber);
}
difExtra(multiplo3,multiplo5);
