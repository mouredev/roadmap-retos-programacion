/*
 --------------------------------------
   * FUNCIONES DEFINIDAS POR EL USUARIO
 ---------------------------------------
*/
// Simple
const funcion = () => {
  console.log("Hola, Javascript  fun1");
};
funcion();

// Con return
const return_greet = () => {
  return "Hola, Javascript fun2";
};
console.log(return_greet());

// Con argumento
const arg_greet = ({ greet, nameS }) => {
  console.log(`${greet} ${nameS} fun3`);
};

arg_greet({ nameS: "Ramirez", greet: "Hola," });

// Con argumento predeterminado

const default_arg_greet = (nameS = "JavaScript") => {
  console.log(`Hola, ${nameS} fun4`);
};
default_arg_greet();

// Con argumento y retorno
const retur_arg_greet = (greet, nameS) => {
  return `${greet} ${nameS} fun5`;
};

console.log(retur_arg_greet("Hola", "Jeff"));

// Con retorno de varios valores
const multiple_return_greet = () => {
  return ["Hola,", "Javascript fun6"];
};

const [greet, languageName] = multiple_return_greet();

console.log(greet);
console.log(languageName);

// Con distintos argumentos en variable

const variable_arg_greet = names => {
  for (let i = 0; i < names.length; i++) {
    console.log(`Hola, ${names[i]} fun7`);
  }
};

variable_arg_greet(["Javascript", "Python", "Jeffrey", "Josue"]);

// funciones dentro de funciones
const outer_funcion = () => {
  inner_funcion = () => {
    console.log("Función interna: Hola Javascript");
  };
  inner_funcion();
};

outer_funcion();

// funciones del lenguaje
console.log(parseInt("10") + parseInt("10.5"));
// -----------------------------
let date = new Date();
console.log(
  date.toISOString() // Ejemplo: '2024-07-29T12:34:56.789Z'
);
/*
 --------------------------------------
   * VARIABLES LOCALES Y GLOBALES
 ---------------------------------------
*/

const global_var = "variable global";

console.log(global_var);

const fucionVar = () => {
  const local_var = "Hola";
  console.log(`${local_var}, ${global_var}`);
};
fucionVar();
/*
 --------------------------------------
    * DIFICULTAD EXTRA (opcional):
 ---------------------------------------
*/

const return_num = (tex1, tex2) => {
  let total = 0;
  for (let i = 0; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
      console.log(tex1 + tex2);
    } else if (i % 3 == 0) {
      console.log(tex1);
    } else if (i % 5 == 0) {
      console.log(tex2);
    } else {
      console.log(i);
      total += 1;
    }
  }

  return console.log(total);
};
return_num("hOla, ", "jeffrey");
