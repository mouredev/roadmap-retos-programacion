// 1º Ejemplos de todas las operaciones que puedes realizar con cadenas.
    let mensaje : string = 'Ola Mundo';
    let mensaje2 : string = 'Soy Igledev';

    // -- charAt
    console.log('charAt' + mensaje.charAt(10)); // Recive un numero y devuelve su caracter.

    // -- Concat
    console.log('concat' + mensaje.concat(' ' + mensaje2)); // Se le puede pasar carárteres como '-' , '/' , '_' , etc...

    // -- startsWith
    console.log('Starswith: ' + mensaje.startsWith('Ola')); // Evalua si el string inicia con lo que le pasamos en el argumento y nos devuelve un boolean.

    // -- endsWith
    console.log('Endswith: ' + mensaje2.endsWith('Igledev')); // Evalua si el string acaba con lo que le pasamos en el argumento y nos devuelve un boolean.

    // -- includes
    let texto : string = 'Mundo';
    console.log('includes: ' + mensaje.includes(texto)); // Comprueba si el substring que le pasamos como argumento está en el string, nos devuelve un booleano.

    // -- indexOf
    console.log('indexOf: ' + mensaje.indexOf(texto)); // Devuelve la posicion en la que un substring inicia dentro de un string, en caso de que se repita devuelve la primera posición encontrada.

    // -- lastIndexof
    console.log('lastIndexOf' + mensaje.lastIndexOf(texto)); // Devuelve la posicion en la que un substring acaba dentro de un string. En caso que la substring se repita, devuelve la posicion de la última encontrada.

    // -- match
    let regex = /[A-Z]/g; //Evalua solo mayusculas.
    console.log('match' + mensaje.match(regex));

    // -- replace
    const ownRegex = /Brais Moure/i
    console.log('replace 1' + mensaje.replace(texto, 'Ola')); // Sustituye uno, varios, o toda un string, con otra string del segundo argumento del metodo.

    // -- slice
    console.log('slice' + mensaje.slice(4)); // Extrae una seccion del string y retorna una nueva, sin modificar la original.

    // -- split
    console.log('split' + mensaje.split(' ')); // Divide y crea un array con los substrings resultantes.

    // -- toLowerCase
    console.log('toLowerCase' + mensaje.toLowerCase()); // Devuelve un string transformado todo a minusculas.

    // -- toUpperCase
    console.log('toUpperCase' + mensaje.toUpperCase()); // Devuelve un string transformado todo a mayuscula.

    // -- trim
    console.log('trim: ' + mensaje.trim()); // Elimina todos los espacios vacios que se encuentren al inicio o al final de un string.

    // -- trimStart
    console.log('trimStart: ' + mensaje.trimStart()); // Elimina solo los espacios vacion que se encuentra al inicio.

    // -- trimEnd
    console.log('trimEnd: ' + mensaje.trimEnd()); // Elimina solo los espacios vacion que se encuentra al final.

// Ejercicio Extra

    // Palíndromo
    let palindromo = (cadena: string) : boolean => {
        let reverse : string = cadena.toLowerCase().split('').reverse().join('')
        if(cadena.toLowerCase() === reverse){
            return true;
        } else {
            return false;
        }
    }

    console.log('La palabra es palíndroma? ' + palindromo('reconocer'));

    // Anagrama
    let anagrama = (cadena1 : string , cadena2 : string) : boolean => {
        let reverse : string = cadena2.toLowerCase().split('').reverse().join('');
        if(cadena1.toLowerCase() === reverse){
            return true;
        } else {
            return false;
        }
    }

    console.log('La palabra es anagrama? ' + anagrama('amor' , 'roma'));

    // Isograma
    let isograma = (cadena1: string): boolean => {
        let letrasArray: String[] = cadena1.toLowerCase().split('');
        let letras = new Set(letrasArray);
        if(letrasArray.length === letras.size){
          return true;
        }else{
          return false;
        }
    }

    console.log('La palabra es un isograma? ' + isograma('murcielago'));