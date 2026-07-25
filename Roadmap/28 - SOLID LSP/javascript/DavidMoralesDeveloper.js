// Principio de Sustitución de Liskov (LSP) 
// "Los objetos de un programa deben ser reemplazables por instancias de sus subtipos (o subclases) sin alterar la corrección de ese programa."

// * DIFICULTAD EXTRA (opcional):
//  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
//  * cumplir el LSP.
//  * Instrucciones:
//  * 1. Crea la clase Vehículo.
//  * 2. Añade tres subclases de Vehículo.
//  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
//  * 4. Desarrolla un código que compruebe que se cumple el LSP.

// donde el subtipo puede sustituir completamente al tipo base sin cambiar su comportamiento observable para los clientes.

class Veiculo{

}
class Volvo extends Veiculo{
    acelerar(){console.log("acelerar")}
 frenar(){console.log("frenarx")}
}
class Bmw extends Veiculo{
    acelerar(){console.log("acelerar")}
 frenar(){console.log("frenarx")}
}
class Renol extends Veiculo{
    acelerar(){console.log("acelerar")}
 frenar(){console.log("frenarx")}
}
