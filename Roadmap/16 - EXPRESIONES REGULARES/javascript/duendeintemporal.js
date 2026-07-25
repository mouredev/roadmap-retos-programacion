// #16 EXPRSIONES REGULARES
// bibliography reference
// Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)

/* EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.*/

// short for console.log()
let log = console.log;

window.addEventListener('load', ()=>{
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #16.';
    title.style.setProperty('font-size', '3.5vmax');
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    setTimeout(()=>{
    alert('Retosparaprogramadores #16. Please open the Browser Developer Tools.');
    }, 2000);
    log( 'Retosparaprogramadores #16'); 
});

/*
Some Flags  (also known as a modifiers)
➤➤
g—Indicates global mode, meaning the pattern will be applied to all of the string instead of
stopping after the first match is found.
➤➤
i—Indicates case-insensitive mode, meaning the case of the pattern and the string are
ignored when determining matches.
➤➤
m—Indicates multiline mode, meaning the pattern will continue looking for matches after
reaching the end of one line of text.
➤➤
y—Indicates sticky mode, meaning the pattern will only look at the string contents
beginning at lastIndex.
➤➤
u—Indicates Unicode mode is enabled.
*/


/*
As with regular expressions in other languages, all metacharacters must be escaped when used as part
of the pattern. The metacharacters are as follows:
( [ { \ ^ $ | ) ] } ? * + .
*/

/*
Each instance of RegExp has the following properties that allow you to get information about
the pattern:
➤➤
global—A Boolean
value indicating whether the g flag has been set.
➤➤
ignoreCase—A Boolean value indicating whether the i flag has been set.
➤➤
unicode—A Boolean value indicating whether the u flag has been set.
➤➤
sticky—A Boolean value indicating whether the y flag has been set.
➤➤
lastIndex—An integer indicating the character position where the next match will be
attempted in the source string. This value always begins as 0.
➤➤
multiline—A Boolean value indicating whether the m flag has been set.
➤➤
source—The string source of the regular expression. This is always returned as if specified
in literal form (without opening and closing slashes) rather than a string pattern as passed
into the constructor.
➤➤
flags—The string flags of the regular expression. This is always returned as if specified in
literal form (without opening and closing slashes) rather than a string pattern as passed into
the constructor.
*/


// Define a pattern and flags
const pattern0 = 'abc';
const flags = 'gi'; // Global and case-insensitive

// Create a regular expression using the RegExp constructor
const regex = new RegExp(pattern0, flags);

log(regex); // /abc/gi

let text = "time: 08:07:06";
let pattern1 = /(time(:)?)? ?([01][0-9]|2[0-3])([:/-])([0-5][0-9])\4([0-5][0-9])/;

/*
**Explanation of the regular expression:**
- **(time(:)?)**: Optionally matches the word "time" followed by an optional colon (:).
- **?**: Matches an optional space.
- **([01][0-9]|2[0-3])**: Matches the hour, allowing values from 00 to 23.
  - **[01][0-9]**: Matches hours from 00 to 19.
  - **|**: "Or" operator.
  - **2[0-3]**: Matches hours from 20 to 23.
- **([:/-])**: Matches one of the characters :, /, or - and captures it for later use.
- **([0-5][0-9])**: Matches the minutes (00 to 59).
- **\4**: References the fourth captured group, which is the separator (it must be the same as used between the hour and the minutes).
- **([0-5][0-9])**: Matches the seconds (00 to 59).
*/

let matches1 = pattern1.exec(text);

if(matches1){
    log(matches1.index); // 0
    log(matches1.input); // time: 08:07:06
    log(matches1[0]); // time: 08:07:06
    log(matches1[1]); // time:
    log(matches1[2]); // :
}

let pattern = /[0-9]/g;
let matches = pattern.exec(text);
if(matches) log(matches) // ['0', index: 6, input: 'time: 08:07:06', groups: undefined]

let matches3 = text.match(pattern);
if(matches3) log(matches3) // ['0', '8', '0', '7', '0', '6']

//Note: that match() return all concidence when using global flat g

if(matches3){
    log(matches3.index); // undefined
    log(matches3.input); // undefined
    log(matches3[0]); // 0
    log(matches3[1]); // 8
    log(matches3[2]); // 0
}

let pattern2 = /\d/g
let matches2 = pattern2.exec(text);
if(matches2) log(matches2) // ['0', index: 6, input: 'time: 08:07:06', groups: undefined]

let matches4 = text.match(pattern2);
if(matches4) log(matches4) // ['0', '8', '0', '7', '0', '6']

/*
exec: Returns the first match and can be used in a loop to find all matches.

match: Returns an array with all matches in a more direct and straightforward way.
*/

//Extra Dificulty Exercise:

const validateTlf = (num)=>{
    if (!/^\d{11}$/.test(num)) {
        console.log("Invalid telephone number. Must be a numeric value and have 11 digits.");
        return false; 
    }    
    return true;
}

const ValidateEmail = (email)=>{
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if(!emailRegex.test(email)){
        console.log("Invalid emnail adress");
        return false;
    }
    return true;
}

const validateURL = (url)=>{
    const urlRegex = /^(https?:\/\/)?([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(\/[^\s]*)?$/;
    if(!urlRegex.test(url) || (!url.startsWith('http://') && !url.startsWith('https://'))){
        console.log("Invalid URL");
        return false;
    }
    return true;
}

let num1 = 1562737848, num2 = 34587452387, email1 = 'kamsutraniko@proton.me', email2 = 'kat@hotgirl.net', url1 = 'http://palnetaneurodiverso.org', url2 = 'https://moebius.org', url3 = 'something.com', url4 = 'gato';

log(validateTlf(num1)); // Invalid telephone number. Must be a numeric value and have 11 digits. false
log(`Is a valid tlf: ${validateTlf(num2)}`) // Is a valid tlf: true
log(`Is a valid tlf: ${ValidateEmail(email1)}`); // Is a valid tlf: true
log(`Is a valid email: ${ValidateEmail(email2)}`); // Is a valid email: true
log(`Is a valid URL: ${validateURL(url1)}`); // Is a valid URL: true
log(`Is a valid URL: ${validateURL(url2)}`); // Is a valid URL: true
log(`Is a valid URL: ${validateURL(url3)}`); // Invalid URL Is a valid URL: false
log(`Is a valid URL: ${validateURL(url4)}`);  // Invalid URL Is a valid URL: false

