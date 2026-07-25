/* I use *Professional JavaScript for Web Developers* by Matt Frisbie as a reference to generate accurate comment descriptions and to understand JavaScript's capabilities in string manipulation. I also use GPT to correct some translations, syntax, and grammar.
*/

//short for console.log
let log = console.log.bind(console);

//STRING TYPE
//The String type is the object representation of strings and is created using the String constructor as follows:
let stringObject = new String("hello girl");
//The methods of a String object are available for all string primitives.

/*Every time a primitive value is read, an object of the corresponding primitive wrapper type is created behind the scenes, allowing access to various methods for manipulating the data. */ 

let q = 'Did you know Internet start as a Pentagon project named ARPANET(Advanced Research Projects Agency Network)?'
let q2 = q.substring(12);
log(q2); // Internet start as a Pentagon project named ARPANET(Advanced Research Projects Agency Network)?

//The JavaScript Character
//JavaScript strings consist of 16-bit code units. For most characters, each 16-bit code unit corresponds to a single character. The length property indicates how many 16-bit code units are present in the string
let message = "Sometimes you make me smile...";
log(message.length); // 30
log(message.charAt(10)); // y
log(message.charCodeAt(10)); // 121
log(message.indexOf('m')); // 2
log(message.lastIndexOf('m')); // 23
let chart = message.lastIndexOf('s');
let chart2 = message.indexOf('.');
log(message.substring(chart, chart2)); // smile
log(message.substring(-8)); // Sometimes you make me smile..
log(message.substr(-8)); // smile... (I believe this method may be deprecated)

log(message.substring(message.length - 8))// smile...
let arr = message.substring(0, 8).split('');
log(arr)// Array(8) [ "S", "o", "m", "e", "t", "i", "m", "e" ]  ( no inclusive the last index )
log(arr.join('-')); // S-o-m-e-t-i-m-e    
log(arr[arr.length - 1].replace('e', 'e-s')); // e-s
log(arr.join('-').replaceAll('-', '') + 's'); // Sometimes 

//Note: It is important to know that some emojis are composed of two 16-bit code units, so you have to take this into consideration when evaluating or using the length property.

let fragment = '   at this point in my life...  ';
log(fragment.trim()); // Logs: at this point in my life... (without spaces at the begining or at the end)

//Note: you can also use trimStart() or trimEnd()

let name = 'anna';
log(name.toUpperCase()); // ANNA
let othername = 'Luna';
log(othername.toLowerCase()); // luna

//we can also use String.fromCharCode() method

log(String.fromCharCode(193, 48, 587, 482, 102, 107)); // Á0ɋǢfk
log(String.fromCharCode(0x68fa)); // 棺

//Note: using fromCharCode() may have performance implications, especially if called frequently or with a large number of characters. 
 
/* The normalize() Method. Some Unicode characters can be encoded in more than one way. Sometimes, a character can be represented by either a single BMP character or a surrogate pair. For example, consider the following: */

// U+00C5: Latin capital letter A with ring above
log(String.fromCharCode(0x00C5)); // Å
// U+212B: Angstrom sign
log(String.fromCharCode(0x212B)); // Å
// U+0041: Latin captal letter A
// U+030A: Combining ring above
log(String.fromCharCode(0x0041, 0x030A)); // Å

let unnormalized_text = String.fromCharCode(0x0041, 0x030A, 0x212B, 0x00C5);
log(unnormalized_text.charCodeAt(1), unnormalized_text.charCodeAt(3)); // 778 197
let normalized_text = unnormalized_text.normalize();
log(normalized_text.charCodeAt(1), normalized_text.charCodeAt(3)); // 197 NaN  (Because the first character is converted from a surrogate pair to a single BMP character, there is no character at charCodeAt(3). After normalization, there are only three characters, all with the same code: 197.)

//Unicode addresses this by providing four normalization forms that allow characters, such as this one, to be normalized into a consistent format, regardless of their character code derivation.

//we can concatenate strings by using the concat() method or the + unary operator
let firstName = 'Patty';
let lastName = ' Smith';
let longName = firstName.concat(lastName);
log(longName)// Patty Smith
//same as
log(firstName + lastName); // Patty Smith

//or make use of the previus methods to f.e capitalize a word
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

log(capitalize(name)); // Anna

//There are two methods for locating substrings within another string: indexOf() and lastIndexOf(). Both methods search a string for a given substring and return the position (or –1 if the substring isn’t found).

let fragment2 = 'the fire is burned, the tables are turned...';
log(fragment2.indexOf('is')); // 9 
log(fragment2.indexOf('house')); // -1
log(fragment2.lastIndexOf('t')); // 35

//String Inclusion Methods
log(fragment2.startsWith("the")); // true
log(fragment2.endsWith("fire")); // false

let say = 'oh';
log(say.repeat(2) + '!'); // ohoh!

//I think padStart() and padEnd() are deprecated, but we can create our own function to achieve the same result. For example, let's try to emulate the padStart() method.

function  addPad(str, width, pad = 0){
    let result = String(str); 
    while (result.length < width) {
         result = `${pad}` + result;
    }
     return result;
 }
 
 
 log(addPad(4, 3, '#')); // ##4
 log(addPad(56, 3, '$')); // $56
 log(addPad(7, 3)); // 007
 log(addPad('something', 3, '-')); // ---something

 const greeting = "tururuuu";
 const paddedString = addPad.call(greeting, greeting, 11, "&");
 log(paddedString); //  &&&tururuuu

//we can use match() and RegExp() (or regular expression patterns) to evaluate regular expressions in a string, f.e.

function toCamelCase(input) {
    return (
        input
            // Replace kebab-case, snake_case, and spaces with a space
            .replace(/[-_\s]+(.)?/g, (_, char) => (char ? char.toUpperCase() : ''))
            // Handle PascalCase
            .replace(/^[A-Z]/, (char) => char.toLowerCase())
    );
}

log(toCamelCase('PascalCase')); // pascalCase
log(toCamelCase('kebab-case-string')); // kebabCaseString
log(toCamelCase('snake_case_string')); // snakeCaseString
log(toCamelCase('string with spaces')); // stringWithSpaces


window.addEventListener('load', function(){
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #4.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    this.setTimeout(()=>{
    alert('Retosparaprogramadores #4. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #4'); // this will be logged at the end cause the nature of window event
});


/*ADDITIONAL DIFFICULTY (optional):
Create a program that analyzes two different words and performs checks
to determine if they are:  Palindromes   Anagrams   Isograms */


//Palindrome: A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

const isPolidrome = (w1, w2)=>{
    if(w1.length != w2.length) return false
  let fw = w1.split('')
  let sw = w2.split('')
    for(let i = 0, k = w1.length;i < w1.length; i++, k--){
      if(fw[i] != sw[k-1]) return false;       
    }  
    return true;
}

log('is isPolidrome: ', isPolidrome('roma', 'amor'))//Logs: true

//Anagram: An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. 

const isAnagram = (w1, w2)=>{

    if(w1.length != w2.length) return false;
  
    let result = w1.split('').some(l =>
        w2.split('').some(v => v == l)
    )
   return result;	
}

log('is anagram: ', isAnagram('nick','kinc')); //Logs: true

//Isogram: An isogram is a word or phrase in which no letter occurs more than once. For example, "lumberjack" and "background" are isograms because none of the letters are repeated.

const isIsogram = (str)=>{
  let countLetters = [];
str.split('').forEach((l,index)=>{
    countLetters[index] = str.split('').filter(char => l == char).length
});
//console.log('countLetters: ', countLetters);  
  for(let num of countLetters){
  if(num > 1) return false;
}
return true;
}

log('is isogram: ', isIsogram('background')); //Logs: true

//the function check when two strings are polidromes, anagrams or isograms
const checkState = (str1, str2)=>{
    let r_poli = isPolidrome(str1, str2);
    let r_anag = isAnagram(str1, str2);
    let f_iso = isIsogram(str1);
    let s_iso = isIsogram(str2);
    let result = '';
    let bool = false;

if(r_poli && r_anag && f_iso && s_iso){
    result = `The words: "${str1}" and "${str2}" are polidromes, anagrams and also isograms.`
    bool = true;
}else if(r_poli){
    result = `The words: "${str1}" and "${str2}" are polidromes and anagrams but they aren't isograms. `
}else if(r_anag && f_iso && s_iso){
    result = `The words: "${str1}" and "${str2}" are anagrams and also isograms.`
    bool = true;
}else if(r_anag){
    result = `The words: "${str1}" and "${str2}" are anagrams. `
}

  if(!bool){  
      if(f_iso && s_iso){
          result = `The words: "${str1}" and "${str2}" are isograms. `
      }else if(f_iso){
          result += `The first word: "${str1}" is an isogram`
      }else if(s_iso){
          result += `The second word: "${str2}" is an isogram`
      }else if(!r_poli&&!r_anag){
       result = `The words: "${str1}" and "${str2}" aren't polidromes, anagrams or isograms.`
      }
  }  

 log(result)

}

checkState('amor','mora'); /* Logs: The words: "amor" and "mora" are anagrams and also isograms */
checkState('amor','roma'); /* logs: The words: "amor" and "roma" are polidromes, anagrams and also isograms.*/
checkState('zeitgest','kaguabumga'); /* Logs: The words: "zeitgest" and "kaguabumga" aren't polidromes, anagrams or isograms.*/
checkState('pizza', 'background'); /* Logs: The second word: "background" is an isogram  */

