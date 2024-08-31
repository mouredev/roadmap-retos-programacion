import Foundation 

/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */

// CallBacks 
let url = URL(string: "https://wwww.swift.org")!

func fetchData(from url: URL, completion: @escaping (Data?, Data?) -> Void) {
    let task: URLSessionDataTask = URLSession.shared.dataTask(with: url) { (data: Data?, response: URLResponse?, error: _) in 
        completion(data, response)
    }
    task.resume()
}

