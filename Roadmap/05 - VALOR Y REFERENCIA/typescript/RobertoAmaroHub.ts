let asigReferencia:number[]=[2,4,6,6,77,1];
let asigValor:string="asignación por valor";

// por valor, no se modifica la variable externa al método
function porValor(_asigValor:string){
    _asigValor="nuevo texto";
    console.log(`Dentro de la función por valor, value es "${_asigValor}"`);
}
porValor(asigValor);
console.log(`Fuera de la función por valor, el valor asigValor es "${asigValor}"`);

// por referencia, sí se modifica la variable externa al método
function porReferencia(_asigReferencia:number[]){
    _asigReferencia[0]=1233;
    console.log (`Dentro de la función, vale [0] es "${_asigReferencia[0]}"`);
}
porReferencia(asigReferencia)
console.log (`Fuera de la función, arrNumeros [0] es "${asigReferencia[0]}"`);

//EXTRA*********************************************
let valor1:string="valor1 inicial";
let valor2:string="valor2 inicial";

function extraPorValor(_valor1:string,_valor2:string):string[]{
    _valor1=valor2;
    _valor2=valor1;
    return [_valor1,_valor2];
}
let newValues:string[]=extraPorValor(valor1,valor2);
let value1:string=newValues[0];
let value2:string=newValues[1];
console.log("\n");
console.log(`Valores originales: valor1 es "${valor1}" y valor2 es "${valor2}"`);
console.log(`Nuevos valores: valor1 es "${value1}" y valor2 es "${value2}"`);


let val1:string[]=["valor1","inicial"];
let val2:string[]=["valor2", "inicial"];

function extraPorReferencia(_val1:string[], _val2:string[]){
    _val1=val2;
    _val2=val1;
    return [_val1, _val2];
}
let newVal:string[][]=extraPorReferencia(val1,val2);
let nVal1:string[]=newVal[0];
let nVal2:string[]=newVal[1];
console.log("\n");
console.log(`Valores originales: valor1 es "${val1}" y valor2 es "${val2}"`);
console.log(`Nuevos valores: valor1 es "${nVal1}" y valor2 es "${nVal2}"`);