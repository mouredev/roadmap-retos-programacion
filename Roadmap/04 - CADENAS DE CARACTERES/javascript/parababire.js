//Cadenas literales

const miNombre = "Ángel Nárvaez";
console.log(miNombre);

//Cadena objeto

const thirdRockFromTheSun = new String("Tierra");
console.log(thirdRockFromTheSun);

//Acceso a un caracter específico

console.log(miNombre.charAt(6));
console.log(thirdRockFromTheSun[2]);

//Subcadenas

console.log(miNombre.substring(0, 6));

//Longitud de cadenas

console.log(miNombre.length);

//Concatenar

let saludo = "Hola ";
console.log(saludo + miNombre);

//Repetición

console.log(saludo.repeat(3) + thirdRockFromTheSun);

//Conversión a mayusculas

console.log(miNombre.toUpperCase());

//Conversión a minusculas

console.log(thirdRockFromTheSun.toLowerCase());

//Recorrido

let miNombreMinu = miNombre.toLocaleLowerCase();
for (let i = 0; i < miNombreMinu.length; i++) {
  console.log(miNombreMinu[i]);
}

//Reemplazo

console.log(miNombre.replace("Ángel", "Lcdo."));

//Dividir cadenas

let str = "Hola programadores de la ruta de programación 2024.";

let palabrasStr = str.split(" ");
console.log(palabrasStr);

//Unir cadenas

let unionDeStr = str.concat(" Mi nombre es ", miNombre);
console.log(unionDeStr);

//Interpolación

let saludo_interpolado = `${str} Bienvenidos, esta es mi solución al reto #04. Mi nombre es ${miNombre}`;
console.log(saludo_interpolado);

//Verificación

console.log(saludo_interpolado.includes(miNombre));//El método includes() es case sensible.