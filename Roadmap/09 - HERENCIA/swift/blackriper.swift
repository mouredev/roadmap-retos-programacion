/* la herencia nos permite crear clases que hereden propiedades y métodos de otras clases
   en swift solo se puede utilizar herencia con las classes no con structs
 */

class Animal{
    var name: String
    init(nam: String) {
        self.name = nam
    }
    func emitSound(){
         print("the animal  \(name) makes a sound")
         
    }
  }


class Dog: Animal{
    var race: String
    init(rac: String, name: String) {
        self.race = rac
        super.init(nam: name)
    }
    override func emitSound() {
        print("the dog \(name) makes guau")
    }
}

class Cat: Animal{
    var race: String
    init(rac: String, name: String) {
        self.race = rac
        super.init(nam: name)
    }
    override func emitSound() {
        print("the cat \(name) makes miau")
    }
}

let dog=Dog(rac: "labrador", name: "Nala")
let cat=Cat(rac: "persa", name: "ONYX")
dog.emitSound()
cat.emitSound()

//ejercicio extra

enum Role{
     case manager
     case proyect_manager
     case developer
}

struct Proyect{
    var name: String  
    var developerList: [Developer]
}


class Employee {
    var id: Int
    var name: String
    var role: Role
    init(id: Int, name: String, role: Role) {
        self.id = id
        self.name = name
        self.role = role
    }
}

class Developer:Employee{
    private let language: String
     init(id: Int, name: String, role: Role, language: String) {
         self.language = language
         super.init(id: id, name: name, role: role)
     }
    func work(){
        print("My name is \(name) and working on a project using \(language)")        
    } 
}

class ProyectManager:Employee{
    private var projectList: [Proyect]
    init(id: Int, name: String, role: Role, projectList: [Proyect]) {
        self.projectList = projectList
        super.init(id: id, name: name, role: role)
    }
    func activeProject(){
        for project in projectList{
            print("Project name: \(project.name) Developer list: \(project.developerList)")
        }
    }
}

class Manager:Employee{
   private var teamList: [ProyectManager]
    init(id: Int, name: String, role: Role, teamList: [ProyectManager]) {
        self.teamList = teamList
        super.init(id: id, name: name, role: role)
    }
    
    func greet(){
        print("Hello, my name is \(name)  I'm a \(role)")
    }

    func activeTeam(){
        for team in teamList{
            print("Team name: \(team.name) ")
        }
    }
}


let dev1=Developer(id: 1, name: "kontroldev", role: .developer, language: "Swift")
let dev2=Developer(id: 2, name: "pguillo02", role: .developer, language: "Java")
let dev3=Developer(id: 3, name: "thegera4", role: .developer, language: "Go")
dev1.work()
dev2.work()
dev3.work()

let proyect1=Proyect(name: "App IOS", developerList: [dev1])
let proyect2=Proyect(name: "App Swing", developerList: [ dev2])
let proyect3=Proyect(name: "Backend", developerList: [dev3])

let team1=ProyectManager(id: 1, name: "roswell", role: .proyect_manager, projectList: [proyect1,proyect2])
let team2=ProyectManager(id: 2, name: "blackriper", role: .proyect_manager, projectList: [proyect3])
team1.activeProject()
team2.activeProject()

let manager1=Manager(id: 1, name: "mouredev", role: .manager, teamList: [team1,team2])
manager1.greet()
manager1.activeTeam()

