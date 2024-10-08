/* ------------------------ CONCATENACIÓN DE CADENAS ------------------------ */

// Usando el operador +
let a: string = "Hello";
let b: string = "World";
let c: string = a + b; // HelloWorld

// Usando el operador +=
let d: string = "Hello";
d += "World"; // HelloWorld

// Usando template literals
let e: string = `Hello ${"World"}`; // Hello World


/* --------------------------- LONGITUD DE CADENA --------------------------- */

// Usando el .length
let f: string = "Hello";
let g: number = f.length; // 5


/* -------------------------- ACCEDER A CARACTERES -------------------------- */

// Usando el []
let h: string = "Hello";
let i: string = h[0]; // H
let j: string = h[4]; // o

// Usando el .charAt()
let k: string = "Hello";
let l: string = k.charAt(0); // H
let m: string = k.charAt(4); // o

// Usando el .charCodeAt()
let n: string = "Hello";
let o: number = n.charCodeAt(0); // 72
let p: number = n.charCodeAt(4); // 111


/* -------------------------- MANIPULACIÓN DE CADENAS ----------------------- */

// Usando el .toUpperCase()
let q: string = "Hello";
let r: string = q.toUpperCase(); // HELLO

// Usando el .toLowerCase()
let s: string = "Hello";
let t: string = s.toLowerCase(); // hello

// Usando el .toLocaleLowerCase()
let v: string = "Hello";
let w: string = v.toLocaleLowerCase(); // hello

// Usando el .toLocaleUpperCase()
let x: string = "Hello";
let y: string = x.toLocaleUpperCase(); // HELLO

// Usando el .replace()
let z: string = "Hello";
let a2: string = z.replace("H", "h"); // hell
let b2: string = z.replace("o", "0"); // HeLl

// Usando el .split()
let c2: string = "Hello, World"; // Hello, World
let d2: string[] = c2.split(", "); // ["Hello", "World"]

// Usando el .substring()
let e2: string = "Hello";
let f2: string = e2.substring(0, 5); // Hello
let g2: string = e2.substring(6); // World

// Usando el .slice()
let h2: string = "Hello";
let i2: string = h2.slice(0, 5); // Hello
let j2: string = h2.slice(6); // World

// Usando el .indexOf()
let k2: string = "Hello";
let gl: number = k2.indexOf("l"); // 2
let m2: number = k2.indexOf("o"); // 4

// Usando el .lastIndexOf()
let n2: string = "Hello";
let o2: number = n2.lastIndexOf("l"); // 5
let p2: number = n2.lastIndexOf("o"); // 4

// Usando el .includes()
let q2: string = "Hello";
let s2: boolean = q2.includes("l"); // true
let t2: boolean = q2.includes("o"); // true

// Usando el .trim()
let u2: string = "   Hello   ";
let w2: string = u2.trim(); // Hello

// Usando el .trimStart()
let x2: string = "   Hello   ";
let y2: string = x2.trimStart(); // Hello   

// Usando el .trimEnd()
let z2: string = "   Hello   ";
let a3: string = z2.trimEnd(); //    Hello

// Usando el .replaceAll()
let b3: string = "Hello";
let c3: string = b3.replaceAll("l", "x"); // Hexxo


/* ----------------------- OTROS MÉTODOS MENOS COMUNES ---------------------- */

// Usando el .padStart()
let d3: string = "Hello";
let e3: string = d3.padStart(10, "0"); // 00000Hello

// Usando el .padEnd()
let f3: string = "Hello";
let g3: string = f3.padEnd(10, "0"); // Hello00000

// Usando el .repeat()
let h3: string = "Hello";
let i3: string = h3.repeat(3); // HelloHelloHello

// Usando el .localeCompare()
let j3: string = "apple";
let k3: number = j3.localeCompare("banana"); // -1 (apple es menor que banana)


// -------------------------- BONUS EJERCICIO ------------------------------- //

// Palíndromos con strings
function isPalindrome(str: string): boolean {
    let reversed: string = str.split("").reverse().join("");
    return str === reversed;
}

isPalindrome("Isaac no ronca así"); // true
isPalindrome("tanto monta monta tanto"); // false


function isAnagram(str1: string, str2: string): boolean {
    let reversed1: string = str1.split("").reverse().join("");
    let reversed2: string = str2.split("").reverse().join("");
    return reversed1 === reversed2;
}

isAnagram("Isaac no ronca así", "Isaac no ronca así"); // true
isAnagram("Isaac no ronca así", "Isaac no ronca así tanto"); // false

function isIsogram(str: string): boolean {
    let letters: string[] = str.toLocaleLowerCase().split("");

    return letters.length === new Set(letters).size;
}

isIsogram("coco"); // true 2 c, 2 o
isIsogram("otra prueba"); // false 1 o, 1 t, 2 r, 2 a,, 1 p, 1 u, 1 e, 1 b