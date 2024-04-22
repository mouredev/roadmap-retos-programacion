fun main() {
    val textoEjemplo = "2 y dos son 4, cuatro y dos son 6, seis y dos son 8 y ocho 16"
    val findNums = Regex("\\d+").findAll(textoEjemplo)
    for (num in findNums) {
        val first = num.range.first
        val last = num.range.last
        println("${num.value} -> ($first,$last)")
    }

    println("${"\n" + "~".repeat(7)} EJERCICIO EXTRA ${"~".repeat(7)}")
    //Validar email
    val email = Regex("\\w+\\S*@\\w+.\\w+")
    val textEmail = "Buenas tardes, el correo electrónico es correo.deprueba_hola@corporacion.es. Muchas gracias"
    val findEmail = email.find(textEmail)
    println(findEmail?.value)

    //Validar teléfono
    val telf = Regex("[+]\\d+\\s\\d+")
    val textTelf = "Puede llamar al número +34 6874521035200 para más información"
    val findTelf = telf.find(textTelf)
    println(findTelf?.value)

    //Validar URL
    val url = Regex("https?://\\w+.\\w+.\\w+[.\\w+]*")
    val textUrl = "Puede visitar nuestra web: https://www.unaweb_deprueba101.com.wordpress.es para más información"
    val findUrl = url.find(textUrl)
    println(findUrl?.value)
}
