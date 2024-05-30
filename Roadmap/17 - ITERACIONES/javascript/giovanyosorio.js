/* EJERCICIO:
* Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
* números del 1 al 10 mediante iteración.
*
* DIFICULTAD EXTRA (opcional):
* Escribe el mayor número de mecanismos que posea tu lenguaje
* para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
*/

// 1 ejemplo

function iteration1(num){
    let mynumber=num

    for(let i=0;i<mynumber;i++){
        console.log(i)
    }
}

iteration1(10)


// 2 ejemplo (using for of)
function iteration2(num){
    for (const key of num) {
        console.log(key)
    }
}

iteration2([1,2,3,4,5,6,7,8,10])

// 3 ejemplo (using for each)
function iteration3(num){
num.forEach(element => {
    console.log(element)
});
}

iteration3([1,2,3,4,5,6,7,8,10])

// 4 ejemplo (using map)
function iteration4(num){

    let mapeo=num.map((item)=>item)
    console.log(mapeo)
    
    }
        
    iteration4([1,2,3,4,5,6,7,8,10])
    
    // 5 bucle (using do while)
    function iteration5(num){
        do {
          console.log(num)
            num++
    
        } while (num<=10);
            
        }
                
    iteration5(1)


        // 6 bucle (using while)
        function iteration6(num){
            while (num<=10) {
                console.log(num)
                num++
            }
                
        }
                    
        iteration6(1)
    
    // 7 ejemplo (using filter)
    function iteration7 (num){
        let filtrado=num.filter((item)=>item)
        console.log(filtrado)
      }
      iteration7([1,2,3,4,5,6,7,8,9,10])

      // 8 ejemplo (using for in)
      function iteration8 (num){
      
        for(let item in num){
          console.log(parseInt(item))
        }
        }
        iteration8([1,2,3,4,5,6,7,8,9,10])