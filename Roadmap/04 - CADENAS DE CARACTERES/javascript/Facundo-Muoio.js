//operacines con cadenas de caracteres
//concatenar cadenas
console.log("hola" + " mundo!");
console.log("Hola ".concat("mundo!"));

// ver el lenght de las cadeans de caracteristicas
let str = "soy un string";
console.log(str.length);

// acceder a un caracter específico del  string
console.log(str[0]);

// acceder a una porción del string
console.log(str.slice(0, 6));
console.log(str.substring(0, 6));

// formatear todo el string a uppercase.
console.log(str.toUpperCase());

// formatear todo el string a lowercase
let upper = "UPPERCASE";
console.log(upper.toLowerCase());

// separa los caracteres segun un separador que pasamos como argumento y te devulte un arreglo con los caracteres de los subtrings producidos.
console.log(str.split(""));

// reemplaza el string o expresion regular que pasamos por el string que pasamos por segundo argumento
console.log(str.replace("s", "f"));

// elimina todos los caracteres de espacios en blanco iniciales y finales dentro de un string
str = " Mauricio    Perez  ";
console.log(str.trim());

// devuelve true si el string que pasamos esta includi en la cadean de texto en la cual aplicamos el método
console.log(str.includes("Mauricio"));

// devuelve el caracter en la posicion que indicamos como argumento del método
console.log(str.charAt(0));

// devulve el indice del primer caracter que coicide con el caracter que pasamos en el método.
console.log(str.indexOf("i"));

// devuelve todas las coicidencias de una expresión regular dentro de un arreglo.
console.log(str.match(/[A-Z]/));

// devuelve un booleano chequeando si la cadena de texto comienza con los caracteres que pasamos como argumento
console.log(str.startsWith(" Maur"));

// devuelve un nuevo string con el mismo repetido el número de veces que pasamos por agumento
console.log("hola".repeat(2));

// Actividad Extra :
function chekcString(str1, str2) {
	str1 = str1.toLowerCase();
	str2 = str2.toLowerCase();

	let palindromo = [];
	let anagrama;
	let isogram = [];

	// vemos si la palabra es un palíndromo
	str1.split("").reverse().join("") === str1
		? (palindromo[0] = true)
		: (palindromo[0] = false);
	str2.split("").reverse().join("") === str2
		? (palindromo[1] = true)
		: (palindromo[1] = false);

	// vemos si la palabra es un anagrama
	str1.split("").sort().join() === str2.split("").sort().join()
		? (anagrama = true)
		: (anagrama = false);

	//vemos si una palabra es un isograma

	function verifyIsogram(str) {
		let obj = {};
		let isogram = true;

		for (let letter of str.toLowerCase()) {
			obj[letter] ? obj[letter]++ : (obj[letter] = 1);
		}

		const arr = Object.values(obj);
		arr.forEach(e => {
			e != arr[0] ? (isogram = false) : "";
		});

		return isogram;
	}

	isogram[0] = verifyIsogram(str1);
	isogram[1] = verifyIsogram(str2);

	return { palindromo, anagrama, isogram };
}
