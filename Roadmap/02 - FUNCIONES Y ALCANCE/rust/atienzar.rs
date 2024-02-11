/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */



 fn funcion_sin_params(){
    let x:i32 = 5;
    println!("aqui x es una variable local de la funcion y vale {x}" );
 }

 fn funcion_con_parametros(x:i32, y:i32){
    println!("La suma de {x} + {y} es {}", x+y);
 }

 // ojo! no termina con ;  => esto lo cambia de una expresion a una declaracion 
 // hace que devuelva ese valor.
 fn mas_uno(x:i32)->i32{
    x + 1
 }

 fn cedemos_cadena(cad:String){
    println!("Cadena vale: {}", cad);
 }

 fn imprimir_cad(cad:String)->String{
    println!("Cadena vale: {}", cad);
    cad
 }

 fn modificar_cadena(cad: &mut String) {
    cad.push_str(" mundo!");
}

// Funcion extra.
fn extra(cad1: String, cad2:String) -> i32{

     let mut cont = 0;

      for i in 1..100{

         if i % 3 == 0 && i % 5 == 0 {
            println!("{}{}",cad1,cad2);
         }else if i % 3 == 0{
            println!("{}",cad1);
         }else if  i % 5 == 0 {
            println!("{}",cad2);
         }else{
               println!("{}",i);
               cont = cont + 1;
         }
      }
      
   return cont

}


const HORAS: u32 = 24;


 fn main(){
    println!("Esta es la funcion ppal por defecto");

    //uso constante
    println!("constante {HORAS}");

    //definimos variables
    let x:i32 = 5;
    let y:i32 = 7;
    println!("x es {x}, y es {y}");

    // x = 8;
    println!("Sopresa! x es {x}");

    // para que las vbles varén tienen que ser mut
    let mut x:i32 = 5;
    x = 8;
    println!("Ahora! x es {x}");


    funcion_sin_params();
    funcion_con_parametros(x,y);
    
    {
        // esto es un nuevo ambito, como una funcion dentro de la funcion
        let x = x +2;
        println!("x es {x}");
    }
    // aqui fuera sigue valiendo 8 el ultimo valor asignado
    println!("x es {x}");

    //Puedes asignar funciones a vbles 
    let incrementar = mas_uno;
    println!("{x} + 1 es: {}", incrementar(x));



    let z:i32 = 7;
    x = mas_uno(z);
    println!("sumamos 1 a z: {z} y el valor es: {x} ");

    x = { 
        z + 1
    };
    println!("Imprimismos x:  {x} y z: {z}");

    // Rust tiene como objetivo ser eficiente en memoria, para ello no te deja
    // tener variables que apunten a la misma referencia, automaticamente se carga la primera.

    

    let cad1 = String::from("Hello World!");
    let cad2 = cad1;
    
    // cad1 ya no existe por lo que no podemos imprimirla.
    //println!("Rust {}", cad1);
    println!("Rust {}", cad2);

    // mas magia => si pasamos la cadena a una funcion, entonces la estmaos prestando y ya no
    // está diponible en el resto del scope

    cedemos_cadena(cad2);
    // Aqui ya no podemos imprimir cad2 pq la hemos perdido
    //println!(" {}", cad2);

    // para que no la perdamos la funcion nos la tiene que devolver de nuevo:
    let mut cad3 = String::from("Hola!");
    cad3 = imprimir_cad(cad3);
    println!("Seguimos teniendo cad1 {}", cad3);

    // Operador &mut para cuando queremos cambiar el contenido del puntero

    let mut cad4 = String::from("Hola");
    modificar_cadena(&mut cad4);
    println!("Modificando cadenas : {}", cad4);


    //LLamamos a la funcion extra
    let cad1 = String::from("Cadena1");
    let cad2 = String::from("Cadena2");

   // Punto extra
    let total:i32 = extra(cad1,cad2);
    println!("Numero de numeros impresos en total: {total}");

 }