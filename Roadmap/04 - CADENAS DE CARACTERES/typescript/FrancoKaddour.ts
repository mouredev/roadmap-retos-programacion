// https://www.typescriptlang.org/

const str: string = "Hello, TypeScript!";

// Acceso a caracteres
console.log(str[0]);
console.log(str.charAt(7));

// Subcadena
console.log(str.slice(7, 17));
console.log(str.substring(7, 17));

// Longitud
console.log(str.length);

// Concatenación
console.log("Hello" + ", " + "World!");
console.log(`${"Hello"}, ${"World!"}`);

// Repetición
console.log("ab".repeat(3));

// Recorrido
for (const char of str) {
  process.stdout.write(char);
}
console.log();

// Mayúsculas / minúsculas
console.log(str.toUpperCase());
console.log(str.toLowerCase());

// Reemplazo
console.log(str.replace("TypeScript", "World"));
console.log(str.replaceAll("l", "L"));

// División
console.log(str.split(", "));

// Unión
console.log(["Hello", "World"].join(" - "));

// Interpolación
const name: string = "FranKaddour";
console.log(`Hola, ${name}!`);

// Verificación
console.log(str.includes("TypeScript"));
console.log(str.startsWith("Hello"));
console.log(str.endsWith("!"));
console.log(str.indexOf("Type"));
console.log(str.trim());

// Dificultad extra: palíndromo, anagrama, isograma
function isPalindrome(word: string): boolean {
  const clean = word.toLowerCase();
  return clean === clean.split("").reverse().join("");
}

function isAnagram(a: string, b: string): boolean {
  const sort = (s: string) => s.toLowerCase().split("").sort().join("");
  return sort(a) === sort(b) && a.toLowerCase() !== b.toLowerCase();
}

function isIsogram(word: string): boolean {
  const lower = word.toLowerCase();
  return new Set(lower).size === lower.length;
}

function classify(a: string, b: string): void {
  console.log(`"${a}" y "${b}":`);
  if (isPalindrome(a)) console.log(`  "${a}" es palíndromo`);
  if (isPalindrome(b)) console.log(`  "${b}" es palíndromo`);
  if (isAnagram(a, b)) console.log("  son anagramas");
  if (isIsogram(a)) console.log(`  "${a}" es isograma`);
  if (isIsogram(b)) console.log(`  "${b}" es isograma`);
}

classify("amor", "roma");
classify("racecar", "carrace");
classify("subdermatoglyphics", "derma");
