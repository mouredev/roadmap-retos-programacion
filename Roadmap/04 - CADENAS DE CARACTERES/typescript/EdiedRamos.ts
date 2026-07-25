// Autor: EdiedRamos

// Ejercicio base
function stringFunctions() {
  const username: string = "Edied Ramos";
  const dirtyUsername: string = "    Edied Ramos     ";

  console.log("Longitud de la cadena:", username.length);
  console.log("Carácter en la primer posición:", username.charAt(0));
  console.log(
    "Carácter en la primer posición pero en código UTF-16:",
    username.charCodeAt(0)
  );

  console.log("Carácter en la última posición:", username.at(-1));
  console.log("Últimos 5 carácteres:", username.slice(-5));
  console.log("Primeros 5 carácteres:", username.substring(0, 5));
  // El método "substr" está deprecado, pero es útil para compatibilidad
  console.log(
    "4 carácteres a partír de la segunda posición:",
    username.substr(1, 4)
  );

  console.log("Nombre de usuario en mayúscula:", username.toUpperCase());
  console.log("Nombre de usuario en minuscula:", username.toLowerCase());

  console.log(
    "Saludo concatenado con el nombre de usuario:",
    "Hola ".concat(username)
  );

  console.log(
    "Nombre de usuario sin espacios al inicio ni al final:",
    dirtyUsername.trim()
  );
  console.log(
    "Nombre de usuario sin espacios al inicio:",
    dirtyUsername.trimStart()
  );
  console.log(
    "Nombre de usuario sin espacios al final:",
    dirtyUsername.trimEnd()
  );

  console.log(" con 15 carácteres:", username.padStart(15, "_"));
  console.log("Nombre de usuario con 15 carácteres:", username.padEnd(15, "_"));

  console.log("2 veces el nombre de usuario:", username.repeat(2));

  console.log("Reemplaza la primer d por D:", username.replace("d", "D"));
  console.log("Reemplaza todas las d por D:", username.replaceAll("d", "D"));

  console.log("Palabras en el nombre de usuario: ", username.split(" "));
}

// Ejercicio extra
function createMessage(
  value: string,
  status: boolean,
  context: string,
  isPlural?: boolean
) {
  return `${value}: ${
    status ? (isPlural ? "Son" : "Es") : isPlural ? "No son " : "No es"
  } ${context}`;
}

function palindromeCase() {
  const isPalindrome = (str: string): boolean => {
    for (let i = 0; i < str.length / 2; i++) {
      if (str[i] !== str[str.length - i - 1]) return false;
    }
    return true;
  };
  const firstWord = "abcba",
    secondWord = "ediedramos";

  console.log(createMessage(firstWord, isPalindrome(firstWord), "palindromo"));
  console.log(
    createMessage(secondWord, isPalindrome(secondWord), "palindromo")
  );
}

function anagramCase() {
  const areAnagram = (wordA: string, wordB: string): boolean => {
    const wordASorted = [...wordA].sort().join("");
    const wordBSorted = [...wordB].sort().join("");
    return wordASorted === wordBSorted;
  };
  const firstWord = "ramosedied",
    secondWord = "ediedramos";

  console.log(
    createMessage(
      `${firstWord} y ${secondWord}`,
      areAnagram(firstWord, secondWord),
      "anagramas",
      true
    )
  );
}

function isogramCase() {
  const isIsogram = (str: string): boolean => {
    const frecuency: Record<number, number> = {};
    for (const char of str) {
      const isALetter = /[a-z]/i.test(char);
      if (isALetter) {
        if (!frecuency[char]) frecuency[char] = 0;
        frecuency[char]++;
      }
    }
    const unique = new Set();
    for (const key of Object.keys(frecuency)) unique.add(frecuency[key]);
    return unique.size === 1;
  };
  const firstWord = "edied",
    secondWord = "ramos";

  console.log(createMessage(firstWord, isIsogram(firstWord), "isograma"));
  console.log(createMessage(secondWord, isIsogram(secondWord), "isograma"));
}

function extraExercise() {
  palindromeCase();
  anagramCase();
  isogramCase();
}

(() => {
  stringFunctions();
  extraExercise();
})();
