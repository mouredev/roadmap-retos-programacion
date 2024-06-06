
//Strings
(()=>{
//Comillas aceptadas
console.log('Comillas sencillas')
console.log("Comillas dobles")
console.log(`Comillas invertidas`)

const texto = 'Hola, Typescript'
console.log(texto.length); //lonigtud


// obtener caracter individual
console.log(texto.charAt(6));
console.log(texto[0]);

// concatenar 
console.log(texto.concat(' bienvenido.'));
console.log(texto+' bienvenido.');
console.log(`${texto} bienvenido.`);

// busca en contenido
console.log(texto.includes('script')); // contiene el texto
console.log(texto.startsWith('T')); // caracter inicial 
console.log(texto.endsWith('.')); // caracter final 
console.log(texto.indexOf(',')); // y devuelve indice de la 1er coincidencia
console.log(texto.match(/\w+,\s\w+/)); //coincidencia con expresion regular
console.log(texto.search(/\s/)); //devuelve indice decoinicencia expresion regular

//motificaciones
console.log(texto.toUpperCase); //mayusulas
console.log(texto.toLowerCase); //minusculas
console.log(texto.repeat(3)); //repite cadena n veces
console.log(texto.replace('Hola','Bienvenido')); //remplaza 
console.log(texto.replace(/^\w+,/,'Bienvenido,')); //remplaza con expreison regular

console.log(texto.split(' ')); // separa por el caracter especifico
console.log(texto.split(', ').join('___')); // une con caracter especifico
console.log(texto.split(', ').reverse().join(' ')); // separa por el caracter especifico, invierte las coincidencias y une


//Dificultad Extra

const validarPalabras= (palabra1:string,palabra2:string) => {

  //palindromos
  [palabra1,palabra2].forEach((texto)=>{
    if (texto.toLowerCase().replace(' ','') == texto.toLowerCase().replace(' ','').split('').reverse().join('') ) {
      console.log(`+ "${texto}" Es palindromo`);
    } else {
      console.log(`- "${texto}" NO es palindromo`);
    }
  })

  //anagrama
  let texto1 = palabra1.toLowerCase().replace(' ','').trim().split('')
  let texto2 = palabra2.toLowerCase().replace(' ','').trim().split('')
  let encontradas = 0;

  if(texto1.length == texto2.length){
    texto1.forEach((letra)=>{
      if (texto2.includes(letra)) {
        let pos = texto2.indexOf(letra)
        texto2.splice(pos,1)
        encontradas++
      }
    })

    if(encontradas == texto1.length){
      console.log(`+ "${palabra1}"-"${palabra2}" Son un anagrama`);
    }else{
      console.log(`- "${palabra1}"-"${palabra2}" NO son un anagrama`);
    }
  }else {
    console.log(`- "${palabra1}"-"${palabra2}" NO son un anagrama`);
  }

  //isograma

  [palabra1,palabra2].forEach((texto)=>{
    let parsed = texto.toLowerCase().trim().replace(' ','')
    let myset = new Set(parsed)

    if(myset.size == parsed.length){
      console.log(`+ "${texto}" Es isograma`);
    }else{
      console.log(`- "${texto}" NO es isograma`);
    }

  })

}

console.log('---');
validarPalabras('radar','isogram')
console.log('---');
validarPalabras('cuaderno','educaron')
console.log('---');











})();


