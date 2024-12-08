//EJERCICIO
let cadena = 'soy una cadena'
// Constructor
// String() constructor
const construct:{} = new String()//The String() constructor creates String objects.
const constructFunction:string = String()//When called as a function, it returns primitive values of type String.
// Static methods
// String.fromCharCode()
String.fromCharCode(104, 111, 108, 97)// returns a string created from the specified sequence of UTF-16 code units. --> this example return hola
// String.fromCodePoint()
String.fromCodePoint(104, 111, 108, 97)//returns a string created from the specified sequence of code points. --> the main diferences is that use unicode points and dont return  'suplement chars' like fromCharCode and required use surrogate pair to return a suplement chars
// String.raw()
const filePath = String.raw`C:\Development\profile\aboutme.html`;
console.log(`The file was uploaded from: ${filePath}`);
// Expected output: "The file was uploaded from: C:\Development\profile\aboutme.html"
// Instance methods
// String.prototype.at()
cadena.at(-1)//The at() method of String values takes an integer value and returns a new String consisting of the single UTF-16 code unit located at the specified offset.  this ex return --> a to 'soy una cadena'
// String.prototype.charAt()
cadena.charAt(3)//return character of specific index --> '' white space after 'soy'
// String.prototype.charCodeAt()
cadena.charCodeAt(3)//return unicode of specific location --> 32
// String.prototype.codePointAt()
cadena.codePointAt(3)//return unicode code point of location index --> 32
// String.prototype.concat()
cadena.concat(' yo tambien') //return string concatenate the first and second string --> return 'soy una cadena yo tambien'
// String.prototype.endsWith()
cadena.endsWith(cadena) // return boolean if string ends with a sequence of string also specific index end point endsWith(string,endIndex)
// String.prototype.includes()
cadena.includes('soy') // return boolean and case-sensitive: search to determine whether a given string may be found within this string
// String.prototype.indexOf()
cadena.indexOf('ca')//Returns the position of the first occurrence of a substring.
// String.prototype.isWellFormed()
cadena.isWellFormed()// returns a boolean indicating whether this string contains any lone surrogates. -->true
// String.prototype.lastIndexOf()
cadena.lastIndexOf('a')//Returns the last occurrence of a substring in the string. --> 13
// String.prototype.localeCompare()
cadena.localeCompare('SOY UNA CADENA')//Returns an integer indicating whether the referenceStr comes before, after or is equivalent to the compareString. --> -1
// String.prototype.match()
cadena.match(/[a-z]/g)//The match() method of String values retrieves the result of matching this string against a regular expression. --> return the same 'soy una cadena' but in array separate by chars
// String.prototype.matchAll()
cadena.matchAll(/[a-z]/g)//The matchAll() method of String values returns an iterator of all results matching this string against a regular expression, including capturing groups.
// String.prototype.normalize()
cadena.normalize()//Returns the String value result of normalizing the string into the normalization form named by form as specified in Unicode Standard Annex #15, Unicode Normalization Forms.
// String.prototype.padEnd()
cadena.padEnd(20,'-')//The padEnd() method of String values pads this string with a given string (repeated, if needed) so that the resulting string reaches a given length. The padding is applied from the end of this string. --> return 'soy una cadena------' but THE LENGTH OF THE RESULTING STRING ONCE THE CURRENT STRING HAS BEEN PADDED. IF THIS PARAMETER IS SMALLER THAN THE CURRENT STRING'S LENGTH, THE CURRENT STRING WILL BE RETURNED AS IT IS.
// String.prototype.padStart()
cadena.padStart(20,'+')//Pads the current string with a given string (possibly repeated) so that the resulting string reaches a given length. The padding is applied from the start (left) of the current string.
// String.prototype.repeat()
cadena.repeat(3)// Returns a String value that is made from count copies appended together. If count is 0, the empty string is returned. -->'soy una cadenasoy una cadenasoy una cadena'
// String.prototype.replace()
cadena.replace('a','@')//Replaces text in a string, using a regular expression or search string.--> 'no soy un@ cadena'
// String.prototype.replaceAll()
cadena.replaceAll('a','@')//Replace all instances of a substring in a string, using a regular expression or search string. --> 'no soy un@ c@den@'
// String.prototype.search()
cadena.search('una')//Finds the first substring match in a regular expression search. -->return 4
// String.prototype.slice()
cadena.slice(0,5)//Returns a section of a string. return --> 'soy u'
// String.prototype.split()
cadena.split('')//Split a string into substrings using the specified separator and return them as an array. return -->[ 's', 'o', 'y', ' ', 'u', 'n', 'a', ' ', 'c', 'a', 'd', 'e', 'n', 'a' ]

// String.prototype.startsWith()
cadena.startsWith('a')//Returns true if the sequence of elements of searchString converted to a String is the same as the corresponding elements of this object (converted to a String) starting at position. Otherwise returns false. return --> 'false'
// String.prototype.substring()
cadena.substring(5,10)//Returns the substring at the specified location within a String object. return -->'na ca'
// String.prototype[Symbol.iterator]()
const iterator = cadena[Symbol.iterator]();
let theChar = iterator.next();
/*
The [Symbol.iterator]() method of String values implements the iterable protocol and allows strings to be consumed by most syntaxes expecting iterables, such as the spread syntax and for...of loops. It returns a string iterator object that yields the Unicode code points of the string value as individual strings.
*/
while (!theChar.done && theChar.value !== ' ') {
  console.log(theChar.value);
  theChar = iterator.next();
  // Expected output: "s"
  //                  "o"
  //                  "y"
}
// String.prototype.toLocaleLowerCase()
cadena.toLocaleLowerCase()//Converts all alphabetic characters to lowercase, taking into account the host environment's current locale. return --> 'soy una cadena'
// String.prototype.toLocaleUpperCase()
cadena.toLocaleUpperCase()//Returns a string where all alphabetic characters have been converted to uppercase, taking into account the host environment's current locale.return --> 'SOY UNA CADENA'
// String.prototype.toLowerCase()
cadena.toLowerCase()//Converts all the alphabetic characters in a string to lowercase. return --> 'soy una cadena'
// String.prototype.toString()
cadena.toString()//Returns a string representation of a string.
// String.prototype.toUpperCase() return --> 'soy una cadena'
cadena.toUpperCase()//Converts all the alphabetic characters in a string to uppercase. return --> 'SOY UNA CADENA'
// String.prototype.toWellFormed()
cadena.toWellFormed()//Returns a string where all lone or out-of-order surrogates have been replaced by the Unicode replacement character (U+FFFD). return -->'SOY UNA CADENA'
// String.prototype.trim()
"  SOY UNA CADENA  ".trim()//Removes the leading and trailing white space and line terminator characters from a string. return --> "SOY UNA CADENA"
// String.prototype.trimEnd()
"  SOY UNA CADENA  ".trimEnd()//Removes the trailing white space and line terminator characters from a string. return -->"SOY UNA CADENA  "
// String.prototype.trimStart()
"  SOY UNA CADENA  ".trimStart()//Removes the leading white space and line terminator characters from a string. return --> "  SOY UNA CADENA"
// String.prototype.valueOf()
cadena.valueOf()//Returns the primitive value of the specified object.
const str = new String('soy una cadena');
console.log(str);
// Expected output: String { "soy una cadena" }
console.log(str.valueOf());
// Expected output: "soy una cadena"
//DIFICULTAD EXTRA
//DIFICULTAD EXTRA
console.log('Hola, soy un programa para analizar tus textos!..dime:¿que quieres hacer hoy?')
console.log(`
  1.-Palindromos
  2.-Anagramas
  3.-Isogramas
  *-Salir de la aplicacion
  `)
  let option :string | null
  do{
option = prompt(`Que quieres hacer?
    1.-Palindromos
  2.-Anagramas
  3.-Isogramas
  *-Salir de la aplicacion escribe cualquier cosa diferente a los numero de las opciones...
    `);

let word;
let response;
switch (option) {
  case '1':
    do{
 word = prompt('Dime la palabra?...')
    }while(!word)
     response = palindromeChecker(word)? (`${word} es un palindromo!`) : (`Ohh...lo siento ${word} no es un palindromo`);
    alert(response)
    break;
  case '2':
    let firstWord
 let secondWord
    do{
  firstWord = prompt('Dime la primera palabra?...')
  secondWord = prompt('Dime la segunda palabra?...')
    }while(!firstWord && !secondWord)
     response = anagramChecker(firstWord!,secondWord!)? (`${firstWord} es un anagrama de ${secondWord}!`) : (`Ohh...lo siento ${firstWord} no es un anagrama de ${secondWord}`);
    alert(response)
    break;
  case '3':

    do{
        word = prompt('Dime la palabra?...')
    }while(!word)
    response = isogramChecker(word) ?  (`${word} es un isograma!`) : (`Ohh...lo siento ${word} no es un isograma`)
    alert(response)
    break;
  default:
    option ? alert('Saliendo del programa....'):'';
    break;
}
}while(['1','2','3'].some(select=> select===option) || !option)

  function palindromeChecker(word:string):boolean{
    const isPalindrome = word.split("").every((letter, position, word) => {
      return letter == word[word.length - position - 1]; //check if the character Position is the same that Inverse character Position in every letter if every letter is equal then is Palindrome
    });
    return isPalindrome
  }
  function isogramChecker(word:string):boolean{
    const letterCounts = word
    .split("")
    .reduce((letterMap: { [key: string]: number }, position) => {
      if (!letterMap[position]) {
        letterMap[position] = 1;
      } else {
        letterMap[position] += 1;
      }
      return letterMap;//this create a map that contain letter and many times appear in the word: {a:1 , b:2 ,c:3}
    }, {});

  const isIsogram = Object.values(letterCounts).every(
    (count) => count === letterCounts[word[0]] //if de first count value is the same that every count then is Isogram by definition
  );
  return isIsogram;
  }
  function anagramChecker(wordOne: string, wordTwo: string): boolean {
    return (
      wordOne.split("").toSorted().join("") == wordTwo.split("").toSorted().join("") // sort alpabhetical letters in every word and compare IF the word one order is the same that the word two order then is Anagram by definition
    );
  }