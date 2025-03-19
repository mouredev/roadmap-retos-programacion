//Operacines con cadenas de carcteres
//Contatenación
const parte1 = "hola ";
const parte2 = "una cadena";
const partesUnidas = parte1+parte2;
console.log(partesUnidas);
//Template iteral es una alternativa a la contatenación normal, además de que permite incluir expresione
console.log(`suma de 4+2 es igual a: ${4+2}`);
const cadena = "CadenaDecaracter";
//conversión entre strings y numeros
const num = "123456";
//De string a número
Number(num);
//De número a string
num.toString();
//Tamaño del string, la pripiedad length permite conocer el numero de caracteres que conformán el string
const long =  cadena.length;
//Buscando substrings, el método includes permite verificar la existancia de un substring dentro de otro 
//más grande, si lo encuentra regresa true.
if(cadena.includes("Cadena")){
    console.log("Cadena encontrada");
} 
else{
    console.log("Cadena no encontrada");

}
//Encontrar la posición de un substring. IndexOf() permite encontrar el indice en donde se encuantra un substring
//Si lo encuentra devuelve el indice, de lo contrario devuelve -1.
const encontrada = cadena.indexOf("caracter");
//Mayúsculas y minúsculas los métodos toUpperCase() y toLowerCase() permiten convertir a mayúsculas y minúsculas
//respectivamente, los caracteres de una cadena.
const MayMin = "cambiodeletra";
console.log(MayMin.toUpperCase());
console.log(MayMin.toLowerCase);
//Actualizar partes de un string, se puden cambiar partes especificas de un estring por medio del método replace()
//Este y otros métodos devuelven un nuevo string, no modifican al string como tal. Para poder modificar el string
//se tiene que declarar como variable "let" y no como constante "const"
const actual = "niña";
const actualizada = actual.replace("ni","pi");
console.log(actualizada);
//Si se tiene un string en donde varios substring se repiten y se desea actualizar cada uno de esos substrings
//se puede hacer por medio del método replaceAll()
let cita =  "ser o no ser";
cita = cita.replaceAll("ser","programar");
console.log(cita);
//Los espacios en blanco se pueden remover con el método trim()
cita = cita.trim();
console.log(cita);
//Se pueden obtener partes especificas de un string, para ello existe el método slice(), utiliza dos parametros
//El primero es para indicar desde donde comienza la substracción; mientras que el segundo indica la posición en
//donde acaba (en realidad la substracción acaba un valor antes del valor especificado en el segundo parametro)
const extraido = "Batman";
console.log(extraido.slice(0,3));
//De string a arreglo y de arreglo a sting
//Las cadenas (strings) son muy similares a los arreglos, de hecho se les pude considerar como un arreglo
//De carcteres, por eso se puede convertir a un arreglo en un string y viceversa.
//De string a arreglo. El método spit() permite convertir un string a un arreglo tomando un parametro como referencia
//Para dividir en string
const datos = "usuario,password,correo,telefono";
const datosArray = datos.split(",");
console.log(datosArray);
//De  arreglo a string. Si lo que se pretende es pasar de un arreglo, entonces es método join() es el indicado
//Funciona de la misma manera que split(), solo que el parametro se utiliza para unir el string en lugar de 
//separarlo
const ndatos = datosArray.join(",");
console.log(ndatos);

//Dificultad extra 

//Verificar si una palabra es un palindromo
function IsPalindromo(palindromo){
    //En mi caso no conicía el método reverse() que permite cambiar el orden, de manera inversa, de los elementos
    //De un arreglo. Si la cadena se apoya de ese método en combinación de split() y join() se tiene algo como
    //Esto palindromo.split("").reverse().join(""); la lógica es la misma, pero de está manera la cadena se convierte
    //En arreglo para aprovechar sus métodos y después vuelve a ser cadena  para realizar la comparación.
  

    let aux = "";
    for(let i = palindromo.length-1; i>=0; i--){
        aux += palindromo[i];

    }
    if(aux===palindromo){
        return "Es palindromo"
    }
    else{
        return "No es palindromo"
        
    }
    
}
//Verificar si es un isograma
function isIsograma(isograma) {

    function apariciones(cadena, letra) {
        const arregloCadena = cadena.split(""); 
        const cadenaFiltrada = arregloCadena.filter(car => car === letra);
        return cadenaFiltrada.length;
    }

    for (let i = 0; i < isograma.length; i++) {
        const aux = apariciones(isograma, isograma[i]);
        if (aux > 1) {
            return "No es un isograma";
        }
    }
    return "Es un isograma";
}
//Verificar si es un anagrama
//Para este función me vase en el trabajo de YgriegaSB.js pero me apoye en chatgpt para acomodarla 
//de una manera que considero más apropiada. 
function isAnagrama(palabra1, palabra2){
    //Contar las frecuancia de las letras en una palabra
    const contarLetras = palabra =>{
        const contador = {}
         for(let letra of palabra){
            //Se accede a la propiedad letra del objeto contador
            //está parte de la lina es muy importante (contador[letra]||0)+1
            //Se utiliza un operador de corto circuito si contador[letra] es undefined (la letra no se ha encontrado)
            //se evalua como 0, por lo que la cuenta de la letra está en 0. En cambio si contador[letra] tiene un valor
            //diferente a undefined, entonces se utiliza ese valor (pues se encontro la letra anteriormente).
            //deespues se le agrega uno para incrementar la cuenta de la letra
            contador[letra] = (contador[letra]||0)+1


         }
         //Al final se devuelve un objeto en donde las claves corresponden a cada una de las letras de la palabra
         //y el valor es el la cantidad de operaciones de dicha palabra.
         return contador;
    };
    //Se verifican la frecuanccia de las palbras

    const freqPalabra1 = contarLetras(palabra1);
    const freqPalabra2 = contarLetras(palabra2);

    //Se utiliza el Object.keys par tener un array de la claves del objeto con la frecuenia de las palabras
    //El objetivo es verificar que posan el mismo numero de letras (que su longitud sea igual)
    //Y por medio del método  every() se verfica que cada una de las claves(las letras) tenga el mismo
    //numero en ambas palabras.
    const sonAnagramas = (Object.keys(freqPalabra1).length === Object.keys(freqPalabra2).length) &&
    Object.keys(freqPalabra1).every(letra => freqPalabra1[letra] === freqPalabra2[letra]);
    return console.log(sonAnagramas ? `${palabra1} y ${palabra2} son anagramas` : 'No son anagramas');
}
function analizaPalabra(pal1, pal2){
    pal1.toLowerCase();
    pal2.toLowerCase();
    isAnagrama(pal1);
    isAnagrama(pal2);
    isIsograma(pal1)
    isIsograma(pa2)
    isAnagrama(pal1,pal2);
    
}
analizaPalabra(amor,roma);
