// SRP(single responsability principel) uns clase o funcion solo tiene una razon para cambiar

class AutoServico {
    constructor(compras, total) {
        this.compras = compras,
        this.total = total
    }

    getCompras (){
        return this.compras
    }
    getTotal(){
        return this.total
    }
}

class Descuentos {
    descuentoDelTotal(total){
        // const diezporciento = total - total * 0.10 
        return total - total * 0.10
    }
}

class ProductoGratisExtra {
    productoDeRegalo(carrito, regalo){
        carrito.getCompras().push(regalo)
        return carrito.getCompras()
    }
}

const miPrimeraCompra = new AutoServico(["queso", "jamon", "tortillas"], 100)

console.log(miPrimeraCompra.getCompras())
console.log(miPrimeraCompra.getTotal())
const descuento = new Descuentos()
console.log("su descuento del 10% se resto de su total :" + descuento.descuentoDelTotal(miPrimeraCompra.getTotal()))
const regaloEnCompra = new ProductoGratisExtra()
console.log("su producto de regalo se agreso a su carrito de compras " + regaloEnCompra.productoDeRegalo(miPrimeraCompra, "aguacate") )
console.log("--------------------------------------Libreria -------------------------------------")

//  Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
//  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
//  * y el procesamiento de préstamos de libros.
//  * Requisitos:

// 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
//    información básica como título, autor y número de copias disponibles.


//  * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
//    información básica como nombre, número de identificación y correo electrónico.

// * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
//   tomar prestados y devolver libros.

// * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
//   los tres aspectos mencionados anteriormente (registro de libros, registro de
//   usuarios y procesamiento de préstamos).

class Libreria {
    constructor( libros, usuarios, prestamos ){
        this.libros= [
            {titulo: "100 años de soledad",
             autor: "Gabriel Marquez",
             copiasDisponibles: 15,
             usuariosConEsteLibro: []
             },
            {titulo: "Don Quijote",
             autor: "Miguel de Cervantes",
             copiasDisponibles: 10,
             usuariosConEsteLibro: []
             },
            {titulo: "El Principito",
             autor: "Saint-Exupery",
             copiasDisponibles: 5,
             usuariosConEsteLibro: []
             }
        ]
        this.usuarios = [
            {nombre: "Juan",
             id: 1,
             email: "Juan@gmail",
             misLibros:[]
             },
            {nombre: "Pedro",
             id: 2,
             email: "Pedor@gmail",
             misLibros:[]
             },
            {nombre: "Julio",
             id: 3,
             email: "Julio@gmail",
             misLibros:[]
             },
        ]
        this.prestamos =[]
    }
    getLibro (){
        return this.libros
    }
    getusuarios (){
        return console.log(this.usuarios)
    }
    getPrestamos (){
        return console.log(this.prestamos)
    }
    addLibro ( newLibro ) {
        return this.libros.push(newLibro)
    }
    addUsurio (newUsuario) {
        return this.usuarios.push(newUsuario)
    }

    // validaciones si el usuario tiene el libro no puede volver a pedirlo
    //si el libro ya esta agitado regresar mensaje
    addPestamo(tituloaBuscar, idUsuario){
        const libroEncontrado =this.libros.find(libro => libro.titulo === tituloaBuscar)
        const idEncontrado = this.usuarios.find(usuario => usuario.id === idUsuario )
         
        if(libroEncontrado && idEncontrado){
            libroEncontrado.copiasDisponibles-=1
            libroEncontrado.usuariosConEsteLibro.push(idEncontrado.id)
            idEncontrado.misLibros.push(libroEncontrado.titulo)
            this.prestamos.push(libroEncontrado)
        }
        
        return this.prestamos
    }

    addDevolver(tituloADevolver, idUsusario){
        const libroEncontrado =this.libros.find(libro => libro.titulo === tituloADevolver)
        const idEncontrado = this.usuarios.find(usuario => usuario.id === idUsusario )
        const devolver = [libroEncontrado, idEncontrado]
        if(libroEncontrado.usuariosConEsteLibro.find(ids => ids === idUsusario)){
            libroEncontrado.copiasDisponibles +=1
            libroEncontrado.usuariosConEsteLibro = libroEncontrado.usuariosConEsteLibro.filter(id => id !== idUsusario)
            idEncontrado.misLibros = idEncontrado.misLibros.filter(nombre => nombre !== tituloADevolver)
        }
        return devolver
    }


}

const libreria = new Libreria()

console.log("-------------------addlibros-----------------")
libreria.addLibro({
    titulo: 'mil y una noche',
    autor: 'Desconocido',
    copiasDisponibles: 10,
    usuariosConEsteLibro: []
  },)
  
  libreria.addUsurio({ nombre: 'Julian', id: 4, email: 'Julian@gmail', misLibros: [] })
  console.log("--------------------prestamos----------------------")
  console.log(libreria.addPestamo('El Principito', 1))
  console.log(libreria.addPestamo('El Principito', 3))
  console.log(libreria.addPestamo('Don Quijote', 1))
  console.log("-----------Prestamos &&&&&&&&&&&&&&&&&&66")
  libreria.getPrestamos()
  console.log("---------------------get libros y usuarios modificados------------------")
  console.log(libreria.getLibro())
  libreria.getusuarios()
  console.log("------------------------Devolver libros-----------")
  console.log(libreria.addDevolver('El Principito', 1))
 console.log(libreria.getLibro())
  libreria.getusuarios()







  