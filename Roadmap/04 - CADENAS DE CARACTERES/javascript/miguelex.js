var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
// Operaciones básicas sobre cadenas de texto
var texto = "Hola, mundo!";
// Interpolación de cadenas (uso de plantillas de cadena)
var nombre = "Migue";
var lenguaje = "PHP";
var mensaje = "Hola, me llamo ".concat(nombre, " y trabajo con ").concat(lenguaje, " a\u00F1os.");
console.log(mensaje);
// Longitud de la cadena
var longitud = texto.length;
console.log("La longitud de la cadena ".concat(texto, " es ").concat(longitud, " caracteres"));
// Obtener el carácter en una posición específica
var primerCaracter = texto[0];
console.log("El primer car\u00E1cter de ".concat(texto, " es ").concat(primerCaracter));
// Concatenar dos cadenas
var nuevaCadena = texto + " TypeScript";
console.log("La nueva cadena de unir ".concat(texto, " con TypeScript es ").concat(nuevaCadena));
// Convertir la cadena a minúsculas
var minusculas = texto.toLowerCase();
console.log("".concat(texto, " en min\u00FAsculas es ").concat(minusculas));
// Convertir la cadena a mayúsculas
var mayusculas = texto.toUpperCase();
console.log("".concat(texto, " en may\u00FAsculas es ").concat(mayusculas));
// Obtener una subcadena
var subcadena = texto.substring(0, 4);
console.log("La subcadena de ".concat(texto, " entre las posiciones 0 y 4 es ").concat(subcadena));
// Reemplazar parte de la cadena
var reemplazada = texto.replace("Hola", "Saludos");
console.log("Vamos a reemplazar Hola por Saludos: ".concat(reemplazada));
// Operaciones adicionales sobre cadenas de texto
var textoConEspacios = "   Hola,      mundo!   ";
// Eliminar espacios en blanco al principio y al final
var sinEspaciosExtremos = textoConEspacios.trim();
console.log("Cadena sin espacios al principio y al final: ".concat(sinEspaciosExtremos));
// Eliminar todos los espacios en blanco
var sinEspacios = textoConEspacios.replace(/\s/g, "");
console.log("Cadena sin espacios: ".concat(sinEspacios));
// Unión de dos cadenas
var cadena1 = "Moure";
var cadena2 = "Dev";
var unionCadenas = cadena1.concat(" ", cadena2);
console.log("La uni\u00F3n de las cadenas ".concat(cadena1, " y ").concat(cadena2, " es ").concat(unionCadenas));
// Intersección de dos cadenas (caracteres comunes)
var interseccionCadenas = __spreadArray([], new Set(cadena1), true).filter(function (char) { return cadena2.includes(char); }).join("");
console.log("Intersecci\u00F3n de las cadenas ".concat(cadena1, " y ").concat(cadena2, " es ").concat(interseccionCadenas));
// Acceso a caracteres específicos (por posición)
var tercerCaracter = texto.charAt(2);
console.log("El tercer car\u00E1cter de ".concat(texto, " es ").concat(tercerCaracter));
// Repetición de una cadena
var cadenaRepetida = "Hola ".repeat(3);
console.log("Cadena Hola repetida 3 veces queda ".concat(cadenaRepetida));
// Recorrido de una cadena (usando un bucle)
for (var i = 0; i < texto.length; i++) {
    console.log("Car\u00E1cter en posici\u00F3n ".concat(i, ": ").concat(texto[i]));
}
// Conversión a título (primera letra en mayúscula)
var titulo = texto.toLowerCase().replace(/\b\w/g, function (char) { return char.toUpperCase(); });
console.log("La cadena ".concat(texto, " como t\u00EDtulo ").concat(titulo));
// División de una cadena en un array de substrings
var palabras = texto.split(" ");
console.log("Palabras en la cadena ".concat(texto, " son ").concat(palabras));
// Verificación de si una cadena comienza o termina con ciertos caracteres
var comienzaCon = texto.startsWith("Hola");
console.log("\u00BFLa cadena ".concat(texto, " comienza con \"Hola\"? ").concat(comienzaCon));
var terminaCon = texto.endsWith("mundo!");
console.log("\u00BFLa cadena ".concat(texto, "termina con \"mundo!\"? ").concat(terminaCon));
// Verificar si una cadena es palíndromo
function esPalindromo(cadena) {
    var sinEspacios = cadena.replace(/\s/g, "").toLowerCase();
    var invertida = sinEspacios.split("").reverse().join("");
    return sinEspacios === invertida;
}
// Verificar si una cadena es un anagrama
function esAnagrama(cadena1, cadena2) {
    var limpiarCadena = function (cadena) { return cadena.replace(/\s/g, "").toLowerCase(); };
    var limpiaCadena1 = limpiarCadena(cadena1);
    var limpiaCadena2 = limpiarCadena(cadena2);
    var ordenada1 = limpiaCadena1.split("").sort().join("");
    var ordenada2 = limpiaCadena2.split("").sort().join("");
    return ordenada1 === ordenada2;
}
// Verificar si una cadena es un isograma
function esIsograma(cadena) {
    var caracteres = new Set();
    for (var _i = 0, cadena_1 = cadena; _i < cadena_1.length; _i++) {
        var char = cadena_1[_i];
        var caracter = char.toLowerCase();
        if (caracteres.has(caracter)) {
            return false;
        }
        caracteres.add(caracter);
    }
    return true;
}
// Ejemplos de uso de las funciones adicionales
console.log("\u00BFEs \"".concat(texto, "\" un pal\u00EDndromo? ").concat(esPalindromo(texto)));
console.log("\u00BFEs Ana un pal\u00EDndromo? ".concat(esPalindromo("Ana")));
console.log("\u00BFEs \"listen\" un anagrama de \"silent\"? ".concat(esAnagrama("listen", "silent")));
console.log("\u00BFEs \"programming\" un isograma? ".concat(esIsograma("programming")));
