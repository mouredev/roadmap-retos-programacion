import Foundation

/* las expresiones regulares son patterns que nos permiten extraer informacion de una cadena de texto
  en swift se puede evaluar la expresion regular con NSRegularExpression o con un metodo de String llamado
  range para crear el regex se utiliza la clase Regex  para mas informacion ver:

  https://developer.apple.com/documentation/foundation/nsregularexpression
  https://www.advancedswift.com/regular-expressions/

  para este ejercicio solo vamos a usar el metodo range
 */


func examplePattern() {
   let exampleText = """
        El manga Hokuto no ken cuenta con 245 capítulos, publicados en la revista semanal Shōnen Jump,
        desde el número 41 de 1983 hasta el número 35 de 1988. Luego fue recopilado en 27 volúmenes
        por Shueisha. Se está publicando en 14 Kanzenban por Shōgakukan y una Master Edition de 27 volúmenes 
        por Coamix.
        """

   do {
     let pattern = try Regex("[0-9]")
     print(exampleText.ranges(of: pattern).map { String(exampleText[$0]) })
   } catch {
     print(error)
   }
   
 }

 examplePattern()

 // ejercicio extra 
 
 enum ValidData {
    case url  
    case email
    case phone
 }
   
  // para mas informacion de los patters te invito a ver mi solucion en kotlin 
 func validateData(_ data: String, type: ValidData) throws ->  Bool {
   
   let regEx = switch type {
   case .url:
        "^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]"

   case .email:
        "^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$"
   
   case .phone:
      #"^\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}$"# 
    }

   let result = data.range(of: regEx, options: .regularExpression) 
   return (result != nil)
 }

 do {
   let validUrl = try validateData("https://google.com", type: .url)
   print(validUrl)

   let validEmail = try validateData("XG7p7@example.com", type: .email)
   print(validEmail)

   let validPhone = try validateData("411-153-1223", type: .phone)
   print(validPhone)

 } catch {
   print(error)
 }
