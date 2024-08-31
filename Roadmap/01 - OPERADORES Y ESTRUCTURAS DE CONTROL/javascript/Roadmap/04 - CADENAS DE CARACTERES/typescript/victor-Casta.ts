// Acceso a caracteres específicos
const myCharacter: string = 'TypeScript';
console.log(myCharacter.charAt(0));

// Subcadenas
const myString1: string = 'Hello TypeScript';
console.log(myString.substring(0, 5));
console.log(myString.slice(6));

// Longitud
const Username: string = 'Victor';
console.log(`the username length is the: ${Username.length} characters`);

// Concatenación
const productTitle: string = 'Product 1';
console.log(`Product: ${productTitle}`);

// Repetición
console.log('-'.repeat(10));

// Recorrido
const programLanguage: string = 'TypeScript';
for (let char of programLanguage) {
  console.log(char);
}

// Conversión a mayúsculas y minúsculas
const myProgramLanguage: string = 'typescript';
const uppercaseProgram: string = myProgramLanguage.toUpperCase();
const lowercaseProgram: string = myProgramLanguage.toLowerCase();
console.log(`Uppercase program: ${uppercaseProgram}`);
console.log(`Lowercase program: ${lowercaseProgram}`);

// Reemplazo
let replacedString1: string = "Hello TypeScript".replace("TypeScript", "JavaScript");
console.log(replacedString);

// División
const myDivideString: string = "Hello,TypeScript,in,the,roadmap";
const parts: string[] = myDivideString.split(',');
console.log(parts);

// Unión
console.log(parts.join(' '));
const greeting: string = 'Hello';
const greeting2: string = 'Mundo';
console.log(`${greeting}, ${greeting2}`);

// Interpolación
let language: string = 'TypeScript';
console.log(`Welcome to ${language}`);

// Verificación
console.log(typeof language);

// "Extra"
const myProgram1 = (word1: string, word2: string) => {
  const formatWord1: string = word1.replace(/\s/g, '').toLowerCase();
  const formatWord2: string = word2.replace(/\s/g, '').toLowerCase();

  const isPalindrome = (word: string): boolean => {
    const reversedWord = word.split('').reverse().join('');
    return word === reversedWord;
  };

  const isAnagram = (word1: string, word2: string): boolean => {
    const sortedWord1 = word1.split('').sort().join('');
    const sortedWord2 = word2.split('').sort().join('');
    return sortedWord1 === sortedWord2;
  };

  const isIsogram = (word: string): boolean => {
    const charSet = new Set<string>(word);
    return charSet.size === word.length;
  };

  if (isPalindrome(formatWord1) && isPalindrome(formatWord2)) {
    console.log(`La palabra ${word1} y ${word2} son palíndromos.`);
  } else if (isAnagram(formatWord1, formatWord2)) {
    console.log(`La palabra ${word1} y ${word2} son anagramas.`);
  } else if (isIsogram(formatWord1) && isIsogram(formatWord2)) {
    console.log(`La palabra ${word1} y ${word2} son isogramas.`);
  } else {
    console.log('No son ni palíndromos ni anagramas ni isogramas.');
  }
};

myProgram('roma', 'amor');
