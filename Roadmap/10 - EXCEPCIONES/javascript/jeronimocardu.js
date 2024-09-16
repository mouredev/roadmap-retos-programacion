try{
    let nums = [0, 1, 2, 3];
    let n = 5;
    if(n > nums.length) throw new Error('Ese indice no existe en este array');
    else console.log(nums[n]);
}catch(e){
    console.log(e.toString())
}

console.log('\n el programa sigue\n\n\n');


/////////////////////////////////////////////////////////
//                  Extra
function excepciones(param1, param2){
    if((param1 + param2) <= 0) throw new Error('El resultado es negativo o 0');
    if(param1 < 0) throw new Error('El primer número es negativo');
    if(param2 < 0) throw new Error('El segundo número es negativo');
    console.log('No se ha producido ningun error!');
}

try{
    excepciones(-2, 2);
    excepciones(-2, 20);
    excepciones(10, -2);
    excepciones(10, 2);
}catch(e){
    console.log(e.toString());
}finally{
    console.log('El programa finalizó');
}