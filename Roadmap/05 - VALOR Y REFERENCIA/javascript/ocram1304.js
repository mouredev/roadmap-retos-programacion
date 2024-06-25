/*Los  tipo valor son aquellas en las que se copia directamenete el valor dentro de su propia asignacipon 
de memoria, los tipo de datos primitivo como number (int, float) string, boolean, null, undenined y symbol, se pueden
utilizar como tipo de  datos por valor.
Los tipo refenrncia en cambio guardan una referenica a donde se encuentran sus datos. Los datos compuestos como arreglos
y objetos son de tipo referencia.
Estrictamente hablando JS no ofrece la opción de pasar por referencia cuando pasamos la varible como parametro de una
función. Lo interesante es que cuando se trata de un objeto o arreglo el "valor" de estos es la referencia.
*/


//NOTA para este ejercisio utilice la información proviniente de está página https://medium.com/laboratoria-developers/por-valor-vs-por-referencia-en-javascript-de3daf53a8b9
//El author origina es Lupo Montero, publicado en  Laboratoria Devs.
//Ejemplo de asignación por valor
//Cundo se asignan valores por valor como en este ejemplo al cambiar el valor de a, b se mantiene independiate
//Cada varible mantien su propio valor.
let a = "12";
let b = a;
a+="5";
console.log(a);//salida esperada [17]
console.log(b);//salida esperada [12]

//Ejemplo de asignación por referencia
//Como se puede observar si se modifica el valor del parametro, se está modificando el mismo valor al que hace
//referencia la variable, por ello para evitar eefectos colaterales se obta por no mutar directamente los argumentos
//pasados a una función

const modi = (arreglo)=>{
    const results= [];
    while(arreglo.length){
        results.push(doSomethingWithArrayItem(arr.shift()))//Se vacia el arreglo/parametro 
    }
    return results;
}
const arreglo = [1,2,3,4];
modi(arreglo);
console.log(arreglo);//salida esperada []
//Como evitar efectos colaterales 
const modi2 = (arreglo)=>{
    const copia = arreglo.slice(0); //Se hace una copia del arreglo
    const results= [];
    while(copia.length){
        results.push(doSomethingWithArrayItem(copia.shift()))//Se vacia la copia del  arreglo/parametro 
    }
    return results;
}
const arreglo2 = [1,2,3,4];
modi(arreglo2);//salida esperada [1,2,3,4];

//Una caracteristica importante a resaltar de los tipo referemcia, es que se pude utilizar en la recursión
//En algo que se llama referencia circulares por ejemplo

const a2 = [1, 2, 3];
a2.push(a2);
console.log(a2);
//El cuarto elemento que se agrega es una referencia hacia el mismo arreglo. Se tiene que tener cuidado con esto
//Pues se pueden producir bucles infinitos.

//Dificultad extra

//Tipo valor
let tValor1 = "valor1";
let tValor2 = "valor2";

function tipoValor(v1,v2){

    let aux =v1;
    v1= v2;
    v2 = aux;
    return [v1,v2]
}
let valoresIntercambiados = tipoValor(tValor1, tValor2);
console.log(valoresIntercambiados); // Debería imprimir ["valor2", "valor1"]
console.log(tValor1); // Debería imprimir "valor1"
console.log(tValor2); // Debería imprimir "valor2"

//Tipo referenia
const  tipoRefe1 = {
  a: 1,
  b: 2,
  c: 3
}
const tipoRefe2 = {
    a: 4,
    b: 5,
    c: 6
  }

function tipoRefencia (ref1, ref2){
    //Se cran copias de los objetos originales
    //Object.assign  crea copias superficiales de los objetos originales. Los valores promitivos se copian directamente
    //mientras que las referencias  a otros objetos se mantienen, pero apuntan a los mismos objetos.
    let aux1 = Object.assign({}, ref1);
    let aux2 = Object.assign({}, ref2);
    let mix = aux1;
    aux1= aux2;
    aux2 = mix;
    return [aux1,aux2];


}
let intercambio = tipoRefencia(tipoRefe1,tipoRefe2);
//Valorse intercambiados
console.log(intercambio[0]);
console.log(intercambio[1]);
//Valores originales 
console.log(tipoRefe1);
console.log(tipoRefe2);
