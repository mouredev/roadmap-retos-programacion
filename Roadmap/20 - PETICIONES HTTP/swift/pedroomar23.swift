import Foundation

/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */

struct ExChange: Decodable {
    let currency: String 
    let dataTime: String? 
    let exChangeDirection: String 
    let rates: Rates 

    enum CodingKeys: String, CodingKey {
        case currency 
        case dataTime = "data_time"
        case exChangeDirection = "exchange_direction"
        case rates 
    }

    init(from decoder: any Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        self.currency = try container.decode(String.self, forKey: .currency)
        self.dataTime = try container.decodeIfPresent(String.self, forKey: .dataTime) ?? ""
        self.exChangeDirection = try container.decode(String.self, forKey: .exChangeDirection)
        self.rates = try container.decode(Rates.self, forKey: .rates)
    }

    init(currency: String, dataTime: String, exChangeDirection: String, rates: Rates) {
        self.currency = currency
        self.dataTime = dataTime
        self.exChangeDirection = exChangeDirection
        self.rates = rates 
    }
}

struct Rates: Decodable {
    let buy: Double 
    let sell: Double 
    let mid: Double 

    enum CodingKeys: CodingKey {
        case buy 
        case sell 
        case mid 
    }

    init(from decoder: any Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        self.buy = try container.decode(Double.self, forKey: .buy)
        self.sell = try container.decode(Double.self, forKey: .sell)
        self.mid = try container.decode(Double.self, forKey: .mid)
    }

    init(buy: Double, sell: Double, mid: Double) {
        self.buy = buy 
        self.sell = sell 
        self.mid = mid 
    }
}

func exchange() async {
    let urlCUP = URL(string: "https://exchange-rate.decubba.com/api/v2/formal/target/cup.json")!

    let (dataCUP, _) = try! await URLSession.shared.data(from: urlCUP)
    let exchangeCUP = try! JSONDecoder().decode(ExChange.self, from: dataCUP)
    print("ExchangeCUP: \(exchangeCUP)")
}
