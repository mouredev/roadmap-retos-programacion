// función simple sin parámetros

function printString(): void {
    console.log("Hola");
  }
  
  printString();
  
  // función simple con parámetros
  
  function printStringPara(name: string): void {
    console.log(`Hola ${name}`);
  }
  
  printStringPara("Brais");
  
  // Retorno y dos parámetros
  
  function add(num1: number, num2: number) {
    return num1 + num2;
  }
  
  console.log(add(2, 5));
  
  // función anónima
  
  const sub = function (num1: number, num2: number) {
    return num1 - num2;
  };
  
  console.log(sub(4, 2));
  
  // funciones flecha en una sola línea con retorno implícito.
  
  const multiply = (num1: number, num2: number) => num1 * num2;
  
  console.log(multiply(34, 55));
  
  // callbacks
  
  const addChar = (arr: string[]) =>
    arr.map((element) => {
      return element + "!";
    });
  
  console.log(addChar(["hola", "chau", "quizás"]));
  
  // Ejemplo de variable global y local
  
  let variableGlobal: string = "Juan";
  
  function variables() {
    let variableLocal: string = "Hola";
    let lasDosVariables: string = `${variableLocal} ${variableGlobal}`;
    return lasDosVariables;
  }
  console.log(variables());
  
  // console.log(variableLocal); No se puede mostrar porque está fuera del scope de la función
  
  // Dificultad Extra
  
  const fizzBuzz = (firstWord: string, secondWord: string) => {
    let totalNum: number = 0;
    for (let i: number = 1; i <= 100; i++) {
      if (i % 15 === 0) console.log(firstWord + secondWord);
      else if (i % 5 === 0) console.log(secondWord);
      else if (i % 3 === 0) console.log(firstWord);
      else {
        totalNum++;
        console.log(i);
      }
    }
    return totalNum;
  };
  
  console.log(fizzBuzz("Fizz", "Buzz"));
  