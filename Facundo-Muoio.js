// Operador de asinacion (=)
let nombre = "Facundo";
console.log("operador de asignacion", nombre);
console.log("operador de asignación de adición", "x += 1");
console.log("operador de asignación de resta", "x -= 1");
console.log("operador de asignación de multiplicacion", "x *= 2");
console.log("operador de asignación de division", "x /= 5");
console.log("operador de asignación de residuo", "x %= 2");
console.log("operador de asignación de exponenciación", "x **= 3");
console.log("operador de asignación de AND lógico", "x &&= y");
console.log("operador de asignación de division", "x ||= y");
console.log("operador de asignación de division", "x ??= y");

//operadores de comparación
console.log("operador de igualdad", 5 == 5);
console.log("operador de desigualdad", 4 != 5);
console.log("operador de igualdad estricta", 5 === "5");
console.log("operador de desigualdad estricta", 4 !== 3);
console.log("operador mayor que", 12 > 1);
console.log("operador menor que", 5 < 3);
console.log("operador mayor igual que", 15 >= 12);
conosole.log("operador menor igual que", 15 <= 12);

//operadores aritméticos (+ - / * %)
console.log("sum", 5 + 5);
console.log("rest", 5 - 5);
console.log("division", 10 / 2);
console.log("multiplication", 10 * 2);
console.log("power", 10 ** 2);
console.log("residue", 10 % 2);

//operadores lógicos
console.log("AND", true && true);
console.log("OR", true && false);
console.log("NOT", !true);

//operador ternario
console.log("operador ternario", true ? true : false);

//operadores uniarios
console.log("operador unario typeof", typeof "Hola Mundo!");

//estucturas de control
if (true) {
	console.log(
		"esta condicion es true y por eso se ejectuca lo que esta dentro de este bloque"
	);
} else {
}

switch (number) {
	case 1:
		console.log(
			"si la expresion evaluada es igual a uno se ejecuta este código"
		);
		break;
	case 20:
		console.log(
			"si la expresion evaluada es igual a veinte se ejecuta este código"
		);
		break;
	default:
		console.log(
			"se ejecuta cuando la expresión evaluado no coincide con ninguno de los casos"
		);
}

//bucles
while (number < 10) {
	console.log(
		"mientras la condicion evaluada sea verdadera ejecuta este código"
	);
}

do {
	let i = 0;
	i++;
	console.log(
		"realiza esta operacion hasta que la condicon while posterior se evalue como false"
	);
} while (number < 5);

for (var i = 0; i < 9; i++) {
	n += i;
	console.log(n);
}

for (const property in object) {
	console.log(`${property}: ${object[property]}`);
}

for (variable of iterable) {
	console.log(variable);
}

//extra point

for (let i = 10; i <= 55; i++) {
	if (i % 2 === 0 && i % 3 !== 0 && i !== 16) {
		console.log(i);
	}
}
