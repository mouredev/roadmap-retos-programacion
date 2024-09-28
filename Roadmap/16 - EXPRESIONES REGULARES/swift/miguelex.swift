import Foundation

func regExpr(_ cadena: String) {
    let pattern = #"-?\d*\.?\d+"#
    let regex = try! NSRegularExpression(pattern: pattern)
    let matches = regex.matches(in: cadena, range: NSRange(cadena.startIndex..., in: cadena))
    
    print("Números encontrados:")
    for match in matches {
        if let range = Range(match.range, in: cadena) {
            print(String(cadena[range]))
        }
    }
    print("\n")
}

func emailValidation(_ email: String) {
    let pattern = #"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"#
    let regex = try! NSRegularExpression(pattern: pattern)
    if regex.firstMatch(in: email, options: [], range: NSRange(location: 0, length: email.utf16.count)) != nil {
        print("El email \(email) es válido.")
    } else {
        print("El email \(email) no es válido.")
    }
}

func phoneValidation(_ phone: String) {
    let pattern = #"^\+?(\d{2,3})?[-. ]?\d{9}$"#
    let regex = try! NSRegularExpression(pattern: pattern)
    if regex.firstMatch(in: phone, options: [], range: NSRange(location: 0, length: phone.utf16.count)) != nil {
        print("El teléfono \(phone) es válido.")
    } else {
        print("El teléfono \(phone) no es válido.")
    }
}

func urlValidation(_ url: String) {
    let pattern = #"^(http|https)://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"#
    let regex = try! NSRegularExpression(pattern: pattern)
    if regex.firstMatch(in: url, options: [], range: NSRange(location: 0, length: url.utf16.count)) != nil {
        print("La URL \(url) es válida.")
    } else {
        print("La URL \(url) no es válida.")
    }
}

let texto = "Este es un texto con números como 123, 45.6, -7 y 1000."
print("Vamos a analizar el siguiente texto:")
print("'\(texto)'\n")
regExpr(texto)

let texto2 = "123Erase una vez un número 1234567890 y otro 0987654321. Y para terminar456"
print("Vamos a analizar el siguiente texto:")
print("'\(texto2)'\n")
regExpr(texto2)

emailValidation("correo@correo.com")
emailValidation("correo@correo")

phoneValidation("+34 123456789")
phoneValidation("123456789")

urlValidation("http://www.google.com")
urlValidation("www.google.com")
