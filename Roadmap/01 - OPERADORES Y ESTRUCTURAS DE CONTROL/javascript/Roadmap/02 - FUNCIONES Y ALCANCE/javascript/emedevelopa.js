//FUNCIONES

//Función Simple
function saludo() {
    console.log("Hola");
}

saludo();

//Con parámetros
function conParametros(a, b) {
    console.log(a + b);
}
conParametros(2, 5)

//Con retorno
function conRetorno (nombre) {
    if (nombre == "Maria") {
    return true;
    } else {
        return false;
    }
}
conRetorno("Maria")

//Funciones anidadas
function hacerPastel () {
    console.log("Hagamos un pastel!");
  
    function mezclarIngredientes () {
      console.log("Hora de mezclar");
    }
    mezclarIngredientes()
  
    function hornear () {
      console.log("Hora de hornear");
    }
    hornear() 
  
    function decorar () {
      console.log("Toca decorar el pastel")
    }
    decorar()

    function listo () {
        console.log("Pastel listo! A comer!")
    }
    listo()
  }
  
  hacerPastel()


  //Variable local
  function variableLocal() {
    let a = "a";
  }
  variableLocal() //Esto imprime a. 
  console.log(a) // Undefined

  //Variable Global
  let b = "b";
  function variableGlobal() {
    console.log(b);
  }
  variableGlobal() //Imprime b.
  

  //Ejercicio Extra
  function numeros(a, b) {
    let contador = 0;
    for (let i = 0; i <= 100; i++) {
      if (i % 3 == 0) {
        console.log(a);
      } else if (i % 5 == 0) {
        console.log(b);
      } else if (i % 3 == 0 && i % 5 == 0) {
        console.log(a + b);
      } else {
        console.log (i);
        contador++;
      }
    }
    return contador;
  }

  console.log("Número de veces que se ha impreso el número: " + numeros("Hola", "Adios"));