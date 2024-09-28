// Expresiones regulares

let texto = `En un día soleado de verano, caminé por la ciudad y vi a 5 pájaros volando en el cielo. 
            Pasé por 10 tiendas diferentes, donde compré 3 manzanas y 2 botellas de agua. 
            Luego, me senté en un banco y leí durante 2 horas un libro fascinante sobre la historia 
            del universo. Después, conocí a 7 amigos en un café y compartimos risas y conversaciones 
            durante toda la tarde. Finalmente, al regresar a casa, preparé una deliciosa cena con 4 
            tipos diferentes de pasta y disfruté de una película emocionante hasta altas horas de la 
            noche.`

let regex = /\d+/g

// console.log(texto.match(regex));

//  DIFICULTAD EXTRA

let regexCorro = /.+@\w+[.]\w+/
let regexTelefono = /\d{3}-\d{3}-\d{4}/
let regexUrl = /(http|https):[/][/].+[.].+/

let correo = "marmodeyvid@gmail.com"
let telefono = "809-447-5619"
let url = "https://retosdeprogramacion.com/roadmap/"

function validar(nombre, texto, expresion)
{
    console.log("*".repeat(25) + ` ${nombre} ` + "*".repeat(25));
    console.log(expresion.test(texto) ? "Coincidencia: Si" : "Coincidencia: No");
    console.log(`Texto extraido: ${texto.match(expresion)[0]}\n`);
}

validar("Correo", correo, regexCorro)
validar("Telefono", telefono, regexTelefono)
validar("Url", url, regexUrl)