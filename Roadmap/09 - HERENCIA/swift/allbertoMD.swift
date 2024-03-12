import Foundation


// Declaración de la calse Animal().
class Animal {
    var breed = "" // Propiedas raza.
}

// Declaración de la clase Cat()
class Cat: Animal {
    var name: String // Propiedad nombre.
    let sex: String // Propiedad sexo.

    // Definición del inicializar de la clase Cat().
    init(name: String, sex: String) {
        self.name = name
        self.sex = sex
    }

    // Definición del metodo sonido del gato
    func catSound() {
        if sex == "macho" { // Si es macho se imprime El gato.
            print("El gato \(name) hace: MIIAAAAU")
        } else if sex == "hembra" { // Si es hembra se imprime La gata.
            print("la gata \(name) hace: MIIAAAAU")
        } else { // Sin no se introduce macho o hembra se imprime sexo no valido.
            print("Sexo del gato no valido. escribe hembra, o macho")
        }
    }
}

print("El Gato")
// Creacion del objeto myCat de la classe Cat().
var myCat = Cat(name: "Icee", sex: "hembra")
myCat.breed = "Gato" // Raza del animal.
myCat.catSound() // Llamada al metodo sonido de gato.


// Declaración de la clase Dog().
class Dog:Animal {
    var name: String // Propiedas nomber.
    let sex: String // Propiedad sexo.

    // Definición del inicializador de la clase Dog().
    init(name: String, sex: String) {
        self.name = name
        self.sex = sex
    }

    // Definición del metodo sonido del perro.
    func dogSound() {
        if sex == "macho" { // Si el sexo es macho imprime El perro.
            print("El perro \(name) hace: GUAUU")
        } else if sex == "hembra" { // Si el sexo es hembra imprime La perra.
            print("La perra \(name) hace: GUAUU")
        } else { // Sin no se introduce macho o hembra se imprime sexo no valido.
            print("Sexo del gato no valido. escribe hembra, o macho")
        }
    }
}

print("\nEl Perro")
// Creación del objeto myDog de la clase Dog().
var myDog = Dog(name: "Parche", sex: "macho")
myDog.breed = "Perro" // Raza del animal.
myDog.dogSound() // Llama al metodo sonido del perro.





// DIFICULTAS EXTRA


// Creacion de la clase Employee()
class Employee {
    let id: String // Propiedd ID.
    var name: String // Propiedad nombre.
    var job: String // Propiedad puesto de trabajo.

    var information: String { // Propiedad computada con la información de usuario.
        return "ID: \(id)\nEompleado: \(name)\nPuesto de trabajo: \(job)"
    }

    // Inicializador de la clase Employee().
    init(id: String = UUID().uuidString, name: String, job: String) {
        self.id = id
        self.name = name
        self.job = job
    }
}



// Definición de la clase Developer() que hereda de la super clase Employee().
class Developer: Employee {
    var language: String // Propieda lenguaje de programación.
    var frontend: Bool // Propiedad si es frontend.
    var backend: Bool // Propiedad si es backend.
    var code: String = ""

    // Inicializador de la clase Developer() y de la super clase Empoyee().
    init(id: String = UUID().uuidString, name: String, job: String, language: String, frontend: Bool, backend: Bool) {
        self.language = language
        self.frontend = frontend
        self.backend = backend
        super.init(id: id, name: name, job: job) // Inicializador de la super clase
    }

    // Definición del metodo escribir codigo.
    func typingCode(_ code: String, of userName: String) {
        print("Este es el codigo de \(userName)")
        self.code = code
        print(code)
    }
}



// Declaración de la clase Manager() que hereda de la super clase Employee().
class Manager: Employee {
    var scheduleMeeting: Bool // Propiedas si creo una reunión.

    // Inicializador de la clase Manager() y de la super clase Employee().
    init(id: String = UUID().uuidString, name: String, job: String, scheduleMeeting: Bool = false) {
        self.scheduleMeeting = scheduleMeeting
        super.init(id: id, name: name, job: job) // Inicializador de la super clase.
    }

    // Definición del metodo crear una reunion.
    func makeScheduleMeeting(with members: [(String, String)], week day: String, hour: String) {
        print("La reunion es el \(day) a las \(hour) y los mienbros son:")

        for (person, job) in members {
            print("\(person) ---- \(job)")
        }
        scheduleMeeting = true
    }
}



// Declariación de la clase ProyectManager() que  hereda de la super clase Manager().
class ProyectManager: Manager {
    var product: String // Propiedad nombre del proyecto.
    var numberOfDevelopers: Int // Propiedad numero de desarrolladores.
    var verifiedCode: Bool // Propiedad si ha verificado el codigo.
    var developersGroup: [String] = [] // Propiedad de los nombres de los desarrolladores.

    override var information: String { // Propiedad que sobre escribe la propiedad de la super clase Employee().
        return "Proyecto: \(product)\nGerente: \(name)\nNumero de developers: \(numberOfDevelopers)"
    }

    // Definición del inicializador de la clase ProyectManager() y de las super clasees Manger() y Employee().
    init(id: String = UUID().uuidString, name: String, job: String, scheduleMeeting: Bool = false, product: String, numberOdDevelopers: Int = 0, verifiedCode: Bool = false) {
        self.product = product
        self.numberOfDevelopers = numberOdDevelopers
        self.verifiedCode = verifiedCode
        super.init(id: id, name: name, job: job, scheduleMeeting: scheduleMeeting) // Inicializador de las super clases.
    }

    // Definición del metodo añadir desarrollador al proyecto.
    func addDeveloperToProyect(developer name: String) {
        developersGroup.append(name)
        numberOfDevelopers = developersGroup.count
    }
}

print("\nInformación de los desarrolladores.")
// Creación de los objetos desarrolladores de la clase Developer().
var developer1 = Developer(name: "Miguel", job: "Desarrollador", language: "Swift", frontend: true, backend: false)
print(developer1.information)
var developer2: Developer = Developer(name: "Sara", job: "Desarrollador", language: "Swift", frontend: true, backend: false)
print(developer2.information)
var developer3: Developer = Developer(name: "Raquel", job: "Desarrollador", language: "Swift", frontend: false, backend: true)
print(developer3.information)
var developer4: Developer = Developer(name: "Carlos", job: "Desarrollador", language: "Swift", frontend: false, backend: true)
print(developer4.information)

// Creación del objeto gerente de proyecto de la clase ProyectManager().
var proyectManager1: ProyectManager = ProyectManager(name: "Alexa", job: "Gerente de Proyecto", product: "Semafor App")

// Creación del objeto manager de la clase Manager().
var manager: Manager = Manager(name: "John", job: "Gerente")

// Lamadas al metod añadir desarrolladores al proyecto.
proyectManager1.addDeveloperToProyect(developer: developer1.name)
proyectManager1.addDeveloperToProyect(developer: developer2.name)
proyectManager1.addDeveloperToProyect(developer: developer3.name)
proyectManager1.addDeveloperToProyect(developer: developer4.name)

print("\nInformación de un producto.")
// Imprimir la información del proyecto haciendo uso de la propiedad information de la clase ProyectManager().
print(proyectManager1.information)

print("\nCreación y mostrar información de la reunión")
// Llamada al metodo crear una reunión de la clase Manager().
manager.makeScheduleMeeting(with: [(proyectManager1.name, proyectManager1.job),
(developer1.name, developer1.job),
(developer4.name, developer4.job)], week: "Martes", hour: "10:00 am")