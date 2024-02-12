// Funciones y alcance

    //sin parametros ni retorno
function mensaje(){
    console.log("hola!")
}
    // con parametros
function saludar(nombre){
    console.log(`hola ${nombre} que tal!`)
}
    // con retorno
function sum(num1, num2){
    return num1 + num2
}

    //funciones dentro de funciones
function funcionAnidada(condicion){
    if(condicion){
        mensaje("verdadero")
    }else{
        mensaje("falso")
    }

    function mensaje(mnsj){
        console.log(`${mnsj}`)
    }
}
funcionAnidada(true)
    // funciones creadas en el lenguaje
    let str = "Hola amigos"
    let str2 = str.split(" ")
    console.log(str2) //esto separa la cadena en un array de palabras separadas por el espacio

    //variable local y global
    /*una variable local solo puede ser utilizada en el entorno donde fue decalarada esto quiere decir que si fue declarada dentro de un bloque de 
    codigo como una funcion, o un metodo, solo existe y puede ser usada ahi
    */ 
    //hasta donde tengo entendido en javascripot var es una variable  global donde se aque esta sea declarada    

    let num = 5
    function valor(){
        console.log(num)
    }
    valor()//aqui si nos devolveria el valor de num ya que la funcion si puede acceder al valor de la variable num

    function palabra(){
        let pal = "palabra" 
    }
    console.log(pal) /*aqui nos saltaria un error debido a auqe la variable pal esta declarada dentro de un bloque de codigo al cual la funcion console.log no tiene acceso */

        // reto extra
    function param(str1, str2){
        count = 0
        for(let i =1 ;i<= 100; i++){
            if(i %3 == 0 && i% 5 == 0){
                console.log(`${str1}${str2}`)
            }else if(i % 3 == 0){
                console.log(`${str1}`)
            }else if(i % 5 == 0){
                console.log(`${str2}`)
            }else{
                console.log(i)
                count++
            }
        }
        console.log(`los numeros han reemplazado a las palabras un total de ${count} veces`)
    }
    param("fizz", "fuzz")