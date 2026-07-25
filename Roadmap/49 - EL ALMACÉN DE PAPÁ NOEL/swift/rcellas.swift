import Foundation

func generatePassword() -> String {
    let letters = ["A", "B", "C"]
    let numbers = ["1", "2", "3"]
    let passwordElements = letters + numbers
    return passwordElements.shuffled().prefix(4).joined()
}

func runGame() {
    let secretPassword = generatePassword()
    var attempts = 1
    let passwordElements = ["A", "B", "C", "1", "2", "3"]

    print("Adivina la contraseña del almacén de Papá Noel.")

    while attempts <= 10 {
        print("Intento: \(attempts)")
        print("Introduce la contraseña: ", terminator: "")
        
        if let input = readLine()?.uppercased() {
            if input.count != 4 {
                print("Error: La contraseña debe tener 4 caracteres.")
                continue
            }
            if !input.allSatisfy({ passwordElements.contains(String($0)) }) {
                print("Error: Sólo se permiten los caracteres \(passwordElements).")
                continue
            }

            if input == secretPassword {
                print("¡Contraseña correcta! Has descifrado el código del almacén. Feliz Navidad.")
                break
            }

            for (index, character) in input.enumerated() {
                if character == secretPassword[secretPassword.index(secretPassword.startIndex, offsetBy: index)] {
                    print("\(character): Correcto")
                } else if secretPassword.contains(character) {
                    print("\(character): Presente")
                } else {
                    print("\(character): Incorrecto")
                }
            }

            attempts += 1

            if attempts > 10 {
                print("Lo siento, los 10 intentos para descifrar el código han finalizado.")
                print("Papá Noel no ha podido entregar los regalos.")
            }
        }
    }
}

runGame()