import Foundation
/*
 Una peticion http  utiliza el protocolo Hypertext Transfer Protocol (HTTP). para comunicar
 datos atravez  de la red. esta peticion suele hacerse a un servidor o backend para obtener
 datos.

 una solicitud http se componene de los siguintes elementos:
  un metodo (GET, POST, PUT, DELETE, PATCH)
  una url (url de la peticion)
  un encabezado (cabeceras)
  version del protocolo (HTTP/1.1)

 Glosario basico de conceptos

 el metodo (GET, POST, PUT, DELETE, PATCH) es un verbo que se utiliza para
 saber la operacion que se va a realizar. por ejemplo:

 GET: obtiene informacion
 POST: permite enviar datos al servidor
 PUT:  nos permite enviar datos para actualizar
 DELETE: elimina datos

 el encabezado (cabeceras) es un conjunto de datos que se envia con la peticion
 estos pueden aportar informacion  adcional al servidor. por ejemplo:

  Accept: acepta informacion de la peticion ya sea JSON o XML o texto plano

  Peticiones http en Swift

  en swift la libreria  de Foundation es la encargada de hacer las peticiones http
  y asu vez nos permite convertir los datos recibidos  a una estructura de datos
  de swift gracias al protocolo Codable.
  
  */
  //1.- crear estructura para decodificar los datos de la solicitud
   
   struct Drink: Codable{
        let strDrink: String
        let strDrinkThumb: URL
        let idDrink: String
    }

   struct Drinks: Codable {
        let drinks: [Drink]
    }

   // 2.- hacer  solicitud http
   
   func fetchDrinks(url: URL) async throws -> [Drink] {
        let (data, _) = try await URLSession.shared.data(from: url)
        let drinks = try JSONDecoder().decode(Drinks.self, from: data)
        return drinks.drinks
    }


   // 3.- llamar a la funcion de manera concurrente y crear el objeto url

   let url = URL(string: "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Vodka")!

   Task {
       let drinks = try await fetchDrinks(url: url)
       print(drinks)
   }

