import java.util.regex.Pattern

fun regExpr(cadena: String) {
    val patron = "-?\\d+(\\.\\d+)?"
    val regex = Pattern.compile(patron)
    val numeros = regex.matcher(cadena)

    println("Números encontrados:")
    while (numeros.find()) {
        println(numeros.group())
    }
    println()
}

fun main() {
    var texto = "Este es un texto con números como 123, 45.6, -7 y 1000."
    println("Vamos a analizar el siguiente texto:")
    println("'$texto'\n")
    regExpr(texto)

    texto = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456"
    println("Vamos a analizar el siguiente texto:")
    println("'$texto'\n")
    regExpr(texto)

    emailValidation("correo@correo.com")
    emailValidation("correo@correo")

    phoneValidation("+34 123456789")
    phoneValidation("123456789")

    urlValidation("http://www.google.com")
    urlValidation("www.google.com")
}

fun emailValidation(email: String) {
    val patron = "^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}$"
    if (Pattern.matches(patron, email)) {
        println("El email $email es válido.")
    } else {
        println("El email $email no es válido.")
    }
}

fun phoneValidation(phone: String) {
    val patron = "^\\+?(\\d{2,3})?[-. ]?\\d{9}$"
    if (Pattern.matches(patron, phone)) {
        println("El teléfono $phone es válido.")
    } else {
        println("El teléfono $phone no es válido.")
    }
}

fun urlValidation(url: String) {
    val patron = "^(http|https):\\/\\/[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,4}"
    if (Pattern.matches(patron, url)) {
        println("La URL $url es válida.")
    } else {
        println("La URL $url no es válida.")
    }
}
