// #16 { Retosparaprogramadores } EXPRESIONES REGULARES
// Bibliography reference:
// Professional JavaScript for web developers by Matt Frisbie [Frisbie, Matt] (z-lib.org)

/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
 */

// Short for console.log()
const log = console.log;

// Conditional check for browser environment
if (typeof window !== 'undefined') {
    window.addEventListener('load', () => {
        const body: HTMLBodyElement | null = document.querySelector('body');
        const title = document.createElement('h1');

        body?.style.setProperty('background', '#000');
        body?.style.setProperty('text-align', 'center');

        title.textContent = 'Retosparaprogramadores #16.';
        title.style.setProperty('font-size', '3.5vmax');
        title.style.setProperty('color', '#fff');
        title.style.setProperty('line-height', '100vh');

        body?.appendChild(title);

        setTimeout(() => {
            alert('Retosparaprogramadores #16. Please open the Browser Developer Tools.');
        }, 2000);
        log('Retosparaprogramadores #16');
});
} else {
    log('This code is designed to run in a browser environment. Skipping window-related code.');
    log('Retosparaprogramadores #16');
}

/*
 * Regular Expression Flags (Modifiers):
 * - g: Global mode (applies to all matches in the string).
 * - i: Case-insensitive mode.
 * - m: Multiline mode.
 * - y: Sticky mode.
 * - u: Unicode mode.
 */

/*
 * Regular Expression Metacharacters:
 * ( [ { \ ^ $ | ) ] } ? * + .
 * These must be escaped when used in a pattern.
 */

/*
 * RegExp Instance Properties:
 * - global: Boolean indicating if the 'g' flag is set.
 * - ignoreCase: Boolean indicating if the 'i' flag is set.
 * - unicode: Boolean indicating if the 'u' flag is set.
 * - sticky: Boolean indicating if the 'y' flag is set.
 * - lastIndex: Integer indicating the position for the next match.
 * - multiline: Boolean indicating if the 'm' flag is set.
 * - source: The source string of the regular expression.
 * - flags: The flags of the regular expression.
 */

// Define a pattern and flags
const pattern0: string = 'abc';
const flags: string = 'gi'; // Global and case-insensitive

// Create a regular expression using the RegExp constructor
const regex: RegExp = new RegExp(pattern0, flags);

log(regex); // Output: /abc/gi

let text: string = "time: 08:07:06";
let pattern1 = /(time(:)?)? ?([01][0-9]|2[0-3])([:/-])([0-5][0-9])\4([0-5][0-9])/;

/*
 * Explanation of the regular expression:
 * - (time(:)?): Optionally matches the word "time" followed by an optional colon (:).
 * - ?: Matches an optional space.
 * - ([01][0-9]|2[0-3]): Matches the hour (00-23).
 * - ([:/-]): Matches a separator (:, /, or -).
 * - ([0-5][0-9]): Matches the minutes (00-59).
 * - \4: References the fourth captured group (separator).
 * - ([0-5][0-9]): Matches the seconds (00-59).
 */

let matches1 = pattern1.exec(text);

if (matches1) {
    log(matches1.index); // 0
    log(matches1.input); // time: 08:07:06
    log(matches1[0]); // time: 08:07:06
    log(matches1[1]); // time:
    log(matches1[2]); // :
}

let pattern = /[0-9]/g;
let matches = pattern.exec(text);
if (matches) log(matches); // ['0', index: 6, input: 'time: 08:07:06', groups: undefined]

let matches3 = text.match(pattern);
if (matches3) log(matches3); // ['0', '8', '0', '7', '0', '6']

// Note: match() returns all matches when using the global flag 'g'.

if (matches3) {
    log(matches3.index); // undefined
    log(matches3.input); // undefined
    log(matches3[0]); // 0
    log(matches3[1]); // 8
    log(matches3[2]); // 0
}

let pattern2 = /\d/g;
let matches2 = pattern2.exec(text);
if (matches2) log(matches2); // ['0', index: 6, input: 'time: 08:07:06', groups: undefined]

let matches4 = text.match(pattern2);
if (matches4) log(matches4); // ['0', '8', '0', '7', '0', '6']

/*
 * exec: Returns the first match and can be used in a loop to find all matches.
 * match: Returns an array with all matches in a more direct and straightforward way.
 */

// Extra Difficulty Exercise:

/**
 * Validates a telephone number.
 * @param num - The telephone number to validate.
 * @returns True if the telephone number is valid, otherwise false.
 */
const validateTlf = (num: string): boolean => {
    if (!/^\d{11}$/.test(num)) {
        console.log("Invalid telephone number. Must be a numeric value and have 11 digits.");
        return false;
    }
    return true;
};

/**
 * Validates an email address.
 * @param email - The email address to validate.
 * @returns True if the email address is valid, otherwise false.
 */
const validateEmail = (email: string): boolean => {
    const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailRegex.test(email)) {
        console.log("Invalid email address.");
        return false;
    }
    return true;
};

/**
 * Validates a URL.
 * @param url - The URL to validate.
 * @returns True if the URL is valid, otherwise false.
 */
const validateURL = (url: string): boolean => {
    const urlRegex = /^(https?:\/\/)?([a-zA-Z0-9.-]+)(:[0-9]{1,5})?(\/[^\s]*)?$/;
    if (!urlRegex.test(url) || (!url.startsWith('http://') && !url.startsWith('https://'))) {
        console.log("Invalid URL.");
        return false;
    }
    return true;
};

// Test cases
let num1 = "1562737848"; // Invalid (less than 11 digits)
let num2 = "34587452387"; // Valid (11 digits)
let email1 = 'kamsutraniko@proton.me'; // Valid
let email2 = 'kat@hotgirl.net'; // Valid
let url1 = 'http://palnetaneurodiverso.org'; // Valid
let url2 = 'https://moebius.org'; // Valid
let url3 = 'something.com'; // Invalid (missing protocol)
let url4 = 'gato'; // Invalid (not a URL)

log(validateTlf(num1)); // Invalid telephone number. Must be a numeric value and have 11 digits. 
//false
log(`Is a valid tlf: ${validateTlf(num2)}`); // Is a valid tlf: true
log(`Is a valid email: ${validateEmail(email1)}`); // Is a valid email: true
log(`Is a valid email: ${validateEmail(email2)}`); // Is a valid email: true
log(`Is a valid URL: ${validateURL(url1)}`); // Is a valid URL: true
log(`Is a valid URL: ${validateURL(url2)}`); // Is a valid URL: true
log(`Is a valid URL: ${validateURL(url3)}`); // Invalid URL. 
// Is a valid URL: false
log(`Is a valid URL: ${validateURL(url4)}`); // Invalid URL. 
// Is a valid URL: false