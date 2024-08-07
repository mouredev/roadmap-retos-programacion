//-------------------------
//  Cadena de caracteres
//-------------------------

let string1 = "Ciudad ";
let string2 = "Guatemala";
let string3 = "Bienvenido a Guatemala"

console.log(typeof(string1)); //string


// ---Longitud string2
console.log(string2.length); // 9


// ---Concatenación
console.log(string1 + string2); // Por el operador '+'
console.log(string1.concat(string2));//-metodo 'concat()'
console.log(`${string1}${string2}`); // -Con plantillas literales


// ---Acceso
console.log(string1[0]); // C  -por su indice
console.log(string1.charAt(1)); // i -Con el metodo charAt

// ---Interpolación
console.log(`Bienvendio a la  ${string1} de ${string2}`); // 'Bienvenido a la Ciudad de Guatemala'

// ---Repetición
console.log(string1.repeat(5));

// ---Devuelve código UTF-16

console.log(string1.charCodeAt(0)); // 67 = C
console.log(string1.codePointAt(1)); // 105 = i

// ---Elimnacion de espacio a los extremos
console.log(string1.trim().length); // 6


// ---Busqueda de palabra
console.log(string3.includes("Bienvenido")); // True

// ---Busqueda por posicion
console.log("Guatemala".indexOf("a")); // 2
// ---Busqueda de la ultima posicion posicion
console.log("Bienvenido".lastIndexOf("i")); // 2


// ---Determinar la ulitma palabra o caracter
console.log("Bienvenido a Guatemala".endsWith("ala")); // true
console.log("Bienvenido a Guatemala".endsWith("Guatemala")); //true


// ---Comparación
console.log("Guatemala".localeCompare(string2)); // 0 = true
console.log("2".localeCompare("10"));


// ---Remplazar
console.log(string3.replace("Guatemala", "Coban")); //Bienvenido a Coban
 //El Coban se representa en la modena de un Coban
console.log("El quetzal se representa en la modena de un quetzal".replaceAll("quetzal", "Coban"));


// ---Extraer parte
console.log(string2.slice(0,5)); // Guate
console.log(string2.substring(0,5)); // Guate
console.log(string2.substring(5,0)); // Guate


// ---Dividir => Array
let arr = string2.split("", 9); //['G', 'u', 'a', 't', 'e', 'm', 'a', 'l', 'a']
console.log(arr);
console.log(arr[0]); //G

// ---Conversion a minuscula y mayuscula
console.log(string1.toLowerCase()); // ciudad
console.log(string1.toLocaleLowerCase()); // ciudad

console.log(string1.toUpperCase()); // CIUDAD
console.log(string1.toLocaleUpperCase()); // CIUDAD

//-------------------------
//  Dificultad extra
//-------------------------

//funcion para invertir la cadena de caracteres
function invertir(cadena){
    let reverso="";
    for(let i=cadena.length-1; i>=0; i--){
        reverso= reverso.concat(cadena[i]);
    }
    return reverso;
}
//funcion palindromo
function juegoDePalabras(cad1, cad2){
   
    //Palindromo
    if(invertir(cad1).toLowerCase()==cad1.toLowerCase()){
        console.log(`La palabra "${cad1}" es palindromo`);
    }else{
       console.log(cad1 + " no es palindromo");
    }
    if(invertir(cad2).toLowerCase()==cad2.toLowerCase()){
        console.log(`La palabra "${cad2}" es palindromo`);
    }else{
       console.log(cad2 + " no es palindromo");
    }
   
    //Anagrama
    if(cad1.split("").sort().join()==cad2.split("").sort().join()){
      console.log(`La palabra "${cad2}" es anagrama de "${cad1}" `);
    }else{
      console.log(`"${cad2}" no es anagrama de "${cad1}"`);
    }
    //Isograma
    if(cad1.length==new Set(cad1).size){
        console.log(`la palabra "${cad1}" es isograma`);
    }else{
         console.log(`la palabra "${cad1}" no es isograma`);
    }
    if(cad2.length==new Set(cad2).size){
        console.log(`la palabra "${cad2}" es isograma`);
    }else{
         console.log(`la palabra "${cad2}" no es isograma`);
    }
 
}
   
//juegoDePalabras("murcielago","lago");
juegoDePalabras("ramo","mora");