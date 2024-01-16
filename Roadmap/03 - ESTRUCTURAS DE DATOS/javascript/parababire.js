//Built in data structure (primitive)

/**Arrays**/

let names = ["maria", "angel", "pedro", "luisa"];
names.push("rogelio");//Insertar dato
console.log(names);
names.pop();//Eliminar dato
console.log(names);
names[0] = "lupita";//Actualizar dato
console.log(names);
names.sort();//Reordenar datos
console.log(names);

/**Objects**/

const joy = {
  raza: "poodle",
  color: "blanco",
  patas: 4,
  ladra: function () {
    console.log("woof, woof, woof");
  }
}
console.log(joy);
joy.raza = "mixed";//Actualizar propiedad
console.log(joy);
joy.cola = true;//Crear propiedad
console.log(joy);
joy.vive = false;
console.log(joy);
delete joy.vive;//Eliminar propiedad
console.log(joy);

//Not built in data structure (non-primitive)