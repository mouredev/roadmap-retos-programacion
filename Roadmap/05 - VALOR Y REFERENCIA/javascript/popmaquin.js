/*---Por valor y referencia---*/

//---Por referencia a datos primitivos
console.log("---Por valor");
let a= "hola";
let b= a;

a+="!";
console.log(a);
console.log(b);

//---Por referencia a datos complejos
console.log("---Por referencia");
let arr= ["hola","Juan","Bienvenido"];
let ref= arr;

arr.push("Guatemala");
console.log(arr);
console.log(ref);

//---Funcion por valor datos primitivos
console.log("---Funcion por valor");
function xvalor(a){
    let b=a;
    a="4"
    return [b, a];
}

let a_ ="hola";

console.log(xvalor(a_));
console.log(a_);


//---Funcion por referencia a datos complejos
console.log("---Funcion por referencia");
function xrefencia(arr2){
    let ref2=arr2;
    arr2.set(34)
    return [ref2,arr2];
}
let mymap2= new Map([[10],[24]]);

console.log(xrefencia(mymap2));
console.log(mymap2);

//---Dificultad extra---
console.log("---Dificultad Extra---");
console.log("---x valor");
function parametro_x_valor(num1,num2){
    let temp=num1;
        num1=num2;
        num2=temp;
    return {num1,num2}  
}
let num3 = 5;
let num4 = 2;
let result = parametro_x_valor(num3,num4);

console.log(result);
console.log(`num3: ${num3} num4: ${num4}`);


console.log("---x refrencia");
function parametro_x_ref(matriz1,matriz2){
    let temp=matriz1;
        matriz1=matriz2;
        matriz2=temp;
    return {matriz1, matriz2}
}
let arr1 = [1,2,3];
let arr2 = [4,5,6];
let arr_result = parametro_x_ref(arr1,arr2);

console.log(arr_result);
console.log(`arr1: ${arr1} arr2: ${arr2}`);