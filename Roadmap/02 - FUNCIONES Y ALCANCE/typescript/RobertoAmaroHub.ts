/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...*/
function sinParametros(){
    console.log("prueba de función sin parametros");
}

function conParametro(texto: string){
    console.log(`prueba de función con parametro: ${texto}`)
}

function conParametros(texto1: string, texto2: string){
    console.log(`prueba de función con parametros: ${texto1} y ${texto2}`)
}

function conRetorno(): string{
    return "prueba de función con retorno";
}

function conRetornoParametrosOpcionales(valor1:number, valor2?:number): string{
    let res: string;
    if(valor2){
        let suma= valor1+valor2;
        res=`la suma de ambos valores es: ${suma}`;
    } else {
        res=`el único parámetro ingresado es: ${valor1}`;
    }
    return res;
}

function conParametrosPorDefecto(valor1: number, valor2: number=4){
    let suma:number=valor1+valor2;
    console.log(`la suma de ${valor1} mas ${valor2} es: ${suma}`)
}

//Otra característica de TypeScript es la posibilidad de pasar una lista indefinida de valores y que los reciba un vector.
//El concepto de parámetro Rest se logra antecediendo tres puntos al nombre del parámetro:
function conParametroRest(...valores:number[]){
    let suma:number=0;
    for(let i of valores){
        suma+=i;
    }
    console.log(`la suma de todos los parametros es: ${suma}`)
}

sinParametros();
conParametro("parámetro");
conParametros("var1", "var2");
console.log(conRetorno());
console.log(conRetornoParametrosOpcionales(3));
console.log(conRetornoParametrosOpcionales(3,5));
conParametrosPorDefecto(7);
conParametroRest(3,4,5);
/**El operador Spread permite descomponer una estructura de datos en elementos individuales. 
Es la operación inversa de los parámetros Rest. La sintaxis se aplica anteponiendo al nombre de la variable tres puntos:*/
function sumar(valor1:number, valor2:number, valor3:number):number {
    return valor1+valor2+valor3;
  }
  
  const vec=[10,20,30] as const;
  console.log(`la suma de los datos es: ${sumar(...vec)}`);

/*
 * - Comprueba si puedes crear funciones dentro de funciones.*/
function funcionPrincipal(){
    console.log("llamado de la primera función")
    function funcionAnidada(){
        console.log("llamado a la función anidada")
    }
    funcionAnidada();
}
funcionPrincipal();


/*
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.*/
function contarLetrasEnFrase(frase: string){
    console.log(`la frase "${frase}" contiene ${frase.length} caracteres incluyendo espacios`);
}
contarLetrasEnFrase("Probando funciones ya creadas en typescript");

/*
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.*/
let varGlobal:boolean=true;
function testVarGlobal(){
    let varLocal:boolean=false;
    if(varGlobal && varLocal){
        console.log("puedo usar la variable global y la local dentro del método")
    }
}
console.log(`puedo acceder a la variable global con el valor ${varGlobal} pero es imposible acceder al la variable local (dentro del método)`)

/*
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */

function returnNumber(texto1: string, texto2: string):number{
    let count:number=0;
    for(let i=0; i<100; i++){
        if(i%3==0 && i%5==0){
            console.log(`los dos parámetros son ${texto1} y ${texto2}`);
        } else if(i%3==0){
            console.log(`primer parámetro: ${texto1}`);
        } else if (i%5==0){
            console.log(`segundo parámetro: ${texto2}`);
        } else {
            console.log(i);
            count++;
        }
    }
   return count;
}

console.log("El número total de números mostrados es: "+returnNumber("valor1","valor2"));