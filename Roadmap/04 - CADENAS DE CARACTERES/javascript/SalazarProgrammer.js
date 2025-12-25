/*
 * 04 CADENAS DE CARACTERES
 * Dificultad: Media | Publicación: 22/01/24 | Corrección: 29/01/24
 */

/*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones con cadenas de caracteres
 */

console.log('=== OPERACIONES CON CADENAS EN JAVASCRIPT ===');

// 1. CREACIÓN DE CADENAS
console.log('\n1. CREACIÓN DE CADENAS:');
let cadena1 = 'Hola Mundo';
let cadena2 = 'JavaScript es genial';
let cadena3 = `Plantillas literales`;
let cadena4 = String(123); // Conversión a string
console.log('cadena1:', cadena1);
console.log('cadena2:', cadena2);
console.log('cadena3:', cadena3);
console.log('cadena4:', cadena4);

// 2. LONGITUD DE CADENA
console.log('\n2. LONGITUD:');
console.log("Longitud de '" + cadena1 + "':", cadena1.length);

// 3. ACCESO A CARACTERES
console.log('\n3. ACCESO A CARACTERES:');
console.log('Primer carácter:', cadena1[0]);
console.log('Último carácter:', cadena1[cadena1.length - 1]);
console.log('charAt(5):', cadena1.charAt(5));
console.log('charCodeAt(0):', cadena1.charCodeAt(0)); // Código Unicode

// 4. SUBCADENAS
console.log('\n4. SUBCADENAS:');
console.log('slice(0, 4):', cadena1.slice(0, 4)); // "Hola"
console.log('substring(5, 10):', cadena1.substring(5, 10)); // "Mundo"
console.log('substr(2, 3):', cadena1.substr(2, 3)); // "la " (deprecado)

// 5. CONCATENACIÓN
console.log('\n5. CONCATENACIÓN:');
let concatenacion = cadena1 + ' ' + cadena2;
console.log('Concatenación con +:', concatenacion);
console.log('concat():', cadena1.concat(' - ', cadena2));

// 6. REPETICIÓN
console.log('\n6. REPETICIÓN:');
console.log('repeat(3):', 'Hola '.repeat(3));

// 7. RECORRIDO
console.log('\n7. RECORRIDO:');
console.log('For...of:');
for (let char of cadena1) {
	console.log('  ' + char);
}

console.log('split() y forEach():');
cadena1.split('').forEach((char, index) => {
	console.log(`  ${index}: ${char}`);
});

// 8. CONVERSIÓN MAYÚSCULAS/MINÚSCULAS
console.log('\n8. CONVERSIÓN DE CASES:');
console.log('toUpperCase():', cadena1.toUpperCase());
console.log('toLowerCase():', cadena1.toLowerCase());

// 9. BÚSQUEDA
console.log('\n9. BÚSQUEDA:');
console.log("indexOf('Mundo'):", cadena1.indexOf('Mundo'));
console.log("lastIndexOf('o'):", cadena1.lastIndexOf('o'));
console.log("includes('Hola'):", cadena1.includes('Hola'));
console.log("startsWith('Hola'):", cadena1.startsWith('Hola'));
console.log("endsWith('Mundo'):", cadena1.endsWith('Mundo'));
console.log('match(/[aeiou]/g):', cadena1.match(/[aeiou]/g));

// 10. REEMPLAZO
console.log('\n10. REEMPLAZO:');
console.log(
	"replace('Mundo', 'JavaScript'):",
	cadena1.replace('Mundo', 'JavaScript')
);
console.log("replaceAll('o', '0'):", cadena1.replaceAll('o', '0'));
console.log('replace con regex:', cadena1.replace(/[aeiou]/g, '-'));

// 11. DIVISIÓN Y UNIÓN
console.log('\n11. DIVISIÓN Y UNIÓN:');
let palabras = cadena1.split(' ');
console.log("split(' '):", palabras);
console.log("join('-'):", palabras.join('-'));

// 12. ELIMINACIÓN DE ESPACIOS
console.log('\n12. ELIMINACIÓN DE ESPACIOS:');
let conEspacios = '   Hola Mundo   ';
console.log('trim():', `"${conEspacios.trim()}"`);
console.log('trimStart():', `"${conEspacios.trimStart()}"`);
console.log('trimEnd():', `"${conEspacios.trimEnd()}"`);

// 13. VERIFICACIÓN
console.log('\n13. VERIFICACIÓN:');
console.log("includes('Hola'):", cadena1.includes('Hola'));
console.log("startsWith('H'):", cadena1.startsWith('H'));
console.log("endsWith('o'):", cadena1.endsWith('o'));

// 14. INTERPOLACIÓN (TEMPLATE LITERALS)
console.log('\n14. INTERPOLACIÓN:');
let nombre = 'Juan';
let edad = 30;
console.log(`Mi nombre es ${nombre} y tengo ${edad} años.`);

// 15. COMPARACIÓN
console.log('\n15. COMPARACIÓN:');
console.log("'a' < 'b':", 'a' < 'b');
console.log("'a' === 'A':", 'a' === 'A');
console.log('localeCompare:', 'ñ'.localeCompare('n'));

// 16. MÉTODOS ADICIONALES
console.log('\n16. MÉTODOS ADICIONALES:');
console.log("padStart(15, '-'):", cadena1.padStart(15, '-'));
console.log("padEnd(15, '-'):", cadena1.padEnd(15, '-'));
console.log('codePointAt(0):', cadena1.codePointAt(0));

/*
 * DIFICULTAD EXTRA (opcional):
 * Analizar dos palabras para ver si son palíndromos, anagramas o isogramas
 */

console.log('\n=== DIFICULTAD EXTRA ===');

function analizarPalabras(palabra1, palabra2) {
	console.log(`Analizando: "${palabra1}" y "${palabra2}"`);

	// 1. PALÍNDROMOS (se leen igual al derecho y al revés)
	function esPalindromo(palabra) {
		const limpia = palabra.toLowerCase().replace(/[^a-záéíóúüñ]/g, '');
		return limpia === limpia.split('').reverse().join('');
	}

	console.log(`¿"${palabra1}" es palíndromo?`, esPalindromo(palabra1));
	console.log(`¿"${palabra2}" es palíndromo?`, esPalindromo(palabra2));

	// 2. ANAGRAMAS (mismas letras en diferente orden)
	function sonAnagramas(p1, p2) {
		const limpiar = (str) => str.toLowerCase().replace(/[^a-záéíóúüñ]/g, '');
		const p1Limpia = limpiar(p1);
		const p2Limpia = limpiar(p2);

		if (p1Limpia.length !== p2Limpia.length) return false;

		return (
			p1Limpia.split('').sort().join('') === p2Limpia.split('').sort().join('')
		);
	}

	console.log(`¿Son anagramas?`, sonAnagramas(palabra1, palabra2));

	// 3. ISOGRAMAS (ninguna letra se repite)
	function esIsograma(palabra) {
		const limpia = palabra.toLowerCase().replace(/[^a-záéíóúüñ]/g, '');
		const letrasUnicas = new Set(limpia.split(''));
		return limpia.length === letrasUnicas.size;
	}

	console.log(`¿"${palabra1}" es isograma?`, esIsograma(palabra1));
	console.log(`¿"${palabra2}" es isograma?`, esIsograma(palabra2));
}

// Ejemplos de prueba
analizarPalabras('reconocer', 'cerco negro');
console.log('\n' + '='.repeat(40));
analizarPalabras('amor', 'roma');
console.log('\n' + '='.repeat(40));
analizarPalabras('murciélago', 'programación');
