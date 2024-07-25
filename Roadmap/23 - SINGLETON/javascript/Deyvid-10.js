// Patron de diseno singleton

class Office
{
    constructor(name, employees)
    {
        this.name = name,
        this.employees = employees

        if(typeof Office.instance === "object")
        {
            return Office.instance
        }

        Office.instance = this
        return this
    }
}

let office1 = new Office("Principal", 30)

let office2 = new Office("Principal", 40)

console.log(office1);
console.log(office2);


// DIFICULTAD EXTRA

class Usuario
{
    constructor(id, username, name, email)
    {
        this.id = id
        this.username = username
        this.name = name
        this.email = email


        if(typeof Usuario.instance === "object")
        {
            return Usuario.instance
        }

        Usuario.instance = this
        return this
    }

    getData()
    {
        console.log(`Identificador: ${this.id}\nUsuario: ${this.username}\nNombre: ${this.name}\nEmail: ${this.email}`);
    }

    deleteData()
    {
        this.id = ""
        this.username = ""
        this.name = ""
        this.email = ""
    }
}

let usuario1 = new Usuario(1, "Daniel-10", "Daniel Ramirez", "daniel1524@gmail.com")

let usuario2 = new Usuario(2, "Raquel-20", "Raquel Herrera", "herrara_2596@gmail.com")

usuario1.getData()
usuario2.getData()

usuario2.deleteData()

usuario1.getData()
usuario2.getData()