/* 🔥 EJERCICIO:
Utilizando tu lenguaje, explora el concepto de expresiones regulares,
creando una que sea capaz de encontrar y extraer todos los números
de un texto.
*/
const texto = "El precio es de 123 euros, pero con un descuento del 15%. Además, hay 4 productos disponibles.";

// Expresión regular para encontrar números
const regexNumeros = /\d+/g;

// Extraer números del texto
const numeros = texto.match(regexNumeros);

console.log("Números encontrados:", numeros);
// Números encontrados:  (3) ['123', '15', '4']

/*
Dictionary 📗 [ /\d+/g ] = {
    \d: Coincide con cualquier dígito (0-9).
    +: Indica que debe coincidir con uno o más dígitos consecutivos.
    g: Modificador global que busca todas las coincidencias en el texto (no solo la primera).
}
*/
//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------

/* 🔥 DIFICULTAD EXTRA (opcional):
Crea 3 expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una url.
*/

function validarEmail(email) {
    const regexEmail = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return regexEmail.test(email);
}

function validarTelefono(telefono) {
    const regexTelefono = /^\+?\d{1,3}?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$/;
    return regexTelefono.test(telefono);
}

function validarURL(url) {
    const regexURL = /^(https?:\/\/)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(\/.*)?$/;
    return regexURL.test(url);
}

console.log("¿Es válido el email 'usuario@example.com'?", validarEmail("usuario@example.com"))
console.log("¿Es válido el email 'usuario@.com'?", validarEmail("usuario@.com"))
// ¿Es válido el email 'usuario@example.com'? true
// ¿Es válido el email 'usuario@.com'? false

console.log("¿Es válido el teléfono '+51-999-999-999'?", validarTelefono("+51-999-999-999"))
console.log("¿Es válido el teléfono '123'?", validarTelefono("123"))
// ¿Es válido el teléfono '+51-999-999-999'? true
// ¿Es válido el teléfono '123'? false

console.log("¿Es válida la URL 'https://www.example.com'?", validarURL("https://www.example.com"))
console.log("¿Es válida la URL 'www.example'?", validarURL("www.example"))
// ¿Es válida la URL 'https://www.example.com'? true
// ¿Es válida la URL 'www.example'? true


/*
Dictionary 📗 [ expresiones regulares ] = {
    regexEmail : {
        ^[a-zA-Z0-9._%+-]+: Parte local del email (antes del @), permite letras, números y caracteres especiales como ., _, %, +, -.
        @[a-zA-Z0-9.-]+: Dominio del email, permite letras, números, puntos (.) y guiones (-).
        \.[a-zA-Z]{2,}$: Extensión del dominio (ejemplo: .com, .es), debe tener al menos 2 caracteres.
    }
    regexTelefono : {
        ^\+?: Opcionalmente comienza con un + (indicador de país).
        \d{1,3}?: Código de país (1 a 3 dígitos).
        [-.\s]?: Separadores opcionales (-, ., espacio).
        \(?\d{1,4}\)?: Código de área opcionalmente entre paréntesis.
        \d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}$: Número principal, separado en partes.
    }
    regexURL : {
        ^(https?:\/\/)?: Protocolo opcional (http:// o https://).
        [a-zA-Z0-9.-]+\.[a-zA-Z]{2,}: Dominio y extensión (ejemplo: example.com).
        (\/.*)?$: Ruta opcional después del dominio.
    }
}
*/