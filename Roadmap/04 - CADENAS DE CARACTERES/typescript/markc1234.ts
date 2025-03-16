(() => {
    //Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
    // - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...

    // concantencacion
    const cadena1 = "nombre"
    const cadena2 = "apellido"
    const cadena3 = cadena1 + cadena2
    const cadena4 = cadena2.concat(cadena1)

    // longitud de la cadena
    const cadena5 = cadena4.length

    // acceso a un caracter
    const char = cadena3.charAt(0)

    // convertir a mayuscula y minuscula
    const cadena6 = char.toUpperCase()
    const cadena7 = cadena6.toLowerCase()

    // buscar posicion de una subcadena dentro de una cadena
    const cadena8 = cadena2.indexOf("lli")
    // subcadena de una cadena
    const cadena9 = cadena1.substring(0,3)

    // repeticion
    const cadena10 = cadena9.repeat(3); 
    // recorrer
    for (let char of cadena10) {
        console.log(char);
    }

    // remplazar 
    const cadena11 = cadena10.replace("nom", "nombre");
    
    // dividir cadena
    const cadena12 = cadena2.split("ll");

    // union 
    const palabras = ["Hola", "Adios"];
    console.log(palabras.join(" "));


    // interpolacion
    const cadena13 = "Mundo";
    console.log(`Hola ${cadena13}`);

    // verificar cadena
    console.log(cadena11.includes("nombre"));
    console.log(cadena11.startsWith("n"));
    console.log(cadena11.endsWith("e"));



    // DIFICULTAD EXTRA (opcional):
    // Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
    // - Palíndromos
    // - Anagramas
    // - Isogramas

    function reseverseString(str:string):string {
        let result:string = ""
        for (let i = str.length-1; i >= 0; i--) {
            const element = str[i];
            result += element   
        }

        return result
    }

    function palindrome(str1:string, str2:string):boolean {
        // const reverseStr = reseverseString(str1)
        const str1ToLower = str1.toLowerCase()
        const str2ToLower = str2.toLowerCase()

        for (let i = 0; i < str1ToLower.length; i++) {
            const element = str1ToLower[i];
            if(element !== str2ToLower[i]) {
                return false
            }
        }
        return true
    }

    function anagram(str1:string, str2:string):boolean {
        const str1ToLower = str1.toLowerCase()
        const str2ToLower = str2.toLowerCase()

        if(str1ToLower.length !== str2ToLower.length) {
            return false
        }

        for (let i = 0; i < str1ToLower.length; i++) {
            const element = str1ToLower[i];
            
            if(!str2ToLower.includes(element)) {
                return false
            }
            
        }

        return true
    }

    function isogram(str: string): boolean {
        const strToLower = str.toLowerCase();
        let letrasVistas = new Set<string>();
    
        for (let letra of strToLower) {
            if (letrasVistas.has(letra)) {
                return false;
            }
            letrasVistas.add(letra);
        }
        return true;
    }

    function bothAreIsogram(str1: string, str2: string): boolean { 
        return isogram(str1) && isogram(str2)
    } 

})()