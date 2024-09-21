/* #3 ESTRUCTURAS DE DATOS  */
//I use Professional JavaScript for web developers by Matt Frisbie (z-lib.org) for give acurate information in some coments.
//Also use GPT

/* In JavaScript, there are several built-in data structures that you can use to store and manipulate data. Here’s a list of the most common ones: */

let log = console.log.bind(console);

/* Primitive Data Types */
   //Number: Represents both integer and floating-point numbers. 
/* Perhaps the most interesting data type in ECMAScript is Number, which uses the IEEE–754 format
to represent both integers and floating-point values (also called double–precision values in some languages). To support the various types of numbers, there are several different number literal formats. */
   let age = 35; // Integer
   let total = 118.87; // Floating-point      
   log('age: ', age + ', total: ', total)// age: 35, total: 118.87
   log(.3)// 0.3
//To define a floating-point value, you must include a decimal point and at least one number after the decimal point. Although an integer is not necessary before a decimal point, it is recommended.

   let octNum = 045;
   log(octNum)// 37

   let hexNum = 0x2f;
   log(hexNum)// 47
//Note: Numbers created using octal or hexadecimal format are treated as decimal numbers in all arithmetic operations.
   
/* There is a special numeric value called NaN, short for Not a Number, which is used to indicate when an operation intended to return a number has failed (as opposed to throwing an error). For exam-
ple, dividing any number by 0 typically causes an error in other programming languages, halting
code execution. In ECMAScript, dividing a number by 0 returns NaN, which allows other processing
to continue. */

/*  The value NaN has a couple of unique properties. First, any operation involving NaN always returns NaN (for instance, NaN /10), which can be problematic in the case of multistep computations. Second, NaN is not equal to any value, including NaN. For example, the following returns false: */
  
   log('Hi man how you doing?' * 4)// NaN
   log(NaN == NaN); // false

//For this reason, ECMAScript provides the isNaN() function. 

   log(isNaN("04"))// false cause can be converted to NaN

//Note: there is a particular difference between the Number() and parseInt() function when they are used to convert types(you can search for more information)   

   //String: Represents a sequence of characters. The String data type represents a sequence of zero or more 16-bit Unicode characters. Strings can be delineated by either double quotes ("), single quotes ('), or backticks (`)

   let dreamyGirl = "Lucy";
   let song = dreamyGirl + ' in the sky with dimonds';
   let song_info = `"${song}" is a song from The Beatles that allude to the LSD`
   log(song_info)// "Lucy in the sky with dimonds" is a song from The Beatles that allude to the LSD

   /* Character Literals
The String data type includes several character literals to represent nonprintable or otherwise useful characters: */
/* LITERAL MEANING
\n New line
\t Tab
\b Backspace
\r Carriage return
\f Form feed
\\ Backslash (\)
\' Single quote (')—used when the string is delineated by single quotes. Example: 'He
said, \'hey.\''.
\" Double quote (")—used when the string is delineated by double quotes. Example:
"He said, \"hey.\"".
\` Backtick (`)—used when the string is delineated by backticks. Example: `He said,
\`hey.\``.
\xnn A character represented by hexadecimal code nn (where n is a hexadecimal digit
0-F). Example: \x41 is equivalent to "A".
\unnnn A Unicode character represented by the hexadecimal code nnnn (where n is a
hexadecimal digit 0-F). Example: \u03a3 is equivalent to the Greek character Σ. */

//Template literals also support the ability to define tag functions
  let num1 = 40;
  let num2 = 80;

  let sum = `${num1} + ${num2} = ${num1 + num2}`;
  log(sum)// "40 + 80 = 120"

/* Raw Strings
It is also possible to use template literals to give you access to the raw template literal contents without being converted into actual character representations, such as a new line or Unicode character. This can be done by using the String.raw tag function, which is available by default. */
// Unicode demo
// \u57A8 is the 垨  character. 

/* Info: The character 𗞨 (yǐ) is often associated with the meaning of "to be" or "to exist." However, it is important to note that this character is quite rare and may not be found in everyday usage or standard dictionaries. It may appear in historical texts or specific contexts.(gpt brings me this last info, I type an aleatory unicode secuence) */

 log(`\u57A8`); // 垨   or  ?  if you run in Console with Node
 log(String.raw`\u57A8`); // \u57A8
// Newline demo
 log(`first line\nsecond line`);
// first line
// second line
 log(String.raw`first line\nsecond line`); // "first line\nsecond line" 


   /* Boolean: Represents a logical entity and can have two values: `true` and `false`. The Boolean type is one of the most frequently used types in ECMAScript and has only two literalvalues: true and false. These values are distinct from numeric values, so true is not equal to 1, and false is not equal to 0. */
   let isChecked = true;
   log(!isChecked)// false
 //Note that the Boolean literals true and false are case–sensitive, so True and False (and other mixings of uppercase and lowercase) are valid as identifiers but not as Boolean values.
   
   //Undefined: A variable that has been declared but has not yet been assigned a value.
    let somebody;
    log(somebody)// undefined
    let explicitlyUndefined = void(0);
    log(explicitlyUndefined)// undefined
  //Note: the use of void(0) is deprecated cause allow some javascript injection that can cause vulnerabilities in the structure of the code.  

   //Null: Represents the intentional absence of any object value. Is common to initialize objects with null value.  That way, you can explicitly check for the value null to determine if the variable has been filled with an object reference at a later time.
    let animals = null;
    log(animals)// null

   //Symbol: A unique and immutable primitive value, often used as object property keys. The purpose is guaranteed unique identifier that does not risk property collision.
   const Id = Symbol('xm');
   const otherid = Symbol('xm');
   log('equal symbols: ', Id == otherid)// false

  /* You can also use symbols as object's properties .We'll use a common property name like email, but we'll use a symbol to ensure that this property is unique and not easily accessible or overridden. */


// Create a unique symbol for the email property
const emailSymbol = Symbol('email');

class User {
    constructor(name, email) {
        this.name = name;
        this[emailSymbol] = email; // Use the symbol as the key for the email property
    }

    // Method to get the email
    getEmail() {
        return this[emailSymbol];
    }
}

// Create a new user
const user1 = new User('Barbarella', 'softbaby@something.com');

console.log(user1.name); // Barbarella
console.log(user1.getEmail()); // softbaby@something.com

// Trying to access the email property directly
console.log(user1[emailSymbol]); // softbaby@something.com
console.log(user1.email); // undefined, as 'email' is not a property of the object


   //BigInt: Represents integers with arbitrary precision.
   let bigNumber = BigInt(765466743212345679874653358945321);
   log(bigNumber)// 765466743212345679874653358945321

  /*  Note: Many modern cryptographic libraries and implementations do use BigInt or similar constructs to handle large integers, especially for operations that involve large prime numbers, modular arithmetic, and other mathematical computations common in cryptography.  */


/*  Reference Data Types */

  // Object: A collection of key-value pairs. Objects can store multiple values as properties and methods who can interact with that properties.

  let debian = {
      name: 'Debian',
      description: 'Ardilla parlante cuyo nucleo esta basado en un Sistema Operativo del mismo nombre, lucha contra el Sistema establecido y habita más alla del Borde(el Universo conocido)',
      location: 'No Found',

      speak: ()=> {
        console.log(this.description)
      }
  }
   
    log(debian.description)// Ardilla parlante cuyo nucleo esta basado en un Sistema Operativo del mismo nombre, lucha contra el Sistema establecido y habita más alla del Borde(el Universo conocido)

  // Array: A special type of object used to store ordered collections of values. Arrays can hold elements of any type and are indexed numerically.

  let friends = ['Susan', 'Maryatta','Denise','Luna', 'Kena', 'Maria']
  log(friends) 
  // Function: A special type of object that can be called to perform a specific task. Functions can also be stored in variables, passed as arguments, and returned from other functions.

  let from = 4, to = 12; 
  const randomValue = (from, to)=> {
    return Math.floor(Math.random() * (to - from + 1)) + from;
  }

  let count = from;
  while(count < to){
      log('random value: ', randomValue(from, to));
      count++;
  }
//Logs: numbers between 4 and 12 inclusive
/* Specialized Data Structures */
   //Set: A collection of unique values. Sets can store any type of value, and duplicate values are automatically removed.

   let uniqueNumbers = new Set([4, 4, 3, 5, 8, 1, 8, 1, 7]);
   log(uniqueNumbers); //  Set {4, 3, 5, 8, 1, 7 }

   //Map: A collection of key-value pairs where keys can be of any type. Maps maintain the insertion order of their elements.
   
   let map = new Map();
   map.set('gopi_name', 'Khamala');
   map.set('age', 35);
   log(map.get('gopi_name')); //  Khamala

   //WeakSet: Similar to a Set, but it holds "weak" references to its values, allowing for garbage collection if there are no other references to the object.
   
   let weakSet = new WeakSet();
   let obj = {};
   weakSet.add(obj);
   log(weakSet.has(obj)); //  true

   //WeakMap: Similar to a Map, but it holds "weak" references to its keys, allowing for garbage collection if there are no other references to the key object.

   let weakMap = new WeakMap();
   let keyObj = {};
   weakMap.set(keyObj, "crasylady");
   log(weakMap.get(keyObj)); //  crazylady

   //Note: garbage collection allow memory management by automatically allocating what is needed and reclaiming memory that is no longer being used. 

     /* Typed Arrays */ 
  /* Typed arrays in JavaScript provide a way to work with binary data directly in memory. They are particularly useful for handling raw binary data, such as in scenarios involving graphics, audio, and network communications. 
  They provide a way to work with binary data in a more efficient manner. Examples include `Int8Array`, `Uint8Array`, `Float32Array`, etc. */

   //int8Array: Represents an array of 8-bit integers.
   let int8Array = new Int8Array([-3, 5, -8, 99, 76]);
   log(int8Array)// [-3, 5, -8, 99, 76]

   //Uint8Array: Represents an array of 8-bit unsigned integers.
   let uint8Array = new Uint8Array([1, 2, 3]);
   
   //Uint8ClampedArray: Represents an array of 8-bit unsigned integers clamped to the range [0, 255].
   let uint8ClampedArray = new Uint8ClampedArray([-1, 256, 100]);

   
   //Int16Array: Represents an array of 16-bit signed integers.
   let int16Array = new Int16Array([1, -2, 3]);
   
  // Uint16Array: Represents an array of 16-bit unsigned integers.
   let uint16Array = new Uint16Array([1, 2, 3]);
   
  // Int32Array: Represents an array of 32-bit signed integers.
   let int32Array = new Int32Array([1, -2, 3]);
   
   //Uint32Array: Represents an array of 32-bit unsigned integers.
   let uint32Array = new Uint32Array([1, 2, 3]);
   
  // Float32Array: Represents an array of 32-bit floating-point numbers.
   let float32Array = new Float32Array([1.5, 2.5, 3.5]);
   
  // Float64Array: Represents an array of 64-bit floating-point numbers.
   let float64Array = new Float64Array([1.5, 2.5, 3.5]);
   
  // BigInt64Array: Represents an array of 64-bit signed integers (BigInt).
   let bigInt64Array = new BigInt64Array([1n, 2n, 3n]);
   
  // BigUint64Array: Represents an array of 64-bit unsigned integers (BigInt).
   let bigUint64Array = new BigUint64Array([1n, 2n, 3n]);
   log(bigUint64Array)/* Logs:
  BigUint64Array(3) [ {}, {}, {} ]
   0: 1n
   1: 2n
   2: 3n
   buffer: ArrayBuffer { byteLength: 24 }
   byteLength: 24
   byteOffset: 0
   length: 3
   <prototype>: BigUint64Array.prototype { … } */

   window.addEventListener('load', function(){
    const body = document.querySelector('body');
    const title = document.createElement('h1');
    
    body.style.setProperty('background', '#000');
    body.style.setProperty('text-align', 'center');
    
    title.textContent = 'Retosparaprogramadores #3.';
    title.style.setProperty('font-size', '3.5vmax')
    title.style.setProperty('color', '#fff');
    title.style.setProperty('line-height', '100vh');
    
    body.appendChild(title);
    
    alert('Retosparaprogramadores #3. Please open the Browser Developer Tools.');
    log( 'Retosparaprogramadores #3')// this will be logged at the end cause the nature of window event
});





/*   EXTRA DIFFICULTY (optional):
   Create a contact book via the terminal.
       You must implement functionalities for searching, inserting, updating, and deleting contacts.
       Each contact must have a name and a phone number.
       The program first asks which operation you want to perform, and then the necessary data to carry it out.
       The program cannot allow the input of non-numeric phone numbers and those with more than 11 digits (or the number of digits you choose).
       An option to terminate the program should also be provided.
*/

//Node.js was used to achieve interaction with the console.
//Then you should copy the exercise, save it with a .js extension, and run it in a terminal using the command node plus the name of the file.
/*
   const rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let contacts = [];

function showMenu(){
    console.log("--- List of Contacts ---");
    console.log("1. Insert Contact");
    console.log("2. Buscar Contact");
    console.log("3. Update Contact");
    console.log("4. Delate Contact");
    console.log("5. Exit");
    rl.question("Chose and Option: ", (option) => {
        switch (option) {
            case '1':
                insertContact();
                break;
            case '2':
                searchContact();
                break;
            case '3':
                updateContact();
                break;
            case '4':
                delateContact();
                break;
            case '5':
                console.log("living the program...");
                rl.close();
                break;
            default:
                console.log("No Valid Option. Try again.");
                showMenu();
        }
    });
}


function askQuestion(query){
    return new Promise(resolve => {
        rl.question(query, resolve);
    });
}

async function insertContact(){
  try {
        const name = await askQuestion("Type the contact name: ");
        
        const telefone = await askQuestion("Type the telephone number (11 digits): ");
        if (!/^\d{11}$/.test(telefone)) {
            console.log("Invalid telephone number. Must be a numeric value and have 11 digits.");
            return showMenu(); 
        }
    
        const email = await askQuestion("Type the email of the contact: ");
        const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        if (!emailRegex.test(email)) {
            console.log("Invalid email. Must be a valid email address.");
            return showMenu(); 
        }
    
        contacts.push({ name, telefone, email });
        console.log(`Contact ${name} added.`);
    
  } catch (error) {
      console.error("An error occurred:", error.message);
  } finally {
      showMenu(); 
  }
}

function searchContact(){
    rl.question("Ingrese el name del contact a search: ", (name) => {
        const contact = contacts.find(c => c.name.toLowerCase() === name.toLowerCase());
        if (contact) {
            console.log(`Contact found: ${contact.name}, Telefone: ${contact.telefone}, Email: ${contact.email}`);
        } else {
            console.log("Contact not found.");
        }
        showMenu();
    });
}

async function updateContact(){
  try {
        const name = await askQuestion("Type the name of the contact to update: ");
        const contact = contacts.find(c => c.name.toLowerCase() === name.toLowerCase());
    
        if (contact) {
            const telefone = await askQuestion("Type the new number of telephone (11 digits): ");
            if (/^\d{11}$/.test(telefone)) {
                contact.telefone = telefone;
                console.log(`Contact ${name} updated with new number.`);
            } else {
                console.log("Invalid telephone number. Must be a numeric value and have 11 digits.");
            }
    
            const email = await askQuestion("Type the email of the contact: ");
            const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (emailRegex.test(email)) {
                contact.email = email; 
                console.log(`Contact ${name} updated with new email.`);
            } else {
                console.log("Invalid email. Must be a valid email address.");
            }
        } else {
            console.log("Contact not found.");
        }
  } catch (error) {
      console.error("An error occurred:", error.message);
  } finally {
      showMenu(); 
  }
}


function delateContact(){
    rl.question("Type the name of the contact to delate: ", (name) => {
        const index = contacts.findIndex(c => c.name.toLowerCase() === name.toLowerCase());
        if (index !== -1) {
            contacts.splice(index, 1);
            console.log(`Contact ${nombre} delated.`);
        } else {
            console.log("Contact not found.");
        }
        showMenu();
    });
}

showMenu();

*/
 /*  /^(?=.{1,254}$)(?=.{1,64}@)([a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+)(?<!\.)(?<!\.\.)@[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$/i  */

//Regular Expression Breakdown

  //  (?=.{1,254}$): Ensures that the total length of the email does not exceed 254 characters.

  //  (?=.{1,64}@): Ensures that the local part (before the @) does not exceed 64 characters.

  //  (?<!\.) and (?<!\.\.): Ensures that the local part does not end with a period and does not contain consecutive periods.

  //  [a-zA-Z0-9]: Allows uppercase letters in the local part and in the domain.

  //  (?:\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+: Ensures that the domain has at least one period and that each part of the domain follows the length rules.


  