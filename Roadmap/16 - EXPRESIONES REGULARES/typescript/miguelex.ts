function regExpr(cadena: string): void {
    let patron: RegExp = /-?\d+(\.\d+)?/g;
    let numeros: RegExpMatchArray | null = cadena.match(patron);

    console.log("Números encontrados:");
    if (numeros) {
        numeros.forEach(numero => console.log(numero));
    }
    console.log();
}

let texto: string = "Este es un texto con números como 123, 45.6, -7 y 1000.";
console.log("Vamos a analizar el siguiente texto:");
console.log("'" + texto + "'\n");
regExpr(texto);

texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456";
console.log("Vamos a analizar el siguiente texto:");
console.log("'" + texto + "'\n");
regExpr(texto);

function emailValidation(email: string): void {
    let patron: RegExp = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (patron.test(email)) {
        console.log("El email " + email + " es válido.");
    } else {
        console.log("El email " + email + " no es válido.");
    }
}

function phoneValidation(phone: string): void {
    let patron: RegExp = /^\+?(\d{2,3})?[-. ]?\d{9}$/;
    if (patron.test(phone)) {
        console.log("El teléfono " + phone + " es válido.");
    } else {
        console.log("El teléfono " + phone + " no es válido.");
    }
}

function urlValidation(url: string): void {
    let patron: RegExp = /^(http|https):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}/;
    if (patron.test(url)) {
        console.log("La URL " + url + " es válida.");
    } else {
        console.log("La URL " + url + " no es válida.");
    }
}

emailValidation("correo@correo.com");
emailValidation("correo@correo");

phoneValidation("+34 123456789");
phoneValidation("123456789");

urlValidation("http://www.google.com");
urlValidation("www.google.com");
