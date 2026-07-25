// * EJERCICIO:
//  * Explora el patrón de diseño "singleton" y muestra cómo crearlo
//  * con un ejemplo genérico.
class singleton{
    constructor(){
        if(!singleton.instance){
            this.valor="Soy la unica instancia"
            singleton.instance=this
        }
        return singleton.instance
    }
    obtenerValor(){
        return this.valor
    }
}

const instancia1=new singleton()
const instancia2=new singleton()

console.log(instancia1===instancia2);
console.log(instancia1.obtenerValor());

class Usuario{
    constructor(id,username,nombre,email){
        if(!Usuario.instance){
            this.id=id
            this.username=username
            this.nombre=nombre
            this.email=email
            Usuario.instance=this
        }
        return Usuario.instance
    }
    mostrarUsuario(){
        return this.id
            ? { id: this.id, username: this.username, nombre: this.nombre, email: this.email }
            : "Error: Instancia no definida";
    }
    resetInstance(){
        Usuario.instance=null
        this.id=null
        this.username=null
        this.nombre=null
        this.email=null
        return console.log(('Instancia borrada'));
        
    }
}
let usuario1=new Usuario(1,"Andreskratos","felipe","felipe@gmail")

console.log(`El id del usuario es: ${usuario1.mostrarUsuario().id}\n el username del usuario es: ${usuario1.mostrarUsuario().username}\n el nombre del usuario es: ${usuario1.mostrarUsuario().nombre}\n el email del usuario es: ${usuario1.mostrarUsuario().email}`);
console.log(usuario1.mostrarUsuario());





