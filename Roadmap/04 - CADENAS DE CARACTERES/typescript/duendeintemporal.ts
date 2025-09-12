//#04 { retosparaprogramadores } CADENAS DE CARACTERES
/* I use *Professional JavaScript for Web Developers* by Matt Frisbie as a 
reference to generate accurate comment descriptions and to understand JavaScript's capabilities in string manipulation. I also use GPT and Deepseek to correct some translations, syntax, and grammar.
*/

//short for console.log
let log = console.log;

//STRING TYPE
//The String type is the object representation of strings and is created using the String constructor as follows:
let stringObject = new String("hello girl"); // it will throw an ts(2322) error if we attend to set string type to stringObject so it is preferible to avoid using new String() in TypeScript. Use primitive strings (let str: string = "hello") instead. The primitive string type automatically gives access to all string methods.
log(stringObject) // [String: 'hello girl']

//The methods of a String object are available for all string primitives.

/*Every time a primitive value is read, an object of the corresponding primitive wrapper type is created behind the scenes, allowing access to various methods for manipulating the data. */ 

let q: string = 'Did you know Internet start as a Pentagon project named ARPANET(Advanced Research Projects Agency Network)?'
let q2: string = q.substring(12); // Extracts the substring starting from index 12
log(q2); // Internet start as a Pentagon project named ARPANET(Advanced Research Projects Agency Network)?

//The JavaScript Character
//JavaScript strings consist of 16-bit code units. For most characters, each 16-bit code unit corresponds to a single character. The length property indicates how many 16-bit code units are present in the string
let message: string = "Sometimes you make me smile...";
log(message.length); // 30
log(message.charAt(10)); // y
log(message.charCodeAt(10)); // 121 (charCodeAt returns the UTF-16 code unit for the character at the given index)
log(message.indexOf('m')); // 2
log(message.lastIndexOf('m')); // 23
let chart: number = message.lastIndexOf('s');
let chart2: number = message.indexOf('.');
log(message.substring(chart, chart2)); // smile
log(message.substring(-8)); // Sometimes you make me smile..
log(message.substr(-8)); // smile... (I believe this method may be deprecated)

log(message.substring(message.length - 8))// smile...
let arr: any = message.substring(0, 8).split('');
log(arr)// Array(8) [ "S", "o", "m", "e", "t", "i", "m", "e" ]  ( no inclusive the last index )
log(arr.join('-')); // S-o-m-e-t-i-m-e    
log(arr[arr.length - 1].replace('e', 'e-s')); // e-s
log(arr.join('-').replaceAll('-', '') + 's'); // Sometimes 

//Note: It is important to know that some emojis are composed of two 16-bit code units, so you have to take this into consideration when evaluating or using the length property.

let fragment = '   at this point in my life...  ';
log(fragment.trim()); // Logs: at this point in my life... (without spaces at the begining or at the end)

//Note: you can also use trimStart() or trimEnd()

let userName: string = 'anna';
log(userName.toUpperCase()); // ANNA
let othername: string = 'Luna';
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
let normalized_text: string = unnormalized_text.normalize();
log(normalized_text.charCodeAt(1), normalized_text.charCodeAt(3)); // 197 NaN  (Because the first character is converted from a surrogate pair to a single BMP character, there is no character at charCodeAt(3). After normalization, there are only three characters, all with the same code: 197.)

//Unicode addresses this by providing four normalization forms that allow characters, such as this one, to be normalized into a consistent format, regardless of their character code derivation.

//we can concatenate strings by using the concat() method or the + unary operator
let firstName: string = 'Patty';
let lastName: string = ' Smith';
let longName: string = firstName.concat(lastName);
log(longName)// Patty Smith
//same as
log(firstName + lastName); // Patty Smith
// a better way
log(`${firstName}${lastName}`); // Patty Smith

//or make use of the previus methods to f.e capitalize a word
function capitalize(str: string): string {
    if (!str) return str;
    return str.charAt(0).toUpperCase() + str.slice(1);
}

log(capitalize(userName)); // Anna

//There are two methods for locating substrings within another string: indexOf() and lastIndexOf(). Both methods search a string for a given substring and return the position (or –1 if the substring isn’t found).

let fragment2: string = 'the fire is burned, the tables are turned...';
log(fragment2.indexOf('is')); // 9 
log(fragment2.indexOf('house')); // -1
log(fragment2.lastIndexOf('t')); // 35

//String Inclusion Methods
log(fragment2.startsWith("the")); // true
log(fragment2.endsWith("fire")); // false

let say: string = 'oh';
log(say.repeat(2) + '!'); // ohoh!

//I think padStart() and padEnd() are deprecated, but we can create our own function to achieve the same result. For example, let's try to emulate the padStart() method.

function  addPad(str: any, width: number, pad: any = 0): string {
    let result = String(str); 
    while (result.length < width) {
         result = `${pad}` + result;
    }
     return result;
 }
 
 
 log(addPad(4, 3, '#')); // ##4
 log(addPad(56, 3, '$')); // $56
 log(addPad(7, 3)); // 007
 log(addPad('something', 3, '-')); // something  (cause something length is bigger than 3)

 const greeting: string = "tururuuu";
 const paddedString: string = addPad.call(greeting, greeting, 11, "&");
 log(paddedString); //  &&&tururuuu

//we can use match() and RegExp() (or regular expression patterns) to evaluate regular expressions in a string, f.e.

function toCamelCase(input: string): string {
    return (
        input // Replace kebab-case, snake_case, and spaces with a space
            .replace(/[-_\s]+(.)?/g, (_, char) => (char ? char.toUpperCase() : ''))
            .replace(/^[A-Z]/, (char) => char.toLowerCase()) // Handle PascalCase
    );
}

log(toCamelCase('PascalCase')); // pascalCase
log(toCamelCase('kebab-case-string')); // kebabCaseString
log(toCamelCase('snake_case_string')); // snakeCaseString
log(toCamelCase('string with spaces')); // stringWithSpaces


    log( 'Retosparaprogramadores #4'); // Retosparaprogramadores #4 



/*ADDITIONAL DIFFICULTY (optional):
Create a program that analyzes two different words and performs checks
to determine if they are:  Palindromes   Anagrams   Isograms */


//Palindrome: A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.

const isPolidrome = (w1: string, w2: string): boolean => {
    if (w1.length !== w2.length) return false;
    return w1 === w2.split('').reverse().join('');
};

log('is isPolidrome: ', isPolidrome('roma', 'amor'))//Logs: true

//Anagram: An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. 

const isAnagram = (w1: string, w2: string): boolean => {
    if (w1.length !== w2.length) return false;
    return w1.split('').sort().join('') === w2.split('').sort().join('');
};

log('is anagram: ', isAnagram('nick','kinc')); //Logs: true

//Isogram: An isogram is a word or phrase in which no letter occurs more than once. For example, "lumberjack" and "background" are isograms because none of the letters are repeated.

const isIsogram = (str: string): boolean => {
    const charSet = new Set(str);
    return charSet.size === str.length;
};

log('is isogram: ', isIsogram('background')); //Logs: true

//the function check when two strings are polidromes, anagrams or isograms
const checkState = (str1: string, str2: string): void => {
    const isPoli = isPolidrome(str1, str2);
    const isAna = isAnagram(str1, str2);
    const isIso1 = isIsogram(str1);
    const isIso2 = isIsogram(str2);

    let result = '';
    if (isPoli && isAna && isIso1 && isIso2) {
        result = `The words: "${str1}" and "${str2}" are palindromes, anagrams, and isograms.`;
    } else if (isPoli) {
        result = `The words: "${str1}" and "${str2}" are palindromes.`;
    } else if (isAna && isIso1 && isIso2) {
        result = `The words: "${str1}" and "${str2}" are anagrams and isograms.`;
    } else if (isAna) {
        result = `The words: "${str1}" and "${str2}" are anagrams.`;
    } else if (isIso1 && isIso2) {
        result = `The words: "${str1}" and "${str2}" are isograms.`;
    } else if (isIso1) {
        result = `The first word: "${str1}" is an isogram.`;
    } else if (isIso2) {
        result = `The second word: "${str2}" is an isogram.`;
    } else {
        result = `The words: "${str1}" and "${str2}" are not palindromes, anagrams, or isograms.`;
    }

    log(result);
};

checkState('amor','mora'); /* Logs: The words: "amor" and "mora" are anagrams and also isograms */
checkState('amor','roma'); /* logs: The words: "amor" and "roma" are polidromes, anagrams and also isograms.*/
checkState('zeitgest','kaguabumga'); /* Logs: The words: "zeitgest" and "kaguabumga" aren't polidromes, anagrams or isograms.*/
checkState('pizza', 'background'); /* Logs: The second word: "background" is an isogram  */

